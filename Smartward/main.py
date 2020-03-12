#This file is done
from PyQt5.QtWidgets import QApplication,QMainWindow
import pickle

from mainwindow import Ui_WardWindow
from registerwindow import Ui_RegisterWindow

if __name__=="__main__":
    import sys
    app = QApplication(sys.argv)
    
    try:
        with open('ward.pickle','rb') as obj:
            read = pickle.load(obj)
            WardWindow = QMainWindow()
            ui_ward = Ui_WardWindow()
            ui_ward.setupUi(WardWindow)
            WardWindow.show()
            print ("Open MainWindow. Ward registered.")
    except FileNotFoundError:
        RegisterWindow = QMainWindow()
        ui_register = Ui_RegisterWindow()
        ui_register.setupUi(RegisterWindow)
        RegisterWindow.show()
        print ("Open RegisterWindow. Ward not registered.")

    sys.exit(app.exec_())
