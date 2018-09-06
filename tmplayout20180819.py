# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tmplayout.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

import time
import sys
import subprocess
import threading
import time
from threading import Thread
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, QThread, pyqtSignal, pyqtSlot
from PyQt5.QtWidgets import QWidget, QApplication, QMessageBox
from turtlecoin import TurtleCoind
from datetime import datetime


'''
To do:
- conditional search, if it is not a hash, search nothing, if it is a hash, check whether it is transaction or block hash

'''

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1180, 870)
        #set unresizeable window frame
        MainWindow.setMaximumSize(1180, 870)   
        MainWindow.setMinimumSize(1180, 870)
        
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        MainWindow.setPalette(palette)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("material\\img\\turtlecoin_icon_color.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("")
        MainWindow.setIconSize(QtCore.QSize(36, 36))
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 621, 811))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.layoutWidget)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tableWidget_Blk = QtWidgets.QTableWidget(self.tab)
        self.tableWidget_Blk.setGeometry(QtCore.QRect(0, 0, 620, 771))
        self.tableWidget_Blk.setObjectName("tableWidget_Blk")
        self.tableWidget_Blk.setColumnCount(6)
        self.tableWidget_Blk.setRowCount(0)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tableWidget_2_tx = QtWidgets.QTableWidget(self.tab_2)
        self.tableWidget_2_tx.setGeometry(QtCore.QRect(0, 0, 620, 771))
        self.tableWidget_2_tx.setObjectName("tableWidget_2_tx")
        self.tableWidget_2_tx.setColumnCount(4)
        self.tableWidget_2_tx.setRowCount(0)
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.label_blockchain_stat = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_blockchain_stat.sizePolicy().hasHeightForWidth())
        self.label_blockchain_stat.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_blockchain_stat.setFont(font)
        self.label_blockchain_stat.setAlignment(QtCore.Qt.AlignCenter)
        self.label_blockchain_stat.setObjectName("label_blockchain_stat")
        self.verticalLayout.addWidget(self.label_blockchain_stat)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(642, 12, 521, 811))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.textEdit_blk = QtWidgets.QTextEdit(self.layoutWidget1)
        self.textEdit_blk.setReadOnly(True)
        self.textEdit_blk.setObjectName("textEdit_blk")
        self.verticalLayout_2.addWidget(self.textEdit_blk)
        self.lineEdit_Blk = QtWidgets.QLineEdit(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_Blk.sizePolicy().hasHeightForWidth())
        self.lineEdit_Blk.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        self.lineEdit_Blk.setPalette(palette)
        self.lineEdit_Blk.setText("")
        self.lineEdit_Blk.setClearButtonEnabled(True)
        self.lineEdit_Blk.setObjectName("lineEdit_Blk")
        self.verticalLayout_2.addWidget(self.lineEdit_Blk)
        self.btn_search_blk = QtWidgets.QPushButton(self.layoutWidget1)
        self.btn_search_blk.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_search_blk.sizePolicy().hasHeightForWidth())
        self.btn_search_blk.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        self.btn_search_blk.setPalette(palette)
        self.btn_search_blk.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn_search_blk.setAutoFillBackground(False)
        self.btn_search_blk.setObjectName("btn_search_blk")
        self.verticalLayout_2.addWidget(self.btn_search_blk)
        self.textEdit_4_tx = QtWidgets.QTextEdit(self.layoutWidget1)
        self.textEdit_4_tx.setReadOnly(True)
        self.textEdit_4_tx.setObjectName("textEdit_4_tx")
        self.verticalLayout_2.addWidget(self.textEdit_4_tx)
        self.lineEdit_tx = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEdit_tx.setObjectName("lineEdit_tx")
        self.verticalLayout_2.addWidget(self.lineEdit_tx)
        self.btn_search_tx = QtWidgets.QPushButton(self.layoutWidget1)
        self.btn_search_tx.setObjectName("btn_search_tx")
        self.verticalLayout_2.addWidget(self.btn_search_tx)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1179, 21))
        self.menubar.setNativeMenuBar(False)
        self.menubar.setObjectName("menubar")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionContributor_Sabo_Revolutionary = QtWidgets.QAction(MainWindow)
        self.actionContributor_Sabo_Revolutionary.setObjectName("actionContributor_Sabo_Revolutionary")
        self.actionAbout_Qt = QtWidgets.QAction(MainWindow)
        self.actionAbout_Qt.setObjectName("actionAbout_Qt")
        self.menuHelp.addAction(self.actionContributor_Sabo_Revolutionary)
        self.menuHelp.addAction(self.actionAbout_Qt)
        self.menubar.addAction(self.menuHelp.menuAction())

