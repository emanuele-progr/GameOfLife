from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow
from Ui_interface import Ui_MainWindow
from controller import Controller
from model import Model
import sys


class MainWindow(QMainWindow):

    def __init__(self, model):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


        self.controller = Controller(model, self.ui.display)
        self.controller.setFixedWidth(575)
        self.controller.setFixedHeight(400)
        self.layout().addWidget(self.controller)

        self.ui.playButton.clicked.connect(self.playButtonTransition)
        self.ui.fpsSelector.currentIndexChanged.connect(self.setFramerate)
        self.ui.clearButton.clicked.connect(self.clearBoard)
        self.ui.verticalSlider.setTracking(True)
        self.ui.verticalSlider.valueChanged.connect(self.setZoom)
        self.ui.historyCheck.stateChanged.connect(self.setHistory)





    def playButtonTransition(self):

        self.controller.play()
        if self.ui.playButton.text() == 'Play':
            self.ui.playButton.setText('Pause')
        else:
            self.ui.playButton.setText('Play')

    def clearBoard(self):

        self.controller.clear()
        self.ui.playButton.setText('Play')

    def setFramerate(self):

        fpsValue = self.ui.fpsSelector.currentText()
        self.controller.setFramerate(fpsValue)



    def setZoom(self):

        self.controller.zoomAdjust(100 - self.ui.verticalSlider.value())

    def setHistory(self, state):

        if state == QtCore.Qt.Checked:
            self.controller.setHistoryMode(True)
        else:
            self.controller.setHistoryMode(False)



if __name__ == '__main__':

    app = QApplication(sys.argv)
    sshFile = "Aqua.qss"
    with open(sshFile, "r") as fh:
        app.setStyleSheet(fh.read())
    model = Model()
    w = MainWindow(model)
    w.show()
    sys.exit(app.exec_())