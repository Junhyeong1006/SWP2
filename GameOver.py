from PyQt5 import QtCore, QtGui, QtWidgets
import startintf

class Ui_Dialog(object):
    def setupUi(self, Dialog, levelnum):
        Dialog.setObjectName("Dialog")
        Dialog.resize(960, 743)
        font = QtGui.QFont()
        font.setFamily("한컴 말랑말랑 Bold")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        Dialog.setFont(font)
        Dialog.setStyleSheet("background-color:rgb(255, 255, 230)")

        self.label = QtWidgets.QLabel(Dialog) # Text Game Over...
        self.label.setGeometry(QtCore.QRect(170, 40, 651, 231))
        font = QtGui.QFont()
        font.setFamily("한컴 말랑말랑 Bold")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(Dialog) # Text Your Level
        self.label_2.setGeometry(QtCore.QRect(340, 340, 191, 61))
        font = QtGui.QFont()
        font.setFamily("한컴 말랑말랑 Bold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.lineEdit = QtWidgets.QLineEdit(Dialog) # display Level
        self.lineEdit.setGeometry(QtCore.QRect(510, 350, 113, 41))
        font = QtGui.QFont()
        font.setFamily("한컴 말랑말랑 Bold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit.setFont(font)
        self.lineEdit.setText(str(levelnum))
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")

        self.pushButton = QtWidgets.QPushButton(Dialog) # 다시 시작 버튼
        self.pushButton.setGeometry(QtCore.QRect(400, 530, 171, 61))
        font = QtGui.QFont()
        font.setFamily("한컴 말랑말랑 Bold")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color:rgb(230, 230, 255)")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(lambda:self.restart(Dialog))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Game Over..."))
        self.label_2.setText(_translate("Dialog", "Your Level:"))
        self.pushButton.setText(_translate("Dialog", "다시 시작"))

    def restart(self, Dialog):
        Dialog.hide()
        Dialog2 = QtWidgets.QDialog()
        ui = intf_test.Ui_Dialog()
        ui.setupUi(Dialog2)
        Dialog2.show()
        Dialog2.exec()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog, 0)
    Dialog.show()
    sys.exit(app.exec_())
