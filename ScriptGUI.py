from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton
from PyQt5.QtCore import Qt
from widgets import QFileWidget, QConfigWidget

class QtScript(QWidget):
    def __init__(self, parent = None, with_file = True):
        super().__init__(parent)

        self._fileWidget = None
        layout = QVBoxLayout()
        if(with_file):
            self._fileWidget = QFileWidget()
            layout.addWidget(self._fileWidget)

        self._configWidget = QConfigWidget()
        layout.addWidget(self._configWidget)

        runButton = QPushButton("Run Script")
        runButton.clicked.connect(self.RunScript)
        layout.addWidget(runButton)

        self.setLayout(layout)

        self._script = None

    def AddWidget(self, name, widget):
        self._configWidget.AddWidget(name, widget)

    def SetScript(self, script):
        self._script = script

    def RunScript(self):
        config = self._configWidget.GetConfig()
        if self._fileWidget:
            config['Target File'] = self._fileWidget.GetFilePath()
        self._script(config)
