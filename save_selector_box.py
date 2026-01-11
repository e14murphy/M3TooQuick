"""The SaveSelectorBox class extends QSpinBox to allow it to display string values in the window at runtime,
where each string represents a save option the user can start from.

Instance Variables:
    saves (list of strings): A list of the names of previous saves of the program, plus an option to start a new save.

Methods:
    textFromValue(v): Overwrites QSpinBox textFromValue(). Allows the spin box to display string values."""

import os
from PyQt6.QtWidgets import QSpinBox

class SaveSelectorBox(QSpinBox):
    def __init__(self, parent = None):
        super(SaveSelectorBox, self).__init__(parent)
        #list of saves + make new save option, used to select starting point in main window
        self.saves = ["Start New Save..."] + os.listdir("Assets/PlaceSaverFiles")
        self.setMaximum(len(self.saves)-1)

    #Overwriting textFromValue() so the spinbox displays save options as values
    def textFromValue(self, v):
        """Overwrite QSpinBox textFromValue() to display string values."""
        print(v)
        return self.saves[v]

