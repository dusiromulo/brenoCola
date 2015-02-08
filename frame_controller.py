__author__ = 'Roland'
from frame import Frame
from interface_element import InterfaceElement


class FrameController():

    frames = {}

    def __init__(self):
        if not 'clipboard_stack' in self.frames:
            self.frames['clipboard_stack'] = self.create_clipboard_stack()

    def create_clipboard_stack(self):
        frame = Frame('Clipboard Stack', 300, 500, 0, 0)
        entry = InterfaceElement('clipboard_entry', "teste")
        frame.add_element(entry)
        return frame

    def get_frame(self, name):
        return self.frames[name]
