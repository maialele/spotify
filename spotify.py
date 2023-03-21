from connect_spotify import token, get_auth_header
from dotenv import load_dotenv
import os
import base64
import json
from requests import post, get

# find the list of aritsts when you search for one 
def find_artists(token,artist):
    url = 'https://api.spotify.com/v1/search?q={}&type=artist&limit=1'.format(artist)
    headers = get_auth_header(token)

    result = get(url, headers=headers) 
    json_result = json.loads(result.content)
    return json_result

# get the top tracks of the artist that you searched
def get_top_tracks(token):
    artist = 'metallica'
    artist_id = find_artists(token, artist)['artists']['items'][0]['id']

    # send a get request
    url = 'https://api.spotify.com/v1/artists/{}/top-tracks?country=IL'.format(artist_id)
    headers = get_auth_header(token)
    result = get(url, headers=headers) 
    json_result = json.loads(result.content)
    return json_result

# format the json file and take out the necessary data
def make_tracks_list(json):
    tracks_list = json['tracks']
    for index, song in enumerate(tracks_list):
        print(f"{index + 1}. {song['name']}")


ready_tracks = make_tracks_list(get_top_tracks(token))