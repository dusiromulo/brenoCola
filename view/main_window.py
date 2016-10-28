from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import Qt
from view.main_view import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__(None, Qt.WindowStaysOnTopHint)
        self.__transparency = 0.6
        self.window = Ui_MainWindow()
        self.window.setupUi(self)
        self.window.transparencySlider.valueChanged.connect(self.changed_transparency_value)
        self.window.transparencySlider.setValue(self.__transparency*100)
        self.setWindowTitle("Breno Cola")
        self.setWindowOpacity(self.__transparency)
        self.show()
        self.update_main_window_transparency()

    def update_main_window_transparency(self):
        self.window.transparencyValueLabel.setText(str(self.__transparency))
        self.setWindowOpacity(self.__transparency)

    def changed_transparency_value(self):
        value = 0.15 + (self.window.transparencySlider.value()/100.0)*0.85
        value = float("{0:.2f}".format(value))
        self.__transparency = value
        self.update_main_window_transparency()
