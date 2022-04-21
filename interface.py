from email.mime import image
import sys
from tkinter import Grid
from PyQt5.QtWidgets import QApplication,QLabel,QPushButton,QVBoxLayout,QWidget,QFileDialog,QGridLayout
from PyQt5.QtGui import QPixmap
from PyQt5 import  QtGui,QtCore
from PyQt5.QtGui import QCursor


app=QApplication(sys.argv)
window=QWidget()
window.setWindowTitle("fly high to the sea")
window.setFixedWidth(800)
window.move(1080,200)
window.setStyleSheet("background : #161219;")


grid = QGridLayout()
 
image =QPixmap("logo.png")
logo = QLabel()
logo.setPixmap(image)
logo.setAlignment(QtCore.Qt.AlignRight)

logo.setStyleSheet("margin-top:100px;")
grid.addWidget(logo,0,0)

window.setLayout(grid)
window.show()
sys.exit(app.exec_())