import numpy as np

# class representing the state of the game simulation.
# basically, the model notifies the display widget of
# changes by passing this class.
#
# * pos -> keeps track of cell occupation.
# ex. pos[i,j,(255,255,255)] - white cell
#     pos[i,j,(0,0,0)] - black cell
# * historyPos -> keeps track of cell's lifetime with a counter.
# * historyColor -> similar to "pos" but with RGB channel.
# * historyMode -> flag to activate\deactivate history mode.

class BoardState(object):

    def __init__(self, width, lenght, check=False, fps=60):

        self.white3DVector = np.full((width, lenght, 3), 255)
        self.zeroVector = np.zeros((width, lenght))
        self.pos = self.white3DVector
        self.historyPos = self.zeroVector
        self.historyColor = self.white3DVector
        self.historyMode = check
        self.fps = fps

    def reset(self):
        self.pos = self.white3DVector
        self.historyPos = self.zeroVector
        self.historyColor = self.white3DVector


    def setState(self, pos, historyPos, historyColor):

        self.pos = pos
        self.historyPos = historyPos
        self.historyColor = historyColor

    def setHistoryMode(self, bool):

        self.historyMode = bool

    def setFps(self, fps):
        self.fps = fps

