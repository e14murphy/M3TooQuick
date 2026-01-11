import M3UQuickMainWindowWidgets
from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow

class StartWindow(QMainWindow):
    def __init__(self, container):
        super(StartWindow, self).__init__()
        self.widgets = M3UQuickMainWindowWidgets.UiMainWindow()
        self.widgets.setup_ui(self)
        #using lambda to wrap self.start_working_widget so I can pass container
        self.widgets.pushButton.clicked.connect(lambda: self.start_working_widget(container))
        self.show()

    def start_working_widget(self, container):
        if self.widgets.saveSelectorSpinBox.value == "Start New Save...":
            container.boolvar_mutator(True)

class WorkWidget(QMainWindow):
    def __init__(self):
        super(WorkWidget, self).__init__()
        uic.loadUi("Assets/UIFiles/M3UQuickWorkWidget.ui", self)


