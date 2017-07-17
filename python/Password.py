# -*- coding: utf-8 -*-

#
#   Author  :   Nevin Baiju
#   Platform:   PyQt5, Python3, sqlite
#   Company :   Tachlog
#   Date    :   17/7/2017
#   
#   Window for setting the password.

from PyQt5 import QtCore, QtGui, QtWidgets

class Password_window(QtWidgets.QMainWindow):
    def __init__(self):

        super().__init__()
        self.PASSWORD = ""
        self.ACTUAL_PASSWORD = "00000"
        self.setupUi()

    def setupUi(self):
        self.setObjectName("MainWindow")
        self.resize(800, 480)
        self.setStyleSheet("background-image:url(\"../sources/password/black_background.jpeg\");")
        self.centralWidget = QtWidgets.QWidget(self)
        self.centralWidget.setObjectName("centralWidget")

        self.frame = QtWidgets.QFrame(self.centralWidget)
        self.frame.setGeometry(QtCore.QRect(200, 20, 400, 440))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.BUTTON_1 = QtWidgets.QPushButton(self.frame)
        self.BUTTON_1.setGeometry(QtCore.QRect(90, 140, 60, 60))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.BUTTON_1.setFont(font)
        self.BUTTON_1.setStyleSheet(" background-color: white;\n"
"color: rgb(255, 255, 255);\n"
" border-style: solid;\n"
" border-width:3px;\n"
" border-radius:30px;\n"
" border-color: white;")
        self.BUTTON_1.setObjectName("BUTTON_1")

        self.BUTTON_2 = QtWidgets.QPushButton(self.frame)
        self.BUTTON_2.setGeometry(QtCore.QRect(170, 140, 60, 60))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.BUTTON_2.setFont(font)
        self.BUTTON_2.setStyleSheet(" background-color: white;\n"
"color: rgb(255, 255, 255);\n"
" border-style: solid;\n"
" border-width:3px;\n"
" border-radius:30px;\n"
" border-color: white;")
        self.BUTTON_2.setObjectName("BUTTON_2")

        self.BUTTON_3 = QtWidgets.QPushButton(self.frame)
        self.BUTTON_3.setGeometry(QtCore.QRect(250, 140, 60, 60))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.BUTTON_3.setFont(font)
        self.BUTTON_3.setStyleSheet(" background-color: white;\n"
"color: rgb(255, 255, 255);\n"
" border-style: solid;\n"
" border-width:3px;\n"
" border-radius:30px;\n"
" border-color: white;")
        self.BUTTON_3.setObjectName("BUTTON_3")

        self.BUTTON_4 = QtWidgets.QPushButton(self.frame)
        self.BUTTON_4.setGeometry(QtCore.QRect(90, 210, 60, 60))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.BUTTON_4.setFont(font)
        self.BUTTON_4.setStyleSheet(" background-color: white;\n"
"color: rgb(255, 255, 255);\n"
" border-style: solid;\n"
" border-width:3px;\n"
" border-radius:30px;\n"
" border-color: white;")
        self.BUTTON_4.setObjectName("BUTTON_4")

        self.BUTTON_5 = QtWidgets.QPushButton(self.frame)
        self.BUTTON_5.setGeometry(QtCore.QRect(170, 210, 60, 60))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.BUTTON_5.setFont(font)
        self.BUTTON_5.setStyleSheet(" background-color: white;\n"
"color: rgb(255, 255, 255);\n"
" border-style: solid;\n"
" border-width:3px;\n"
" border-radius:30px;\n"
" border-color: white;")
        self.BUTTON_5.setObjectName("BUTTON_5")

        self.BUTTON_6 = QtWidgets.QPushButton(self.frame)
        self.BUTTON_6.setGeometry(QtCore.QRect(250, 210, 60, 60))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.BUTTON_6.setFont(font)
        self.BUTTON_6.setStyleSheet(" background-color: white;\n"
"color: rgb(255, 255, 255);\n"
" border-style: solid;\n"
" border-width:3px;\n"
" border-radius:30px;\n"
" border-color: white;")
        self.BUTTON_6.setObjectName("BUTTON_6")

        self.BUTTON_7 = QtWidgets.QPushButton(self.frame)
        self.BUTTON_7.setGeometry(QtCore.QRect(90, 280, 60, 60))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.BUTTON_7.setFont(font)
        self.BUTTON_7.setStyleSheet(" background-color: white;\n"
"color: rgb(255, 255, 255);\n"
" border-style: solid;\n"
" border-width:3px;\n"
" border-radius:30px;\n"
" border-color: white;")
        self.BUTTON_7.setObjectName("BUTTON_8")

        self.BUTTON_8 = QtWidgets.QPushButton(self.frame)
        self.BUTTON_8.setGeometry(QtCore.QRect(170, 280, 60, 60))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.BUTTON_8.setFont(font)
        self.BUTTON_8.setStyleSheet(" background-color: white;\n"
"color: rgb(255, 255, 255);\n"
" border-style: solid;\n"
" border-width:3px;\n"
" border-radius:30px;\n"
" border-color: white;")
        self.BUTTON_8.setObjectName("BUTTON_7")

        self.BUTTON_9 = QtWidgets.QPushButton(self.frame)
        self.BUTTON_9.setGeometry(QtCore.QRect(250, 280, 60, 60))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.BUTTON_9.setFont(font)
        self.BUTTON_9.setStyleSheet(" background-color: white;\n"
"color: rgb(255, 255, 255);\n"
" border-style: solid;\n"
" border-width:3px;\n"
" border-radius:30px;\n"
" border-color: white;")
        self.BUTTON_9.setObjectName("BUTTON_9")
        self.BUTTON_0 = QtWidgets.QPushButton(self.frame)

        self.BUTTON_0.setGeometry(QtCore.QRect(170, 350, 60, 60))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.BUTTON_0.setFont(font)
        self.BUTTON_0.setStyleSheet(" background-color: white;\n"
"color: rgb(255, 255, 255);\n"
" border-style: solid;\n"
" border-width:3px;\n"
" border-radius:30px;\n"
" border-color: white;")
        self.BUTTON_0.setObjectName("BUTTON_0")

        self.DASHES = []


        self.DASH_1 = QtWidgets.QLabel(self.frame)
        self.DASH_1.setGeometry(QtCore.QRect(110, 80, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.DASH_1.setFont(font)
        self.DASH_1.setStyleSheet("color: rgb(255, 255, 255);")
        self.DASH_1.setObjectName("DASH_1")

        self.DASHES.append(self.DASH_1)

        self.DASH_2 = QtWidgets.QLabel(self.frame)
        self.DASH_2.setGeometry(QtCore.QRect(150, 80, 31, 31))
        self.DASH_2.setFont(font)
        self.DASH_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.DASH_2.setObjectName("DASH_2")

        self.DASHES.append(self.DASH_2)

        self.DASH_3 = QtWidgets.QLabel(self.frame)
        self.DASH_3.setGeometry(QtCore.QRect(190, 80, 31, 31))
        self.DASH_3.setFont(font)
        self.DASH_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.DASH_3.setObjectName("DASH_3")

        self.DASHES.append(self.DASH_3)

        self.DASH_4 = QtWidgets.QLabel(self.frame)
        self.DASH_4.setGeometry(QtCore.QRect(230, 80, 31, 31))
        self.DASH_4.setFont(font)
        self.DASH_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.DASH_4.setObjectName("DASH_4")

        self.DASHES.append(self.DASH_4)

        self.DASH_5 = QtWidgets.QLabel(self.frame)
        self.DASH_5.setGeometry(QtCore.QRect(270, 80, 31, 31))
        self.DASH_5.setFont(font)
        self.DASH_5.setStyleSheet("color: rgb(255, 255, 255);")
        self.DASH_5.setObjectName("DASH_5")

        self.DASHES.append(self.DASH_5)


        self.TITLE = QtWidgets.QLabel(self.frame)
        self.TITLE.setGeometry(QtCore.QRect(116, 30, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.TITLE.setFont(font)
        self.TITLE.setStyleSheet("color: rgb(255, 255, 255);")
        self.TITLE.setObjectName("TITLE")

        self.DELETE = QtWidgets.QPushButton(self.frame)
        self.DELETE.setGeometry(QtCore.QRect(310, 80, 51, 51))
        self.DELETE.setStyleSheet("border: none;")
        self.DELETE.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../sources/password/delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.DELETE.setIcon(icon)
        self.DELETE.setIconSize(QtCore.QSize(50, 50))
        self.DELETE.setObjectName("DELETE")
        self.setCentralWidget(self.centralWidget)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.BUTTON_1.setText(_translate("MainWindow", "1"))
        self.BUTTON_2.setText(_translate("MainWindow", "2"))
        self.BUTTON_3.setText(_translate("MainWindow", "3"))
        self.BUTTON_4.setText(_translate("MainWindow", "4"))
        self.BUTTON_5.setText(_translate("MainWindow", "5"))
        self.BUTTON_6.setText(_translate("MainWindow", "6"))
        self.BUTTON_7.setText(_translate("MainWindow", "7"))
        self.BUTTON_8.setText(_translate("MainWindow", "8"))
        self.BUTTON_9.setText(_translate("MainWindow", "9"))
        self.BUTTON_0.setText(_translate("MainWindow", "0"))

        self.DASH_1.setText(_translate("MainWindow", "-"))
        self.DASH_2.setText(_translate("MainWindow", "-"))
        self.DASH_3.setText(_translate("MainWindow", "-"))
        self.DASH_4.setText(_translate("MainWindow", "-"))
        self.DASH_5.setText(_translate("MainWindow", "-"))

        self.TITLE.setText(_translate("MainWindow", "Enter your pin"))

        self.BUTTON_1.clicked.connect(lambda: self.Add_password("1"))
        self.BUTTON_2.clicked.connect(lambda: self.Add_password("2"))
        self.BUTTON_3.clicked.connect(lambda: self.Add_password("3"))
        self.BUTTON_4.clicked.connect(lambda: self.Add_password("4"))
        self.BUTTON_5.clicked.connect(lambda: self.Add_password("5"))
        self.BUTTON_6.clicked.connect(lambda: self.Add_password("6"))
        self.BUTTON_7.clicked.connect(lambda: self.Add_password("7"))
        self.BUTTON_8.clicked.connect(lambda: self.Add_password("8"))
        self.BUTTON_9.clicked.connect(lambda: self.Add_password("9"))
        self.BUTTON_0.clicked.connect(lambda: self.Add_password("0"))

        self.DELETE.clicked.connect(self.Back_space)

######################################################################################################
#   Function for buffering the inputted text.
######################################################################################################


    def Add_password(self, CHARACTER):
        self.PASSWORD =  self.PASSWORD+CHARACTER
        print(self.PASSWORD)
        if(len(self.PASSWORD)==5):
            self.Check_password()
        self.Set_dash()

######################################################################################################
#   Function for setting the password field.
######################################################################################################

    def Set_dash(self):
        try:
            i = 0
            for i in range(0, len(self.PASSWORD)+1):
                font = QtGui.QFont()
                font.setPointSize(20)
                self.DASHES[i].setFont(font)
                self.DASHES[i].setText("*")
                font = QtGui.QFont()
                font.setPointSize(60)
            for i in range(i, 5):
                self.DASHES[i].setText("-")
        except IndexError:
            print("blah")

######################################################################################################
#   Function for clearing the password.
######################################################################################################

    def Back_space(self):
        self.PASSWORD = self.PASSWORD[0:(len(self.PASSWORD)-1)]
        print(self.PASSWORD)
        self.Set_dash()

######################################################################################################
#   Function for checking the password.
######################################################################################################

    def Check_password(self):
        if(self.PASSWORD == self.ACTUAL_PASSWORD):
            self.TITLE.setText("Yes")
            self.PASSWORD = ""
        else:
            self.TITLE.setText("Enter again")
            self.PASSWORD=""
            self.Set_dash()




