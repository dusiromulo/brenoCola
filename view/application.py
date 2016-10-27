from PyQt5.QtWidgets import QApplication, QListWidgetItem
from PyQt5.QtCore import pyqtSignal, pyqtSlot
from view.main_window import MainWindow
from controller.paste_event_signal import PasteEventSignal


class BrenoColaApplication(QApplication):
    STATES = {"NONE": 0,
              "STACK": 1,
              "LIST": 2,
              "REVERT": 3,
              "RANDOM": 4}
    paste_signal = pyqtSignal()

    def __init__(self, argv):
        super(BrenoColaApplication, self).__init__(argv)
        self.__state = self.STATES["NONE"]
        self.__list_elements = []
        self.__clipb = self.clipboard()
        self.__clipb.dataChanged.connect(self.clip_data_changed)
        self.__last_buff = None

        self.w = MainWindow()
        self.w.window.stackRadioButton.toggled.connect(lambda toggle:
                                                       self.change_state(toggle, self.STATES["STACK"]))

        self.w.window.listRadioButton.toggled.connect(lambda toggle:
                                                      self.change_state(toggle, self.STATES["LIST"]))
        self.w.window.revertRadioButton.toggled.connect(lambda toggle:
                                                        self.change_state(toggle, self.STATES["REVERT"]))
        self.w.window.randomRadioButton.toggled.connect(lambda toggle:
                                                        self.change_state(toggle, self.STATES["RANDOM"]))

        self.paste_signal.connect(self.paste)
        self.thread_listen_paste = PasteEventSignal(self, self.paste_signal)
        self.thread_listen_paste.start()

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

    @pyqtSlot()
    def paste(self):
        if self.__state == self.STATES["NONE"]:
            if len(self.__list_elements) > 0:
                item = self.__list_elements[0]
                self.__clipb.setText(item)
        elif self.__state == self.STATES["STACK"]:
            if len(self.__list_elements) > 0:
                item = self.__list_elements[0]
                self.__clipb.setText(item)
                self.w.window.listWidget.takeItem(0)
                self.__list_elements.remove(item)
        elif self.__state == self.STATES["REVERT"]:
            pass
        elif self.__state == self.STATES["LIST"]:
            if len(self.__list_elements) > 0:
                index = len(self.__list_elements) - 1
                item = self.__list_elements[index]
                self.__clipb.setText(item)
                self.w.window.listWidget.takeItem(index)
                self.__list_elements.remove(item)

        self.w.window.listWidget.repaint()
        self.update_info_labels()

    def clip_data_changed(self):
        mimedata = self.__clipb.mimeData()
        text = None
        # if mimedata.hasImage():
        #     image_data = mimedata.imageData()
        #     print("has image")
        # elif mimedata.hasHtml():
        #     html = mimedata.html()
        #     print("has html " + html)
        # el
        if mimedata.hasText():
            text = mimedata.text()
        # else:
        #     print("has other thing")
        if text is None:
            return
        elif self.__last_buff is None:
            self.__last_buff = text
        elif self.__last_buff == text:
            return

        self.__last_buff = text
        if self.__state == self.STATES["NONE"]:
            if len(self.__list_elements) > 0:
                old_item = self.__list_elements[0]
                self.w.window.listWidget.takeItem(0)
                self.__list_elements.remove(old_item)

            QListWidgetItem(text, self.w.window.listWidget)
            self.__list_elements.append(text)

        elif self.__state == self.STATES["STACK"] or self.__state == self.STATES["REVERT"]:
            new_item = QListWidgetItem(text)
            self.w.window.listWidget.insertItem(0, new_item)
            self.__list_elements.append(text)

        elif self.__state == self.STATES["LIST"]:
            QListWidgetItem(text, self.w.window.listWidget)
            self.__list_elements.append(text)
        self.w.window.listWidget.repaint()
        self.update_info_labels()
