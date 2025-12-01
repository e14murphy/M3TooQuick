"""The txt_manip module provides methods that will be commonly used in this program for reading and
writing data from files.

Methods:
    file_to_list(filepath) (returns list): Returns a list of strings in which each string has the text from a line in a file, without newline escape sequences.
    list_to_file(list_of_text, filepath): Makes a new file or overwrites a file with empty space, and writes a list to the text file in which each element in a list of strings becomes a line in the file.
    append_line_to_file(line, filepath): Writes a line to a file on a new line.
"""


def file_to_list(filepath):
    """Returns a list of strings in which each string has the text from a line in a file, without newline escape sequences."""
    with open(filepath, "r") as file:
        new_list = [line.strip() for line in file.readlines()]
    return new_list

def list_to_file(list_of_text, filepath):
    """Makes a new file or overwrites a file with empty space, and writes a list to the text file in which each element in a list of strings becomes a line in the file."""
    with open(filepath, "w") as file:
        for line in list_of_text:
            file.write(line + "\n")

def append_line_to_file(line, filepath):
    """Writes a line to a file on a new line."""
    with open(filepath, "a") as file:
        file.write(line)
