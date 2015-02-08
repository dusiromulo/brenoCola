#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
ZetCode PyQt4 tutorial 

In this example, we create a simple
window in PyQt4.

author: Jan Bodnar
website: zetcode.com 
last edited: October 2011
"""

import sys
from PyQt4 import QtGui, QtCore
from frame_controller import FrameController
from interface_element import InterfaceElement
from pprint import pprint
app = None


class ClipboardEvent():

    def __init__(self, text, clip):
        self.clip = clip;
        self.clip.dataChanged.connect(self.on_data_change)
        self.clip.setText(text)

    def on_data_change(self):
        interface_elem = InterfaceElement('clipboard_entry', self.clip.text())
        frame = FrameController().get_frame('clipboard_stack')
        frame.add_element(interface_elem)


def main():
    global app
    app = QtGui.QApplication(sys.argv)
    clip = app.clipboard()
    frame_controller = FrameController()
    frame = frame_controller.get_frame('clipboard_stack')

    clip.dataChanged.connect(call_event)
    sys.exit(app.exec_())


def call_event():
    ClipboardEvent(app.clipboard().text(), app.clipboard())

if __name__ == '__main__':
    main()