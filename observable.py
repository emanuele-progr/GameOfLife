from PyQt5.QtCore import QObject, pyqtSignal, pyqtProperty


class Observable(QObject):

    valueChanged = pyqtSignal(object)
    def __init__(self, val):
        super().__init__()
        self._value = val

    # Register observers.
    def register(self, slot):
        self.valueChanged.connect(slot)

    @pyqtProperty(object, notify=valueChanged)
    def value(self):
        return self._value

    @value.setter
    def value(self, newval):
        self._value = newval
        self.valueChanged.emit(self.value)  
