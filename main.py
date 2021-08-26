#https://ytmusicapi.readthedocs.io/en/latest/reference.html
from ytmusicapi import YTMusic

ytmusic = YTMusic('headers_auth.json')

playlist_id = '<playlist_id_from_url>'

playlist = ytmusic.get_playlist(playlist_id)

library_songs = ytmusic.get_library_songs(5000)
library_songs_ids = [song_id.get('videoId') for song_id in library_songs]
for i, song_id in enumerate(library_songs_ids):
    print(f'Library song {i} of {len(library_songs_ids)}')
    ytmusic.add_playlist_items(playlist_id, [song_id], duplicates=False)

uploaded_songs = ytmusic.get_library_upload_songs(5000)
uploaded_ids = [song_id.get('videoId') for song_id in uploaded_songs]
for i, song_id in enumerate(uploaded_ids):
    print(f'Uploaded song {i} of {len(uploaded_ids)}')
    ytmusic.add_playlist_items(playlist_id, [song_id], duplicates=False)
