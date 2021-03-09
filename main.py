from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow
from Ui_interface import Ui_MainWindow
from displayWidget import DisplayWidget
from model import Model
import sys


BOARD_WIDTH = 575
BOARD_HEIGHT = 400

# class that conceptually most of the view; this class performs the
# setup of the UI generated by Qt designer, adds a widget representing
# the display (a label equipped with a pixmap) and passes a model.


class MainWindow(QMainWindow):

    def __init__(self, model):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.model = model

        self.display = DisplayWidget(model, BOARD_WIDTH, BOARD_HEIGHT)
        self.display.setFixedWidth(BOARD_WIDTH)
        self.display.setFixedHeight(BOARD_HEIGHT)

        self.layout().addWidget(self.display)

        # connection of ui events to class functions and to the model

        self.eventConnect()


    # change text in the play button and trigger the play function on the display widget

    def playButtonTransition(self):

        self.display.play()
        if self.ui.playButton.text() == 'Play':
            self.ui.playButton.setText('Pause')
        else:
            self.ui.playButton.setText('Play')

    # reset text in the play button and trigger the clear function on the display widget

    def clearBoard(self):

        self.display.clear()
        self.ui.playButton.setText('Play')

    # gets fps value from the comboBox and sets it in the model

    def setFramerate(self):

        fpsValue = self.ui.fpsSelector.currentText()
        self.model.setFps(fpsValue)

    # gets vslider values and passes them to a display widget function that
    # uses them to zoom

    def setZoom(self):

        self.display.zoomAdjust(100 - self.ui.verticalSlider.value())

    # sets the history mode on the model

    def setHistory(self, state):

        if state == QtCore.Qt.Checked:
            self.model.setHistoryMode(True)
        else:
            self.model.setHistoryMode(False)

    # function to connect events

    def eventConnect(self):

        self.ui.playButton.clicked.connect(self.playButtonTransition)
        self.ui.clearButton.clicked.connect(self.clearBoard)
        self.ui.verticalSlider.setTracking(True)
        self.ui.verticalSlider.valueChanged.connect(self.setZoom)
        self.ui.historyCheck.stateChanged.connect(self.setHistory)
        self.ui.fpsSelector.currentIndexChanged.connect(self.setFramerate)


# main code which instantiates a model, a mainwindow and starts the application

if __name__ == '__main__':
    app = QApplication(sys.argv)
    sshFile = "Aqua.qss"
    with open(sshFile, "r") as fh:
        app.setStyleSheet(fh.read())
    model = Model()
    w = MainWindow(model)
    w.show()
    sys.exit(app.exec_())