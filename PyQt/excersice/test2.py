#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 14:43:29 2017

@author: wei
"""

import sys

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit, QVBoxLayout, QFormLayout





class MainWindow(QWidget):

    def __init__(self):

        super(self.__class__, self).__init__()

        self.setupUi()

        self.show()



    def setupUi(self):

        self.setWindowTitle("Hello World!")



        self.label = QLabel()

        self.label.setText("加油加油加油加油")



        self.button_hello = QPushButton()

        self.button_hello.setText("hello")



        self.button_world = QPushButton()

        self.button_world.setText("world")



        self.line_hello = QLineEdit()

        self.line_world = QLineEdit()



        form_layout = QFormLayout()

        form_layout.addRow(self.button_hello, self.line_hello)

        form_layout.addRow(self.button_world, self.line_world)



        h_layout = QVBoxLayout()

        h_layout.addWidget(self.label)

        h_layout.addLayout(form_layout)



        self.setLayout(h_layout)





if __name__ == "__main__":

    app = QApplication(sys.argv)

    MainWindow = MainWindow()

    sys.exit(app.exec_())