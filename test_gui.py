import sys
from widgets import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

if __name__ == '__main__':
    '''
    Main function when you call this program
    Starts the WobbleMain UI and keeps it open until "x"ed out
    '''
    app = QApplication(sys.argv)
    window = QConfigWidget()
    sb = QSpinBox()
    window.AddWidget("A Spin Box",sb)

    window.show()

    app.exec_()
