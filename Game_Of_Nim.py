#!/usr/bin/python3
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
from Informative_Window import Ui_Dialog as IWindow
from Endgame_Window import Ui_Dialog as EGWindow
from Illegalmove_Window import Ui_Dialog as IMWindow
from time import sleep
import random



class Ui_MainWindow(QMainWindow):
    """The GUI class which contains all functionality in regards to the main window."""
    def setupUi(self, MainWindow):
        """Sets the UI for the Mainwindow, containing all its buttons and attributes"""
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(570, 450)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.QuestionMarkButton = QtWidgets.QPushButton(self.centralwidget)
        self.QuestionMarkButton.setGeometry(QtCore.QRect(510, 10, 30, 30))
        self.QuestionMarkButton.setText("?")
        font = QtGui.QFont()
        font.setFamily("Serif")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.QuestionMarkButton.setFont(font)
        self.QuestionMarkButton.setCursor(QtGui.QCursor(QtCore.Qt.WhatsThisCursor))
        self.QuestionMarkButton.setAutoFillBackground(False)
        self.QuestionMarkButton.setFlat(True)
        self.QuestionMarkButton.clicked.connect(lambda: self.open_informativeWindow())

        self.btnlist1 = []
        self.btnlist2 = []
        self.btnlist3 = []
        self.btnlist4 = []
        self.btnlists = [self.btnlist1, self.btnlist2, self.btnlist3, self.btnlist4]
        """The for loop creates the card buttons and assigns them to a buttonlist corresponding to their row"""
        for row in range(4):
            cards = 1 + (row*2)
            for card in range(cards):
                button = QtWidgets.QPushButton(self.centralwidget)
                button.setGeometry(QtCore.QRect(250+(50*card)-(50*row), 130+(70*row), 30, 60))
                button.setEnabled(False)
                if row == 0:
                    button.clicked.connect(lambda: self.cardClicked(str(0))) #The string here is a pointer to the row of the card
                    self.btnlist1.append(button)
                elif row == 1:
                    button.clicked.connect(lambda: self.cardClicked(str(1)))
                    self.btnlist2.append(button)
                elif row == 2:
                    button.clicked.connect(lambda: self.cardClicked(str(2)))
                    self.btnlist3.append(button)
                else:
                    button.clicked.connect(lambda: self.cardClicked(str(3)))
                    self.btnlist4.append(button)

        self.difficultyBox = QtWidgets.QGroupBox(self.centralwidget)
        self.difficultyBox.setGeometry(QtCore.QRect(370, 80, 190, 60))
        self.difficultyBox.setTitle("Svårighet")
        self.radioButton1_1 = QtWidgets.QRadioButton(self.difficultyBox)
        self.radioButton1_1.setGeometry(QtCore.QRect(10, 30, 80, 25))
        self.radioButton1_1.setChecked(True)
        self.radioButton1_1.setText("Amatör")
        self.radioButton1_2 = QtWidgets.QRadioButton(self.difficultyBox)
        self.radioButton1_2.setGeometry(QtCore.QRect(110, 30, 80, 25))
        self.radioButton1_2.setText("Omöjlig")

        self.starterBox = QtWidgets.QGroupBox(self.centralwidget)
        self.starterBox.setGeometry(QtCore.QRect(370, 160, 190, 60))
        self.starterBox.setTitle("Startspelare")
        self.radioButton2_1 = QtWidgets.QRadioButton(self.starterBox)
        self.radioButton2_1.setGeometry(QtCore.QRect(10, 30, 100, 25))
        self.radioButton2_1.setChecked(True)
        self.radioButton2_1.setText("Utmanaren")
        self.radioButton2_2 = QtWidgets.QRadioButton(self.starterBox)
        self.radioButton2_2.setGeometry(QtCore.QRect(110, 30, 80, 25))
        self.radioButton2_2.setText("Datorn")

        self.FinishedButton = QtWidgets.QPushButton(self.centralwidget)
        self.FinishedButton.setGeometry(QtCore.QRect(60, 170, 90, 25))
        self.FinishedButton.setText("Klar")
        self.FinishedButton.setEnabled(False)
        self.FinishedButton.clicked.connect(lambda: Game.gameEngine())

        self.RegretButton = QtWidgets.QPushButton(self.centralwidget)
        self.RegretButton.setGeometry(QtCore.QRect(60, 200, 90, 25))
        self.RegretButton.setText("Ångra")
        self.RegretButton.setEnabled(False)
        self.RegretButton.clicked.connect(lambda: self.resetState())

        self.StartButton = QtWidgets.QPushButton(self.centralwidget)
        self.StartButton.setGeometry(QtCore.QRect(80, 90, 140, 40))
        self.StartButton.setStyleSheet("font: 75 13pt \"URW Bookman L\";")
        self.StartButton.setText("Starta spelet!")
        self.StartButton.clicked.connect(lambda: self.start())

        self.Title = QtWidgets.QLabel(self.centralwidget)
        self.Title.setGeometry(QtCore.QRect(170, 0, 230, 80))
        font = QtGui.QFont()
        font.setFamily("URW Chancery L")
        font.setPointSize(32)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.Title.setFont(font)
        self.Title.setObjectName("Title")
        self.Title.setText("Game Of Nim")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setEnabled(True)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    @classmethod
    def open_endGameWindow(cls, current_player, difficulty):
        """Creates a new window with UI from separate file 'Endgame_Window', sends it the current player
        and difficulty so it can display the corresponding end game window. Is called from the game engine
        when the game is over."""
        dialog = QtWidgets.QDialog()
        dialog.ui = EGWindow
        dialog.ui.setupUi(cls, dialog, current_player, difficulty)
        dialog.exec_()
        dialog.show()

    @classmethod
    def open_informativeWindow(cls):
        """Creates a new window with UI from separate file 'Informative_Window which contains the rules
        and some trivia. Is called from the question mark button in the top right corner of the main window."""
        dialog = QtWidgets.QDialog()
        dialog.ui = IWindow
        dialog.ui.setupUi(cls, dialog)
        dialog.exec_()
        dialog.show()

    @classmethod
    def open_illegalMoveWindow(cls):
        """Creates a new window with UI from separate file 'Illegalmove_Window' which notifies the user that he/she
        made a invalid move."""
        dialog = QtWidgets.QDialog()
        dialog.ui = IMWindow
        dialog.ui.setupUi(cls, dialog)
        dialog.exec_()
        dialog.show()

    def start(self):
        """Starts the game and sets the correct difficulty and starting player based upon user's choice.
        Is called from the start button."""
        Game.setupGame()
        self.FinishedButton.setEnabled(True)
        self.RegretButton.setEnabled(True)
        for btnlist in self.btnlists:   #shows all the card buttons
            for btn in btnlist:
                btn.show()
                btn.setEnabled(True)
        if self.radioButton1_2.isChecked():
            Game.difficulty = "Omöjlig"
        if self.radioButton2_2.isChecked():
            Game.current_player = "Datorn"
            sleep(0.3)
            Game.badAi()

    def cardClicked(self, row):
        """Hides the card buttons when they are pressed and removes one card from the value of the row
        the button was in. Also stores the button in the memory in case the user regrets his/her move or
        the move is invalid."""
        Game.memory.append(self.sender())
        self.sender().hide()
        Game.values[int(row)] = Game.values[int(row)] - 1

    @classmethod
    def aiClicker(cls, move):
        """Allows the computer to 'click' on cards. Takes the move the computer wants to make as a argument
        and then makes that move. Will always take cards from left to right.
        Is called from the bad and goodAi functions."""
        iter = 0
        row = move[0]
        cards = move[1]
        btnlist = ui.btnlists[row]
        for btn in btnlist:
            if btn.isHidden() == False:
                btn.hide()
                Game.values[row] = Game.values[row] - 1
                iter += 1
                if iter == cards:
                    break
        Game.oldvalues = list(Game.values)

    @classmethod
    def resetState(cls):
        """Resets the board to its previous state by hiding the buttons and values stored in the memory.
        Is called from the user through the 'regret' button or from the game engine in the event of an invalid move"""
        for btn in range(len(Game.memory)):
            if Game.memory[btn].isHidden() == True:
                Game.memory[btn].show()
        Game.values = list(Game.oldvalues)
        Game.memory = []


