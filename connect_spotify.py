from dotenv import load_dotenv
import os
import base64
import json
from requests import post, get

load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret  = os.getenv("CLIENT_SECRET")

#class Token: --how to do it when one function depends on the other 
class Token: 
    def __init__(self, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret
        
    def get_token(self):
        #Encode the client id and secret to access spotify api
        auth_string = client_id + ":" + client_secret
        auth_bytes = auth_string.encode("utf-8")
        auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")

        #Add headers to the token post request and other shit for the json request
        url = "https://accounts.spotify.com/api/token"
        headers = {
            "Authorization": "Basic " + auth_base64,
            "Content-Type": "application/x-www-form-urlencoded"
        }
        data = { "grant_type": "client_credentials" }

        # send a post request to spotify server
        result = post(url, headers=headers, data=data)

        #returning the response of the post request in a json format
        json_result = json.loads(result.content)

        #accessing the value of the access token key to just get the access token and return it
        token = json_result["access_token"]
        return token

    #format the token
    def get_auth_header(self,token):
        try:
            return {"Authorization": "Bearer " + token}
        except:
            print("no token provided")