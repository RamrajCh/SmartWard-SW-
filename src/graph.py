import sys
import matplotlib
import dbconnect
import datetime
from nepali_date import NepaliDate
matplotlib.use('Qt5Agg')

from PyQt5 import QtCore, QtWidgets

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure

db=dbconnect.database_statwindow('localhost','root')
rdb=dbconnect.database_receipt('localhost','root')

class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)


class Ui_StatWindow(object):
    def __init__(self,name,table_name):
        self.name=name
        self.table_name=table_name

    def setupUi(self,MainWindow):
        MainWindow.setWindowTitle("{} Statistics".format(self.name))
        MainWindow.setFixedSize(900,600)

        def define_dropdown(sc):
            self.dropdown=QtWidgets.QComboBox(sc)
            self.dropdown.setGeometry(QtCore.QRect(0,0,200,30))
            self.dropdown.addItem("--Choose the parameter--")
            self.dropdown.addItem('Month')        
            self.dropdown.addItem('Day')
            self.dropdown.addItem('Year')
            self.dropdown.setObjectName('dropdown')
            self.dropdown.currentTextChanged.connect(change_parameter)

        def plot_year():
            print("Year")
            year = MplCanvas(self, width=5, height=4, dpi=100)
            define_dropdown(year)
            x_axis=list(range(1,11))
            x__axis=[]
            x_labels=[]
            today = NepaliDate.today()
            this_year=int(today.year)
            for i in range(this_year-9,this_year+1):
                date=NepaliDate(i,1,1)
                x__axis.append(date.strfdate('%Y/%'))
                x_labels.append(date.strfdate('%Y'))
            y_axis=[]
            for x in x__axis:
                y_axis.append(db.getRowCount('RegDate',self.table_name,x))
            
            print(y_axis)
            year.axes.plot(x_axis,y_axis)
            year.axes.set_title("{0} by {1}".format(self.name,"Year"))
            year.axes.set_xlabel("Year")
            year.axes.set_ylabel("No. of {}".format(self.name))
            #year.axes.set_xscale()
            #year.axes.set_xticklabels(x_labels)
            MainWindow.setCentralWidget(year)

        def plot_month():
            print("Month")
            month = MplCanvas(self, width=5, height=4, dpi=100)
            define_dropdown(month)
            x_axis=list(range(1,13))
            x__axis=[]
            today=NepaliDate.today().year
            for i in range(1,13):
                date=NepaliDate(today,i,1)
                x__axis.append(date.strfdate('%Y/%m/%'))
            y_axis=[]
            for x in x__axis:
                y_axis.append(db.getRowCount('RegDate',self.table_name,x))
            
            print(y_axis)
            month.axes.plot(x_axis,y_axis)
            month.axes.set_title("{0} by {1}".format(self.name,"Month"))
            month.axes.set_xlabel("Month")
            month.axes.set_ylabel("No. of {}".format(self.name))
            MainWindow.setCentralWidget(month)

        def plot_day():
            print("Day")
            day = MplCanvas(self, width=5, height=4, dpi=100)
            define_dropdown(day)
            x_axis=[]
            x__axis=[]
            this_year=NepaliDate.today().year
            this_month=NepaliDate.today().month
            print(this_month)
            for x in range(1,33):
                try:
                    date=NepaliDate(this_year,this_month,x)
                    x_axis.append(x)
                    x__axis.append(date.strfdate('%Y/%m/%d'))
                except Exception:
                    print("No date of day: {}".format(x))
                    break
            y_axis=[]
            for x in x__axis:
                y_axis.append(db.getRowCount('RegDate',self.table_name,x))
            
            print(y_axis)
            day.axes.plot(x_axis,y_axis)
            day.axes.set_title("{0} by {1}".format(self.name,"Day"))
            day.axes.set_xlabel("Day")
            day.axes.set_ylabel("No. of {}".format(self.name))
            MainWindow.setCentralWidget(day)
        
        def change_parameter():
            parameter=self.dropdown.currentText()
            if parameter=="Year":
                plot_year()
            elif parameter=="Month":
                plot_month()
            elif parameter=="Day":
                plot_day()
        

        plot_month()

class Ui_ReceiptStat(object):
    def setupUi(self,MainWindow):
        MainWindow.setWindowTitle("Receipt Stat")
        MainWindow.setFixedSize(900,600)

        def define_dropdown(sc):
            self.dropdown=QtWidgets.QComboBox(sc)
            self.dropdown.setGeometry(QtCore.QRect(0,0,200,30))
            self.dropdown.addItem("--Choose the parameter--")
            self.dropdown.addItem('Total Income')
            self.dropdown.addItem('Total Number')
            self.dropdown.setObjectName('dropdown')
            self.dropdown.currentTextChanged.connect(change_parameter)
   
        def plot_totalincome():
            income = MplCanvas(self, width=5, height=4, dpi=100)
            define_dropdown(income)
            x_axis=list(range(1,13))
            x__axis=[]
            today=NepaliDate.today().year
            for i in range(1,13):
                date=NepaliDate(today,i,1)
                x__axis.append(date.strfdate('%Y/%m/%'))
            y_axis=[]
            for x in x__axis:
                y_axis.append(rdb.getAmount(x))
            
            print(y_axis)
            income.axes.plot(x_axis,y_axis)
            income.axes.set_title("Income by month")
            income.axes.set_xlabel("Month")
            income.axes.set_ylabel("Total monthly income")
            MainWindow.setCentralWidget(income)

        def plot_totalnumber():
            number = MplCanvas(self, width=5, height=4, dpi=100)
            define_dropdown(number)
            x_axis=list(range(1,13))
            x__axis=[]
            today=NepaliDate.today().year
            for i in range(1,13):
                date=NepaliDate(today,i,1)
                x__axis.append(date.strfdate('%Y/%m/%'))
            y_axis=[]
            for x in x__axis:
                y_axis.append(rdb.getRowCount(x))
            
            print(y_axis)
            number.axes.plot(x_axis,y_axis)
            number.axes.set_title("No. by month")
            number.axes.set_xlabel("Month")
            number.axes.set_ylabel("No. of receipts")
            MainWindow.setCentralWidget(number)

        def change_parameter():
            parameter=self.dropdown.currentText()
            if parameter=="Total Income":
                plot_totalincome()
            elif parameter=="Total Number":
                plot_totalnumber()
            else:
                pass

        plot_totalincome()

#if __name__=="__main__":
    
    #app = QtWidgets.QApplication(sys.argv)
    #StatWindow=QtWidgets.QMainWindow()
    #window = Ui_StatWindow("Birth","birthregistration")
    #window.setupUi(StatWindow)
    #StatWindow.show()
    #app.exec_()
    
    #app = QtWidgets.QApplication(sys.argv)
    #ReceiptStatWindow=QtWidgets.QMainWindow()
    #window = Ui_ReceiptStat()
    #window.setupUi(ReceiptStatWindow)
    #ReceiptStatWindow.show()
    #app.exec_()