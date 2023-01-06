import sys
from PyQt5 import uic, QtCore, QtGui, QtWidgets


class MainWin(QtWidgets.QMainWindow):
    ServerAdress = 'http://localhost:5000'
    MessID = 0

    def __init__(self, *args, **qwargs) -> None:
        super(MainWin, self).__init__(*args, **qwargs)
        uic.loadUi('gui.ui')



if __name__=='__main':
    app = QtWidgets.QApplication(sys.argv)
    win = MainWin()
    win.show()
    sys.exit(app.exec())