#-----------------------------------------------------------------------------
# This are the objects for updating blockchain info and searching
        self.daemon_thread = Daemon_Connect()
        self.block_finder = Block_Finder()
        self.tx_finder = Tx_Finder()
#This variable is used to check whether if it is first time synched after opening the program or not
        self.firstTimeOpen = True
#-----------------------------------------------------------------------------   

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #update the blockchain stat when receiving the signal from Daemon_connect
        self.daemon_thread.signal.connect(self.set_daemon_stat)
        #update the search result when receiving the signal from Block_Finder
        self.block_finder.Resultsignal.connect(self.update_search_result)
        self.tx_finder.Resultsignal.connect(self.update_search_result)

 
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "TRTL Local Block-Explorer v.Beta"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Recent Blocks"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Transaction Pool"))
        self.label_blockchain_stat.setText(_translate("MainWindow", "TRTL Chain Status -"))
        self.btn_search_blk.setText(_translate("MainWindow", "Go to Block"))
        self.btn_search_blk.setEnabled(False)
        self.btn_search_tx.setText(_translate("MainWindow", "Find Transaction"))
        self.btn_search_tx.setEnabled(False)
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionContributor_Sabo_Revolutionary.setText(_translate("MainWindow", "About TRTL Local Block-Explorer"))
        self.actionAbout_Qt.setText(_translate("MainWindow", "About Qt"))

        horblkheader = ["Height","Size","Block Hash","Difficulty","Txs Count","Date & Time"]
        horTxpoolheader = ["Amount","Fee","Size","Hash"]
        #Set blk table header
        self.tableWidget_Blk.setHorizontalHeaderLabels(horblkheader)
        #Set Txpool table header
        self.tableWidget_2_tx.setHorizontalHeaderLabels(horTxpoolheader)

        #Starts the daemon thread on GUI start
        self.daemon_thread.start()
        
        #When button clicked, starts the thread of Block_finder object and passes the hash from lineEdit()
        self.btn_search_blk.clicked.connect(self.block_search)
        self.btn_search_tx.clicked.connect(self.tx_search)
        
    def block_search(self):
        self.block_finder.blk_searchHash= self.lineEdit_Blk.text()
        self.btn_search_blk.setEnabled(False)
        self.btn_search_tx.setEnabled(False)
        self.textEdit_blk.setText("Searching might take a while depending on your connection...")
        self.block_finder.start()
        
    def tx_search(self):
        self.tx_finder.tx_searchHash= self.lineEdit_tx.text()
        self.btn_search_blk.setEnabled(False)
        self.btn_search_tx.setEnabled(False)
        self.textEdit_4_tx.setText("Searching might take a while depending on your connection...")
        self.tx_finder.start()
        
        
    def update_search_result(self, Resultsignal):

        if Resultsignal['method'] == "block":
            if Resultsignal['error'] == "yes":
                self.textEdit_blk.setText(Resultsignal['response'])
                self.btn_search_blk.setEnabled(True)
                self.btn_search_tx.setEnabled(True)
            else:
                self.textEdit_blk.setText(self.formatting_Text(Resultsignal))
                self.btn_search_blk.setEnabled(True)
                self.btn_search_tx.setEnabled(True)
        elif Resultsignal['method'] == "tx":
            if Resultsignal['error'] == "yes":
                self.textEdit_4_tx.setText(Resultsignal['response'])
                self.btn_search_blk.setEnabled(True)
                self.btn_search_tx.setEnabled(True)
            else:
                self.textEdit_4_tx.setText(self.formatting_Text(Resultsignal))
                self.btn_search_blk.setEnabled(True)
                self.btn_search_tx.setEnabled(True)
            #0659022
            #新北市中和區華新街143巷106弄19號2F
    def formatting_Text(self, Resultsignal):
        if Resultsignal['method'] == "block":
            resultString = "Height: {}\nTimestamp: {}\nVersion: {}\nDifficulty: {}\nOrphan: {}\nTransaction: {}\nTotal coins in the network: {} trtl\nTotal transactions in the network: {}\n\nTotal transaction size, bytes: {}\nTotal block size, bytes: {}\nCurrent txs median, bytes: {}\nEffective txs median, bytes: {}\nReward penalty: {}%\nTransaction fee: {} trtl\nReward: {}\n\n"
            resultString = resultString.format(Resultsignal['response']['result']['block']['height'],
                                               datetime.fromtimestamp(Resultsignal['response']['result']['block']['timestamp']).strftime('%Y-%m-%d %H:%M:%S'),
                                               str(Resultsignal['response']['result']['block']['major_version'])+"."+str(Resultsignal['response']['result']['block']['minor_version']),
                                               Resultsignal['response']['result']['block']['difficulty'],
                                               Resultsignal['response']['result']['block']['orphan_status'],
                                               len(Resultsignal['response']['result']['block']['transactions']),
                                               str(int(Resultsignal['response']['result']['block']['alreadyGeneratedCoins'])/100),
                                               Resultsignal['response']['result']['block']['alreadyGeneratedTransactions'],
                                               Resultsignal['response']['result']['block']['transactionsCumulativeSize'],
                                               Resultsignal['response']['result']['block']['blockSize'],
                                               Resultsignal['response']['result']['block']['sizeMedian'],
                                               Resultsignal['response']['result']['block']['effectiveSizeMedian'],
                                               Resultsignal['response']['result']['block']['penalty'],
                                               Resultsignal['response']['result']['block']['totalFeeAmount']/100,
                                               Resultsignal['response']['result']['block']['reward']/100)

            resultString = resultString + "************************************************\n\nTransactions:\n"
            i = 0
            for tx in Resultsignal['response']['result']['block']['transactions']:
                i+=1
                tmpstring = "Transaction "+str(i)+"\nHash: {}\nFee: {}\nAmount Out: {}\nSize: {}\n---------------------------------------\n"
                tmpstring = tmpstring.format(tx['hash'],tx['fee']/100,tx['amount_out']/100,tx['size'])
                resultString = resultString + tmpstring

            return resultString

        elif Resultsignal['method'] == "tx":
            
            sumOut = 0

            for outp in Resultsignal['response']['result']['tx']['vout']:
                sumOut += outp['amount']

            sumOut = sumOut/100

            resultString = "Confirmations: {}\nFirst confirmation time: {}\nFee: {} trtl\nSum of outputs: {} trtl\nSize: {}\nMixin count: {}\n\n"
            resultString = resultString.format(Resultsignal['current_blk_height'] - Resultsignal['response']['result']['block']['height'],
                                               datetime.fromtimestamp(Resultsignal['response']['result']['block']['timestamp']).strftime('%Y-%m-%d %H:%M:%S'),
                                               Resultsignal['response']['result']['txDetails']['fee']/100,
                                               sumOut,
                                               Resultsignal['response']['result']['txDetails']['size'],
                                               Resultsignal['response']['result']['txDetails']['mixin'])
            resultString = resultString + "************************************************\n\nIn Block:\nHash: {}\nHeight: {}\n\n"
            resultString = resultString.format(Resultsignal['response']['result']['block']['hash'],
                                               Resultsignal['response']['result']['block']['height'],)
            resultString = resultString + "************************************************\n\nINPUTs:\nInputs("+str(len(Resultsignal['response']['result']['tx']['vin']))+")\n\n"

            #Add inputs to string
            i = 0
            for tx in Resultsignal['response']['result']['tx']['vin']:
                i+=1
                tmpstring = "Input "+str(i)+"\nAmount: {} trtl\nImage: {}\n\n"
                tmpstring = tmpstring.format(tx['value']['amount']/100,
                                             tx['value']['k_image'])
                resultString = resultString + tmpstring
                
            resultString = resultString + "************************************************\n\nOUTPUTs:\nOutputs("+str(len(Resultsignal['response']['result']['tx']['vout']))+")\n\n"

            #Add outputs to string
            i = 0
            for tx in Resultsignal['response']['result']['tx']['vout']:
                i+=1
                tmpstring = "Output "+str(i)+"\nAmount: {} trtl\nKey: {}\n\n"
                tmpstring = tmpstring.format(tx['amount']/100,
                                             tx['target']['data']['key'])
                resultString = resultString + tmpstring
            
            return resultString

    def set_daemon_stat(self, signal):

        if signal['signal'] =="Connecting":
            self.label_blockchain_stat.setText("TRTL Chain Status -\n...Initializing daemon\n"+
                                               "It might take longer depending on your connection.")
            self.textEdit_blk.setText("Search will be available when the daemon is synched!")
            self.textEdit_4_tx.setText("Search will be available when the daemon is synched!")
        elif signal['signal'] =="Connected":
            self.label_blockchain_stat.setText("TRTL Chain Status -\n...daemon initialized waiting to synch")
            self.textEdit_blk.setText("Search will be available when the daemon is synched!")
            
        elif signal['signal'] =="synching":
            
            self.label_blockchain_stat.setText("TRTL Chain Status - Local Block Height:"+ str(signal['current_daemon_height'])+
                                               " / "+"Network Block Height:"+str(signal['network_height'])+"\n...Synching")
        elif signal['signal'] =="synched":
           
            self.label_blockchain_stat.setText("TRTL Chain Status - Local Block Height:"+ str(signal['current_daemon_height'])+
                                               " / "+"Network Block Height:"+str(signal['network_height']))

            self.tableWidget_Blk.setRowCount(len(signal['recentBlocks']))
            self.tableWidget_2_tx.setRowCount(len(signal['transactionPool']))

            for i in range(len(signal['recentBlocks'])):
                #add block info to table
                blockheight = QtWidgets.QTableWidgetItem(str(signal['recentBlocks'][i]['height']))
                size = QtWidgets.QTableWidgetItem(str(signal['recentBlocks'][i]['cumul_size']))
                blockHash = QtWidgets.QTableWidgetItem(str(signal['recentBlocks'][i]['hash']))
                difficulty = QtWidgets.QTableWidgetItem(str(signal['recentBlocks'][i]['difficulty']))
                txs = QtWidgets.QTableWidgetItem(str(signal['recentBlocks'][i]['tx_count']))
                dateTime = QtWidgets.QTableWidgetItem(datetime.fromtimestamp(signal['recentBlocks'][i]['timestamp']).strftime('%Y-%m-%d %H:%M:%S'))
                self.tableWidget_Blk.setItem(i , 0, blockheight)
                self.tableWidget_Blk.setItem(i , 1, size)
                self.tableWidget_Blk.setItem(i , 2, blockHash)
                self.tableWidget_Blk.setItem(i , 3, difficulty)
                self.tableWidget_Blk.setItem(i , 4, txs)
                self.tableWidget_Blk.setItem(i , 5, dateTime)
                self.tableWidget_Blk.resizeColumnsToContents()
                self.tableWidget_Blk.resizeRowsToContents()
                self.tableWidget_Blk.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers) #dsiable editing in table

            for i in range(len(signal['transactionPool'])):
                #add transaction info to table
                amount = QtWidgets.QTableWidgetItem(str(signal['transactionPool'][i]['amount_out']))
                fee = QtWidgets.QTableWidgetItem(str(signal['transactionPool'][i]['fee']/100))
                size = QtWidgets.QTableWidgetItem(str(signal['transactionPool'][i]['size']))
                txHash = QtWidgets.QTableWidgetItem(str(signal['transactionPool'][i]['hash']))
                self.tableWidget_2_tx.setItem(i , 0, amount)
                self.tableWidget_2_tx.setItem(i , 1, fee)
                self.tableWidget_2_tx.setItem(i , 2, size)
                self.tableWidget_2_tx.setItem(i , 3, txHash)
                self.tableWidget_2_tx.resizeColumnsToContents()
                self.tableWidget_2_tx.resizeRowsToContents()
                self.tableWidget_2_tx.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers) #dsiable editing in table

            self.btn_search_blk.setEnabled(True)
            self.btn_search_tx.setEnabled(True)
            #Check whether this is the first sych after opening the program
            if self.firstTimeOpen == True:
                self.textEdit_blk.setText("Daemon is synched! Start searching now!!!")
                self.textEdit_4_tx.setText("Daemon is synched! Start searching now!!!")
                self.firstTimeOpen = False
            else:
                pass

