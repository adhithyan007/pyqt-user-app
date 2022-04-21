import  sys
import io
from turtle import title
import folium
from tkinter import Widget
from PyQt5.QtWidgets import  QApplication,QWidget,QHBoxLayout,QVBoxLayout
from  PyQt5.QtWebEngineWidgets import  QWebEngineView 

class Myapp(QWidget):
    def  __init__(self):
        super().__init__()
        self.setWindowTitle('drone mapping')
        self.setWindow_width,self.window_height = 800,600
        self.setMinimumSize(self.setWindow_width,self.window_height)
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        coordinate =(8.536369, 76.905571)
        m=folium.Map(
            title='trivandrum',
            zoom_start = 13,
            location =coordinate
        )
        
        
        data = io.BytesIO()
        m.save(data,close_file = False)
        
        webView = QWebEngineView()
        webView.setHtml(data.getvalue().decode())
        layout.addWidget(webView)
if __name__== '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet('''
        Qwidget{
            font-size: 35px;
            
        }
         ''' )        
    myapp=Myapp()
    myapp.show()
    try:
        sys.exit(app.exec_())
    except SystemExit:
        print('Closing Window...')