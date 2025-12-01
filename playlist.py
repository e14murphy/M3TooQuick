"""Holds information about a playlist (WIP)"""

class Playlist:

    def __init__(self, name):
        self.name = name
        self.m3u_filepath = f"Assets/M3Ufiles/{name}.m3u"
        self.thumbnail_filepath = f"Assets/PlaylistThumbs/{name}.jpg"

