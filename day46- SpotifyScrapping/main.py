from bs4 import BeautifulSoup
import lxml
import requests
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth

anwere = input("Which year do you want to travel to? YYYY-MM-DD:")

response = requests.get(url= f"https://www.billboard.com/charts/hot-100/{anwere}")
data =response.text
soup = BeautifulSoup(data, "lxml")



songs = soup.find_all(class_ ="chart-element__information__song text--truncate color--primary")


list_of_songs = []

for song in songs:
    list_of_songs.append(song.getText())

print(list_of_songs)

clientid = "5d6cddbe7b9143688558970254968207"
client_secret = "15f7ea2126684ca0839c477a5190b902"

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=clientid,
        client_secret=client_secret,
        show_dialog=True,
        cache_path="token.txt"
    )
)

user_id = sp.current_user()["id"]

sp.