class Daemon_Connect(QThread):
    signal= pyqtSignal(object)

    def __init__(self, parent = None):
        super(Daemon_Connect, self).__init__(parent)

        #-------------explorer parameters----------------------------------------------------
        local_host = 'localhost'
        local_port = 11898
        self.turtlecoind = TurtleCoind(local_host, local_port)
        trtlDaemon = "turtleDaemon\\TurtleCoind.exe --enable_blockexplorer --rpc-bind-ip=0.0.0.0 --rpc-bind-port=11898"  #remove --rpc-bind-ip=0.0.0.0 if you don't want to be connected
       #-------------------------------------------------------------------------------------
        #start Daemon throught subprocess
        subprocess.Popen(trtlDaemon)
        
    def run(self):  #initializing the connection with daemon and update the status between local and remote chain

        current_daemon_height = None
        network_height = None
        recentBlocks = None
        transactionPool = None
        
        mySignal = {}
        
        while current_daemon_height  == None or network_height== None :  #this while loop makes sure that local daemon is connected first
            try:
                current_daemon_height = self.turtlecoind.get_height()['height']
                network_height = self.turtlecoind.get_height()['network_height']
            except Exception as e:
                mySignal['signal'] = "Connecting"
                self.signal.emit(mySignal)
                #print(e)
                pass
            
        mySignal['signal'] = "Connected"
        self.signal.emit(mySignal)
        
        
        while True:  #updating synching status
            
            try:
                network_height = self.turtlecoind.get_height()['network_height']
                current_daemon_height = self.turtlecoind.get_height()['height']
                recentBlocks = self.turtlecoind.get_blocks(current_daemon_height)
                transactionPool = self.turtlecoind.get_transaction_pool()
                
                if current_daemon_height == network_height or current_daemon_height >= network_height:
                    
                    mySignal['signal'] = "synched"
                    mySignal['network_height'] = network_height
                    mySignal['current_daemon_height'] = current_daemon_height 
                    mySignal['recentBlocks'] = recentBlocks['result']['blocks'] #a list of recent blocks
                    mySignal['transactionPool'] = transactionPool['result']['transactions'] #a list of transaction
                    
                    self.signal.emit(mySignal)
              
                else:
                    
                    mySignal['signal'] = "synching"
                    mySignal['network_height'] = network_height
                    mySignal['current_daemon_height'] = current_daemon_height 
                    
                    self.signal.emit(mySignal)

            except Exception as e:
                #print(e)
                pass
            

