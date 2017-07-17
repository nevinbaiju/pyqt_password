from PyQt5 import QtCore, QtGui, QtWidgets
from Password import Password_window

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    home = Password_window()
    home.show()
    sys.exit(app.exec_())


