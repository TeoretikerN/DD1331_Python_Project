#!/usr/bin/python3
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.resize(280, 110)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 0, 250, 90))
        self.label.setStyleSheet("font: 75 14pt \"Ubuntu Mono\";")
        self.label.setText("Så där får man inte göra.\nProva igen!")
        QtCore.QMetaObject.connectSlotsByName(Dialog)
