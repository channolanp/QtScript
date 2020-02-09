from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QFileDialog
from PyQt5.QtCore import Qt

class QFileWidget(QWidget):
    """Simple widget that has a button to open a file dialog/browser to allow
    the user to select a file, and display it on screen.

    Args:
        parent (QWIdget): PyQt5 Widget.

    Attributes:
        _fileLabel (QLabel): The label showing the file selected.
        _filePath (str): The full file path the user has selected.

    """
    def __init__(self, parent = None):
        """Create a widget that simply lets the user select a file

        Args:
            parent (QWidget): Required for QWidget inheritance.

        Returns:
            None
        """
        super().__init__(parent)

        #Generate Private GUI objects
        helpLabel = QLabel('Please select a file')
        self._fileLabel = QLabel('No File Selected')
        self._fileLabel.setToolTip('Select a file using the button below')
        fileButton = QPushButton('Select')
        fileButton.clicked.connect(self._requestUserFile)

        #Build layout for window
        self.setWindowTitle('Wobble Grapher Tool')
        layout = QVBoxLayout()
        layout.addWidget(helpLabel)
        layout.addWidget(self._fileLabel)
        layout.addWidget(fileButton)
        self.setLayout(layout)

        #Initialize other attributes
        self._filePath = ''

    def GetFilePath(self):
        """Public call to get the file path selected by this widget

        Returns:
            str: The full file path the user has selected, '' if none selected.

        """
        return self._filePath

    def _requestUserFile(self):
        """Open a file dialaog to allow the user to select a file. The file
        name, without the full path is displayed to self._fileLabel

        Returns:
            None: The file path is saved to self._filePath
        """
        dialog = QFileDialog()
        filename, _ = dialog.getOpenFileName()

        if filename:
            self._filePath = filename
            self._fileLabel.setText(filename.split('/')[-1])
            self._fileLabel.setToolTip(filename)
