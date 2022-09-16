# -*- coding: utf-8 -*-
"""
Housing Charge Calculator

Created on Wed August 22 2022
@author: WR Woods

Version:  0.0.0
"""
from distutils.cmd import Command
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtWidgets 
from PyQt5.QtCore import *
from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QApplication

import sys

from os import path

from PyQt5.uic import loadUiType

FORM_CLASS,_=loadUiType(path.join(path.dirname('__file__'),"main.ui"))



class Main(QMainWindow, FORM_CLASS):
    def __init__(self,parent=None):
        super(Main,self).__init__(parent)
        QMainWindow.__init__(self)
        self.desktop = QApplication.desktop()
        self.screenRect = self.desktop.screenGeometry()
        self.height = self.screenRect.height()
        self.width = self.screenRect.width()
        print('height is '+str(self.height) + '  width is '+str(self.width))
        self.setGeometry(0, 0, self.width, self.height)
        self.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.setWindowTitle("Housing Charge Calculator")
        self.setWindowIcon(QIcon('Images/SCIcon.ico'))
        self.setupUi(self) 



def main():
    app=QApplication(sys.argv)
    window=Main()
    window.show()
    app.exec_()

if __name__=='__main__':
    main()