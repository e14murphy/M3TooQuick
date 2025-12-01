"""Contains static methods implementing pyglet to play songs.

Methods:
    play_song(song_filename, start_time): Plays a song beginning at a specified time in seconds)

"""

import pyglet
class MusicPlayer:

    @staticmethod
    def play_song(song_filename, start_time = None):
        #Loading song
        player = pyglet.media.Player()
        song = pyglet.media.load(f"Assets/MusicFolder/{song_filename}")
        player.queue(song)
        if start_time:
            player.seek(start_time)
        #Playing song
        player.play()
        pyglet.app.run()
        #Insert Event to stop playback before moving to next song
