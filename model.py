import numpy as np
import scipy
import scipy.ndimage
from observable import Observable
from boardState import BoardState

# RGB color global definition

COLOR_BLACK = 0, 0, 0
COLOR_WHITE = 255, 255, 255
COLOR_LIGHTBLUE = 49, 188, 174
COLOR_YELLOW = 246, 225, 38
COLOR_ORANGE = 253, 117, 66
COLOR_RED = 164, 4, 4

# model class derived from Observable to notify
# the display on value changed.
# the class is equipped with a state attribute wich represents
# the current state of the simulation.
class Model(Observable):

    def __init__(self, width=100, len=200, initval=0):

        super().__init__(initval)

        self.width = width
        self.lenght = len
        self.state = BoardState(width, len)
        self.pos = np.full((self.width, self.lenght, 3), 255)
        self.historyPos = np.zeros((self.width, self.lenght))
        self.historyColor = np.full((self.width, self.lenght, 3), 255)


    def setFps(self, fps):

        self.state.setFps(fps)
        self.value = self.state

    def setHistoryMode(self, bool):

        self.state.setHistoryMode(bool)
        self.value = self.state


    def clear(self):

        self.pos = np.full((self.width, self.lenght, 3), 255)
        self.historyColor = np.full((self.width, self.lenght, 3), 255)
        self.historyPos = np.zeros((self.width, self.lenght))

        self.state.reset()
        self.value = self.state


    def setPos(self, y, x):

        self.pos[y, x, 0:3] = COLOR_BLACK
        self.historyColor[y, x, 0:3] = COLOR_LIGHTBLUE
        self.historyPos[y, x] += 1
        self.state.setState(self.pos, self.historyPos, self.historyColor)
        self.value = self.state

    def delPos(self, y, x):

        self.pos[y, x, 0:3] = COLOR_WHITE
        self.historyColor[y, x, 0:3] = COLOR_WHITE
        self.historyPos[y, x] = 0
        self.state.setState(self.pos, self.historyPos, self.historyColor)
        self.value = self.state

    # core function to calculate next state
    def nextState(self):

        neighbours = self.findNeighbours()
        for i in range(self.width):
            for j in range(self.lenght):
                if neighbours[i, j] % 2 == 0:
                    # case of unpopulated location that becomes populated because it has
                    # exactly three populated neighbors
                    if neighbours[i, j] / 2 == 3:
                        self.pos[i, j, 0:3] = COLOR_BLACK
                        self.historyPos[i, j] += 1
                    else:
                        self.pos[i, j, 0:3] = COLOR_WHITE
                        self.historyPos[i, j] = 0
                elif (neighbours[i, j] - 1) / 2 == 2 or (neighbours[i, j] - 1) / 2 == 3:
                    # case of populated location with 2 or 3 neighbors
                    self.pos[i, j, 0:3] = COLOR_BLACK
                    self.historyPos[i, j] += 1
                else:
                    self.pos[i, j, 0:3] = COLOR_WHITE
                    self.historyPos[i, j] = 0

        self.computeHistoryMap()
        self.state.setState(self.pos, self.historyPos, self.historyColor)
        self.value = self.state
        return


    # function to set to 1 every location populated (needed later for convolution)
    
    def valueConversion(self, pos):

        valueConverted = np.zeros((self.width, self.lenght))
        for i in range(self.width):
            for j in range(self.lenght):
                if pos[i][j][0] == 0 and pos[i][j][1] == 0 and pos[i][j][1] == 0:
                    valueConverted[i][j] = 1
        return valueConverted


    # function that uses convolution to track the number of neighbours
    
    def findNeighbours(self):

        kernel = np.array([[2, 2, 2], [2, 1, 2], [2, 2, 2]])
        pos = self.valueConversion(self.pos)
        neighbours = scipy.ndimage.filters.convolve(pos, kernel, mode='constant', cval=0)

        return neighbours

    # function that uses historypos values to draw the historymap
    # lightblue(newborn) -> yellow -> orange -> red(ancient)
    
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
                    self.historyColor[i, j, 0:3] = COLOR_WHITE


