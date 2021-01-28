import numpy as np
from qimage2ndarray import array2qimage
from PyQt5.QtGui import QPainterPath
from PyQt5.QtCore import QSize, QTimer, Qt, QRect
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel, QWidget

# RGB color global definition

COLOR_BLACK = 0, 0, 0
COLOR_WHITE = 255, 255, 255

class Controller(QWidget):

    def __init__(self, model, label,  widthPx=400, lenghtPx = 575):

        QWidget.__init__(self)
        self.model = model
        self.width, self.lenght = self.model.getSize()
        self.widthPx = widthPx
        self.lenghtPx = lenghtPx
        self.pos = np.zeros((self.width, self.lenght, 3))
        self.historyColor = np.zeros((self.width, self.lenght, 3))
        self.QIm = self.arrayToQImage(self.pos)
        self.historyMode = False
        self.historyPos = np.zeros((self.width, self.lenght))
        self.pixMap = QPixmap(self.QIm)
        self.pixMap = self.pixMap.scaled(self.lenghtPx, self.widthPx)
        self.yZoom = 100
        self.xZoom = 200
        self.yDef = 50
        self.xDef = 100
        self.simulation_started = False
        self.fps = 60
        self.path = QPainterPath()
        self.label = QLabel(self)
        self.label.setPixmap(self.pixMap)
        self.label.setGeometry(QRect(10, 10, self.lenghtPx, self.widthPx))
        self.label.setFixedSize(self.lenghtPx, self.widthPx)
        self.label.show()
        
        self.xStart = 0#int((self.lenght / 2) - (100 / 2))
        self.xEnd = 200#self.xZoom + self.xStart

        self.yStart = 0#int((self.width / 2) - (50 / 2))
        self.yEnd = 100#self.yZoom + self.yStart

    def play(self):
        if not self.simulation_started:
            self.simulation_started = True
            self.generation()
        else:
            self.simulation_started = False

    def setFramerate(self, fps):

        self.fps = 1000/int(fps)



    def mousePressEvent(self, event):


        self.path.moveTo(event.pos())
        posY = (int(self.path.currentPosition().y())) - 10
        posX = (int(self.path.currentPosition().x())) - 10
        if event.button() == Qt.LeftButton:
            self.setPos(posY, posX)
        elif event.button() == Qt.RightButton:
            self.delPos(posY, posX)

        self.display()

    def mouseMoveEvent(self, event):

        self.path.lineTo(event.pos())
        posY = (int(self.path.currentPosition().y())) - 10
        posX = (int(self.path.currentPosition().x())) - 10

        self.setPos(posY, posX)

        self.display()


    def setPos(self, y, x):

        posY, posX = self.adjustPos(y, x)
        if 0 <= posY < self.yZoom and 0 <= posX < self.xZoom:
            self.pos[posY + self.yStart, posX + self.xStart, 0:3] = COLOR_WHITE
            self.historyPos[posY + self.yStart, posX + self.xStart] += 1



    def adjustPos(self, y, x):

        y = int((self.yZoom * y) / self.widthPx)
        x = int((self.xZoom * x) / self.lenghtPx)

        return y, x

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
            self.pos[posY + self.yStart, posX + self.xStart, 0:3] = COLOR_BLACK
            self.historyColor[posY + self.yStart, posX + self.xStart, 0:3] = COLOR_BLACK
            self.historyPos[posY + self.yStart, posX + self.xStart] = 0

    def arrayToQImage(self, npArray):

        QImage = array2qimage(npArray)
        return QImage

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

    # function triggered by the view's clearbutton that reset the pos and the historymap
    # to 0 and then display
    
    def clear(self):

        self.simulation_started = False
        self.model.setClear()
        self.pos = np.zeros((self.width, self.lenght, 3))
        self.historyColor = np.zeros((self.width, self.lenght, 3))
        self.historyPos = np.zeros((self.width, self.lenght))
        self.display()

    def generation(self):

        if self.simulation_started:

            self.model.setState(self.pos, self.historyPos)
            self.pos, self.historyColor = self.model.getNextState()

            self.display()
            QTimer.singleShot(self.fps, self.generation)

    def getSizeW(self):

        return QSize(self.widthPx, self.lenghtPx)


    # function triggered by the view's checkbox that set the bool
    
    def setHistoryMode(self, bool):

        self.historyMode = bool



