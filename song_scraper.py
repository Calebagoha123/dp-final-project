import csv
import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv

load_dotenv()

def get_spotify_client():
    """this function initializes and returns a Spotify client using Spotipy."""
    return spotipy.Spotify(auth_manager=SpotifyClientCredentials(
        client_id=os.getenv('SPOTIPY_CLIENT_ID'),         # expects SPOTIPY_CLIENT_ID in .env
        client_secret=os.getenv('SPOTIPY_CLIENT_SECRET')      # expects SPOTIPY_CLIENT_SECRET in .env
    ))

def get_top_tracks_from_playlist(playlist_id, year, n):
    """
    this function fetches the top tracks from a Spotify playlist for a given year.
    it takes the playlist ID, year, and number of tracks to fetch as input.
    it returns a list of dictionaries containing song details.
    """
    sp = get_spotify_client()
    results = sp.playlist_items(playlist_id, limit=n)
    tracks = results['items']
    
    songs_data = []
    
    # iterate through the tracks and extract relevant information
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
    """ this function writes the list of song dictionaries to a CSV file."""
    if not songs_data:
        print("No songs data to write.")
        return
    
    # get the keys from the first song dictionary to use as CSV headers
    keys = songs_data[0].keys()
    
    # create a CSV file with the song data
    with open(filename, 'w', newline='', encoding='utf-8') as output_file:
        dict_writer = csv.DictWriter(output_file, fieldnames=keys)
        dict_writer.writeheader()
        dict_writer.writerows(songs_data)
        
    print(f"CSV file '{filename}' created with {len(songs_data)} songs.")
    
if __name__ == '__main__':
    # playlists of hit songs from 2020-2024
    # link to page: https://open.spotify.com/user/125382564/playlists
    year_playlists = {
        2000:'https://open.spotify.com/playlist/3ZnAcblT0kJSxBoNDyjVmi?si=IbvUXp2WS76u8CxbPnjABw',
        2001:'https://open.spotify.com/playlist/1PY76KImg5m78MafOavzzT?si=7oZ7DlxDSne8_w3QepGvMQ',
        2002: 'https://open.spotify.com/playlist/31orNwRGta1pVcTEbb1Rig?si=h0X6C0maQye83dtFfvd5jw',
        2003: 'https://open.spotify.com/playlist/0dxgrFpByUvzGwQB6LlUC6?si=l86yJS2FQnOg9NtUrKqXlw',
        2004: 'https://open.spotify.com/playlist/3pM6OEFeTo4L1yd4eRltjL?si=m8Q5FjyhR8qhNYg2_YT-IA',
        2005: 'https://open.spotify.com/playlist/0a3zRGDDLL1nwZmIuQT8LP?si=iRkwLlDLQnK7uyMyAH7hMw',
        2006: 'https://open.spotify.com/playlist/2NYo0q9T7NFPE24XB4IPuA?si=k9uMzMGERtO0PDgCLn54Hg',
        2007: 'https://open.spotify.com/playlist/0sNsM6d2k9jurLXB0QRYH7?si=JfFtq3TWSR2a1TI49gVI9Q',
        2008: 'https://open.spotify.com/playlist/0EIOwG3l57IeUNMYopujrL?si=NtnD6NEwQ7WXU4pRfrNR9g',
        2009: 'https://open.spotify.com/playlist/3HoMt2eIHGueEAT3LP8HjI?si=HFpbWxybTxySxMbgeIvQbw',
        2010: 'https://open.spotify.com/playlist/3iz6BGeQFOv4bSAKpTOzIN?si=ZFfaxAm5QIejOfsrCtAQbQ',
        2011: 'https://open.spotify.com/playlist/3McBfDOrmbD1g8Gki4Ry8U?si=KfArrwr6QDWgqM36iw-Rfg',
        2012: 'https://open.spotify.com/playlist/3mmG90Ig9YrdZOH7yDQJVp?si=A2aAkpx1QYu5KnPUN_4LTw',
        2013: 'https://open.spotify.com/playlist/49USVFK89mquEevzyoWwV7?si=9PwelxN3RbOGKWGloZuPeQ',
        2014: 'https://open.spotify.com/playlist/5KpUsCuhv4kN4LzSdIvaG8?si=uV1iLk9zQ5KIMbkNymFdUQ',
        2015: 'https://open.spotify.com/playlist/20K12yslgchif3E69cjAYz?si=qWoICYubQzysAABiq1SBYQ',
        2016: 'https://open.spotify.com/playlist/0a41v1jx28RyoDHhKi5DJR?si=p2I_ky4xRUSPYhARyNnxEg',
        2017: 'https://open.spotify.com/playlist/0yWHPqOEM9olSXpEaagxc6?si=mE8a7Rl_Qyy38RXdi-AKAw',
        2018: 'https://open.spotify.com/playlist/5TgwU962oxYOeAF3lnKONs?si=3yxp7kL8Ta2OxOC9tEE8Eg',
        2019: 'https://open.spotify.com/playlist/78NSwK8U2PdNGBmkrI5i66?si=fUyf2jV2Teul33c9sY5PQw',
        2020: 'https://open.spotify.com/playlist/4jSVL6ZfBtvzrWmmPSTgkI?si=9_aCIQp_TwaBJXZcPGueBw',
        2021: 'https://open.spotify.com/playlist/5GhQiRkGuqzpWZSE7OU4Se?si=txi_65LaSQCcKyyMuMR8qA',
        2022: 'https://open.spotify.com/playlist/56r5qRUv3jSxADdmBkhcz7?si=rqYKZA7ZTKqosy8JvQLMpg',
        2023: 'https://open.spotify.com/playlist/6unJBM7ZGitZYFJKkO0e4P?si=vVEL7g0iRnmlkAU2kevdzQ',
        2024: 'https://open.spotify.com/playlist/774kUuKDzLa8ieaSmi8IfS?si=iP8T6YYmRt-qEVAS7lSkhQ',
        }
    
    # pull data from spotify
    all_songs_data = []
    for year, playlist_id in year_playlists.items():
        print(f"Fetching top tracks for {year} from playlist {playlist_id}...")
        songs_data = get_top_tracks_from_playlist(playlist_id, year, n=100)
        all_songs_data.extend(songs_data)
    
    # save to csv    
    write_csv(all_songs_data, 'top_songs_by_year.csv')