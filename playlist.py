"""The playlist class is used to hold information about playlists and update M3U files by
appending songs, getting their information by utilizing the TinyTag library.

Instance Variables:
    name (string): The name of a playlist, obtained from the GUI playlist thumbnails
    m3u_filepath (string): The filepath of the M3U file associated with the playlist
    thumbnail_filepath (string): The filepath of the GUI thumbnail associated with the playlist

Methods:
    add_song(tinytag_song) utilizes a TinyTag tag to append a song to a playlist"""

import os
from tinytag import TinyTag
from txt_manip import *
class Playlist:

    def __init__(self, place_saver_directory_path, thumbnail_filepath):
        #Gets playlist name from the name of the playlist thumbnail
        name = os.path.splitext(os.path.basename(thumbnail_filepath))[0]
        self.name = name
        #Making new M3U file, or only setting the filepath if the M3U exists
        self.m3u_filepath = f"{place_saver_directory_path}/M3Ufiles/{name}.m3u"
        if not os.path.exists(self.m3u_filepath):
            list_to_file(["#EXTM3U"], self.m3u_filepath)
        self.thumbnail_filepath = thumbnail_filepath

    def add_song(self, tinytag_song):
        """Append a song to an M3U File utilizing TinyTag."""
        #Adding song information
        song_name = os.path.splitext(os.path.basename(tinytag_song.filename))[0]
        line = f"#EXTINF:{int(tinytag_song.duration)},{tinytag_song.artist} - {song_name}"
        append_line_to_file(line, self.m3u_filepath)
        #Adding song filepath
        append_line_to_file(tinytag_song.filename, self.m3u_filepath)