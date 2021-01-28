import numpy as np
import scipy
import scipy.ndimage

COLOR_BLACK = 0, 0, 0
COLOR_WHITE = 255, 255, 255
COLOR_LIGHTBLUE = 49, 188, 174
COLOR_YELLOW = 246, 225, 38
COLOR_ORANGE = 253, 117, 66
COLOR_RED = 164, 4, 4

class Model(object):

    def __init__(self, width=100, len=200):

        self.width = width
        self.lenght = len
        self.heathmapCheck = False
        self.clear = False
        self.pos = np.zeros((self.width, self.lenght, 3))
        self.historyPos = np.zeros((self.width, self.lenght))
        self.historyColor = np.zeros((self.width, self.lenght, 3))


    def setSize(self, width, lenght):

        self.width = width
        self.lenght = lenght

    def getSize(self):

         return self.width, self.lenght


    def setClear(self):

        self.clear = True


    def setState(self, pos, history):

        self.pos = pos
        self.historyPos = history



    def getNextState(self):

        self.nextState()
        return self.pos, self.historyColor

    def nextState(self):

        neighbours = self.findNeighbours()
        for i in range(self.width):
            for j in range(self.lenght):
                if neighbours[i, j] % 2 == 0:
                    if neighbours[i, j] / 2 == 3:
                        self.pos[i, j, 0:3] = COLOR_WHITE
                        self.historyPos[i, j] += 1
                    else:
                        self.pos[i, j, 0:3] = COLOR_BLACK
                        self.historyPos[i, j] = 0
                elif (neighbours[i, j] - 1) / 2 == 2 or (neighbours[i, j] - 1) / 2 == 3:
                    self.pos[i, j, 0:3] = COLOR_WHITE
                    self.historyPos[i, j] += 1
                else:
                    self.pos[i, j, 0:3] = COLOR_BLACK
                    self.historyPos[i, j] = 0

        self.computeHistoryMap()
        return

    def valueConversion(self, pos, conversion):

        valueConverted = np.zeros((self.width, self.lenght))
        for i in range(self.width):
            for j in range(self.lenght):
                if pos[i][j][0] == 255 and pos[i][j][1] == 255 and pos[i][j][1] == 255:
                    valueConverted[i][j] = 1
        return valueConverted



    def findNeighbours(self):

        kernel = np.array([[2, 2, 2], [2, 1, 2], [2, 2, 2]])
        pos = self.valueConversion(self.pos, True)
        neighbours = scipy.ndimage.filters.convolve(pos, kernel, mode='constant', cval=0)


        return neighbours

    def computeHistoryMap(self):

        for i in range(self.width):
            for j in range(self.lenght):
                if self.historyPos[i, j] > 0:
                    if self.historyPos[i, j] <= 5:
                        self.historyColor[i, j, 0:3] = COLOR_LIGHTBLUE

                    elif self.historyPos[i, j] > 5 and self.historyPos[i, j] <= 10:
                        self.historyColor[i, j, 0:3] = COLOR_YELLOW

                    elif self.historyPos[i, j] > 10 and self.historyPos[i, j] <= 40:
                        self.historyColor[i, j, 0:3] = COLOR_ORANGE

                    elif self.historyPos[i, j] > 40:
                        self.historyColor[i, j, 0:3] = COLOR_RED

                else:
                    self.historyColor[i, j, 0:3] = COLOR_BLACK


