from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(960, 743)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        Dialog.setFont(font)
        Dialog.setStyleSheet("background-color:rgb(230, 255, 230);")

        self.label = QtWidgets.QLabel(Dialog) # 상단 memory game
        self.label.setGeometry(QtCore.QRect(350, 120, 291, 51))
        self.label.setStyleSheet("font: 75 18pt \"한컴 말랑말랑 Bold\";\n""")
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setObjectName("label")

        self.pushButton = QtWidgets.QPushButton(Dialog) # no 버튼
        self.pushButton.setGeometry(QtCore.QRect(60, 430, 161, 161))
        font = QtGui.QFont()
        font.setFamily("한컴 말랑말랑 Bold")
        font.setBold(True)
        font.setWeight(75)
        font.setPointSize(23)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color:rgb(255, 255, 204);")
        self.pushButton.setObjectName("pushButton")

        self.pushButton_2 = QtWidgets.QPushButton(Dialog) # mr 버튼
        self.pushButton_2.setGeometry(QtCore.QRect(290, 430, 161, 161))
        font = QtGui.QFont()
        font.setFamily("한컴 말랑말랑 Bold")
        font.setBold(True)
        font.setWeight(75)
        font.setPointSize(23)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color:rgb(255, 255, 204);")
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton_3 = QtWidgets.QPushButton(Dialog) # al 버튼
        self.pushButton_3.setGeometry(QtCore.QRect(520, 430, 161, 161))
        font = QtGui.QFont()
        font.setFamily("한컴 말랑말랑 Bold")
        font.setBold(True)
        font.setWeight(75)
        font.setPointSize(23)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color:rgb(255, 255, 204);")
        self.pushButton_3.setObjectName("pushButton_3")

        self.pushButton_4 = QtWidgets.QPushButton(Dialog) # !! 버튼
        self.pushButton_4.setGeometry(QtCore.QRect(750, 430, 161, 161))
        font = QtGui.QFont()
        font.setFamily("한컴 말랑말랑 Bold")
        font.setBold(True)
        font.setWeight(75)
        font.setPointSize(23)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("background-color:rgb(255, 255, 204);")
        self.pushButton_4.setObjectName("pushButton_4")

        self.label_2 = QtWidgets.QLabel(Dialog) # level:
        self.label_2.setGeometry(QtCore.QRect(70, 240, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setFamily("한컴 말랑말랑 Bold")
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.lineEdit = QtWidgets.QLineEdit(Dialog) # lineedit 레벨 표시창
        self.lineEdit.setGeometry(QtCore.QRect(160, 240, 113, 31))
        font = QtGui.QFont()
        font.setFamily("한컴 말랑말랑 Bold")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit.setFont(font)
        self.lineEdit.setText("")
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")


        
      

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Memory Game"))
        self.pushButton.setText(_translate("Dialog", "no"))
        self.pushButton_2.setText(_translate("Dialog", "rm"))
        self.pushButton_3.setText(_translate("Dialog", "al"))
        self.pushButton_4.setText(_translate("Dialog", "!!"))
        self.label_2.setText(_translate("Dialog", "Level:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

