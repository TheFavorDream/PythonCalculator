from PyQt5 import QtCore, QtGui, QtWidgets

from ComputeEngine import ComputeEngine

class Ui_Calculator(object):
    
    def __init__(self):
        super().__init__()
        self.ComE = ComputeEngine()
        self.IsOnAdvanceMode = False
        self.DisplayText = ""


    def AdvanceMode(self):
        self.IsOnAdvanceMode = not self.IsOnAdvanceMode

        if self.IsOnAdvanceMode == True:
                Calculator.setMinimumSize(QtCore.QSize(600, 400))
                Calculator.setMaximumSize(QtCore.QSize(600, 400))
        else:
                Calculator.setMinimumSize(QtCore.QSize(300, 400))
                Calculator.setMaximumSize(QtCore.QSize(300, 400))

    def SetInput(self, In):
         self.DisplayText += str(In)
         self.Display.setText(self.DisplayText)

    def Calculate(self):
         Sum = self.ComE.Calculate(self.DisplayText)
         self.DisplayText = str(Sum)
         self.Display.setText(self.DisplayText)

    def ClearInput(self):
         self.DisplayText = ""
         self.Display.setText(self.DisplayText)

    def Backspace(self):
         if len(self.DisplayText) == 0:
              return
         self.DisplayText = self.DisplayText[0 : len(self.DisplayText)-1]
         self.Display.setText(self.DisplayText)



    def setupUi(self, Calculator):
        Calculator.setObjectName("Calculator")
        Calculator.resize(600, 400)
        Calculator.setMinimumSize(QtCore.QSize(300, 400))
        Calculator.setMaximumSize(QtCore.QSize(300, 400))
        Calculator.setStyleSheet("background-color: rgb(26, 26, 25);")
        self.centralwidget = QtWidgets.QWidget(Calculator)
        self.centralwidget.setObjectName("centralwidget")

        self.BTN_Num_1 = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.SetInput(1))
        self.BTN_Num_1.setGeometry(QtCore.QRect(30, 160, 41, 41))
        self.BTN_Num_1.setStyleSheet("\n"
"background-color: rgb(255, 193, 37);")
        self.BTN_Num_1.setObjectName("BTN_Num_1")
        self.BTN_Num_2 = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.SetInput(2))
        self.BTN_Num_2.setGeometry(QtCore.QRect(80, 160, 41, 41))
        self.BTN_Num_2.setStyleSheet("\n"
"background-color: rgb(255, 193, 37);")
        self.BTN_Num_2.setObjectName("BTN_Num_2")
        self.BTN_Num_3 = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.SetInput(3))
        self.BTN_Num_3.setGeometry(QtCore.QRect(130, 160, 41, 41))
        self.BTN_Num_3.setStyleSheet("\n"
"background-color: rgb(255, 193, 37);")
        self.BTN_Num_3.setObjectName("BTN_Num_3")
        self.BTN_Num_4 = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.SetInput(4))
        self.BTN_Num_4.setGeometry(QtCore.QRect(30, 210, 41, 41))
        self.BTN_Num_4.setStyleSheet("\n"
"background-color: rgb(255, 193, 37);")
        self.BTN_Num_4.setObjectName("BTN_Num_4")
        self.BTN_Num_5 = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.SetInput(5))
        self.BTN_Num_5.setGeometry(QtCore.QRect(80, 210, 41, 41))
        self.BTN_Num_5.setStyleSheet("\n"
"background-color: rgb(255, 193, 37);")
        self.BTN_Num_5.setObjectName("BTN_Num_5")
        self.BTN_Num_6 = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.SetInput(6))
        self.BTN_Num_6.setGeometry(QtCore.QRect(130, 210, 41, 41))
        self.BTN_Num_6.setStyleSheet("\n"
"background-color: rgb(255, 193, 37);")
        self.BTN_Num_6.setObjectName("BTN_Num_6")
        self.BTN_Num_7 = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.SetInput(7))
        self.BTN_Num_7.setGeometry(QtCore.QRect(30, 260, 41, 41))
        self.BTN_Num_7.setStyleSheet("\n"
"background-color: rgb(255, 193, 37);")
        self.BTN_Num_7.setObjectName("BTN_Num_7")
        self.BTN_Num_8 = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.SetInput(8))
        self.BTN_Num_8.setGeometry(QtCore.QRect(80, 260, 41, 41))
        self.BTN_Num_8.setStyleSheet("\n"
"background-color: rgb(255, 193, 37);")
        self.BTN_Num_8.setObjectName("BTN_Num_8")
        self.BTN_Num_9 = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.SetInput(9))
        self.BTN_Num_9.setGeometry(QtCore.QRect(130, 260, 41, 41))
        self.BTN_Num_9.setStyleSheet("\n"
"background-color: rgb(255, 193, 37);")
        self.BTN_Num_9.setObjectName("BTN_Num_9")
        self.BTN_Num_10 = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.SetInput(0))
        self.BTN_Num_10.setGeometry(QtCore.QRect(30, 310, 91, 41))
        self.BTN_Num_10.setStyleSheet("\n"
"background-color: rgb(255, 193, 37);")
        self.BTN_Num_10.setObjectName("BTN_Num_10")
        self.Display = QtWidgets.QTextEdit(self.centralwidget)
        self.Display.setGeometry(QtCore.QRect(30, 10, 241, 61))
        self.Display.setStyleSheet("color: rgb(255, 255, 255);\n"
"")
        self.Display.setObjectName("Display")
        self.BTN_OP_Equal = QtWidgets.QPushButton(self.centralwidget, clicked=lambda:self.Calculate())
        self.BTN_OP_Equal.setGeometry(QtCore.QRect(130, 310, 41, 41))
        self.BTN_OP_Equal.setStyleSheet("\n"
"background-color: rgb(255, 193, 37);")
        self.BTN_OP_Equal.setObjectName("BTN_OP_Equal")
        self.BTN_OP_Add = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.SetInput("+"))
        self.BTN_OP_Add.setGeometry(QtCore.QRect(180, 260, 41, 91))
        self.BTN_OP_Add.setStyleSheet("\n"
"background-color: rgb(255, 193, 37);")
        self.BTN_OP_Add.setObjectName("BTN_OP_Add")
        self.BTN_OP_Sub = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.SetInput("-"))
        self.BTN_OP_Sub.setGeometry(QtCore.QRect(180, 210, 41, 41))
        self.BTN_OP_Sub.setStyleSheet("\n"
"background-color: rgb(255, 193, 37);")
        self.BTN_OP_Sub.setObjectName("BTN_OP_Sub")
        self.pushButton_14 = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.SetInput("x"))
        self.pushButton_14.setGeometry(QtCore.QRect(180, 160, 41, 41))
        self.pushButton_14.setStyleSheet("\n"
"background-color: rgb(255, 193, 37);")
        self.pushButton_14.setObjectName("pushButton_14")
        self.BTN_OP_Devide = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.SetInput('/'))
        self.BTN_OP_Devide.setGeometry(QtCore.QRect(230, 210, 41, 41))
        self.BTN_OP_Devide.setStyleSheet("\n"
"background-color: rgb(255, 193, 37);")
        self.BTN_OP_Devide.setObjectName("BTN_OP_Devide")
        self.BTN_Backspace = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.Backspace())  
        self.BTN_Backspace.setGeometry(QtCore.QRect(230, 260, 41, 41))
        self.BTN_Backspace.setStyleSheet("\n"
"background-color: rgb(255, 193, 37);")
        self.BTN_Backspace.setObjectName("BTN_Backspace")
        self.BTN_Clear = QtWidgets.QPushButton(self.centralwidget, clicked=lambda:self.ClearInput())
        self.BTN_Clear.setGeometry(QtCore.QRect(230, 310, 41, 41))
        self.BTN_Clear.setStyleSheet("\n"
"background-color: rgb(255, 193, 37);")
        self.BTN_Clear.setObjectName("BTN_Clear")
        self.BTN_Parantes = QtWidgets.QPushButton(self.centralwidget, clicked=lambda:self.SetInput("("))
        self.BTN_Parantes.setGeometry(QtCore.QRect(30, 110, 41, 31))
        self.BTN_Parantes.setStyleSheet("background-color: rgb(255, 193, 37);")
        self.BTN_Parantes.setObjectName("BTN_Parantes")
        self.BTN_Cos = QtWidgets.QPushButton(self.centralwidget)
        self.BTN_Cos.setGeometry(QtCore.QRect(130, 110, 41, 31))
        self.BTN_Cos.setStyleSheet("\n"
"background-color: rgb(255, 193, 37);")
        self.BTN_Cos.setObjectName("BTN_Cos")
        self.BTN_Pars_Open = QtWidgets.QPushButton(self.centralwidget, clicked=lambda:self.SetInput(")"))
        self.BTN_Pars_Open.setGeometry(QtCore.QRect(80, 110, 41, 31))
        self.BTN_Pars_Open.setStyleSheet("\n"
"background-color: rgb(255, 193, 37);")
        self.BTN_Pars_Open.setObjectName("BTN_Pars_Close")
        self.BTN_Sin = QtWidgets.QPushButton(self.centralwidget)
        self.BTN_Sin.setGeometry(QtCore.QRect(180, 110, 41, 31))
        self.BTN_Sin.setStyleSheet("\n"
"background-color: rgb(255, 193, 37);")
        self.BTN_Sin.setObjectName("BTN_Sin")
        self.BTN_Last = QtWidgets.QPushButton(self.centralwidget)
        self.BTN_Last.setGeometry(QtCore.QRect(230, 110, 41, 31))
        self.BTN_Last.setStyleSheet("\n"
"background-color: rgb(255, 193, 37);")
        self.BTN_Last.setObjectName("BTN_Last")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(110, 360, 101, 16))
        self.label.setObjectName("label")
        self.BTN_Num_A = QtWidgets.QPushButton(self.centralwidget)
        self.BTN_Num_A.setGeometry(QtCore.QRect(430, 110, 41, 41))
        self.BTN_Num_A.setStyleSheet("\n"
"background-color: rgb(255, 193, 37);")
        self.BTN_Num_A.setObjectName("BTN_Num_A")
        self.BTN_Num_B = QtWidgets.QPushButton(self.centralwidget)
        self.BTN_Num_B.setGeometry(QtCore.QRect(480, 110, 41, 41))
        self.BTN_Num_B.setStyleSheet("\n"
"background-color: rgb(255, 193, 37);")
        self.BTN_Num_B.setObjectName("BTN_Num_B")
        self.BTN_Num_C = QtWidgets.QPushButton(self.centralwidget)
        self.BTN_Num_C.setGeometry(QtCore.QRect(530, 110, 41, 41))
        self.BTN_Num_C.setStyleSheet("\n"
"background-color: rgb(255, 193, 37);")
        self.BTN_Num_C.setObjectName("BTN_Num_C")
        self.BTN_Num_D = QtWidgets.QPushButton(self.centralwidget)
        self.BTN_Num_D.setGeometry(QtCore.QRect(430, 160, 41, 41))
        self.BTN_Num_D.setStyleSheet("\n"
"background-color: rgb(255, 193, 37);")
        self.BTN_Num_D.setObjectName("BTN_Num_D")
        self.BTN_Num_E = QtWidgets.QPushButton(self.centralwidget)
        self.BTN_Num_E.setGeometry(QtCore.QRect(480, 160, 41, 41))
        self.BTN_Num_E.setStyleSheet("\n"
"background-color: rgb(255, 193, 37);")
        self.BTN_Num_E.setObjectName("BTN_Num_E")
        self.BTN_Num_F = QtWidgets.QPushButton(self.centralwidget)
        self.BTN_Num_F.setGeometry(QtCore.QRect(530, 160, 41, 41))
        self.BTN_Num_F.setStyleSheet("\n"
"background-color: rgb(255, 193, 37);")
        self.BTN_Num_F.setObjectName("BTN_Num_F")
        self.RB_Decimal = QtWidgets.QRadioButton(self.centralwidget, clicked=lambda: self.SetBase(10))
        self.RB_Decimal.setGeometry(QtCore.QRect(320, 20, 82, 17))
        self.RB_Decimal.setStyleSheet("color: rgb(255, 255, 255);")
        self.RB_Decimal.setChecked(True)
        self.RB_Decimal.setAutoRepeat(False)
        self.RB_Decimal.setObjectName("RB_Decimal")
        self.RB_Binary = QtWidgets.QRadioButton(self.centralwidget, clicked=lambda: self.SetBase(2))
        self.RB_Binary.setGeometry(QtCore.QRect(320, 40, 82, 17))
        self.RB_Binary.setStyleSheet("color: rgb(255, 255, 255);")
        self.RB_Binary.setAutoRepeat(True)
        self.RB_Binary.setObjectName("RB_Binary")
        self.RB_Octal = QtWidgets.QRadioButton(self.centralwidget, clicked=lambda: self.SetBase(8))
        self.RB_Octal.setGeometry(QtCore.QRect(320, 60, 82, 17))
        self.RB_Octal.setStyleSheet("color: rgb(255, 255, 255);")
        self.RB_Octal.setAutoRepeat(True)
        self.RB_Octal.setObjectName("RB_Octal")
        self.RB_Hexadecimal = QtWidgets.QRadioButton(self.centralwidget, clicked=lambda: self.SetBase(16))
        self.RB_Hexadecimal.setGeometry(QtCore.QRect(320, 80, 82, 17))
        self.RB_Hexadecimal.setStyleSheet("color: rgb(255, 255, 255);")
        self.RB_Hexadecimal.setAutoRepeat(True)
        self.RB_Hexadecimal.setObjectName("RB_Hexadecimal")
        self.CB_Advance = QtWidgets.QCheckBox(self.centralwidget, clicked=lambda: self.AdvanceMode())
        self.CB_Advance.setGeometry(QtCore.QRect(40, 80, 70, 17))
        self.CB_Advance.setStyleSheet("color: rgb(255, 255, 255);")
        self.CB_Advance.setObjectName("CB_Advance")
        self.BTN_OP_SqaureRoot = QtWidgets.QPushButton(self.centralwidget)
        self.BTN_OP_SqaureRoot.setGeometry(QtCore.QRect(320, 110, 41, 41))
        self.BTN_OP_SqaureRoot.setStyleSheet("image: url(:/Icons/Radical.svg);\n"
"background-color: rgb(255, 193, 37);")
        self.BTN_OP_SqaureRoot.setText("")
        self.BTN_OP_SqaureRoot.setObjectName("BTN_OP_SqaureRoot")
        self.BTN_OP_Isprime = QtWidgets.QPushButton(self.centralwidget)
        self.BTN_OP_Isprime.setGeometry(QtCore.QRect(370, 110, 51, 41))
        self.BTN_OP_Isprime.setStyleSheet("\n"
"background-color: rgb(255, 193, 37);")
        self.BTN_OP_Isprime.setObjectName("BTN_OP_Isprime")
        self.BTN_OP_Logarithm = QtWidgets.QPushButton(self.centralwidget)
        self.BTN_OP_Logarithm.setGeometry(QtCore.QRect(370, 160, 51, 41))
        self.BTN_OP_Logarithm.setStyleSheet("\n"
"background-color: rgb(255, 193, 37);")
        self.BTN_OP_Logarithm.setObjectName("BTN_OP_Logarithm")
        self.BTN_OP_Exponent = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.SetInput("^"))
        self.BTN_OP_Exponent.setGeometry(QtCore.QRect(320, 160, 41, 41))
        self.BTN_OP_Exponent.setStyleSheet("\n"
"background-color: rgb(255, 193, 37);")
        self.BTN_OP_Exponent.setObjectName("BTN_OP_Exponent")
        self.CB_From = QtWidgets.QComboBox(self.centralwidget)
        self.CB_From.setGeometry(QtCore.QRect(320, 230, 101, 22))
        self.CB_From.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 193, 37);")
        self.CB_From.setObjectName("CB_From")
        self.CB_From.addItem("")
        self.CB_From.addItem("")
        self.CB_From.addItem("")
        self.CB_From.addItem("")
        self.CB_To = QtWidgets.QComboBox(self.centralwidget)
        self.CB_To.setGeometry(QtCore.QRect(320, 300, 101, 22))
        self.CB_To.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 193, 37);")
        self.CB_To.setObjectName("CB_To")
        self.CB_To.addItem("")
        self.CB_To.addItem("")
        self.CB_To.addItem("")
        self.CB_To.addItem("")
        self.LE_In = QtWidgets.QLineEdit(self.centralwidget)
        self.LE_In.setGeometry(QtCore.QRect(320, 270, 151, 20))
        self.LE_In.setStyleSheet("color: rgb(255, 255, 255);")
        self.LE_In.setObjectName("LE_In")
        self.LE_Out = QtWidgets.QLineEdit(self.centralwidget)
        self.LE_Out.setGeometry(QtCore.QRect(320, 340, 151, 20))
        self.LE_Out.setStyleSheet("color: rgb(255, 255, 255);")
        self.LE_Out.setObjectName("LE_Out")
        self.BTN_OP_Inuse = QtWidgets.QPushButton(self.centralwidget)
        self.BTN_OP_Inuse.setGeometry(QtCore.QRect(480, 340, 71, 21))
        self.BTN_OP_Inuse.setStyleSheet("\n"
"background-color: rgb(255, 193, 37);")
        self.BTN_OP_Inuse.setObjectName("BTN_OP_Inuse")
        self.BTN_Dot = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.SetInput('.'))
        self.BTN_Dot.setGeometry(QtCore.QRect(230, 160, 41, 41))
        self.BTN_Dot.setStyleSheet("\n"
"background-color: rgb(255, 193, 37);")
        self.BTN_Dot.setObjectName("BTN_Dot")
        Calculator.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Calculator)
        self.statusbar.setObjectName("statusbar")
        Calculator.setStatusBar(self.statusbar)

        self.retranslateUi(Calculator)
        QtCore.QMetaObject.connectSlotsByName(Calculator)

    def retranslateUi(self, Calculator):
        _translate = QtCore.QCoreApplication.translate
        Calculator.setWindowTitle(_translate("Calculator", "Calculator"))
        self.BTN_Num_1.setText(_translate("Calculator", "1"))
        self.BTN_Num_2.setText(_translate("Calculator", "2"))
        self.BTN_Num_3.setText(_translate("Calculator", "3"))
        self.BTN_Num_4.setText(_translate("Calculator", "4"))
        self.BTN_Num_5.setText(_translate("Calculator", "5"))
        self.BTN_Num_6.setText(_translate("Calculator", "6"))
        self.BTN_Num_7.setText(_translate("Calculator", "7"))
        self.BTN_Num_8.setText(_translate("Calculator", "8"))
        self.BTN_Num_9.setText(_translate("Calculator", "9"))
        self.BTN_Num_10.setText(_translate("Calculator", "0"))
        self.BTN_OP_Equal.setText(_translate("Calculator", "="))
        self.BTN_OP_Add.setText(_translate("Calculator", "+"))
        self.BTN_OP_Sub.setText(_translate("Calculator", "-"))
        self.pushButton_14.setText(_translate("Calculator", "x"))
        self.BTN_OP_Devide.setText(_translate("Calculator", "/"))
        self.BTN_Backspace.setText(_translate("Calculator", "<-"))
        self.BTN_Clear.setText(_translate("Calculator", "CL"))
        self.BTN_Parantes.setText(_translate("Calculator", "("))
        self.BTN_Cos.setText(_translate("Calculator", "Cos"))
        self.BTN_Pars_Open.setText(_translate("Calculator", ")"))
        self.BTN_Sin.setText(_translate("Calculator", "Sin"))
        self.BTN_Last.setText(_translate("Calculator", "Last"))
        self.label.setText(_translate("Calculator", "Made by Poya"))
        self.BTN_Num_A.setText(_translate("Calculator", "A"))
        self.BTN_Num_B.setText(_translate("Calculator", "B"))
        self.BTN_Num_C.setText(_translate("Calculator", "C"))
        self.BTN_Num_D.setText(_translate("Calculator", "D"))
        self.BTN_Num_E.setText(_translate("Calculator", "E"))
        self.BTN_Num_F.setText(_translate("Calculator", "F"))
        self.RB_Decimal.setText(_translate("Calculator", "Decimal"))
        self.RB_Binary.setText(_translate("Calculator", "Binary"))
        self.RB_Octal.setText(_translate("Calculator", "Octal"))
        self.RB_Hexadecimal.setText(_translate("Calculator", "Hexadecimal"))
        self.CB_Advance.setText(_translate("Calculator", "Advance"))
        self.BTN_OP_Isprime.setText(_translate("Calculator", "Is Prime"))
        self.BTN_OP_Logarithm.setText(_translate("Calculator", "Log"))
        self.BTN_OP_Exponent.setText(_translate("Calculator", "x^y"))
        self.CB_From.setItemText(0, _translate("Calculator", "Decimal"))
        self.CB_From.setItemText(1, _translate("Calculator", "Octal"))
        self.CB_From.setItemText(2, _translate("Calculator", "Binary"))
        self.CB_From.setItemText(3, _translate("Calculator", "HexaDecimal"))
        self.CB_To.setItemText(0, _translate("Calculator", "Decimal"))
        self.CB_To.setItemText(1, _translate("Calculator", "Octal"))
        self.CB_To.setItemText(2, _translate("Calculator", "Binary"))
        self.CB_To.setItemText(3, _translate("Calculator", "HexaDecimal"))
        self.BTN_OP_Inuse.setText(_translate("Calculator", "In Use"))
        self.BTN_Dot.setText(_translate("Calculator", "."))
import Icons_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Calculator = QtWidgets.QMainWindow()
    ui = Ui_Calculator()
    ui.setupUi(Calculator)
    Calculator.show()
    sys.exit(app.exec_())
