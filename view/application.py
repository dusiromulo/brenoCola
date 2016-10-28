from PyQt5.QtWidgets import QApplication, QListWidgetItem
from PyQt5.QtCore import pyqtSignal
from view.main_window import MainWindow
from controller.paste_event_signal import PasteEventSignal


class BrenoColaApplication(QApplication):
    STATES = {
        "NONE": 0,
        "STACK": 1,
        "LIST": 2,
        "CONCAT": 3,
        "RANDOM": 4
    }
    paste_signal = pyqtSignal()

    def __init__(self, argv):
        super(BrenoColaApplication, self).__init__(argv)
        self.__state = self.STATES["NONE"]
        self.__list_elements = []
        self.__clipb = self.clipboard()
        self.__clipb.dataChanged.connect(self.copy)
        self.__ignore_paste = False

        self.w = MainWindow()
        self.w.window.stackRadioButton.toggled.connect(lambda toggle:
                                                       self.change_state(toggle, self.STATES["STACK"]))

        self.w.window.listRadioButton.toggled.connect(lambda toggle:
                                                      self.change_state(toggle, self.STATES["LIST"]))
        self.w.window.concatRadioButton.toggled.connect(lambda toggle:
                                                        self.change_state(toggle, self.STATES["CONCAT"]))
        self.w.window.randomRadioButton.toggled.connect(lambda toggle:
                                                        self.change_state(toggle, self.STATES["RANDOM"]))

        self.paste_signal.connect(self.paste)
        self.thread_listen_paste = PasteEventSignal(self, self.paste_signal)
        self.thread_listen_paste.start()
        self.update_info_labels()

    def update(self):
        self.w.window.listWidget.repaint()
        self.update_info_labels()

    def update_info_labels(self):
        self.w.window.bufferSizeValueLabel.setText(str(len(self.__list_elements)))
        total = 0
        for elem in self.__list_elements:
            total += len(elem)
        self.w.window.totalBytesValueLabel.setText(str(total))

    def change_state(self, toggle, state):
        if toggle:
            self.__state = state

    def paste(self):
        self.__ignore_paste = True
        if self.__state == self.STATES["NONE"]:
            if len(self.__list_elements) > 0:
                item = self.__list_elements[0]
                self.__clipb.setText(item)
        elif self.__state == self.STATES["STACK"] or self.__state == self.STATES["LIST"]:
            if len(self.__list_elements) > 0:
                item_to_rmv = self.__list_elements[0]
                if len(self.__list_elements) > 1:
                    item = self.__list_elements[1]
                    self.__clipb.setText(item)
                else:
                    self.__clipb.setText("")
                self.w.window.listWidget.takeItem(0)
                self.__list_elements.remove(item_to_rmv)
        self.update()

    def copy(self):
        mimedata = self.__clipb.mimeData()
        text = None
        # if mimedata.hasImage():
        #     image_data = mimedata.imageData()
        #     print("has image")mage
        # elif mimedata.hasHtml():
        #     html = mimedata.html()
        #     print("has html " + html)
        # el
        if self.__ignore_paste:
            self.__ignore_paste = False
            return

        if mimedata.hasText():
            text = mimedata.text()
        # else:
        #     print("has other thing")
        if text is None or text == "":
            return

        if self.__state == self.STATES["NONE"]:
            if len(self.__list_elements) > 0:
                old_item = self.__list_elements[0]
                self.w.window.listWidget.takeItem(0)
                self.__list_elements.remove(old_item)

            QListWidgetItem(text, self.w.window.listWidget)
            self.__list_elements.append(text)

        elif self.__state == self.STATES["STACK"]:
            new_item = QListWidgetItem(text)
            self.w.window.listWidget.insertItem(0, new_item)
            self.__list_elements.insert(0, text)

        elif self.__state == self.STATES["CONCAT"]:
            if len(self.__list_elements) > 0:
                item = self.w.window.listWidget.item(0)
                item_text = item.text() + text
                item.setText(item_text)
                self.__list_elements[0] = item_text
                self.__ignore_paste = True
                self.__clipb.setText(item_text)
            else:
                QListWidgetItem(text, self.w.window.listWidget)
                self.__list_elements.append(text)
        self.update()
