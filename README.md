### Project details
This is project work for the course DD1331 - Fundamentals of programming at KTH. It is an implementation of the game of Nim with a graphical, clickable interface, using pyqt5.
Note that the rest of the Readme is in swedish as was expected for the course.
The last commit to this work was made on oct 18 2018.

# Specifikation
## Inledning
Jag har för avsikt att programmera ett simpelt program som kan spela spelet NIM mot en användare via ett grafiskt användargränssnitt. Programmet ska startas från en terminal och sedan ritas upp i ett separat fönster, som användare ska man bemötas av en meny där man kan välja svårighetsgrad och startordning samt läsa lite om spelets regler eller kuriosa genom att trycka på frågetecknet i det övre högra hörnet. De två svårighetsgraderna är "Amatör" och "Omöjlig" där amatör motsvarar slumpmässigt spelande av datorn och omöjlig motsvarar den optimala strategin som innebär att det inte går att vinna om man börjar. De största svårigheterna kommer troligtvis vara att programmera den algoritm som styr datorns "Omöjlig"-nivå och att få den att återkoppla till användargränssnittet.

## Användarscenario
Johnny är en inbiten datorspelsnörd och när han får reda på att ett av de första datorspelen nånsin, skapat av Pavel Pelikan i dåvarande Tjeckoslovakien på 60-talet, finns rekonstruerat med ett simpelt användargränssnitt hämtar han genast hem koden. Han läser igenom reglerna för spelet och väljer sedan att testa sin lycka på svårighetsgraden "Amatör", efter ett par matcher känner han att han börjar förstå spelet lite bättre och svårighetsgraden börjar bli lätt, kaxigt trycker han på "Omöjlig"...hur svårt kan det va? 20 minuter senare ger han upp, djupt imponerad av datorns överlägsenhet väljer han att trycka på frågetecknet ännu en gång och läsa på lite om den algoritm som besegrat honom gång på gång. Med en känsla av att ha lärt sig något och att få upplevt lite datorspelshistoria stänger han ner programmet och går vidare med sitt, numera lite bättre, liv.

## Kodskelett
```
class Ui_MainWindow(object):
  """The Ui is run in the MainWindow"""
  def setupUi(self, MainWindow):
  """Creates the Main window that is displayed and all the buttons and their functions"""
    pass
  def cardClicked(self):
  """Defines how cards are removed and how they affect the lists contained in "Game" when pressed"""
    pass
  def startButtonClicked(self):
  """Defines what happens when the startButton is clicked", that is to say: starts the game""
    pass
  def finishedButtonClicked(self):
  """Defines what happens when the finishedButton is clicked, that is to say: let the computer play"""
    pass
  def aiClicker(self, row, cards):
  """Allows the computer to "click" on cards, takes two arguments: the row from which to pick cards and the amount of cards to pick"""
    pass
  def resetBoard(self):
  """Resets all the cards which has been clicked to their original position, is called when the game ends to allow for another game"""
    pass 
  def open_informativeWindow(self):
  """Creates new window with information about the rules and the history of the game, opens dialogwindow from separate file        	   "Informative_Window.py"""
    pass
  def open_endgameWindow(self):
  """Creates new window which displays the winner, opens dialogwindow from separate file "endgame_Window.py"""
    pass
  def open_illegalmoveWindow(self):
  """Creates new window stating that the player's move was illegal, opens dialogwindow from separate file "illegalmove_Window.py"
    pass

class Game(object):
"""The game that runs underneath the UI, has the list "values" as an attribute which describes the current game state"""
  def setupGame(self):
  """Sets the starting position of the game"""
    pass
  def nimSum(self, values):
  """Acts as a helper function for "bestMove" and finds the so called nim sum of the current state of the game(values)"""
    pass
  def bestMove(self, values)
    """Determines what the best move are for the current game state(values) with help from the "nimSum" function"""
      pass
  def goodAi(self):
  """Describes how the computer plays when difficulty is set to "Omöjlig" by using the "nimSum" and "bestMove" helper functions. Returns   the row and the amount of cards to be clicked by "aiClicker" """
    pass
  def badAi(self):
  """Describes how the computer plays when difficulty is set to "Amatör". Returns the row and the amount of cards to be clicked by
  "aiClicker" """
    pass    
    def gameEngine(self, values):
  """Runs the game and controls that every move follows the rules, displays winner and ends game when finished"""
    pass
  
```

# Programflöde och dataflöde
Programmet börjar med att skapa ett MainWindow och sätta startvärdena för spelet. Spelet startas då spelaren trycker på start avslutas då en vinnare blivit korad, då skapas ett endgameWindow och såväl fönstret som spelets värden återställs till ursprungsläget. När man trycker på ett kort anropas cardClicked-funktionen och kortet göms samt stängs av i fönstret och spelvärdena ändras. När man trycker på klar-knappen blir det datorns tur att spela och spelmotorn tar hand om det genom att anropa good/bad-Ai beroende på vilken svårighetsgrad man satt.
Trycker man på frågetecknet kallas "open_informativeWindow" och ett separat fönster skapas som körs oberoende av spelet. Detta fönster kodas i en separat fil "Informative_Window.py" som importeras i början av koden och samma sak gäller även för såväl endgameWindow som illegalmoveWindow vilka kallas från spelmotorn vid behov. 

