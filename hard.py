from PyQt5 import QtCore, QtGui, QtWidgets, QtTest
import random, sys, GameOver

class Ui_Dialog(object):
    def __init__(self):
        self.realBreak = True
        self.number = 0  # 생성자
        self.numlist = []  # 랜덤난수 리스트
        self.numlist_user = []  # 내가 입력한수 리스트
        self.roundcnt = 1
        self.counting = 0
        self.gamestart = False

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(960, 743)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        Dialog.setFont(font)
        Dialog.setStyleSheet("background-color:rgb(230, 255, 230);")

        self.label = QtWidgets.QLabel(Dialog)  # memory game
        self.label.setGeometry(QtCore.QRect(350, 120, 291, 51))
        self.label.setStyleSheet("font: 75 18pt \"한컴 말랑말랑 Bold\";\n""")
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setObjectName("label")

        self.pushButton = QtWidgets.QPushButton(Dialog)  # h
        self.pushButton.setGeometry(QtCore.QRect(40, 450, 131, 131))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(23)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color:rgb(255, 173, 153);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(lambda: self.countingnum(1, Dialog))

        self.pushButton_2 = QtWidgets.QPushButton(Dialog)  # a
        self.pushButton_2.setGeometry(QtCore.QRect(230, 450, 131, 131))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(23)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color:rgb(255, 173, 153);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(lambda: self.countingnum(2, Dialog))

        self.pushButton_3 = QtWidgets.QPushButton(Dialog)  # r
        self.pushButton_3.setGeometry(QtCore.QRect(420, 450, 131, 131))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(23)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color:rgb(255, 173, 153);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(lambda: self.countingnum(3, Dialog))

        self.pushButton_4 = QtWidgets.QPushButton(Dialog)  # d
        self.pushButton_4.setGeometry(QtCore.QRect(610, 450, 131, 131))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(23)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("background-color:rgb(255, 173, 153);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(lambda: self.countingnum(4, Dialog))

        self.pushButton_5 = QtWidgets.QPushButton(Dialog)  # !
        self.pushButton_5.setGeometry(QtCore.QRect(790, 450, 131, 131))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(23)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("background-color:rgb(255, 173, 153);")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(lambda: self.countingnum(5, Dialog))

        self.label_2 = QtWidgets.QLabel(Dialog)  # level
        self.label_2.setGeometry(QtCore.QRect(70, 240, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.lineEdit = QtWidgets.QLineEdit(Dialog)  # lineedit
        self.lineEdit.setGeometry(QtCore.QRect(160, 240, 113, 31))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.playGame()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Memory Game"))
        self.pushButton.setText(_translate("Dialog", "1"))
        self.pushButton_2.setText(_translate("Dialog", "2"))
        self.pushButton_3.setText(_translate("Dialog", "3"))
        self.pushButton_4.setText(_translate("Dialog", "4"))
        self.pushButton_5.setText(_translate("Dialog", "5"))
        self.label_2.setText(_translate("Dialog", "Level:"))

    def playGame(self):
        breaktime = 400
        if self.roundcnt % 3 == 0:
            breaktime -= 50
        self.number = random.choices(range(1, 6), k=1)[0]
        self.numlist.append(self.number)
        self.lineEdit.setText(str(self.roundcnt))
        for k in range(len(self.numlist)):
            if self.numlist[k] == 1:
                self.pushButton.setStyleSheet("background-color: #DB4455")
                QtTest.QTest.qWait(breaktime)
            elif self.numlist[k] == 2:
                self.pushButton_2.setStyleSheet("background-color: #DB4455")
                QtTest.QTest.qWait(breaktime)
            elif self.numlist[k] == 3:
                self.pushButton_3.setStyleSheet("background-color: #DB4455")
                QtTest.QTest.qWait(breaktime)
            elif self.numlist[k] == 4:
                self.pushButton_4.setStyleSheet("background-color: #DB4455")
                QtTest.QTest.qWait(breaktime)
            elif self.numlist[k] == 5:
                self.pushButton_5.setStyleSheet("background-color: #DB4455")
                QtTest.QTest.qWait(breaktime)
            if len(self.numlist) > 1:
                self.pushButton_3.setStyleSheet("background-color:rgb(255, 173, 153);")
                self.pushButton_2.setStyleSheet("background-color:rgb(255, 173, 153);")
                self.pushButton.setStyleSheet("background-color:rgb(255, 173, 153);")
                self.pushButton_4.setStyleSheet("background-color:rgb(255, 173, 153);")
                self.pushButton_5.setStyleSheet("background-color:rgb(255, 173, 153);")
                QtTest.QTest.qWait(200)

    def countingnum(self, key, Dialog):
        self.numlist_user.append(key)
        if self.numlist_user[self.counting] == self.numlist[self.counting]:
            self.counting += 1
            if len(self.numlist) == len(self.numlist_user):
                self.numlist_user.clear()
                self.counting = 0
                self.roundcnt += 1
                self.playGame()
            else:
                pass
        else:
            Dialog.hide()
            Dialog1 = QtWidgets.QDialog()
            self.dialog = GameOver.Ui_Dialog()
            self.dialog.setupUi(Dialog1, self.roundcnt)
            Dialog1.show()
            Dialog1.exec()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())