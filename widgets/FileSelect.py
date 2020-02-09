from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt5.QtCore import Qt

class QFileWidget(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)

        #Generate Private GUI objects
        helpLabel = QLabel('Please select a file')
        self.__fileLabel = QLabel('No File Selected')
        self.__fileLabel.setToolTip('Select a file using the button below')
        fileButton = QPushButton('Select')
        fileButton.clicked.connect(self.__requestUserFile)

        #Build layout for window
        self.setWindowTitle('Wobble Grapher Tool')
        layout = QVBoxLayout()
        layout.addWidget(helpLabel)
        layout.addWidget(self.__fileLabel)
        layout.addWidget(fileButton)
        self.setLayout(layout)

        #Initialize other attributes
        self.__filePath = ''

    def GetFilePath(self):
        '''
        External call to get the file path selected by this widget
        '''
        return self.__filePath

    def __requestUserFile(self):
        '''
        Open a file dialog to allow the user to select a file.
        The file path is saved in self.__filePath
        self.__fileLabel is set to just the file name
        self.__fileLabel's tooltip will show the full path
        '''
        dialog = QFileDialog()
        filename, _ = dialog.getOpenFileName()

        if filename:
            self.__filePath = filename
            self.__fileLabel.setText(filename.split('/')[-1])
            self.__fileLabel.setToolTip(filename)
