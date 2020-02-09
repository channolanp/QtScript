import sys
from QtScript import QtScript
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
import motion_generator_script

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QtScript(with_file = False)
    window.SetScript(motion_profile_generator.generate)

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
    The strings provided as names must match what you're calling in the script
    '''

    window.AddWidget('Max Idle', idle)
    window.AddWidget('Target Velocity', vel)
    window.AddWidget('Target Acceleration', accel)
    window.AddWidget('Target Deceleration', decel)
    window.AddWidget('Move Distance', distance)
    window.AddWidget('Sampling Frequency', frequency)
    window.AddWidget('Noise Amplitude', noise)
    window.show()

    app.exec_()
