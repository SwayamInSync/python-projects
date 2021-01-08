import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

date = input("Enter date in YYYY-MM-DD format: ")
year = date.split("-")[0]

# web scraping to get the name of songs


billbord_url = f"https://www.billboard.com/charts/hot-100/{date}"
res = requests.get(url=billbord_url)
song_data = res.text
soup = BeautifulSoup(song_data, "html.parser")
songs = soup.find_all(name="span", class_="chart-element__information__song")
song_names = [song.getText() for song in songs]

# Authenticating with spotify to get the user id

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private playlist-modify-public",
        redirect_uri="http://example.com",
        client_id="<Your spotify app client id>",
        client_secret="Your spotify app secret id",
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]
print(user_id)


# getting URIs of all the songs

song_uris = []

for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    # print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        pass
        print(f"The song: {song}  not found!!")

# creating playlist

# sp.user_playlist_create(user=user_id,
#                         name=f"{date}Billboard top 100",
#                         public=True,
#                         collaborative=False,
#                         description=f"Top 100 Billboard songs of {date}")



# creating list of only song URIs to pass to add songs to playlist

only_song_uris = [uri.split(':')[2] for uri in song_uris]

# adding songs to playlist

sp.playlist_add_items(playlist_id="<Your spotify playlist id>",
                      items=only_song_uris)


