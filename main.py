#https://ytmusicapi.readthedocs.io/en/latest/reference.html
from ytmusicapi import YTMusic

ytmusic = YTMusic('headers_auth.json')

playlist_id = '<playlist_id>'

playlist = ytmusic.get_playlist(playlist_id)

library_songs = ytmusic.get_library_songs(5000)
library_songs_ids = [song_id.get('videoId') for song_id in library_songs]

# Add 100 songs to the playlist at a time
for i in range(0, len(library_songs_ids), 10):
    song_ids = library_songs_ids[i:i+10]
    ytmusic.add_playlist_items(playlist_id, song_ids, duplicates=False)
    print(f'Added {i} library songs to playlist')

uploaded_songs = ytmusic.get_library_upload_songs(5000)
uploaded_ids = [song_id.get('videoId') for song_id in uploaded_songs]

# Add 100 songs to the playlist at a time
for i in range(0, len(uploaded_ids), 10):
    song_ids = uploaded_ids[i:i+10]
    ytmusic.add_playlist_items(playlist_id, song_ids, duplicates=False)
    print(f'Added {i} uploaded songs to playlist')