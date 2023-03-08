"""
# File       : main.py
# Encoding   : utf-8
# Date       ：2023/3/7
# Author     ：LiFZ
# Email      ：lifzcn@gmail.com
# Version    ：python 3.9
# Description：
"""

import re
import sys
import binascii
import time
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import *
from PyQt5.QtSerialPort import QSerialPort, QSerialPortInfo
from PyQt5.QtWidgets import QApplication, QMainWindow
from interface import Ui_Form


class mainWindow(QMainWindow, Ui_Form):
    def __init__(self, parent=None):
        super(mainWindow, self).__init__(parent)
        self.setupUi(self)
        self.createItems()
        self.createSignalSlot()

    def createItems(self):
        self.com = QSerialPort()
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.showTime)
        self.timer.start(100)

    def createSignalSlot(self):
        self.pushButton_Open.clicked.connect(self.comOpen)
        self.pushButton_Close.clicked.connect(self.comClose)
        self.pushButton_Refresh.clicked.connect(self.comRefresh)
        self.com.readyRead.connect(self.receiveData)
        self.checkBox_HexShow.stateChanged.connect(self.hexShow)
        self.pushButton_Set1.clicked.connect(self.setChannelValue1)
        self.pushButton_Set2.clicked.connect(self.setChannelValue2)
        self.pushButton_Set3.clicked.connect(self.setChannelValue3)

    def setChannelValue1(self):
        txData1 = self.textEdit_SetLight1.toPlainText() + ".1"
        if len(txData1) == 0:
            return
        self.com.write(txData1.encode("utf-8"))
        self.textEdit_SetLight1.clear()

    def setChannelValue2(self):
        txData2 = self.textEdit_SetLight2.toPlainText() + ".2"
        if len(txData2) == 0:
            return
        self.com.write(txData2.encode("utf-8"))
        self.textEdit_SetLight2.clear()

    def setChannelValue3(self):
        txData3 = self.textEdit_SetLight3.toPlainText() + ".3"
        if len(txData3) == 0:
            return
        self.com.write(txData3.encode("utf-8"))
        self.textEdit_SetLight3.clear()

    def showTime(self):
        self.label_CurrentTime.setText(time.strftime("%B %d,%H:%M:%S", time.localtime()))

    def receiveData(self):
        try:
            rxData = bytes(self.com.readAll())
            rxDataList = rxData.decode("utf-8").split(',')
        except:
            QMessageBox.critical(self, "严重错误", "串口接收数据错误!")
        if self.checkBox_HexShow.isChecked() == False:
            try:
                self.textEdit_MonitorChannel1.insertPlainText(rxDataList[0] + '\n')
                self.textEdit_MonitorChannel2.insertPlainText(rxDataList[1] + '\n')
                self.textEdit_MonitorChannel3.insertPlainText(rxDataList[2])
            except:
                pass
        else:
            data = binascii.b2a_hex(rxData).decode("ascii")
            hexStr = " 0x".join(re.findall("(.{2})", data))
            hexStr = "0x" + hexStr
            self.textEdit_MonitorChannel1.insertPlainText(hexStr)

    def comRefresh(self):
        self.comboBox_ComNo.clear()
        com = QSerialPort()
        com_list = QSerialPortInfo.availablePorts()
        for info in com_list:
            com.setPort(info)
            if com.open(QSerialPort.ReadWrite):
                self.comboBox_ComNo.addItem(info.portName())
                com.close()

    def hexShow(self):
        if self.checkBox_HexShow.isChecked() == True:
            self.lineEdit_MonitorChannel1.setText('')

    def comOpen(self):
        comName = self.comboBox_ComNo.currentText()
        comBaud = int(self.comboBox_Baud.currentText())
        self.com.setPortName(comName)
        try:
            if self.com.open(QSerialPort.ReadWrite) == False:
                QMessageBox.critical(self, "严重错误", "串口打开失败!")
                return
        except:
            QMessageBox.critical(self, "严重错误", "串口打开失败!")
            return
        self.pushButton_Close.setEnabled(True)
        self.pushButton_Open.setEnabled(False)
        self.pushButton_Refresh.setEnabled(False)
        self.comboBox_ComNo.setEnabled(False)
        self.comboBox_Baud.setEnabled(False)
        self.label_ComStatement.setText("已打开!")
        self.com.setBaudRate(comBaud)

    def comClose(self):
        self.com.close()
        self.pushButton_Close.setEnabled(False)
        self.pushButton_Open.setEnabled(True)
        self.pushButton_Refresh.setEnabled(True)
        self.comboBox_ComNo.setEnabled(True)
        self.comboBox_Baud.setEnabled(True)
        self.label_ComStatement.setText("已关闭!")

    def close(self):
        sys.exit(app.exec_())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = mainWindow()
    myWin.show()
    sys.exit(app.exec_())
