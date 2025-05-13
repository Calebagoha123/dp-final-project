import csv
import os
import time
from dotenv import load_dotenv
import lyricsgenius

load_dotenv()

# expects SPOTIPY_CLIENT_ID in .env
GENIUS_ACCESS_TOKEN = os.getenv('GENIUS_ACCESS_TOKEN')

genius = lyricsgenius.Genius(GENIUS_ACCESS_TOKEN, timeout=15, retries=3)

INPUT_CSV = 'top_songs_by_year.csv'
OUTPUT_CSV = 'top_songs_with_lyrics.csv'

def get_lyrics(song_name, artist):
    try:
        song = genius.search_song(song_name, artist)
        if song:
            return song.lyrics
    except Exception as e:
        print(f"Error fetching lyrics for '{song_name}' by {artist}: {e}")
    return ''

if __name__ == '__main__':
    all_rows = []
    
    with open(INPUT_CSV, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        fieldnames = reader.fieldnames + ['lyrics']
        
        for row in reader:
            song_name = row.get("name")
            artist = row.get("artists")
            print(f"Fetching lyrics for '{song_name}' by {artist}...")
            row['lyrics'] = get_lyrics(song_name, artist)
            all_rows.append(row)
            time.sleep(1)  # Delay to avoid rate limiting
            
    with open(OUTPUT_CSV, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(all_rows)
        
    print(f"CSV file '{OUTPUT_CSV}' created with lyrics appended.")