from app import app
from models import db, Playlist, Song, PlaylistSong

# Connect to the database
db.drop_all()
db.create_all()

# Create sample playlists
sample_playlists = [
    Playlist(name="Rock Classics", description="Some classic rock songs"),
    Playlist(name="Pop Hits", description="Top pop hits"),
    Playlist(name="Hip-Hop Favorites", description="Popular hip-hop tracks"),
    Playlist(name="Country Vibes", description="Country music for the soul"),
    Playlist(name="EDM Party", description="Electronic dance music for the party"),
]

# Add playlists to the database
for playlist in sample_playlists:
    db.session.add(playlist)

# Commit the changes to the database
db.session.commit()

# Create sample songs
sample_songs = [
    Song(title="Bohemian Rhapsody", artist="Queen"),
    Song(title="Shape of You", artist="Ed Sheeran"),
    Song(title="Lose Yourself", artist="Eminem"),
    Song(title="Sweet Home Alabama", artist="Lynyrd Skynyrd"),
    Song(title="Despacito", artist="Luis Fonsi"),
]

# Add songs to the database
for song in sample_songs:
    db.session.add(song)

# Commit the changes to the database
db.session.commit()

# Create mappings between playlists and songs
playlist_song_mappings = [
    PlaylistSong(playlist_id=1, song_id=1),
    PlaylistSong(playlist_id=2, song_id=2),
    PlaylistSong(playlist_id=3, song_id=3),
    PlaylistSong(playlist_id=4, song_id=4),
    PlaylistSong(playlist_id=5, song_id=5),
]

# Add mappings to the database
for mapping in playlist_song_mappings:
    db.session.add(mapping)

# Commit the changes to the database
db.session.commit()

print("Sample data has been seeded to the database.")