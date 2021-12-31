#!/usr/bin/python3
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.resize(640, 450)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(5, 0, 630, 130))
        self.label.setStyleSheet("font: 57 12pt \"Ubuntu\";")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(5, 140, 630, 240))
        self.label_2.setStyleSheet("font: 57 italic 11pt \"Ubuntu\";")
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Information"))

        self.label.setText(_translate("Dialog", "Regler:\n"
"Varje spelare turas om att välja valfri mängd kort från en rad. Man får ej ta kort från\n"
"fler än en rad åt gången och man måste ta minst ett kort varje omgång. \n"
"Spelets mål är att ta det sista kortet.\n"
"Svårighetsgrad och startspelare kan ställas in till höger.\n"
"Spelet börjar när du trycker på startknappen och när du gjort ditt drag\n"
"måste du trycka på \"klar\" "))

        self.label_2.setText(_translate("Dialog", "Kuriosa:\n"
"Det här spelet torde vara ett av de första datorspelen som byggts.\n"
"I början av sextiotalet gick en doktorand vid namn Pavel Pelikan på tekniska högskolan i\n"
"Prag, i dåvarande Tjeckoslovakien.\n"
"Pavel fick höra om spelet och gillade det. Medan han var vakt i lumpen klurade han \n"
"ut spelets vinnande algoritm, för att på högskolan hitta på och rita kretsschemat\n"
"för spelet. Han lödde ihop maskinen som spelade nim och som alltid vann. \n"
"En tidning publicerade en serie om hurman bygger nimspelet själv och maskinen fick\n"
"komma ända till Tekniska museet i Paris, där den väl står och samlar damm på vinden än i dag.\n"
"Det här programmets \"omöjliga\" svårighetsgrad bygger på just den algoritmen och\n"
"kan därför aldrig förlora. Så länge du börjar det vill säga, låter du datorn börja\n"
"så har du fördelen och behöver \"bara\" spela perfekt för att vinna!"))

        QtCore.QMetaObject.connectSlotsByName(Dialog)
