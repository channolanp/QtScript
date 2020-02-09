import sys
from QtScript import QtScript
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
import moving_average_script

if __name__ == '__main__':
    #First start off by starting the QApplication for PyQt5
    app = QApplication(sys.argv)

    '''
    Use the QtScript class as the application window
    There's a simple file selecting dialog widget that is added as the first
    widget when with_file is True
    '''
    window = QtScript(with_file = True)

    #Set the script that will trigger when "Run Script" is clicked.
    #Note that this must have 1 arugment, as your config dict or throw away var
    window.SetScript(moving_average_script.main)

    #Here we build a bunch of UI elements and limit them however we like
    filter_window = QSpinBox()
    filter_window.setSingleStep(5)
    filter_window.setMinimum(0)
    filter_window.setMaximum(1000)
    filter_window.setValue(20)

    with_debounce = QCheckBox()

    debounce_trigger = QDoubleSpinBox()
    debounce_trigger.setSingleStep(0.5)
    debounce_trigger.setMinimum(0)
    debounce_trigger.setMaximum(100)
    debounce_trigger.setValue(1)

    debounce_window = QSpinBox()
    debounce_window.setSingleStep(5)
    debounce_window.setMinimum(0)
    debounce_window.setMaximum(500)
    debounce_window.setValue(50)

    '''
    Here we start adding the above widgets to the QtScript widget
    Note that the first argument is the string name to be used for everything.
    This name is used for all the JSON stuff, as well as the config dict that
    is passed to your script
    '''
    window.AddWidget('Filter Window', filter_window)
    window.AddWidget('Debounce Signal', with_debounce)
    window.AddWidget('Debounce Value', debounce_trigger)
    window.AddWidget('Debounce Window', debounce_window)

    '''
    Show the widget, and lock us into the event loop
    '''
    window.show()
    app.exec_()
