# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'breno-qt/brenoCola/mainoptionswindow.ui'
#
# Created: Thu Oct 27 00:53:47 2016
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainOptionsWindow(object):
    def setupUi(self, MainOptionsWindow):
        MainOptionsWindow.setObjectName("MainOptionsWindow")
        MainOptionsWindow.setEnabled(True)
        MainOptionsWindow.resize(311, 603)
        font = QtGui.QFont()
        font.setFamily("Garuda")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        MainOptionsWindow.setFont(font)
        self.centralWidget = QtWidgets.QWidget(MainOptionsWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralWidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.centralWidgetLayout = QtWidgets.QVBoxLayout()
        self.centralWidgetLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.centralWidgetLayout.setObjectName("centralWidgetLayout")
        self.listWidget = QtWidgets.QListWidget(self.centralWidget)
        self.listWidget.setObjectName("listWidget")
        self.centralWidgetLayout.addWidget(self.listWidget)
        self.optionsAreaLayout = QtWidgets.QHBoxLayout()
        self.optionsAreaLayout.setObjectName("optionsAreaLayout")
        self.groupBox = QtWidgets.QGroupBox(self.centralWidget)
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setContentsMargins(0, 10, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.stackRadioButton = QtWidgets.QRadioButton(self.groupBox)
        self.stackRadioButton.setObjectName("stackRadioButton")
        self.verticalLayout.addWidget(self.stackRadioButton)
        self.listRadioButton = QtWidgets.QRadioButton(self.groupBox)
        self.listRadioButton.setObjectName("listRadioButton")
        self.verticalLayout.addWidget(self.listRadioButton)
        self.revertRadioButton = QtWidgets.QRadioButton(self.groupBox)
        self.revertRadioButton.setObjectName("revertRadioButton")
        self.verticalLayout.addWidget(self.revertRadioButton)
        self.randomRadioButton = QtWidgets.QRadioButton(self.groupBox)
        self.randomRadioButton.setObjectName("randomRadioButton")
        self.verticalLayout.addWidget(self.randomRadioButton)
        self.optionsAreaLayout.addWidget(self.groupBox)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.bufferSizeValueLabel = QtWidgets.QLabel(self.centralWidget)
        self.bufferSizeValueLabel.setText("")
        self.bufferSizeValueLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.bufferSizeValueLabel.setObjectName("bufferSizeValueLabel")
        self.gridLayout.addWidget(self.bufferSizeValueLabel, 0, 1, 1, 1)
        self.bufferSizeLabel = QtWidgets.QLabel(self.centralWidget)
        self.bufferSizeLabel.setMaximumSize(QtCore.QSize(66, 66))
        self.bufferSizeLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.bufferSizeLabel.setWordWrap(True)
        self.bufferSizeLabel.setObjectName("bufferSizeLabel")
        self.gridLayout.addWidget(self.bufferSizeLabel, 0, 0, 1, 1)
        self.totalSizeBytes = QtWidgets.QLabel(self.centralWidget)
        self.totalSizeBytes.setMaximumSize(QtCore.QSize(66, 66))
        self.totalSizeBytes.setAlignment(QtCore.Qt.AlignCenter)
        self.totalSizeBytes.setWordWrap(True)
        self.totalSizeBytes.setObjectName("totalSizeBytes")
        self.gridLayout.addWidget(self.totalSizeBytes, 1, 0, 1, 1)
        self.totalBytesValueLabel = QtWidgets.QLabel(self.centralWidget)
        self.totalBytesValueLabel.setText("")
        self.totalBytesValueLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.totalBytesValueLabel.setObjectName("totalBytesValueLabel")
        self.gridLayout.addWidget(self.totalBytesValueLabel, 1, 1, 1, 1)
        self.optionsAreaLayout.addLayout(self.gridLayout)
        self.centralWidgetLayout.addLayout(self.optionsAreaLayout)
        self.verticalLayout_2.addLayout(self.centralWidgetLayout)
        MainOptionsWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainOptionsWindow)
        QtCore.QMetaObject.connectSlotsByName(MainOptionsWindow)

    def retranslateUi(self, MainOptionsWindow):
        _translate = QtCore.QCoreApplication.translate
        MainOptionsWindow.setWindowTitle(_translate("MainOptionsWindow", "MainOptionsWindow"))
        self.groupBox.setTitle(_translate("MainOptionsWindow", "Options"))
        self.stackRadioButton.setText(_translate("MainOptionsWindow", "Stack"))
        self.listRadioButton.setText(_translate("MainOptionsWindow", "List"))
        self.revertRadioButton.setText(_translate("MainOptionsWindow", "Revert"))
        self.randomRadioButton.setText(_translate("MainOptionsWindow", "Random LOL"))
        self.bufferSizeLabel.setText(_translate("MainOptionsWindow", "Elements Size"))
        self.totalSizeBytes.setText(_translate("MainOptionsWindow", "Total Size Bytes"))
