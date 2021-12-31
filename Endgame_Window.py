#!/usr/bin/python3
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog, current_player, difficulty):
        Dialog.resize(380, 120)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 0, 350, 100))
        self.label.setStyleSheet("font: 75 14pt \"Ubuntu Mono\";")
        self.utskrift = ""
        if current_player == "Datorn":
            if difficulty == "Amatör":
                self.utskrift = "Osis, datorn klådde dig"
            if difficulty == "Omöjlig":
                self.utskrift = 'Osis, datorn klådde dig...\nKanske borde hålla dig till "Amatör"?'
        else:
            if difficulty == "Omöjlig":
                self.utskrift = "Snyggt jobbat utmanaren...\nDu vann!"
            else:
                self.utskrift = 'Snyggt jobbat utmanaren...\nDu vann!\nKanske dags att prova "Omöjlig"?'
        self.label.setText(self.utskrift)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
