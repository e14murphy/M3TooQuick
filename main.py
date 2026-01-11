import M3UQuickMainWindowWidgets
from gui import *
from M3UQuickMainWindowWidgets import *
from music_player import *
import os
from place_saver import *
from playlist import *
from PyQt6.QtWidgets import QApplication, QMainWindow
import shutil
import sys
from boolean_wrapper import BooleanWrapper
from tinytag import TinyTag
#
# def display_song_info(tinytag_song):
#     pass
#
# def save():
#     place_to_save.update_save_info(song_queue)
#     place_to_save.save_place()
#
# def select_save():
#     """Displays available saves and returns the name of whichever the user selects"""
#     place_list = ""
#     for place in os.listdir("Assets/PlaceSaverFiles"):
#         place_list += place + " "
#     print(place_list)
#     return input("Type the name of the save you wish to select: ")
#
container = BooleanWrapper()
# playlist_list = []
#
# #Opening a save or making a new save
# if container.make_new_save:
#     place_to_save = PlaceSaver(input("Name the save: "))
#     #Move thumbnails to associated save folder
#     os.mkdir(f"{place_to_save.place_saver_directory_path}/PlaylistThumbs")
#     for thumbnail in os.listdir("Assets/PlaylistThumbs"):
#         permanent_thumb_path = f"{place_to_save.place_saver_directory_path}/PlaylistThumbs/{thumbnail}"
#         shutil.move(f"Assets/PlaylistThumbs/{thumbnail}", permanent_thumb_path)
# else:
#     place_to_save = PlaceSaver(select_save())
#
# #Creating playlist_list
# temp_thumbnail_path = f"{place_to_save.place_saver_directory_path}/PlaylistThumbs"
# for thumbnail in os.listdir(temp_thumbnail_path):
#     playlist_list.append(Playlist(place_to_save.place_saver_directory_path, f"{temp_thumbnail_path}/{thumbnail}"))
#
# #Creating song queue or getting song queue from saved place
# song_queue = place_to_save.song_queue
# if not song_queue:
#     song_queue = (os.listdir("Assets/MusicFolder"))
#     song_queue.remove(".gitkeep")
#
# #Main loop
# while song_queue:
#     #Playing and displaying info of next son
#     current_song = song_queue.pop()
#     tinytag_current_song = TinyTag.get(f"Assets/MusicFolder/{current_song}")
#     display_song_info(current_song)
#     MusicPlayer.play_song(current_song, 20)
#
#     #Take user input
#     print("\nSelect an option:")
#     choice = input("Please input an integer between 1 & 5: ")
#     try:
#         choice = int(choice)
#     except ValueError:
#         print("Choice must be an integer!")
#     else:
#         if choice == 1:
#             MusicPlayer.pause_song()
#         elif choice == 2:
#             #Next song (do nothing)
#             pass
#         elif choice == 3:
#             MusicPlayer.seek_song()
#         elif choice == 4:
#             playlist_num = input("Please input an integer between 1 & 5: ")
#             while True:
#                 print("\nSelect playlists:")
#                 playlist_num = input("Please input the number associated with each playlist, or q to go to the next song ")
#                 if playlist_num == "q":
#                     break
#                 try:
#                     choice = int(choice)
#                 except ValueError:
#                     print("Choice must be an integer!")
#                 else:
#                     playlist_list[playlist_num].add_song(tinytag_current_song)
#         elif choice == 5:
#             save()
#             break
#         elif choice > 5 or choice < 1:
#             print("Choice must be between 1 & 5")
# save()
#
m3uquick = QApplication(sys.argv)
window = StartWindow(container)
m3uquick.exec()

