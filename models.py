from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Playlist(db.Model):
    """Playlist."""

    __tablename__='playlists'

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    name = db.Column(db.Text,
                     nullable=False)
    description = db.Column(db.Text)

    def __repr__(self):
        return f'<Playlist {self.id} name={self.name} description={self.description}>'
    
    # def a many to many relationship between Playlist and PlaylistSong
    playlist_songs = db.relationship('Song',
                            secondary='playlistsongs', 
                            backref='playlists')


class Song(db.Model):
    """Song."""

    __tablename__= 'songs'

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    title = db.Column(db.Text,
                      nullable=False)
    artist = db.Column(db.Text,
                       nullable=False)

    def __repr__(self):
        return f'<Song {self.id} title={self.title} artist={self.artist}>'
    
    # def a many to many relationship between Song and PlaylistSong
    related_playlists = db.relationship('Playlist',
                                 secondary='playlistsongs',
                                 backref='songs')


class PlaylistSong(db.Model):
    """Mapping of a playlist to a song."""

    __tablename__ = 'playlistsongs'

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    playlist_id = db.Column(db.Integer,
                            db.ForeignKey('playlists.id'),
                            nullable=False)
    song_id = db.Column(db.Integer,
                        db.ForeignKey('songs.id'),
                        nullable=False)
    
    


# DO NOT MODIFY THIS FUNCTION
def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)
