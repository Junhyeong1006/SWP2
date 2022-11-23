from PyQt5 import QtCore, QtGui, QtWidgets

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


        self.pushButton = QtWidgets.QPushButton(self.gridLayoutWidget) # Easy 버튼
        self.pushButton.setStyleSheet("background-color:rgb(179, 230, 255);\n""font: 75 9pt \"한컴 말랑말랑 Bold\";")
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)

        self.pushButton_2 = QtWidgets.QPushButton(self.gridLayoutWidget) # Normal 버튼
        self.pushButton_2.setStyleSheet("background-color:rgb(255, 255, 204);\n""font: 75 9pt \"한컴 말랑말랑 Bold\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 1, 0, 1, 1)

        self.pushButton_3 = QtWidgets.QPushButton(self.gridLayoutWidget) # Hard 버튼
        self.pushButton_3.setStyleSheet("background-color:rgb(255, 179, 179);\n""font: 75 9pt \"한컴 말랑말랑 Bold\";")
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 2, 0, 1, 1)

        self.label = QtWidgets.QLabel(Dialog) # 상단 Memory Game 글씨
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


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())