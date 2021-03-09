import numpy as np
from qimage2ndarray import array2qimage
from PyQt5.QtGui import QPainterPath
from PyQt5.QtCore import QTimer, Qt, QRect
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel, QWidget, QFrame


# constant to allign

STRIDE = 10

# this class is conceptually part of the view mixed with controller code.
# essentially, it's responsible for defining the part of the interface dedicated
# to the display and managing the dialogue between the view and model.

class DisplayWidget(QWidget):

    def __init__(self, model, lenghtPx, widthPx):

        QWidget.__init__(self)
        self.model = model
        self.width, self.lenght = 100, 200
        self.widthPx = widthPx
        self.lenghtPx = lenghtPx

        self.pos = np.full((self.width, self.lenght, 3), 255)
        self.historyPos = np.zeros((self.width, self.lenght))
        self.historyColor = np.full((self.width, self.lenght, 3), 255)
        self.path = QPainterPath()

        # conversion to pos array -> Qimage -> pixmap -> label
        self.QIm = self.arrayToQImage(self.pos)
        self.pixMap = QPixmap(self.QIm)
        self.pixMap = self.pixMap.scaled(self.lenghtPx, self.widthPx)
        self.label = QLabel(self)
        self.setLabel()

        # parameters to zoom and adjust positions
        self.yZoom = self.width
        self.xZoom = self.lenght
        self.yDef = self.width / 2
        self.xDef = self.lenght / 2

        self.xStart = 0
        self.xEnd = self.lenght

        self.yStart = 0
        self.yEnd = self.width

        self.historyMode = False
        self.simulation_started = False
        self.timeBetweenGenerations = 0

        # register as an observer of the model
        model.register(self.updateState)

    # function called on value changed of the model that simply update
    # the board state.
    # "state" is a BoardState object.
    def updateState(self, state):

        self.pos = state.pos
        self.historyPos = state.historyPos
        self.historyColor = state.historyColor
        self.historyMode = state.historyMode
        self.timeBetweenGenerations = 1000 / int(state.fps)
        self.display()

        # print("update notify by model")

        return

    def setLabel(self):

        self.label.setPixmap(self.pixMap)
        self.label.setGeometry(QRect(STRIDE, STRIDE, self.lenghtPx, self.widthPx))
        self.label.setFrameShape(QFrame.Box)
        self.label.setFrameShadow(QFrame.Sunken)
        self.label.show()

    # function triggered by play button that change flag value and start
    # the game simulation
    def play(self):
        if not self.simulation_started:
            self.simulation_started = True
            self.generation()
        else:
            self.simulation_started = False

    # functions triggered by mouse click and move that change cell's value
    def mousePressEvent(self, event):

        self.path.moveTo(event.pos())
        posY = (int(self.path.currentPosition().y())) - STRIDE
        posX = (int(self.path.currentPosition().x())) - STRIDE
        if event.button() == Qt.LeftButton:
            self.setPos(posY, posX)
        elif event.button() == Qt.RightButton:
            self.delPos(posY, posX)

        #self.display()

    def mouseMoveEvent(self, event):

        self.path.lineTo(event.pos())
        posY = (int(self.path.currentPosition().y())) - STRIDE
        posX = (int(self.path.currentPosition().x())) - STRIDE

        self.setPos(posY, posX)

        #self.display()

    def setPos(self, y, x):

        posY, posX = self.adjustPos(y, x)
        if 0 <= posY < self.yZoom and 0 <= posX < self.xZoom:
            self.model.setPos(posY + self.yStart, posX + self.xStart)

    def adjustPos(self, y, x):

        y = int((self.yZoom * y) / self.widthPx)
        x = int((self.xZoom * x) / self.lenghtPx)

        return y, x

    # zoom effect is realized by calculating a submatrix of the value
    # to be shown
    def zoomAdjust(self, value):

        self.xZoom = int(self.xDef + value)
        self.yZoom = int(self.yDef * (100 + value) / 100)

        self.xStart = int(self.xZoom / 2)
        self.xStart = int((self.lenght / 2) - self.xStart)
        self.xEnd = int(self.lenght - self.xStart)

        self.yStart = int(self.yZoom / 2)
        self.yStart = int((self.width / 2) - self.yStart)
        self.yEnd = int(self.width - self.yStart)

        self.display()

    def delPos(self, y, x):

        posY, posX = self.adjustPos(y, x)
        if 0 <= posY < self.yZoom and 0 <= posX < self.xZoom:
            self.model.delPos(posY + self.yStart, posX + self.xStart)

    # conversion np array of values to QImage
    def arrayToQImage(self, npArray):

        QImage = array2qimage(npArray)
        return QImage

    # function that updates and shows the label
    def display(self):
        if self.historyMode:
            toDisplay = self.historyColor[self.yStart:self.yEnd, self.xStart:self.xEnd, 0:3]
        else:
            toDisplay = self.pos[self.yStart:self.yEnd, self.xStart:self.xEnd, 0:3]

        self.QIm = self.arrayToQImage(np.require(toDisplay, requirements='C'))
        self.pixMap = QPixmap(self.QIm)
        self.pixMap = self.pixMap.scaled(self.lenghtPx, self.widthPx)
        self.label.setPixmap(self.pixMap)
        self.label.show()

    # function triggered by the view's clearbutton that resets the start flag and
    # calls the model's clear function
    def clear(self):

        self.simulation_started = False

        self.model.clear()

    # recursive function(based on fps) called by play that calls the
    # model function to compute the next state
    def generation(self):

        if self.simulation_started:

            self.model.nextState()

            QTimer.singleShot(self.timeBetweenGenerations, self.generation)


