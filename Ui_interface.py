# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(660, 500)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(660, 475))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setItalic(True)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setItalic(False)
        self.centralwidget.setFont(font)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.controlWidget = QtWidgets.QWidget(self.centralwidget)
        self.controlWidget.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.controlWidget.setObjectName("controlWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.controlWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.playButton = QtWidgets.QPushButton(self.controlWidget)
        self.playButton.setObjectName("playButton")
        self.horizontalLayout.addWidget(self.playButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.clearButton = QtWidgets.QPushButton(self.controlWidget)
        self.clearButton.setObjectName("clearButton")
        self.horizontalLayout.addWidget(self.clearButton)
        spacerItem1 = QtWidgets.QSpacerItem(174, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.fpsText = QtWidgets.QLabel(self.controlWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.fpsText.setFont(font)
        self.fpsText.setObjectName("fpsText")
        self.horizontalLayout.addWidget(self.fpsText)
        self.fpsSelector = QtWidgets.QComboBox(self.controlWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fpsSelector.sizePolicy().hasHeightForWidth())
        self.fpsSelector.setSizePolicy(sizePolicy)
        self.fpsSelector.setIconSize(QtCore.QSize(10, 10))
        self.fpsSelector.setObjectName("fpsSelector")
        self.fpsSelector.addItem("")
        self.fpsSelector.addItem("")
        self.fpsSelector.addItem("")
        self.fpsSelector.addItem("")
        self.fpsSelector.addItem("")
        self.fpsSelector.addItem("")
        self.horizontalLayout.addWidget(self.fpsSelector)
        self.historyCheck = QtWidgets.QCheckBox(self.controlWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setItalic(False)
        self.historyCheck.setFont(font)
        self.historyCheck.setObjectName("historyCheck")
        self.horizontalLayout.addWidget(self.historyCheck)
        self.gridLayout.addWidget(self.controlWidget, 1, 0, 1, 3)
        self.display = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.display.sizePolicy().hasHeightForWidth())
        self.display.setSizePolicy(sizePolicy)
        self.display.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.display.setAutoFillBackground(False)
        self.display.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.display.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.display.setText("")
        self.display.setObjectName("display")
        self.gridLayout.addWidget(self.display, 0, 0, 1, 1)
        self.zoomWidget = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.zoomWidget.sizePolicy().hasHeightForWidth())
        self.zoomWidget.setSizePolicy(sizePolicy)
        self.zoomWidget.setMaximumSize(QtCore.QSize(45, 16777215))
        self.zoomWidget.setObjectName("zoomWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.zoomWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.verticalSlider = QtWidgets.QSlider(self.zoomWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.verticalSlider.sizePolicy().hasHeightForWidth())
        self.verticalSlider.setSizePolicy(sizePolicy)
        self.verticalSlider.setTracking(False)
        self.verticalSlider.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.verticalSlider.setObjectName("verticalSlider")
        self.verticalLayout.addWidget(self.verticalSlider)
        self.zoomText = QtWidgets.QLabel(self.zoomWidget)
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setItalic(True)
        self.zoomText.setFont(font)
        self.zoomText.setObjectName("zoomText")
        self.verticalLayout.addWidget(self.zoomText)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.gridLayout.addWidget(self.zoomWidget, 0, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 660, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "GameOfLife"))
        self.playButton.setText(_translate("MainWindow", "Play"))
        self.clearButton.setText(_translate("MainWindow", "Clear"))
        self.fpsText.setText(_translate("MainWindow", "FPS"))
        self.fpsSelector.setCurrentText(_translate("MainWindow", "60"))
        self.fpsSelector.setItemText(0, _translate("MainWindow", "60"))
        self.fpsSelector.setItemText(1, _translate("MainWindow", "40"))
        self.fpsSelector.setItemText(2, _translate("MainWindow", "30"))
        self.fpsSelector.setItemText(3, _translate("MainWindow", "15"))
        self.fpsSelector.setItemText(4, _translate("MainWindow", "5"))
        self.fpsSelector.setItemText(5, _translate("MainWindow", "1"))
        self.historyCheck.setText(_translate("MainWindow", "History mode"))
        self.zoomText.setText(_translate("MainWindow", "Zoom"))
