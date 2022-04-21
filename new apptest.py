from sys import prefix
import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg
from numpy import maximum, minimum
from pandas import value_counts

class Mainwindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Drones")
        self.setLayout(qtw.QVBoxLayout())
        my_label=qtw.QLabel("Welcome to Drones: Select the drone you wanted")
        my_label.setFont(qtg.QFont('Helvetica',24))
        self.layout().addWidget(my_label)
        

    
       
        
        my_spin = qtw.QSpinBox(self,
                    value =10,
                    maximum=100,
                    minimum=0,
                    singleStep = 1,
                    prefix="Total #",
                    suffix = " No of Orders")
        my_spin.setFont(qtg.QFont('Helvetica',20))
        self.layout().addWidget(my_spin)
              
        
       
        my_button=qtw.QPushButton("click after entered",
             clicked = lambda : press_it())
        self.layout().addWidget(my_button)
        
        self.show() 
        
        def press_it ():
            my_label.setText(f'You selected : {my_spin.currenttext ()}')
            
        
app=qtw.QApplication([])
mw=Mainwindow()


app.exec_()        