class Game(object):
    """A class that contains the functionality and attributes associated with the underlying game."""
    @classmethod
    def setupGame(cls):
        """Sets the starting attributes of the game, defaults to the user as the starting player and
        the difficulty to be set to novice. Is called from the start button."""
        cls.current_player = "Utmanaren"
        cls.difficulty = "Amatör"
        cls.values = [1, 3, 5, 7]
        cls.oldvalues = [1, 3, 5, 7]
        cls.controll = [0, 0, 0, 0]
        cls.memory = []

    def isLegalmove(values, oldvalues):
        """Controlls wether or not the users move was invalid. Takes a list which describes the current
        state of the board (values) and a list which describes the state of the board before the last move (oldvalues).
        If exactly one row was changed it returns True, otherwise it defaults to False."""
        changedRows = 0
        for iter in range(len(values)):
            if oldvalues[iter] - values[iter] != 0:
                changedRows += 1
        if changedRows == 1:
            return True
        return False

    @classmethod
    def badAi(cls):
        """Defines how the computer plays when the difficulty is set to novice, is also used on 'impossible'
        difficulty in the event that the computer makes the first move. Will make random moves unless a
        move that directly allows it to win presents itself. Is called from the game engine and the start button."""
        n_rows = 0
        rows = []
        for row in range(len(cls.values)):
            if cls.values[row] != 0:
                n_rows += 1
                rows.append(row)
        if n_rows == 1:   #If there is only one row left the computer will win the game. It's a novice, not a complete idiot.
            row = rows[0]
            cards = cls.values[row]
        else:
            row = rows[random.randint(0, n_rows-1)]
            n_cards = cls.values[row]
            try:
                cards = random.randint(1, n_cards)
            except ValueError:
                cards = 1
        move = (row, cards)
        Ui_MainWindow.aiClicker(move)
        cls.oldvalues = list(cls.values) #Updates the state of the game

    @classmethod
    def goodAi(cls):
        """Defines how the computer plays when the difficulty is set to impossible. Uses xor operator
        to decide which move, if there is one, returns the state of the game to a 'balanced' state and
        therefore a winning state for the computer. If there is no winning move it defaults to removing one
        card from the row with most cards left as to leave the user with the most complex board possible.
        Is called from the game engine."""
        binValues = []
        nimValues = []
        for row in range(len(cls.values)):
            binValues.append(int(bin(cls.values[row])[2:].zfill(3))) #zfill is used to ensure all values has the same amount of bits
        nimSum = bin(binValues[0] ^ binValues[1] ^ binValues[2] ^ binValues[3])[2:].zfill(3)
        for row in range(len(binValues)):
            nimValues.append(bin((int(nimSum, base=2)) ^ binValues[row])[2:].zfill(3))
            if int(nimValues[row], base=2) < cls.values[row]:
                cards = cls.values[row] - int(nimValues[row], base=2)
                return row, cards
        max_row = 0
        cards = 0
        for row in range(len(cls.values)): #Default move if no optimal move is found
            if cls.values[row] > cards:
                cards = cls.values[row]
                max_row = row
        return max_row, 1

    @classmethod
    def gameEngine(cls):
        """Checks the current state of the game and the last move to decide upon what should follow.
        Displays the illegal move window or the correct end game window if appropriate, updates the state
        of the board after the users move(if valid) and sends a move to the 'aiClicker' based upon the chosen difficulty.
        Is called from the 'finished' button"""
        if cls.isLegalmove(cls.values, cls.oldvalues):
            cls.oldvalues = list(cls.values)
            cls.memory = [] #clears the memory as it's only supposed to contain the buttons used in the current move.
            if cls.values != cls.controll:
                cls.current_player = "Datorn"
                if cls.difficulty == "Amatör":
                    cls.badAi()
                    if cls.values != cls.controll:
                        cls.current_player = "Utmanaren"
                    else:
                        Ui_MainWindow.open_endGameWindow(cls.current_player, cls.difficulty)
                else:
                    Ui_MainWindow.aiClicker(cls.goodAi())
                    if cls.values!= cls.controll:
                        cls.current_player = "Utmanaren"
                    else:
                        Ui_MainWindow.open_endGameWindow(cls.current_player, cls.difficulty)
            else:
                Ui_MainWindow.open_endGameWindow(cls.current_player, cls.difficulty)
        else:
            Ui_MainWindow.resetState()
            Ui_MainWindow.open_illegalMoveWindow()


if __name__ == "__main__":  #Starts the program and creates the main window.
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
