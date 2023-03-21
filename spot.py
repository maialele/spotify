import requests
from constants import *

class Create():      
    def  create_playlist(self, name, public):
        print(SPOTIFY_CREATE_PLAYLIST_URL)
        response = requests.post(
            SPOTIFY_CREATE_PLAYLIST_URL,
            headers={
                "Authorization": f"Bearer {ACCESS_TOKEN_CREATE_PLAYLIST}"
            },
            json={
                "name": name,
                "public": public
            }
        )
        json_resp = response.json()

        return json_resp

class Get():
    def get_albums(self):
        print(SPOTIFY_GET_ALBUMS_URL)
        request = requests.get(
            SPOTIFY_GET_ALBUMS_URL,
            headers={
                "Authorization": f"Bearer {ACCESS_TOKEN_GET_ALBUMS}"
            }
        )
        json_resp = request.json()
        return json_resp

    def get_album_name(self, album_name):
        all_albums = str(Get.get_albums(self))
        if album_name in all_albums:
            print('yes')
        else:
            print('no')
        request = requests.get(
            'https://api.spotify.com/v1/search?q=track:"' + 'despacito' + '"%20artist:"' + 'bieber' + '"&type=track',
            headers={
                "Authorization": f"Bearer {ACCESS_TOKEN_GET_ALBUMS}"
            }
            )
        json_resp = request.json()
        return json_resp
        



def main():
    #playlist = Create()
    #response = playlist.create_playlist("livingroom", False)
    #playlist = create_playlist(name="shower songs", public=False)
    #print(f"playlist: {response}")

    albums = Get()
    response = albums.get_albums()
    
    my_album = Get().get_album_name('Tortoise')
    print(my_album)


if __name__ == '__main__':
    main()