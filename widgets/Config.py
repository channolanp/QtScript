from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
import json

class QConfigWidget(QWidget):
    get_mapping = {
        QLineEdit: QLineEdit.text,
        QSpinBox: QSpinBox.value,
        QDoubleSpinBox: QDoubleSpinBox.value,
        QCheckBox: QCheckBox.isChecked,
        QComboBox: QComboBox.currentText,
        QSlider: QSlider.value,
        QListWidget: QListWidget.currentItem
    }
    set_mapping = {
        QLineEdit: QLineEdit.text,
        QSpinBox: QSpinBox.setValue,
        QDoubleSpinBox: QDoubleSpinBox.setValue,
        QCheckBox: QCheckBox.setChecked,
        QComboBox: QComboBox.setCurrentText,
        QSlider: QSlider.value,
        QListWidget: QListWidget.setCurrentItem
    }

    def __init__(self, parent = None):
        '''
        This widget is used for the wobble script to change basic global variables
        This widget also allows the saving and loading of the global variables as a JSON config
        '''
        super().__init__(parent)
        self._config = {}

        #Build the save/load button and connect signals
        saveButton = QPushButton("Save Config")
        saveButton.clicked.connect(self._save)
        loadButton = QPushButton("Load Config")
        loadButton.clicked.connect(self._load)

        #Setup the main layout that will have items added to externally
        self._layout = QFormLayout()
        self._layout.addRow(saveButton, loadButton)
        #Set this widget's layout to the form
        self.setLayout(self._layout)

    def AddWidget(self, name, control):
        label = QLabel(name)
        self._layout.addRow(label,control)
        self._config[name] = control

    def GetConfig(self):
        self.__update()
        return self._config
    def _save(self):
        '''
        This method slots to the save button click signal to open a file dialog
        used to save self.__configurations into a JSON format
        '''
        self.__update()
        filePath,_ = QFileDialog().getSaveFileName(self, 'Save File','','JSON config (*.json)')
        if filePath:
            with open(filePath, 'w') as f:
                json.dump(self._config,f, indent=4)

    def _load(self):
        '''
        This method slots to the load button click signal to open a file dialog
        used to load the configuration from a JSON format into self.__configurations
        '''
        dialog = QFileDialog()
        filePath, _ = dialog.getOpenFileName(filter="JSON Config (*.json)")
        if filePath:
            config = None
            with open(filePath, 'r') as f:
                config = json.load(f)
            self._config = config
            self.__setAll()
