__author__ = 'Roland'
from PyQt4 import QtGui


class TypeController():

    def __init__(self):
        self.dict_function_types = {}
        self.dict_function_types['clipboard_entry'] = self.draw_clipboard_entry

    def draw_clipboard_entry(self, frame, data):
        try:
            if frame.v_box_layout:
                pass
        except:
            frame.v_box_layout = QtGui.QVBoxLayout();
        blei_button = QtGui.QPushButton(data)
        blei_button.setStyleSheet("""QPushButton {color: blue;
                                        border: 1px solid #000000;}""")
        frame.v_box_layout.addWidget(blei_button)
        frame.setCentralWidget(QtGui.QWidget())
        frame.centralWidget().setLayout(frame.v_box_layout)

    def get_function(self, type):
        return self.dict_function_types[type]