__author__ = 'Roland'
from PyQt4 import QtGui, QtCore


class Frame(QtGui.QMainWindow):

    def __init__(self, title, size_x, size_y, position_x, position_y):
        QtGui.QMainWindow.__init__(self, None, QtCore.Qt.WindowStaysOnTopHint | QtCore.Qt.FramelessWindowHint)
        self.title = title
        self.size_x = size_x
        self.size_y = size_y
        self.position_x = position_x
        self.position_y = position_y

        self.setWindowTitle(title)
        self.resize(size_x, size_y)
        self.move(position_x, position_y)
        # self.setWindowOpacity(0.5)
        self.show()

    def add_element(self, element):
        element.draw(self)

    def mousePressEvent(self, event):
        self.offset = event.pos()

    def mouseMoveEvent(self, event):
        x=event.globalX()
        y=event.globalY()
        x_w = self.offset.x()
        y_w = self.offset.y()
        self.move(x-x_w, y-y_w)