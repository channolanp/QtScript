from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
import json

class QConfigWidget(QWidget):
    """A widget that allows adding of QtWidgets into a QFormLayout where the
    left column will always be a label matching the name supplied when adding
    widgets to the right column. The values of all the QtWidgets added to this
    widget using AddWidget can be saved to a JSON file, or loaded from a JSON
    file. You can also grab a dictionary of UI element values using GetConfig.

    Args:
        parent (QWidget): PyQt5 QWidget.

    Attributes:
        _config (dict): The protected dict containing keys of the user suppplied
         labels as names and values of the QWidget in its respective row.
        _layout (QLayout): The protected layout that widgets can be added to
        using AddWidget
        get_mapping (static dict): Allows polymorphic behavior for getting
        values from various QWidgets
        set_mapping (static dict): Allows polymorphic behavior for setting
        values to various QWidgets
    """

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
        """Create a simple Config Widget that handles a QFormLayout where
        left column is a QLabel representing the name of the configuration
        parameter, and the right column is a QWidget that is its value.

        Args:
            parent (QWidget): Required for all the behavior for QWidgets

        Returns:
            None

        """
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
        """Add a row of widgets to the form layout.

        Args:
            name (str): The name that will be shown as a QLabel on the left
            column of the form. This format is used for saving/loading config
            to/from JSON as well as GetConfig and SetConfig.
            control (type): Description of parameter `control`.

        Returns:
            None
        """
        label = QLabel(name)
        self._layout.addRow(label,control)
        self._config[name] = control

    def GetConfig(self):
        """Returns the current values from the UI elements added to this widget.

        Returns:
            dict{str:dynamic}: Current UI values as UI element string name and
            its value depending on widget type
        """
        config = {}
        for key in self._config:
            widget = self._config[key]
            config[key] = self.get_mapping[type(widget)](widget)
        return config

    def SetConfig(self, config):
        """Sets values for all UI elements suppplied in config.

        Args:
            config (dict{str:dynamic}): A dictionary containing UI element names
            and the desired value for each. The value types of the widget must
            be respected.

        Returns:
            None

        """
        for key in config:
            if key in self._config:
                widget = self._config[key]
                self.set_mapping[type(widget)](widget, config[key])
            else:
                print(f'Missing Key {key}, will not add')

    def _save(self):
        """This method slots to the save button click signal to open a file
        dialog used to save self.GetConfig into a JSON format

        Returns:
            None: Saves a file on the desktop

        """
        filePath,_ = QFileDialog().getSaveFileName(self, 'Save File','','JSON config (*.json)')
        if filePath:
            with open(filePath, 'w') as f:
                json.dump(self.GetConfig(),f, indent=4)

    def _load(self):
        """This method slots to the load button click signal to open a file
        dialog used to load the configuration from a JSON format and write to
        our UI elements using self.SetConfig

        Returns:
            None
        """
        dialog = QFileDialog()
        filePath, _ = dialog.getOpenFileName(filter="JSON Config (*.json)")
        if filePath:
            config = None
            with open(filePath, 'r') as f:
                config = json.load(f)
            self.SetConfig(config)
