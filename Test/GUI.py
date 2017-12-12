# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import Downloader


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        """
        自动构造的GUI程序主体
        """
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(368, 628)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(100, 460, 141, 51))
        self.pushButton.setObjectName("pushButton")

        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(50, 140, 256, 311))
        self.listView.setObjectName("listView")

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(130, 70, 221, 41))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setMaxLength(5)    #设置要加set

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 70, 101, 41))
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 20, 261, 20))
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(3, 560, 361, 20))
        self.label_3.setObjectName("label_3")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 368, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        MainWindow.setWindowIcon(QtGui.QIcon("D:\c#\SuperMusic\SuperMusic\images\superMusic.ico"))
        
        #绑定按钮事件
        self.pushButton.clicked.connect(self.GUI_pushButton_click)
        
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    
    #此方法的作用是对标签设置标题之类的操作。
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow","百度图片爬取"))
        self.pushButton.setText(_translate("MainWindow", "下载"))
        self.label.setText(_translate("MainWindow", "输入下载的图片名："))
        self.label_2.setText(_translate("MainWindow", "百度图片爬取，默认存储在D:\\temp\\crawle下。"))
        self.label_3.setText(_translate("MainWindow", "此软件仅供个人测试使用，如果不好用，你来打我啊~！"))
    

    #此方法和button被按下的操作连接
    #如果button按下，则执行下载操作
    #下载的关键字从lineEdit中获得
    #同时listview显示正在下载的网页和下载情况
    #下载需要判断是否存在于集合中，同时将全部下载信息存入数据库。
    def GUI_pushButton_click(self):
        word = self.lineEdit.text()
        QtWidgets.QMessageBox.information(self.pushButton,"标题","程序开始启动，嘟嘟嘟嘟~~")
        Downloader.do(word)
        print("下载完成")
        