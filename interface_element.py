__author__ = 'Roland'
from PyQt4 import QtGui
from types_controller import TypeController


class InterfaceElement(QtGui.QWidget):

    def __init__(self, type, data):
        super().__init__()
        self.type = type
        self.data = data
        self.draw_function = TypeController().get_function(type)

    def draw(self, frame):
        self.draw_function(frame, self.data)
        pass