class Block_Finder(QThread):
    Resultsignal = pyqtSignal(object)

    def __init__(self, parent = None):
        super(Block_Finder, self).__init__(parent)
        #-------------daemon parameters----------------------------------------------------
        local_host = 'localhost'
        local_port = 11898
        self.turtlecoind = TurtleCoind(local_host, local_port)
        #-------------------------------------------------------------------------------------
        self.blk_searchHash = ""

   
    def run(self):
        result = {}
        result['method'] = "block"
        try:
            result['response'] = self.turtlecoind.get_block(self.blk_searchHash)
            result['error'] = "no"
        except:
            result['error'] = "yes"
            result['response'] = "Block not found!"
        self.Resultsignal.emit(result)


class Tx_Finder(QThread):
    Resultsignal = pyqtSignal(object)

    def __init__(self, parent = None):
        super(Tx_Finder, self).__init__(parent)
        #-------------daemon parameters----------------------------------------------------
        local_host = 'localhost'
        local_port = 11898
        self.turtlecoind = TurtleCoind(local_host, local_port)
        #-------------------------------------------------------------------------------------
        self.tx_searchHash = ""
   
    def run(self):
        result = {}
        result['method'] = "tx"
        try:
            result['response'] = self.turtlecoind.get_transaction(self.tx_searchHash)
            result['current_blk_height'] = self.turtlecoind.get_height()['height']
            result['error'] = "no"
        except:
            result['error'] = "yes"
            result['response'] = "Transaction not found; either the tx hash is incorrect or it is not added to the blockchain yet."
        self.Resultsignal.emit(result)

#override the closeEvent action here        
class MyWindow(QtWidgets.QMainWindow):
    def closeEvent(self,event):
        result = QtWidgets.QMessageBox.question(self,
                      "Confirm Exit...",
                      "Are you sure you want to exit ?",
                      QtWidgets.QMessageBox.Yes| QtWidgets.QMessageBox.No)
        event.ignore()

        if result == QtWidgets.QMessageBox.Yes:
            event.accept()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = MyWindow()
    #MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

