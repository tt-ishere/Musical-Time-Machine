# Import necessary libraries
import requests
from bs4 import BeautifulSoup
import os
from dotenv import find_dotenv, load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Load environment variables
dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

# Set up Spotify API credentials
Client_ID = os.getenv("Client_ID")
Client_Secret = os.getenv("Client_Secret")
scope = "playlist-modify-public"

# Get user input for travel date and construct URL for Billboard chart
travel_date = input(
    "What date in musical history would you like to visit? NB: Date should be in YYYY-MM-DD format: ")
url = f"https://www.billboard.com/charts/hot-100/{travel_date}"

# Send a GET request to the Billboard URL and retrieve the billboard_100 content
response = requests.get(url)
billboard_100 = response.text

# Parse the the billboard_100 using BeautifulSoup

soup = BeautifulSoup(billboard_100, "lxml")

# Extract the song titles from the HTML using CSS selectors
song_list = (soup.select(
    "div #post-1479786 .pmc-paywall .chart-results-list .o-chart-results-list-row-container .lrv-u-width-100p h3"))

# Extract the artist names from the HTML using CSS selectors
artist_list = (soup.select(
    "div #post-1479786 .pmc-paywall .chart-results-list .o-chart-results-list-row-container .lrv-u-width-100p .o-chart-results-list__item .a-font-primary-s"))

# Store the song titles and artist names in separate lists
song_titles = [title.get_text(strip="True") for title in song_list]
song_artists = [artist.get_text(strip="True") for artist in song_list]

# Set up Spotify authentication and authorization using the Spotipy library
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=Client_ID,
    client_secret=Client_Secret,
    redirect_uri="http://example.com",
    scope=scope, show_dialog=True)
)

user_id = sp.current_user()["id"]

# Search for each song on Spotify and retrieve the track URI
tracks_uri = []
for artist, tittle in zip(song_artists, song_titles):
    track_tittle = artist
    track_artist = tittle
    try:
        results = sp.search(
            q=f"track:{track_tittle} artist:{track_artist}", type="track")
        uri = (results["tracks"]["items"][0]["uri"])
        tracks_uri.append(uri)
    except IndexError:
        pass

# Set the name and description of the playlist to be created
playlist_name = f"{travel_date} Billboard 100"
playlist_description = f"Billboard 100 songs for {travel_date}"

# Create the playlist on the user's Spotify account
billboard_100playlist = sp.user_playlist_create(
    user=user_id, name=playlist_name, public=True, description=playlist_description)

# Add the tracks to the created playlist
add_tracks = sp.user_playlist_add_tracks(
    user=user_id, playlist_id=billboard_100playlist['id'], tracks=tracks_uri)

print(add_tracks["snapshot_id"])
