from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import Qt
from view.main_view import Ui_MainOptionsWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__(None, Qt.WindowStaysOnTopHint)
        self.window = Ui_MainOptionsWindow()
        self.window.setupUi(self)
        self.setWindowTitle("Breno Cola")
        self.setWindowOpacity(0.6)
        self.show()
