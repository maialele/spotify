from connect_spotify import Token
from connect_spotify import client_id, client_secret
from dotenv import load_dotenv
import os
import base64
import json
from requests import post, get

# initialize and get the token string from the class Token at connect_spotify
token = Token(client_id, client_secret)
my_token = token.get_token()

# send request to spotify api
def send_request(url: str):
    """
    The send_request function sends a get request to spotify api for a given url
    :param url: the url path given to send the api request
    :return: a json file (string)
    """
    headers = token.get_auth_header(my_token)
    result = get(url, headers=headers) 
    json_result = json.loads(result.content)
    return json_result

# find the list of aritsts when you search for one 
def find_artists(artist: str):
    """
    the find_artist function searches the spotify api for the first result of a given artist
    :param artist: the artist name
    :return: a json file (string)
    """
    url = 'https://api.spotify.com/v1/search?q={}&type=artist&limit=1'.format(artist)
    response = send_request(url)
    return response


# get the top tracks of the artist that you searched
def get_top_tracks():
    """
    the get_top_tracks function looks for the top songs of a given artist in Israel
    :return: a json file (string)
    """
    artist = 'Odaya'
    artist_id = find_artists(artist)['artists']['items'][0]['id']
    # send a get request
    url = 'https://api.spotify.com/v1/artists/{}/top-tracks?country=IL'.format(artist_id)
    response = send_request(url)
    return response

# format the json file and take out the necessary data, write it into songs.txt
def make_tracks_list(json):
    """
    the make_track_list function simply formats the json given from get_top_tracks and writes it to a file.
    :param json: the soon to be formatted json file
    :return: none
    """
    tracks_list = json['tracks']
    # delete previous content of file songs.txt, soon to be filled with the top tracks
    delete_file_content  = open("songs.txt",'w')
    for index, song in enumerate(tracks_list):
        print(f"{index + 1}. {song['name']}")
        with open("songs.txt", "a") as f:
            print(f"{index + 1}. {song['name']}", file=f)


def main():
    make_tracks_list(get_top_tracks())

if __name__ == "__main__":
    main()