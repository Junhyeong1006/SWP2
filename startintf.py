from PyQt5 import QtCore, QtGui, QtWidgets
import easy, sys, normal, hard


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(960, 743)
        Dialog.setStyleSheet("background-color:rgb(230, 255, 230)")

        self.gridLayoutWidget = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(390, 310, 161, 331))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")

        self.pushButton = QtWidgets.QPushButton(self.gridLayoutWidget)  # Easy 버튼
        self.pushButton.setStyleSheet("background-color:rgb(179, 230, 255);\n""font: 75 9pt \"한컴 말랑말랑 Bold\";")
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)
        self.pushButton.clicked.connect(lambda: self.startgame(1, Dialog))

        self.pushButton_2 = QtWidgets.QPushButton(self.gridLayoutWidget)  # Normal 버튼
        self.pushButton_2.setStyleSheet("background-color:rgb(255, 255, 204);\n""font: 75 9pt \"한컴 말랑말랑 Bold\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 1, 0, 1, 1)
        self.pushButton_2.clicked.connect(lambda: self.startgame(2, Dialog))

        self.pushButton_3 = QtWidgets.QPushButton(self.gridLayoutWidget)  # Hard 버튼
        self.pushButton_3.setStyleSheet("background-color:rgb(255, 179, 179);\n""font: 75 9pt \"한컴 말랑말랑 Bold\";")
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 2, 0, 1, 1)
        self.pushButton_3.clicked.connect(lambda: self.startgame(3, Dialog))

        self.label = QtWidgets.QLabel(Dialog)  # 상단 Memory Game 글씨
        self.label.setGeometry(QtCore.QRect(350, 120, 291, 51))
        self.label.setStyleSheet("font: 75 18pt \"한컴 말랑말랑 Bold\";\n""")
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Memory Game"))
        self.pushButton.setText(_translate("Dialog", "Easy"))
        self.pushButton_2.setText(_translate("Dialog", "Normal"))
        self.pushButton_3.setText(_translate("Dialog", "Hard"))
        self.label.setText(_translate("Dialog", "Memory Game"))

    def startgame(self, level, Dialog):
        Dialog.hide()
        Dialog1 = QtWidgets.QDialog()
        if level == 1:
            self.dialog = easy.Ui_Dialog()
            self.dialog.setupUi(Dialog1)
        elif level == 2:
            self.dialog = normal.Ui_Dialog()
            self.dialog.setupUi(Dialog1)
        elif level == 3:
            self.dialog = hard.Ui_Dialog()
            self.dialog.setupUi(Dialog1)
        Dialog1.show()
        Dialog1.exec_()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

