# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dayscalculator.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DaysCalculator(object):
    def setupUi(self, DaysCalculator):
        DaysCalculator.setObjectName("DaysCalculator")
        DaysCalculator.resize(578, 454)
        DaysCalculator.setMinimumSize(QtCore.QSize(578, 454))
        DaysCalculator.setMaximumSize(QtCore.QSize(578, 454))
        DaysCalculator.setStyleSheet("QDialog{\n"
"background-color: rgb(136, 138, 133);}\n"
"\n"
"QPushButton\n"
"{\n"
"     background-color: yellow;\n"
"    border: 1px solid white;\n"
"     border-radius: 4px;\n"
"    text-align: middle;\n"
"}\n"
"\n"
"QDateEdit\n"
"{\n"
"    height:35px;\n"
"     border-width: 1px;\n"
"      border-style: solid;\n"
"      border-radius: 4px;\n"
"}")
        self.label_daysCalculator = QtWidgets.QLabel(DaysCalculator)
        self.label_daysCalculator.setGeometry(QtCore.QRect(130, 20, 241, 41))
        self.label_daysCalculator.setObjectName("label_daysCalculator")
        self.pushButton_calculate = QtWidgets.QPushButton(DaysCalculator)
        self.pushButton_calculate.setGeometry(QtCore.QRect(40, 340, 89, 25))
        self.pushButton_calculate.setObjectName("pushButton_calculate")
        self.label_totalDays = QtWidgets.QLabel(DaysCalculator)
        self.label_totalDays.setGeometry(QtCore.QRect(170, 340, 361, 41))
        self.label_totalDays.setObjectName("label_totalDays")
        self.pushButton_quit = QtWidgets.QPushButton(DaysCalculator)
        self.pushButton_quit.setGeometry(QtCore.QRect(40, 400, 89, 25))
        self.pushButton_quit.setObjectName("pushButton_quit")
        self.widget = QtWidgets.QWidget(DaysCalculator)
        self.widget.setGeometry(QtCore.QRect(20, 90, 141, 211))
        self.widget.setObjectName("widget")
        self.verticalLayout_text = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_text.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_text.setObjectName("verticalLayout_text")
        self.label_initialDate = QtWidgets.QLabel(self.widget)
        self.label_initialDate.setObjectName("label_initialDate")
        self.verticalLayout_text.addWidget(self.label_initialDate)
        self.label_finalDate = QtWidgets.QLabel(self.widget)
        self.label_finalDate.setObjectName("label_finalDate")
        self.verticalLayout_text.addWidget(self.label_finalDate)
        self.widget1 = QtWidgets.QWidget(DaysCalculator)
        self.widget1.setGeometry(QtCore.QRect(163, 91, 391, 211))
        self.widget1.setObjectName("widget1")
        self.verticalLayout_date = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout_date.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_date.setObjectName("verticalLayout_date")
        self.horizontalLayout_initialDate = QtWidgets.QHBoxLayout()
        self.horizontalLayout_initialDate.setObjectName("horizontalLayout_initialDate")
        self.dateEdit_initialDate = QtWidgets.QDateEdit(self.widget1)
        self.dateEdit_initialDate.setObjectName("dateEdit_initialDate")
        self.horizontalLayout_initialDate.addWidget(self.dateEdit_initialDate)
        self.verticalLayout_date.addLayout(self.horizontalLayout_initialDate)
        self.horizontalLayout_finalDate = QtWidgets.QHBoxLayout()
        self.horizontalLayout_finalDate.setObjectName("horizontalLayout_finalDate")
        self.dateEdit_finalDate = QtWidgets.QDateEdit(self.widget1)
        self.dateEdit_finalDate.setObjectName("dateEdit_finalDate")
        self.horizontalLayout_finalDate.addWidget(self.dateEdit_finalDate)
        self.verticalLayout_date.addLayout(self.horizontalLayout_finalDate)

        self.retranslateUi(DaysCalculator)
        QtCore.QMetaObject.connectSlotsByName(DaysCalculator)

    def retranslateUi(self, DaysCalculator):
        _translate = QtCore.QCoreApplication.translate
        DaysCalculator.setWindowTitle(_translate("DaysCalculator", "Dialog"))
        self.label_daysCalculator.setText(_translate("DaysCalculator", "TextLabel"))
        self.pushButton_calculate.setText(_translate("DaysCalculator", "PushButton"))
        self.label_totalDays.setText(_translate("DaysCalculator", "TextLabel"))
        self.pushButton_quit.setText(_translate("DaysCalculator", "PushButton"))
        self.label_initialDate.setText(_translate("DaysCalculator", "TextLabel"))
        self.label_finalDate.setText(_translate("DaysCalculator", "TextLabel"))
