# Form implementation generated from reading ui file 'ui/1.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(679, 777)
        MainWindow.setStyleSheet("background-color: \"beige\";\n"
"QPushButton#shareFilesButton:pressed{\n"
"      background-color: darkgreen;\n"
"    color: white;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.title = QtWidgets.QLabel(parent=self.centralwidget)
        self.title.setGeometry(QtCore.QRect(70, 10, 551, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.title.sizePolicy().hasHeightForWidth())
        self.title.setSizePolicy(sizePolicy)
        self.title.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.title.setStyleSheet("font: 87 28pt \"Arial Black\";\n"
"color: rgb(0, 170, 0);\n"
"text-align: center")
        self.title.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.title.setObjectName("title")
        self.sharefilesButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.sharefilesButton.setGeometry(QtCore.QRect(150, 130, 341, 61))
        self.sharefilesButton.setStyleSheet("font: 16pt \"Arial\";\n"
"border-radius: 15px;\n"
"border: 3px solid green;")
        self.sharefilesButton.setObjectName("sharefilesButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 679, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.title.setText(_translate("MainWindow", "SWARA FILESHARE"))
        self.sharefilesButton.setText(_translate("MainWindow", "Select file to share"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
