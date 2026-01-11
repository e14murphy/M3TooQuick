"""The PlaceSaver class is used to save information about a session between uses of the program.
It is the primary motivation for making this program in the first place, as sorting through a long
list of song files to make playlists can be a time consuming process.

Instance Variables:
    place_saver_directory_path (string): The file path of a directory in which information about a session is saved.
    song_queue (list): The queue of songs yet to be sorted.

Methods:
    save_place(): Writes information about the session to the directory at the path place_saver_file_path holds.
    update_save_info(list): Updates the PlaceSaver self.song_queue instance variable to the current queue.
"""

import os
import txt_manip
class PlaceSaver:

    def __init__(self, place_saver_name):
        self.place_saver_name = place_saver_name
        self.place_saver_directory_path = f"Assets/PlaceSaverFiles/{place_saver_name}"
        #Attempt to make a directory at place_saver_directory_path. If a directory already exists there, initializes a
        #place_saver with the info from the session when that directory was made. If there is no directory there,
        #creates a new place_saver directory and empty lists to make new associated files.
        try:
            os.mkdir(f"{self.place_saver_directory_path}")
        except FileExistsError:
            self.song_queue = txt_manip.file_to_list(f"{self.place_saver_directory_path}/song_queue.txt")
        else:
            os.mkdir(f"{self.place_saver_directory_path}/M3Ufiles")
            self.song_queue = []

    def update_save_info(self, song_queue):
        self.song_queue = song_queue

    def save_place(self):
        """Make file song_queue.txt if it does not exist, write session info to file."""
        txt_manip.list_to_file(self.song_queue, f"{self.place_saver_directory_path}/song_queue.txt")