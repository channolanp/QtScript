import sys
from QtScript import QtScript
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
import motion_generator_script

if __name__ == '__main__':
    #First start off by starting the QApplication for PyQt5
    app = QApplication(sys.argv)

    '''
    Use the QtScript class as the application window
    There's a simple file selecting dialog widget that is added as the first
    widget when with_file is True
    '''
    window = QtScript(with_file = False)

    #Set the script that will trigger when "Run Script" is clicked.
    #Note that this must have 1 arugment, as your config dict or throw away var
    window.SetScript(motion_generator_script.generate)

    #Here we build a bunch of UI elements and limit them however we like
    idle = QDoubleSpinBox()
    idle.setSingleStep(0.1)
    idle.setMinimum(0)
    idle.setMaximum(5)
    idle.setValue(3)

    vel = QDoubleSpinBox()
    vel.setSingleStep(10)
    vel.setMinimum(0)
    vel.setMaximum(3000)
    vel.setValue(1000)

    accel = QDoubleSpinBox()
    accel.setSingleStep(10)
    accel.setMinimum(0)
    accel.setMaximum(1000)
    accel.setValue(1000)

    decel = QDoubleSpinBox()
    decel.setSingleStep(10)
    decel.setMinimum(0)
    decel.setMaximum(1000)
    decel.setValue(1000)


    distance = QDoubleSpinBox()
    distance.setSingleStep(500)
    distance.setMinimum(0)
    distance.setMaximum(20000)
    distance.setValue(3000)


    frequency = QSpinBox()
    frequency.setSingleStep(10)
    frequency.setMinimum(0)
    frequency.setMaximum(10000)
    frequency.setValue(100)


    noise = QDoubleSpinBox()
    noise.setSingleStep(11)
    noise.setMinimum(0)
    noise.setMaximum(100)
    noise.setValue(10)

    '''
    Here we start adding the above widgets to the QtScript widget
    Note that the first argument is the string name to be used for everything.
    This name is used for all the JSON stuff, as well as the config dict that
    is passed to your script
    '''
    window.AddWidget('Max Idle', idle)
    window.AddWidget('Target Velocity', vel)
    window.AddWidget('Target Acceleration', accel)
    window.AddWidget('Target Deceleration', decel)
    window.AddWidget('Move Distance', distance)
    window.AddWidget('Sampling Frequency', frequency)
    window.AddWidget('Noise Amplitude', noise)

    '''
    Show the widget, and lock us into the event loop
    '''
    window.show()
    app.exec_()
