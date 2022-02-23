import requests

SPOTIFY_CREATE_PLAYLIST_URL = 'https://api.spotify.com/v1/users/eddiebender20/playlists'
ACCESS_TOKEN = 'BQBJ7TaLD3d5wJ28JgQ7-4Hcg2NU6U9CFcMxhAJHAl892-L6SHXwyQQAdJpbs_MLXZc5tHSEKCU7WejZZ3tTZR6kdWtBIxOOvuaQ1OWiNjQW8YLzUlj10-TKFca4pN3iI6Yie3AZLp4Goh8EvLuHo0MYZCo3Skkv8K8_3U8Z4lAVZ10E5SMNiGSLSu4-itrUj3y7h091pdqhihlh'

def create_playlsit_on_spotify(name, public):
    response = requests.post(
        SPOTIFY_CREATE_PLAYLIST_URL,
        headers={
            "Authorization": f"Bearer {ACCESS_TOKEN}"
        },
        json={
            "name": name,
            "public": public
        }
    )
    json_resp = response.json()

    return json_resp

def 

def main():
    playlist = create_playlsit_on_spotify(
        name="My Private Playlist",
        public=False
    )
    print(f"Playlist: {playlist}")

if __name__ == '__main__':
    main()