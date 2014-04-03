# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demoGUI.ui'
#
# Created: Thu Apr 03 12:10:47 2014
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(1112, 789)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("images/puzzlebox.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.tabWidget = QtGui.QTabWidget(Form)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1111, 791))
        self.tabWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tabDrive = QtGui.QWidget()
        self.tabDrive.setObjectName(_fromUtf8("tabDrive"))
        self.groupBox_Speed = QtGui.QGroupBox(self.tabDrive)
        self.groupBox_Speed.setGeometry(QtCore.QRect(690, 230, 301, 301))
        self.groupBox_Speed.setObjectName(_fromUtf8("groupBox_Speed"))
        self.dialSpeed = QtGui.QDial(self.groupBox_Speed)
        self.dialSpeed.setGeometry(QtCore.QRect(30, 60, 241, 201))
        self.dialSpeed.setSingleStep(5)
        self.dialSpeed.setInvertedAppearance(False)
        self.dialSpeed.setInvertedControls(False)
        self.dialSpeed.setNotchesVisible(True)
        self.dialSpeed.setObjectName(_fromUtf8("dialSpeed"))
        self.label_4 = QtGui.QLabel(self.groupBox_Speed)
        self.label_4.setGeometry(QtCore.QRect(50, 250, 53, 16))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self.groupBox_Speed)
        self.label_5.setGeometry(QtCore.QRect(200, 250, 53, 16))
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(self.groupBox_Speed)
        self.label_6.setGeometry(QtCore.QRect(120, 40, 53, 16))
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.groupBox_Drive = QtGui.QGroupBox(self.tabDrive)
        self.groupBox_Drive.setGeometry(QtCore.QRect(120, 150, 381, 441))
        self.groupBox_Drive.setObjectName(_fromUtf8("groupBox_Drive"))
        self.pushButtonStop = QtGui.QPushButton(self.groupBox_Drive)
        self.pushButtonStop.setGeometry(QtCore.QRect(140, 170, 101, 101))
        self.pushButtonStop.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("images/stop.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonStop.setIcon(icon1)
        self.pushButtonStop.setIconSize(QtCore.QSize(70, 70))
        self.pushButtonStop.setObjectName(_fromUtf8("pushButtonStop"))
        self.pushButtonRight = QtGui.QPushButton(self.groupBox_Drive)
        self.pushButtonRight.setGeometry(QtCore.QRect(260, 170, 101, 101))
        self.pushButtonRight.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("images/right.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonRight.setIcon(icon2)
        self.pushButtonRight.setIconSize(QtCore.QSize(70, 70))
        self.pushButtonRight.setObjectName(_fromUtf8("pushButtonRight"))
        self.pushButtonReverse = QtGui.QPushButton(self.groupBox_Drive)
        self.pushButtonReverse.setGeometry(QtCore.QRect(140, 290, 101, 101))
        self.pushButtonReverse.setText(_fromUtf8(""))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8("images/reverse.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonReverse.setIcon(icon3)
        self.pushButtonReverse.setIconSize(QtCore.QSize(70, 70))
        self.pushButtonReverse.setObjectName(_fromUtf8("pushButtonReverse"))
        self.pushButtonForward = QtGui.QPushButton(self.groupBox_Drive)
        self.pushButtonForward.setGeometry(QtCore.QRect(140, 50, 101, 101))
        self.pushButtonForward.setText(_fromUtf8(""))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8("images/forward.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonForward.setIcon(icon4)
        self.pushButtonForward.setIconSize(QtCore.QSize(70, 70))
        self.pushButtonForward.setObjectName(_fromUtf8("pushButtonForward"))
        self.pushButtonLeft = QtGui.QPushButton(self.groupBox_Drive)
        self.pushButtonLeft.setGeometry(QtCore.QRect(20, 170, 101, 101))
        self.pushButtonLeft.setText(_fromUtf8(""))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8("images/left.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonLeft.setIcon(icon5)
        self.pushButtonLeft.setIconSize(QtCore.QSize(70, 70))
        self.pushButtonLeft.setObjectName(_fromUtf8("pushButtonLeft"))
        self.labelWheelchairStatus = QtGui.QLabel(self.tabDrive)
        self.labelWheelchairStatus.setGeometry(QtCore.QRect(440, 30, 261, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labelWheelchairStatus.setFont(font)
        self.labelWheelchairStatus.setObjectName(_fromUtf8("labelWheelchairStatus"))
        self.tabWidget.addTab(self.tabDrive, _fromUtf8(""))
        self.tabMessage = QtGui.QWidget()
        self.tabMessage.setObjectName(_fromUtf8("tabMessage"))
        self.groupBox_keyboard = QtGui.QGroupBox(self.tabMessage)
        self.groupBox_keyboard.setGeometry(QtCore.QRect(40, 160, 1021, 451))
        self.groupBox_keyboard.setObjectName(_fromUtf8("groupBox_keyboard"))
        self.keyboardQ = QtGui.QPushButton(self.groupBox_keyboard)
        self.keyboardQ.setGeometry(QtCore.QRect(30, 120, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.keyboardQ.setFont(font)
        self.keyboardQ.setObjectName(_fromUtf8("keyboardQ"))
        self.keyboardW = QtGui.QPushButton(self.groupBox_keyboard)
        self.keyboardW.setGeometry(QtCore.QRect(110, 120, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.keyboardW.setFont(font)
        self.keyboardW.setObjectName(_fromUtf8("keyboardW"))
        self.keyboardT = QtGui.QPushButton(self.groupBox_keyboard)
        self.keyboardT.setGeometry(QtCore.QRect(350, 120, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.keyboardT.setFont(font)
        self.keyboardT.setObjectName(_fromUtf8("keyboardT"))
        self.keyboardE = QtGui.QPushButton(self.groupBox_keyboard)
        self.keyboardE.setGeometry(QtCore.QRect(190, 120, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.keyboardE.setFont(font)
        self.keyboardE.setObjectName(_fromUtf8("keyboardE"))
        self.keyboardR = QtGui.QPushButton(self.groupBox_keyboard)
        self.keyboardR.setGeometry(QtCore.QRect(270, 120, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.keyboardR.setFont(font)
        self.keyboardR.setObjectName(_fromUtf8("keyboardR"))
        self.keyboardY = QtGui.QPushButton(self.groupBox_keyboard)
        self.keyboardY.setGeometry(QtCore.QRect(430, 120, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.keyboardY.setFont(font)
        self.keyboardY.setObjectName(_fromUtf8("keyboardY"))
        self.keyboardU = QtGui.QPushButton(self.groupBox_keyboard)
        self.keyboardU.setGeometry(QtCore.QRect(510, 120, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.keyboardU.setFont(font)
        self.keyboardU.setObjectName(_fromUtf8("keyboardU"))
        self.keyboardI = QtGui.QPushButton(self.groupBox_keyboard)
        self.keyboardI.setGeometry(QtCore.QRect(590, 120, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.keyboardI.setFont(font)
        self.keyboardI.setObjectName(_fromUtf8("keyboardI"))
        self.keyboardO = QtGui.QPushButton(self.groupBox_keyboard)
        self.keyboardO.setGeometry(QtCore.QRect(670, 120, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.keyboardO.setFont(font)
        self.keyboardO.setObjectName(_fromUtf8("keyboardO"))
        self.keyboardP = QtGui.QPushButton(self.groupBox_keyboard)
        self.keyboardP.setGeometry(QtCore.QRect(750, 120, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.keyboardP.setFont(font)
        self.keyboardP.setObjectName(_fromUtf8("keyboardP"))
        self.keyboardNum5 = QtGui.QPushButton(self.groupBox_keyboard)
        self.keyboardNum5.setGeometry(QtCore.QRect(350, 40, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.keyboardNum5.setFont(font)
        self.keyboardNum5.setObjectName(_fromUtf8("keyboardNum5"))
        self.keyboardNum4 = QtGui.QPushButton(self.groupBox_keyboard)
        self.keyboardNum4.setGeometry(QtCore.QRect(270, 40, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.keyboardNum4.setFont(font)
        self.keyboardNum4.setObjectName(_fromUtf8("keyboardNum4"))
        self.keyboardNum3 = QtGui.QPushButton(self.groupBox_keyboard)
        self.keyboardNum3.setGeometry(QtCore.QRect(190, 40, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.keyboardNum3.setFont(font)
        self.keyboardNum3.setObjectName(_fromUtf8("keyboardNum3"))
        self.keyboardNum2 = QtGui.QPushButton(self.groupBox_keyboard)
        self.keyboardNum2.setGeometry(QtCore.QRect(110, 40, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.keyboardNum2.setFont(font)
        self.keyboardNum2.setObjectName(_fromUtf8("keyboardNum2"))
        self.keyboardNum1 = QtGui.QPushButton(self.groupBox_keyboard)
        self.keyboardNum1.setGeometry(QtCore.QRect(30, 40, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.keyboardNum1.setFont(font)
        self.keyboardNum1.setObjectName(_fromUtf8("keyboardNum1"))
        self.keyboardM = QtGui.QPushButton(self.groupBox_keyboard)
        self.keyboardM.setGeometry(QtCore.QRect(510, 280, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.keyboardM.setFont(font)
        self.keyboardM.setObjectName(_fromUtf8("keyboardM"))
        self.keyboardZ = QtGui.QPushButton(self.groupBox_keyboard)
        self.keyboardZ.setGeometry(QtCore.QRect(30, 280, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.keyboardZ.setFont(font)
        self.keyboardZ.setObjectName(_fromUtf8("keyboardZ"))
        self.keyboardL = QtGui.QPushButton(self.groupBox_keyboard)
        self.keyboardL.setGeometry(QtCore.QRect(670, 200, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.keyboardL.setFont(font)
        self.keyboardL.setObjectName(_fromUtf8("keyboardL"))
        self.keyboardK = QtGui.QPushButton(self.groupBox_keyboard)
        self.keyboardK.setGeometry(QtCore.QRect(590, 200, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.keyboardK.setFont(font)
        self.keyboardK.setObjectName(_fromUtf8("keyboardK"))
        self.keyboardJ = QtGui.QPushButton(self.groupBox_keyboard)
        self.keyboardJ.setGeometry(QtCore.QRect(510, 200, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.keyboardJ.setFont(font)
        self.keyboardJ.setObjectName(_fromUtf8("keyboardJ"))
        self.keyboardH = QtGui.QPushButton(self.groupBox_keyboard)
        self.keyboardH.setGeometry(QtCore.QRect(430, 200, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.keyboardH.setFont(font)
        self.keyboardH.setObjectName(_fromUtf8("keyboardH"))
        self.keyboardG = QtGui.QPushButton(self.groupBox_keyboard)
        self.keyboardG.setGeometry(QtCore.QRect(350, 200, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.keyboardG.setFont(font)
        self.keyboardG.setObjectName(_fromUtf8("keyboardG"))
        self.keyboardF = QtGui.QPushButton(self.groupBox_keyboard)
        self.keyboardF.setGeometry(QtCore.QRect(270, 200, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.keyboardF.setFont(font)
        self.keyboardF.setObjectName(_fromUtf8("keyboardF"))
        self.keyboardD = QtGui.QPushButton(self.groupBox_keyboard)
        self.keyboardD.setGeometry(QtCore.QRect(190, 200, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.keyboardD.setFont(font)
        self.keyboardD.setObjectName(_fromUtf8("keyboardD"))
        self.keyboardS = QtGui.QPushButton(self.groupBox_keyboard)
        self.keyboardS.setGeometry(QtCore.QRect(110, 200, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.keyboardS.setFont(font)
        self.keyboardS.setObjectName(_fromUtf8("keyboardS"))
        self.keyboardA = QtGui.QPushButton(self.groupBox_keyboard)
        self.keyboardA.setGeometry(QtCore.QRect(30, 200, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.keyboardA.setFont(font)
        self.keyboardA.setObjectName(_fromUtf8("keyboardA"))
        self.keyboardX = QtGui.QPushButton(self.groupBox_keyboard)
        self.keyboardX.setGeometry(QtCore.QRect(110, 280, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.keyboardX.setFont(font)
        self.keyboardX.setObjectName(_fromUtf8("keyboardX"))
        self.keyboardC = QtGui.QPushButton(self.groupBox_keyboard)
        self.keyboardC.setGeometry(QtCore.QRect(190, 280, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.keyboardC.setFont(font)
        self.keyboardC.setObjectName(_fromUtf8("keyboardC"))
        self.keyboardV = QtGui.QPushButton(self.groupBox_keyboard)
        self.keyboardV.setGeometry(QtCore.QRect(270, 280, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.keyboardV.setFont(font)
        self.keyboardV.setObjectName(_fromUtf8("keyboardV"))
        self.keyboardB = QtGui.QPushButton(self.groupBox_keyboard)
        self.keyboardB.setGeometry(QtCore.QRect(350, 280, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.keyboardB.setFont(font)
        self.keyboardB.setObjectName(_fromUtf8("keyboardB"))
        self.keyboardN = QtGui.QPushButton(self.groupBox_keyboard)
        self.keyboardN.setGeometry(QtCore.QRect(430, 280, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.keyboardN.setFont(font)
        self.keyboardN.setObjectName(_fromUtf8("keyboardN"))
        self.keyboardNum8 = QtGui.QPushButton(self.groupBox_keyboard)
        self.keyboardNum8.setGeometry(QtCore.QRect(590, 40, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.keyboardNum8.setFont(font)
        self.keyboardNum8.setObjectName(_fromUtf8("keyboardNum8"))
        self.keyboardNum9 = QtGui.QPushButton(self.groupBox_keyboard)
        self.keyboardNum9.setGeometry(QtCore.QRect(670, 40, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.keyboardNum9.setFont(font)
        self.keyboardNum9.setObjectName(_fromUtf8("keyboardNum9"))
        self.keyboardNum7 = QtGui.QPushButton(self.groupBox_keyboard)
        self.keyboardNum7.setGeometry(QtCore.QRect(510, 40, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.keyboardNum7.setFont(font)
        self.keyboardNum7.setObjectName(_fromUtf8("keyboardNum7"))
        self.keyboardNum6 = QtGui.QPushButton(self.groupBox_keyboard)
        self.keyboardNum6.setGeometry(QtCore.QRect(430, 40, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.keyboardNum6.setFont(font)
        self.keyboardNum6.setObjectName(_fromUtf8("keyboardNum6"))
        self.keyboardNum0 = QtGui.QPushButton(self.groupBox_keyboard)
        self.keyboardNum0.setGeometry(QtCore.QRect(750, 40, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.keyboardNum0.setFont(font)
        self.keyboardNum0.setObjectName(_fromUtf8("keyboardNum0"))
        self.keyboardPeriod = QtGui.QPushButton(self.groupBox_keyboard)
        self.keyboardPeriod.setGeometry(QtCore.QRect(670, 280, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.keyboardPeriod.setFont(font)
        self.keyboardPeriod.setObjectName(_fromUtf8("keyboardPeriod"))
        self.keyboardQuestionMark = QtGui.QPushButton(self.groupBox_keyboard)
        self.keyboardQuestionMark.setGeometry(QtCore.QRect(750, 280, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.keyboardQuestionMark.setFont(font)
        self.keyboardQuestionMark.setObjectName(_fromUtf8("keyboardQuestionMark"))
        self.keyboardExclamationMark = QtGui.QPushButton(self.groupBox_keyboard)
        self.keyboardExclamationMark.setGeometry(QtCore.QRect(840, 280, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.keyboardExclamationMark.setFont(font)
        self.keyboardExclamationMark.setObjectName(_fromUtf8("keyboardExclamationMark"))
        self.keyboardApostrophe = QtGui.QPushButton(self.groupBox_keyboard)
        self.keyboardApostrophe.setGeometry(QtCore.QRect(750, 200, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.keyboardApostrophe.setFont(font)
        self.keyboardApostrophe.setObjectName(_fromUtf8("keyboardApostrophe"))
        self.keyboardBackspace = QtGui.QPushButton(self.groupBox_keyboard)
        self.keyboardBackspace.setGeometry(QtCore.QRect(840, 40, 151, 71))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.keyboardBackspace.setFont(font)
        self.keyboardBackspace.setObjectName(_fromUtf8("keyboardBackspace"))
        self.keyboardSpace = QtGui.QPushButton(self.groupBox_keyboard)
        self.keyboardSpace.setGeometry(QtCore.QRect(190, 360, 471, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.keyboardSpace.setFont(font)
        self.keyboardSpace.setObjectName(_fromUtf8("keyboardSpace"))
        self.keyboardColon = QtGui.QPushButton(self.groupBox_keyboard)
        self.keyboardColon.setGeometry(QtCore.QRect(840, 200, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.keyboardColon.setFont(font)
        self.keyboardColon.setObjectName(_fromUtf8("keyboardColon"))
        self.keyboardSemiColon = QtGui.QPushButton(self.groupBox_keyboard)
        self.keyboardSemiColon.setGeometry(QtCore.QRect(920, 200, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.keyboardSemiColon.setFont(font)
        self.keyboardSemiColon.setObjectName(_fromUtf8("keyboardSemiColon"))
        self.keyboardLeftParen = QtGui.QPushButton(self.groupBox_keyboard)
        self.keyboardLeftParen.setGeometry(QtCore.QRect(840, 120, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.keyboardLeftParen.setFont(font)
        self.keyboardLeftParen.setObjectName(_fromUtf8("keyboardLeftParen"))
        self.keyboardRightParen = QtGui.QPushButton(self.groupBox_keyboard)
        self.keyboardRightParen.setGeometry(QtCore.QRect(920, 120, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.keyboardRightParen.setFont(font)
        self.keyboardRightParen.setObjectName(_fromUtf8("keyboardRightParen"))
        self.keyboardSlash = QtGui.QPushButton(self.groupBox_keyboard)
        self.keyboardSlash.setGeometry(QtCore.QRect(920, 280, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.keyboardSlash.setFont(font)
        self.keyboardSlash.setObjectName(_fromUtf8("keyboardSlash"))
        self.keyboardComma = QtGui.QPushButton(self.groupBox_keyboard)
        self.keyboardComma.setGeometry(QtCore.QRect(590, 280, 71, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.keyboardComma.setFont(font)
        self.keyboardComma.setObjectName(_fromUtf8("keyboardComma"))
        self.messageClearButton = QtGui.QPushButton(self.groupBox_keyboard)
        self.messageClearButton.setGeometry(QtCore.QRect(840, 360, 151, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.messageClearButton.setFont(font)
        self.messageClearButton.setObjectName(_fromUtf8("messageClearButton"))
        self.groupBox_message = QtGui.QGroupBox(self.tabMessage)
        self.groupBox_message.setGeometry(QtCore.QRect(40, 20, 1021, 131))
        self.groupBox_message.setObjectName(_fromUtf8("groupBox_message"))
        self.messageTextBox = QtGui.QLineEdit(self.groupBox_message)
        self.messageTextBox.setGeometry(QtCore.QRect(20, 30, 831, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.messageTextBox.setFont(font)
        self.messageTextBox.setText(_fromUtf8(""))
        self.messageTextBox.setObjectName(_fromUtf8("messageTextBox"))
        self.messageSendButton = QtGui.QPushButton(self.groupBox_message)
        self.messageSendButton.setGeometry(QtCore.QRect(870, 30, 131, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.messageSendButton.setFont(font)
        self.messageSendButton.setObjectName(_fromUtf8("messageSendButton"))
        self.groupBox_Controls = QtGui.QGroupBox(self.tabMessage)
        self.groupBox_Controls.setGeometry(QtCore.QRect(40, 630, 1021, 121))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.groupBox_Controls.setFont(font)
        self.groupBox_Controls.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_Controls.setObjectName(_fromUtf8("groupBox_Controls"))
        self.keyboardSelectLeft = QtGui.QPushButton(self.groupBox_Controls)
        self.keyboardSelectLeft.setGeometry(QtCore.QRect(30, 30, 321, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.keyboardSelectLeft.setFont(font)
        self.keyboardSelectLeft.setStyleSheet(_fromUtf8("background-color: rgb(112, 174, 255);"))
        self.keyboardSelectLeft.setObjectName(_fromUtf8("keyboardSelectLeft"))
        self.keyboardSelectRight = QtGui.QPushButton(self.groupBox_Controls)
        self.keyboardSelectRight.setGeometry(QtCore.QRect(670, 30, 321, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.keyboardSelectRight.setFont(font)
        self.keyboardSelectRight.setStyleSheet(_fromUtf8("background-color: rgb(255, 115, 80);"))
        self.keyboardSelectRight.setObjectName(_fromUtf8("keyboardSelectRight"))
        self.tabWidget.addTab(self.tabMessage, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.tabControlPanel = QtGui.QWidget()
        self.tabControlPanel.setObjectName(_fromUtf8("tabControlPanel"))
        self.groupBox_EEGsetup = QtGui.QGroupBox(self.tabControlPanel)
        self.groupBox_EEGsetup.setGeometry(QtCore.QRect(30, 30, 211, 241))
        self.groupBox_EEGsetup.setObjectName(_fromUtf8("groupBox_EEGsetup"))
        self.comboBox_EEG = QtGui.QComboBox(self.groupBox_EEGsetup)
        self.comboBox_EEG.setGeometry(QtCore.QRect(20, 30, 171, 31))
        self.comboBox_EEG.setObjectName(_fromUtf8("comboBox_EEG"))
        self.comboBox_EEG.addItem(_fromUtf8(""))
        self.pushButton_EEGconnect = QtGui.QPushButton(self.groupBox_EEGsetup)
        self.pushButton_EEGconnect.setGeometry(QtCore.QRect(20, 190, 171, 31))
        self.pushButton_EEGconnect.setObjectName(_fromUtf8("pushButton_EEGconnect"))
        self.label = QtGui.QLabel(self.groupBox_EEGsetup)
        self.label.setGeometry(QtCore.QRect(10, 100, 53, 16))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.groupBox_EEGsetup)
        self.label_2.setGeometry(QtCore.QRect(10, 150, 53, 16))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.lineEdit_Host = QtGui.QLineEdit(self.groupBox_EEGsetup)
        self.lineEdit_Host.setGeometry(QtCore.QRect(60, 90, 131, 31))
        self.lineEdit_Host.setInputMask(_fromUtf8(""))
        self.lineEdit_Host.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_Host.setDragEnabled(True)
        self.lineEdit_Host.setPlaceholderText(_fromUtf8(""))
        self.lineEdit_Host.setObjectName(_fromUtf8("lineEdit_Host"))
        self.lineEdit_Port = QtGui.QLineEdit(self.groupBox_EEGsetup)
        self.lineEdit_Port.setGeometry(QtCore.QRect(60, 140, 131, 31))
        self.lineEdit_Port.setText(_fromUtf8(""))
        self.lineEdit_Port.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_Port.setDragEnabled(True)
        self.lineEdit_Port.setObjectName(_fromUtf8("lineEdit_Port"))
        self.groupBox_Device = QtGui.QGroupBox(self.tabControlPanel)
        self.groupBox_Device.setGeometry(QtCore.QRect(270, 40, 221, 121))
        self.groupBox_Device.setObjectName(_fromUtf8("groupBox_Device"))
        self.comboBoxDeviceSelect = QtGui.QComboBox(self.groupBox_Device)
        self.comboBoxDeviceSelect.setGeometry(QtCore.QRect(20, 30, 181, 31))
        self.comboBoxDeviceSelect.setObjectName(_fromUtf8("comboBoxDeviceSelect"))
        self.comboBoxDeviceSelect.addItem(_fromUtf8(""))
        self.comboBoxDeviceSelect.addItem(_fromUtf8(""))
        self.pushButtonDeviceSearch = QtGui.QPushButton(self.groupBox_Device)
        self.pushButtonDeviceSearch.setGeometry(QtCore.QRect(20, 80, 71, 28))
        self.pushButtonDeviceSearch.setObjectName(_fromUtf8("pushButtonDeviceSearch"))
        self.pushButtonDeviceConnect = QtGui.QPushButton(self.groupBox_Device)
        self.pushButtonDeviceConnect.setGeometry(QtCore.QRect(100, 80, 101, 28))
        self.pushButtonDeviceConnect.setObjectName(_fromUtf8("pushButtonDeviceConnect"))
        self.groupBox_MsgDest = QtGui.QGroupBox(self.tabControlPanel)
        self.groupBox_MsgDest.setGeometry(QtCore.QRect(540, 50, 241, 211))
        self.groupBox_MsgDest.setObjectName(_fromUtf8("groupBox_MsgDest"))
        self.selectDestType = QtGui.QComboBox(self.groupBox_MsgDest)
        self.selectDestType.setGeometry(QtCore.QRect(20, 30, 201, 31))
        self.selectDestType.setObjectName(_fromUtf8("selectDestType"))
        self.selectDestType.addItem(_fromUtf8(""))
        self.selectDestType.addItem(_fromUtf8(""))
        self.lineEditMsgDest = QtGui.QLineEdit(self.groupBox_MsgDest)
        self.lineEditMsgDest.setGeometry(QtCore.QRect(20, 120, 201, 31))
        self.lineEditMsgDest.setInputMask(_fromUtf8(""))
        self.lineEditMsgDest.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditMsgDest.setDragEnabled(True)
        self.lineEditMsgDest.setPlaceholderText(_fromUtf8(""))
        self.lineEditMsgDest.setObjectName(_fromUtf8("lineEditMsgDest"))
        self.clearMsgDest = QtGui.QPushButton(self.groupBox_MsgDest)
        self.clearMsgDest.setGeometry(QtCore.QRect(20, 170, 71, 28))
        self.clearMsgDest.setObjectName(_fromUtf8("clearMsgDest"))
        self.setMsgDest = QtGui.QPushButton(self.groupBox_MsgDest)
        self.setMsgDest.setGeometry(QtCore.QRect(120, 170, 101, 28))
        self.setMsgDest.setObjectName(_fromUtf8("setMsgDest"))
        self.selectPhoneCarrier = QtGui.QComboBox(self.groupBox_MsgDest)
        self.selectPhoneCarrier.setGeometry(QtCore.QRect(20, 70, 201, 31))
        self.selectPhoneCarrier.setObjectName(_fromUtf8("selectPhoneCarrier"))
        self.selectPhoneCarrier.addItem(_fromUtf8(""))
        self.selectPhoneCarrier.addItem(_fromUtf8(""))
        self.selectPhoneCarrier.addItem(_fromUtf8(""))
        self.selectPhoneCarrier.addItem(_fromUtf8(""))
        self.tabWidget.addTab(self.tabControlPanel, _fromUtf8(""))

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Capstone C6", None))
        self.groupBox_Speed.setTitle(_translate("Form", "Wheelchair Speed", None))
        self.label_4.setText(_translate("Form", "Stopped", None))
        self.label_5.setText(_translate("Form", "Maximum", None))
        self.label_6.setText(_translate("Form", "Slow", None))
        self.groupBox_Drive.setTitle(_translate("Form", "Wheelchair Control", None))
        self.labelWheelchairStatus.setText(_translate("Form", "Status: ", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabDrive), _translate("Form", "Drive", None))
        self.groupBox_keyboard.setTitle(_translate("Form", "Keyboard", None))
        self.keyboardQ.setText(_translate("Form", "Q", None))
        self.keyboardW.setText(_translate("Form", "W", None))
        self.keyboardT.setText(_translate("Form", "T", None))
        self.keyboardE.setText(_translate("Form", "E", None))
        self.keyboardR.setText(_translate("Form", "R", None))
        self.keyboardY.setText(_translate("Form", "Y", None))
        self.keyboardU.setText(_translate("Form", "U", None))
        self.keyboardI.setText(_translate("Form", "I", None))
        self.keyboardO.setText(_translate("Form", "O", None))
        self.keyboardP.setText(_translate("Form", "P", None))
        self.keyboardNum5.setText(_translate("Form", "5", None))
        self.keyboardNum4.setText(_translate("Form", "4", None))
        self.keyboardNum3.setText(_translate("Form", "3", None))
        self.keyboardNum2.setText(_translate("Form", "2", None))
        self.keyboardNum1.setText(_translate("Form", "1", None))
        self.keyboardM.setText(_translate("Form", "M", None))
        self.keyboardZ.setText(_translate("Form", "Z", None))
        self.keyboardL.setText(_translate("Form", "L", None))
        self.keyboardK.setText(_translate("Form", "K", None))
        self.keyboardJ.setText(_translate("Form", "J", None))
        self.keyboardH.setText(_translate("Form", "H", None))
        self.keyboardG.setText(_translate("Form", "G", None))
        self.keyboardF.setText(_translate("Form", "F", None))
        self.keyboardD.setText(_translate("Form", "D", None))
        self.keyboardS.setText(_translate("Form", "S", None))
        self.keyboardA.setText(_translate("Form", "A", None))
        self.keyboardX.setText(_translate("Form", "X", None))
        self.keyboardC.setText(_translate("Form", "C", None))
        self.keyboardV.setText(_translate("Form", "V", None))
        self.keyboardB.setText(_translate("Form", "B", None))
        self.keyboardN.setText(_translate("Form", "N", None))
        self.keyboardNum8.setText(_translate("Form", "8", None))
        self.keyboardNum9.setText(_translate("Form", "9", None))
        self.keyboardNum7.setText(_translate("Form", "7", None))
        self.keyboardNum6.setText(_translate("Form", "6", None))
        self.keyboardNum0.setText(_translate("Form", "0", None))
        self.keyboardPeriod.setText(_translate("Form", ".", None))
        self.keyboardQuestionMark.setText(_translate("Form", "?", None))
        self.keyboardExclamationMark.setText(_translate("Form", "!", None))
        self.keyboardApostrophe.setText(_translate("Form", "\'", None))
        self.keyboardBackspace.setText(_translate("Form", "Backspace", None))
        self.keyboardSpace.setText(_translate("Form", "Space", None))
        self.keyboardColon.setText(_translate("Form", ":", None))
        self.keyboardSemiColon.setText(_translate("Form", ";", None))
        self.keyboardLeftParen.setText(_translate("Form", "(", None))
        self.keyboardRightParen.setText(_translate("Form", ")", None))
        self.keyboardSlash.setText(_translate("Form", "/", None))
        self.keyboardComma.setText(_translate("Form", ",", None))
        self.messageClearButton.setText(_translate("Form", "Clear", None))
        self.groupBox_message.setTitle(_translate("Form", "Message", None))
        self.messageSendButton.setText(_translate("Form", "Send", None))
        self.groupBox_Controls.setTitle(_translate("Form", "Controls", None))
        self.keyboardSelectLeft.setText(_translate("Form", "Select", None))
        self.keyboardSelectRight.setText(_translate("Form", "Next", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabMessage), _translate("Form", "Send Message", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Form", "Placeholder", None))
        self.groupBox_EEGsetup.setTitle(_translate("Form", "EEG Device Setup", None))
        self.comboBox_EEG.setItemText(0, _translate("Form", "Emotiv EPOC", None))
        self.pushButton_EEGconnect.setText(_translate("Form", "Connect", None))
        self.label.setText(_translate("Form", "Host", None))
        self.label_2.setText(_translate("Form", "Port", None))
        self.groupBox_Device.setTitle(_translate("Form", "Device Select", None))
        self.comboBoxDeviceSelect.setItemText(0, _translate("Form", "Wheelchair", None))
        self.comboBoxDeviceSelect.setItemText(1, _translate("Form", "RC Car", None))
        self.pushButtonDeviceSearch.setText(_translate("Form", "Search", None))
        self.pushButtonDeviceConnect.setText(_translate("Form", "Connect", None))
        self.groupBox_MsgDest.setTitle(_translate("Form", "Message Destination", None))
        self.selectDestType.setItemText(0, _translate("Form", "Phone Number", None))
        self.selectDestType.setItemText(1, _translate("Form", "Email Address", None))
        self.clearMsgDest.setText(_translate("Form", "Clear", None))
        self.setMsgDest.setText(_translate("Form", "Set Destination", None))
        self.selectPhoneCarrier.setItemText(0, _translate("Form", "AT&T", None))
        self.selectPhoneCarrier.setItemText(1, _translate("Form", "Sprint", None))
        self.selectPhoneCarrier.setItemText(2, _translate("Form", "T-Mobile", None))
        self.selectPhoneCarrier.setItemText(3, _translate("Form", "Verizon", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabControlPanel), _translate("Form", "Control Panel", None))

