from PyQt5.QtCore import QThread, pyqtSignal
from pynput.keyboard import Key, Listener, KeyCode


class PasteEventSignal(QThread):
    def __init__(self, parent, paste_signal):
        super(PasteEventSignal, self).__init__(parent)
        self.paste_signal = paste_signal
        self.listener = None
        self.pressed = {Key.ctrl: 0, "v": 0}

    def run(self):
        with Listener(on_press=self.on_press,
                      on_release=self.on_release) as self.listener:
            self.listener.join()

    def on_press(self, key):
        if key == KeyCode(char="v"):
            if self.pressed[Key.ctrl] and not self.pressed["v"]:
                # EMIT SIGNAL
                self.paste_signal.emit()
                self.pressed["v"] = 1
        elif key == Key.ctrl:
            self.pressed[Key.ctrl] = 1

    def on_release(self, key):
        if key == KeyCode(char="v"):
            self.pressed["v"] = 0
        elif key == Key.ctrl:
            self.pressed[Key.ctrl] = 0
