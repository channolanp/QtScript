import sys
from QtScript import QtScript
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QtScript()
    window.SetScript(lambda config:print(f'Hello {config["Some text box"]}'))
    sb = QSpinBox()
    tb = QLineEdit()
    cb = QCheckBox()
    window.AddWidget("A Spin Box",sb)
    window.AddWidget("Some text box", tb)
    window.AddWidget("A checkbox", cb)

    window.show()

    app.exec_()
