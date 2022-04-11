from tkinter import Label
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow
import sys
def clicked():
    print("clicked")
def demo():
    app= QApplication(sys.argv)
    win=QMainWindow()
    win.setGeometry(300,300,300,300)
    win.setWindowTitle("USER DEMO APP")
    label=QtWidgets.QLabel(win)
    label.setText("USER APP")
    label.move(100,100)
    
    b1=QtWidgets.QPushButton(win)
    b1.setText("Click me")
    b1.clicked.connect(clicked)
    win.show()
    sys.exit(app.exec_())
    
    
demo()