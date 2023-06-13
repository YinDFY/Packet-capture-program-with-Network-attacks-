from ui import Ui_MainWindow
from scapy.all import *
import cryptography
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import  QtWidgets,uic
from PyQt5.QtWidgets import QApplication, QTableWidget, QHeaderView, QTableWidgetItem
from PyQt5.QtGui import QPalette, QBrush, QPixmap,QColor,QIcon
import time
from PyQt5.QtWidgets import QApplication, QTabWidget, QWidget
from PyQt5.QtGui import QPixmap
class UI(Ui_MainWindow):
    def __init__(self):
        super(UI, self).__init__()
        uic.loadUi('ui.ui', self)
        self.setWindowTitle('Wire&Bite')
        self.comboBox.addItem('Realtek 8822CE Wireless LAN 802.11ac PCI-E NIC')
        self.comboBox.addItem('VMware Virtual Ethernet Adapter for VMnet8')
        self.comboBox.addItem('VMware Virtual Ethernet Adapter for VMnet1')
        self.choose_eth.addItem('Realtek 8822CE Wireless LAN 802.11ac PCI-E NIC')
        self.choose_eth.addItem('VMware Virtual Ethernet Adapter for VMnet8')
        self.choose_eth.addItem('VMware Virtual Ethernet Adapter for VMnet1')
        self.choose_eth_3.addItem('Realtek 8822CE Wireless LAN 802.11ac PCI-E NIC')
        self.choose_eth_3.addItem('VMware Virtual Ethernet Adapter for VMnet8')
        self.choose_eth_3.addItem('VMware Virtual Ethernet Adapter for VMnet1')
        self.choose_eth_2.addItem('VMware Virtual Ethernet Adapter for VMnet1')
        self.choose_eth_7.addItem('VMware Virtual Ethernet Adapter for VMnet1')
        self.choose_eth_7.addItem('Realtek 8822CE Wireless LAN 802.11ac PCI-E NIC')
        self.choose_eth_7.addItem('VMware Virtual Ethernet Adapter for VMnet8')
        self.choose_eth_2.addItem('Realtek 8822CE Wireless LAN 802.11ac PCI-E NIC')
        self.choose_eth_2.addItem('VMware Virtual Ethernet Adapter for VMnet8')
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(0, QHeaderView.Fixed)
        self.tableWidget.setColumnCount(5)
        self.tableWidget_2.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget_2.horizontalHeader().setSectionResizeMode(0, QHeaderView.Fixed)
        self.tableWidget_2.setColumnCount(3)
        self.tableWidget_4.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget_4.horizontalHeader().setSectionResizeMode(0, QHeaderView.Fixed)
        self.tableWidget_4.setColumnCount(4)
        self.pushButton_3.setFixedSize(140, 40)
        self.comboBox.setFixedSize(300,40)
        self.pushButton_4.setFixedSize(140, 40)
        self.pushButton_5.setFixedSize(140, 40)
        self.pushButton_8.setFixedSize(111, 31)
        #self.pushButton_9.setFixedSize(111, 31)
        self.pushButton_20.setFixedSize(111, 31)
        self.pushButton_19.setFixedSize(111, 31)
        self.pushButton.setFixedSize(140, 40)
        self.pushButton_2.setFixedSize(140, 40)
        self.pushButton_6.setFixedSize(41,41)
        self.pushButton_10.setFixedSize(131, 31)
        self.pushButton_7.setFixedSize(91, 31)
        self.pushButton_33.setFixedSize(91, 31)
        self.pushButton_32.setFixedSize(91, 31)
        #self.pushButton_9.setStyleSheet(
            #'''QPushButton{background:rgb(150,212,255);border-radius:5px;}QPushButton:hover{background:rgb(70, 212, 255);}''')
        self.pushButton_8.setStyleSheet(
            '''QPushButton{background:rgb(150,212,255);border-radius:5px;}QPushButton:hover{background:rgb(70, 212, 255);}''')
        self.pushButton_19.setStyleSheet(
            '''QPushButton{background:rgb(150,212,255);border-radius:5px;}QPushButton:hover{background:rgb(70, 212, 255);}''')
        self.pushButton_20.setStyleSheet(
            '''QPushButton{background:rgb(150,212,255);border-radius:5px;}QPushButton:hover{background:rgb(70, 212, 255);}''')
        self.pushButton_32.setStyleSheet(
            '''QPushButton{background:rgb(150,212,255);border-radius:5px;}QPushButton:hover{background:rgb(70, 212, 255);}''')
        self.pushButton_33.setStyleSheet(
            '''QPushButton{background:rgb(150,212,255);border-radius:5px;}QPushButton:hover{background:rgb(70, 212, 255);}''')
        self.pushButton_7.setStyleSheet(
            '''QPushButton{background:rgb(150,212,255);border-radius:5px;}QPushButton:hover{background:rgb(70, 212, 255);}''')
        self.pushButton_10.setStyleSheet(
            '''QPushButton{background:rgb(150,212,255);border-radius:5px;}QPushButton:hover{background:rgb(70, 212, 255);}''')
        self.pushButton_6.setStyleSheet(
            '''QPushButton{background:rgb(150,212,255);border-radius:5px;}QPushButton:hover{background:rgb(70, 212, 255);}''')
        self.pushButton_3.setStyleSheet(
            '''QPushButton{background:rgb(150,212,255);border-radius:5px;}QPushButton:hover{background:rgb(70, 212, 255);}''')
        self.pushButton_5.setStyleSheet(
            '''QPushButton{background:rgb(150,212,255);border-radius:5px;}QPushButton:hover{background:rgb(70, 212, 255);}''')
        self.pushButton_2.setStyleSheet(
            '''QPushButton{background:rgb(150,212,255);border-radius:5px;}QPushButton:hover{background:rgb(70, 212, 255);}''')
        self.pushButton_4.setStyleSheet(
            '''QPushButton{background:rgb(150,212,255);border-radius:5px;}QPushButton:hover{background:rgb(70, 212, 255);}''')
        self.pushButton.setStyleSheet(
            '''QPushButton{background:rgb(150,212,255);border-radius:5px;}QPushButton:hover{background: rgb(70, 212, 255);}''')
        self.tableWidget.setStyleSheet("QTableWidget::Item{background-color:#FF3EFF}")
        self.tableWidget.setStyleSheet("selection-background-color: rgb(70, 212, 255)")
        self.tableWidget.setStyleSheet('background-color:rgb(150,212,255)')
        header1 = self.tableWidget.verticalHeader()
        header1.setStyleSheet('background-color: rgb(20, 212, 255);')
        self.tableWidget_2.setStyleSheet("QTableWidget::Item{background-color:#FF3EFF}")
        self.tableWidget_2.setStyleSheet("selection-background-color: rgb(70, 212, 255)")
        self.tableWidget_2.setStyleSheet('background-color:rgb(150,212,255)')
        self.tableWidget_4.setStyleSheet("QTableWidget::Item{background-color:#FF3EFF}")
        self.tableWidget_4.setStyleSheet("selection-background-color: rgb(70, 212, 255)")
        self.tableWidget_4.setStyleSheet('background-color:rgb(150,212,255)')
        self.textEdit.setStyleSheet('background-color: rgb(150, 212, 255);')
        self.textEdit_2.setStyleSheet('background-color: rgb(150, 212, 255);')
        self.textEdit_6.setStyleSheet('background-color: rgb(150, 212, 255);')
        self.textEdit_8.setStyleSheet('background-color: rgb(150, 212, 255);')
        self.textEdit_13.setStyleSheet('background-color: rgb(150, 212, 255);')
        self.textEdit_48.setStyleSheet('background-color: rgb(150, 212, 255);')
        self.textEdit_49.setStyleSheet('background-color: rgb(150, 212, 255);')
        self.textEdit_9.setStyleSheet('background-color: rgb(150, 212, 255);')
        self.textEdit_10.setStyleSheet('background-color: rgb(150, 212, 255);')
        self.textEdit_11.setStyleSheet('background-color: rgb(150, 212, 255);')
        self.textEdit_3.setStyleSheet('background-color: rgb(150, 212, 255);')
        self.textEdit_7.setStyleSheet('background-color: rgb(150, 212, 255);')
        self.textEdit_4.setStyleSheet('background-color: rgb(150, 212, 255);')
        self.textEdit_47.setStyleSheet('background-color: rgb(150, 212, 255);')
        #self.textEdit_25.setStyleSheet('background-color: rgb(150, 212, 255);')
        #self.textEdit_27.setStyleSheet('background-color: rgb(150, 212, 255);')
        #self.textEdit_28.setStyleSheet('background-color: rgb(150, 212, 255);')
        self.textEdit_12.setStyleSheet('background-color: rgb(150, 212, 255);')
        self.textEdit_29.setStyleSheet('background-color: rgb(150, 212, 255);')
        self.textEdit_26.setStyleSheet('background-color: rgb(150, 212, 255);')
        self.tabWidget.setStyleSheet("QTabWidget::pane {border: 0; background-image: url(./background.jpg)}")
        self.p = True

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = UI()
    window.show()
    sys.exit(app.exec_())