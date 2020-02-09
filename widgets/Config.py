from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
import json

class QConfigWidget(QWidget):
    '''
    Static dictionaries used for mapping behavior for polymorphic uses
    of different UI elements. This makes it so we can reference these
    dictionaries to call widget.getValue/getItem/getText, etc. and same for
    setting.
    '''
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
        QLineEdit: QLineEdit.setText,
        QSpinBox: QSpinBox.setValue,
        QDoubleSpinBox: QDoubleSpinBox.setValue,
        QCheckBox: QCheckBox.setChecked,
        QComboBox: QComboBox.setCurrentText,
        QSlider: QSlider.value,
        QListWidget: QListWidget.setCurrentItem
    }

    def __init__(self, parent = None):
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
        config = {}
        for key in self._config:
            widget = self._config[key]
            config[key] = self.get_mapping[type(widget)](widget)
        return config

    def SetConfig(self, config):
        for key in config:
            if key in self._config:
                widget = self._config[key]
                self.set_mapping[type(widget)](widget, config[key])
            else:
                print(f'Missing Key {key}, will not add')

    def _save(self):
        '''
        This method slots to the save button click signal to open a file dialog
        used to save self.__configurations into a JSON format
        '''
        filePath,_ = QFileDialog().getSaveFileName(self, 'Save File','','JSON config (*.json)')
        if filePath:
            with open(filePath, 'w') as f:
                json.dump(self.GetConfig(),f, indent=4)

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
            self.SetConfig(config)
