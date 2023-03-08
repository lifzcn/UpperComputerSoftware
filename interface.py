# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setEnabled(True)
        Form.resize(480, 640)
        Form.setMinimumSize(QtCore.QSize(480, 640))
        Form.setMaximumSize(QtCore.QSize(480, 640))
        self.label_Title = QtWidgets.QLabel(Form)
        self.label_Title.setGeometry(QtCore.QRect(110, 10, 261, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_Title.setFont(font)
        self.label_Title.setObjectName("label_Title")
        self.label_CurrentTime = QtWidgets.QLabel(Form)
        self.label_CurrentTime.setGeometry(QtCore.QRect(330, 590, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_CurrentTime.setFont(font)
        self.label_CurrentTime.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_CurrentTime.setAlignment(QtCore.Qt.AlignCenter)
        self.label_CurrentTime.setObjectName("label_CurrentTime")
        self.pushButton_Open = QtWidgets.QPushButton(Form)
        self.pushButton_Open.setGeometry(QtCore.QRect(350, 120, 93, 28))
        self.pushButton_Open.setObjectName("pushButton_Open")
        self.pushButton_Close = QtWidgets.QPushButton(Form)
        self.pushButton_Close.setGeometry(QtCore.QRect(350, 160, 93, 28))
        self.pushButton_Close.setObjectName("pushButton_Close")
        self.label_ComStatement = QtWidgets.QLabel(Form)
        self.label_ComStatement.setGeometry(QtCore.QRect(30, 590, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_ComStatement.setFont(font)
        self.label_ComStatement.setObjectName("label_ComStatement")
        self.checkBox_HexShow = QtWidgets.QCheckBox(Form)
        self.checkBox_HexShow.setGeometry(QtCore.QRect(30, 170, 121, 19))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBox_HexShow.setFont(font)
        self.checkBox_HexShow.setObjectName("checkBox_HexShow")
        self.label_CurrentTimeTitle = QtWidgets.QLabel(Form)
        self.label_CurrentTimeTitle.setGeometry(QtCore.QRect(231, 590, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_CurrentTimeTitle.setFont(font)
        self.label_CurrentTimeTitle.setObjectName("label_CurrentTimeTitle")
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 80, 291, 71))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.label_ComNo = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_ComNo.setFont(font)
        self.label_ComNo.setObjectName("label_ComNo")
        self.gridLayout_7.addWidget(self.label_ComNo, 0, 0, 1, 1)
        self.comboBox_ComNo = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox_ComNo.setObjectName("comboBox_ComNo")
        self.gridLayout_7.addWidget(self.comboBox_ComNo, 0, 1, 1, 1)
        self.label_Baud = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_Baud.setFont(font)
        self.label_Baud.setObjectName("label_Baud")
        self.gridLayout_7.addWidget(self.label_Baud, 1, 0, 1, 1)
        self.comboBox_Baud = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox_Baud.setObjectName("comboBox_Baud")
        self.comboBox_Baud.addItem("")
        self.comboBox_Baud.addItem("")
        self.comboBox_Baud.addItem("")
        self.comboBox_Baud.addItem("")
        self.comboBox_Baud.addItem("")
        self.comboBox_Baud.addItem("")
        self.gridLayout_7.addWidget(self.comboBox_Baud, 1, 1, 1, 1)
        self.pushButton_Refresh = QtWidgets.QPushButton(Form)
        self.pushButton_Refresh.setGeometry(QtCore.QRect(350, 80, 93, 28))
        self.pushButton_Refresh.setObjectName("pushButton_Refresh")
        self.layoutWidget1 = QtWidgets.QWidget(Form)
        self.layoutWidget1.setGeometry(QtCore.QRect(31, 201, 421, 81))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_MonitorName1 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_MonitorName1.setFont(font)
        self.label_MonitorName1.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_MonitorName1.setObjectName("label_MonitorName1")
        self.gridLayout.addWidget(self.label_MonitorName1, 0, 0, 1, 1)
        self.textEdit_MonitorChannel1 = QtWidgets.QTextEdit(self.layoutWidget1)
        self.textEdit_MonitorChannel1.setReadOnly(True)
        self.textEdit_MonitorChannel1.setObjectName("textEdit_MonitorChannel1")
        self.gridLayout.addWidget(self.textEdit_MonitorChannel1, 0, 1, 1, 1)
        self.label_UnitName1 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_UnitName1.setFont(font)
        self.label_UnitName1.setObjectName("label_UnitName1")
        self.gridLayout.addWidget(self.label_UnitName1, 0, 2, 1, 1)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(30, 290, 421, 31))
        self.widget.setObjectName("widget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_SetLight1 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_SetLight1.setFont(font)
        self.label_SetLight1.setObjectName("label_SetLight1")
        self.gridLayout_2.addWidget(self.label_SetLight1, 0, 0, 1, 1)
        self.textEdit_SetLight1 = QtWidgets.QTextEdit(self.widget)
        self.textEdit_SetLight1.setObjectName("textEdit_SetLight1")
        self.gridLayout_2.addWidget(self.textEdit_SetLight1, 0, 1, 1, 1)
        self.pushButton_Set1 = QtWidgets.QPushButton(self.widget)
        self.pushButton_Set1.setObjectName("pushButton_Set1")
        self.gridLayout_2.addWidget(self.pushButton_Set1, 0, 2, 1, 1)
        self.widget1 = QtWidgets.QWidget(Form)
        self.widget1.setGeometry(QtCore.QRect(31, 331, 421, 81))
        self.widget1.setObjectName("widget1")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.widget1)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_MonitorName2 = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_MonitorName2.setFont(font)
        self.label_MonitorName2.setObjectName("label_MonitorName2")
        self.gridLayout_3.addWidget(self.label_MonitorName2, 0, 0, 1, 1)
        self.textEdit_MonitorChannel2 = QtWidgets.QTextEdit(self.widget1)
        self.textEdit_MonitorChannel2.setReadOnly(True)
        self.textEdit_MonitorChannel2.setObjectName("textEdit_MonitorChannel2")
        self.gridLayout_3.addWidget(self.textEdit_MonitorChannel2, 0, 1, 1, 1)
        self.label_UnitName2 = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_UnitName2.setFont(font)
        self.label_UnitName2.setObjectName("label_UnitName2")
        self.gridLayout_3.addWidget(self.label_UnitName2, 0, 2, 1, 1)
        self.widget2 = QtWidgets.QWidget(Form)
        self.widget2.setGeometry(QtCore.QRect(30, 420, 421, 31))
        self.widget2.setObjectName("widget2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.widget2)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_SetLight2 = QtWidgets.QLabel(self.widget2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_SetLight2.setFont(font)
        self.label_SetLight2.setObjectName("label_SetLight2")
        self.gridLayout_4.addWidget(self.label_SetLight2, 0, 0, 1, 1)
        self.textEdit_SetLight2 = QtWidgets.QTextEdit(self.widget2)
        self.textEdit_SetLight2.setObjectName("textEdit_SetLight2")
        self.gridLayout_4.addWidget(self.textEdit_SetLight2, 0, 1, 1, 1)
        self.pushButton_Set2 = QtWidgets.QPushButton(self.widget2)
        self.pushButton_Set2.setObjectName("pushButton_Set2")
        self.gridLayout_4.addWidget(self.pushButton_Set2, 0, 2, 1, 1)
        self.widget3 = QtWidgets.QWidget(Form)
        self.widget3.setGeometry(QtCore.QRect(30, 460, 421, 81))
        self.widget3.setObjectName("widget3")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.widget3)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_MonitorName3 = QtWidgets.QLabel(self.widget3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_MonitorName3.setFont(font)
        self.label_MonitorName3.setObjectName("label_MonitorName3")
        self.gridLayout_5.addWidget(self.label_MonitorName3, 0, 0, 1, 1)
        self.textEdit_MonitorChannel3 = QtWidgets.QTextEdit(self.widget3)
        self.textEdit_MonitorChannel3.setReadOnly(True)
        self.textEdit_MonitorChannel3.setObjectName("textEdit_MonitorChannel3")
        self.gridLayout_5.addWidget(self.textEdit_MonitorChannel3, 0, 1, 1, 1)
        self.label_UnitName3 = QtWidgets.QLabel(self.widget3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_UnitName3.setFont(font)
        self.label_UnitName3.setObjectName("label_UnitName3")
        self.gridLayout_5.addWidget(self.label_UnitName3, 0, 2, 1, 1)
        self.widget4 = QtWidgets.QWidget(Form)
        self.widget4.setGeometry(QtCore.QRect(30, 550, 421, 31))
        self.widget4.setObjectName("widget4")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.widget4)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label_SetLight3 = QtWidgets.QLabel(self.widget4)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_SetLight3.setFont(font)
        self.label_SetLight3.setObjectName("label_SetLight3")
        self.gridLayout_6.addWidget(self.label_SetLight3, 0, 0, 1, 1)
        self.textEdit_SetLight3 = QtWidgets.QTextEdit(self.widget4)
        self.textEdit_SetLight3.setObjectName("textEdit_SetLight3")
        self.gridLayout_6.addWidget(self.textEdit_SetLight3, 0, 1, 1, 1)
        self.pushButton_Set3 = QtWidgets.QPushButton(self.widget4)
        self.pushButton_Set3.setObjectName("pushButton_Set3")
        self.gridLayout_6.addWidget(self.pushButton_Set3, 0, 2, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_Title.setText(_translate("Form", "智能照明控制系统"))
        self.label_CurrentTime.setText(_translate("Form", "Date & Time"))
        self.pushButton_Open.setText(_translate("Form", "开启"))
        self.pushButton_Close.setText(_translate("Form", "关闭"))
        self.label_ComStatement.setText(_translate("Form", "Statement"))
        self.checkBox_HexShow.setText(_translate("Form", "16进制显示"))
        self.label_CurrentTimeTitle.setText(_translate("Form", "当前时间："))
        self.label_ComNo.setText(_translate("Form", "串口号"))
        self.label_Baud.setText(_translate("Form", "波特率"))
        self.comboBox_Baud.setItemText(0, _translate("Form", "1200"))
        self.comboBox_Baud.setItemText(1, _translate("Form", "2400"))
        self.comboBox_Baud.setItemText(2, _translate("Form", "4800"))
        self.comboBox_Baud.setItemText(3, _translate("Form", "9600"))
        self.comboBox_Baud.setItemText(4, _translate("Form", "38400"))
        self.comboBox_Baud.setItemText(5, _translate("Form", "115200"))
        self.pushButton_Refresh.setText(_translate("Form", "刷新"))
        self.label_MonitorName1.setText(_translate("Form", "监测通路1"))
        self.label_UnitName1.setText(_translate("Form", "Lux"))
        self.label_SetLight1.setText(_translate("Form", "通路1照度"))
        self.pushButton_Set1.setText(_translate("Form", "设置"))
        self.label_MonitorName2.setText(_translate("Form", "监测通路2"))
        self.label_UnitName2.setText(_translate("Form", "Lux"))
        self.label_SetLight2.setText(_translate("Form", "通路2照度"))
        self.pushButton_Set2.setText(_translate("Form", "设置"))
        self.label_MonitorName3.setText(_translate("Form", "监测通路3"))
        self.label_UnitName3.setText(_translate("Form", "Lux"))
        self.label_SetLight3.setText(_translate("Form", "通路3照度"))
        self.pushButton_Set3.setText(_translate("Form", "设置"))
