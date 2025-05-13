import csv
import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv

load_dotenv()

def get_spotify_client():
    return spotipy.Spotify(auth_manager=SpotifyClientCredentials(
        client_id=os.getenv('SPOTIPY_CLIENT_ID'),         # expects SPOTIPY_CLIENT_ID in .env
        client_secret=os.getenv('SPOTIPY_CLIENT_SECRET')      # expects SPOTIPY_CLIENT_SECRET in .env
    ))

def get_top_tracks_from_playlist(playlist_id, year, n=50):
    sp = get_spotify_client()
    results = sp.playlist_items(playlist_id, limit=n)
    tracks = results['items']
    
    songs_data = []
    for item in tracks:
        track = item.get('track')
        if not track:
            continue
        track_data = {
            "year": year,
            "name": track.get('name'),
            "artists": ', '.join(artist.get('name') for artist in track.get('artists', [])),
            "album": track.get('album', {}).get('name'),
            "popularity": track.get('popularity'),
            "release_date": track.get('album', {}).get('release_date')
        }
        songs_data.append(track_data)
    return songs_data

def write_csv(songs_data, filename):
    if not songs_data:
        print("No songs data to write.")
        return
    keys = songs_data[0].keys()
    with open(filename, 'w', newline='', encoding='utf-8') as output_file:
        dict_writer = csv.DictWriter(output_file, fieldnames=keys)
        dict_writer.writeheader()
        dict_writer.writerows(songs_data)
    print(f"CSV file '{filename}' created with {len(songs_data)} songs.")
    
if __name__ == '__main__':
    year_playlists = {} # link to page: https://open.spotify.com/user/125382564/playlists
    
    # pull data from spotify
    all_songs_data = []
    for year, playlist_id in year_playlists.items():
        print(f"Fetching top tracks for {year} from playlist {playlist_id}...")
        songs_data = get_top_tracks_from_playlist(playlist_id, year, n=50)
        all_songs_data.extend(songs_data)
    
    # save to csv    
    write_csv(all_songs_data, 'top_songs_by_year.csv')