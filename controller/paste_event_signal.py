from PyQt5.QtCore import QThread
from threading import Timer
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

    def toggle_key(self, key, toggled):
        if key == KeyCode(char="v"):
            self.pressed["v"] = toggled
        elif key == Key.ctrl:
            self.pressed[Key.ctrl] = toggled

    def on_press(self, key):
        self.toggle_key(key, 1)

    def on_release(self, key):
        if self.pressed["v"] and self.pressed[Key.ctrl]:
            Timer(0.1, lambda: self.paste_signal.emit()).start()
        self.toggle_key(key, 0)
