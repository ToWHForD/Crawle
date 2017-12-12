# -*- coding: utf-8 -*-
"""
@author = wpf
@version = 1.0
@mail = wpf196970716@gmail.com
@desc : this program provide a lineEdit to get input and provide a button to execute a method what can download imgaines with your input.
"""
import sys



from PyQt5.QtWidgets import QApplication , QMainWindow
from GUI import *


#这是入口程序，执行此程序即可。
app = QApplication(sys.argv)
mainWindow = QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(mainWindow)
mainWindow.show()
sys.exit(app.exec_())

