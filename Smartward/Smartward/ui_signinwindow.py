# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'signinwindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

import json
#import os
import re
import socket
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtSql import *
from sw_string import *
from dbconnect import *
from swgmail import *
import mysql.connector
from mainwindow import *

db=database_signinwindow("localhost","root","smartward")
mygmail=SWGmail()

class Ui_MainWindow(QWidget):
    def window_functions(self,MainWindow):

        #checking whether ward is registered or not
        try:
            with open('ward.json','r') as obj:
                read=json.load(obj)
                print("Ward already registered.")
                self.signStack.setCurrentIndex(2)
        except Exception:
            self.signStack.setCurrentIndex(0)

        # definition of signinwindow functions
        def on_signup_clicked():
            print("signup clicked")
            #get value from lineedits
            municipality=self.municipality.text().title()
            wardno=self.wardno.text()
            address=self.address.text().title()
            state=self.state.text()
            phone=self.phoneNo.text()
            email=self.email.text()
            mun_logo=self.mun_logo.text()
            password=self.password.text()
            confirmpassword = self.confirmpassword.text()

            #check if all fields are filled
            if(isEmpty(municipality,wardno,address,phone,email,password,confirmpassword)):
                QMessageBox.warning(self,"SignUp Failed","All fields are not filled!")
            elif(not(password == confirmpassword)):
                QMessageBox.warning(self,"Password Confirmation Invalid","Password doesnot match!")
            else:
                db.createWardTable()
                if(not db.checkValid(municipality,wardno)):
                    QMessageBox.information(self,"SignUp Failed","Ward Office already Registered!")
                else:
                    if(not db.checkEmailValid(email)):
                        QMessageBox.information(self,"Signup Failed","Email Already in Use.Try another email.")
                    else:
                        id=generateID(municipality.lower(),wardno,state)
                        print(id)
                        ip = socket.gethostbyname(socket.gethostname())
                        wada={'id':id,'municipality':municipality,'ward_no':wardno,'state':state,'address':address,'phone':phone,'email':email,'mun_logo':mun_logo,'password':password,'ip':ip}
                        if(db.InsertIntoward_registrationTable(id,municipality,wardno,state,address,phone,email,"****",mun_logo,password)):
                            with open('ward.json','w') as obj:
                                json.dump(wada,obj)
                                #mygmail.sendRegistrationSuccessfulMail(id,municipality,wardno,state,address,phone,email,ip,password)
                                QMessageBox.information(self,"Registration Successful","We have sent mail to your email account.\nCheck the mail for login details.")

        def on_browse_clicked():
            print("browse clicked")
            #set browse file for images
            path=QFileDialog.getOpenFileName(self,"Municipality Logo","/home","Images(*.png)")[0]
            self.mun_logo.setText(path)

        def on_signin_2_clicked():
            # go to signinPage
            self.signStack.setCurrentIndex(2)


        def on_signin_clicked():
            #get id or email and password from line edits
            login_id=self.login_id.text()
            login_password=self.login_password.text()
            if (isEmpty(login_id,login_password)):
                QMessageBox.warning(self,"Login Unsucessful","Login ID or Password is Missing!")
            else:
                ip,email,id=db.checkLoginValidity(login_id,login_password)
                print(ip,email,id)
                if(ip=="invalid" and email=="" and id==""):
                    QMessageBox.warning(self,"Login Unsucessful","Login ID or Password Invalid")
                else:
                    ip_add = socket.gethostbyname(socket.gethostname())
                    if not(ip==ip_add):
                        db.updateIP(login_id,ip_add)
                        #mygmail.sendLoginMail(email,ip)
                        
                        
                        MainWindow.hide()
                        #os.startfile('mainwindow.py') #not a good idea
                        self.WardWindow = QtWidgets.QMainWindow()
                        self.home_window = Ui_WardWindow()
                        self.home_window.setupUi(self.WardWindow)
                        self.WardWindow.show()                
                        print("login window opened")


                        """
                        get id or email and password from line edits
                        --connect to database
                        ---check email or id to resemble
                        ----check password
                        ----if new ip address replace in table
                        -----send mail to inform sign in
                        -----go to smart ward main workstation
                        """


        def on_signup_2_clicked():
            # go to signupPage
            try:
                with open('ward.json','r') as obj:
                    read=json.load(obj)
                    QMessageBox.information(self,"Cannot register","Ward already registered.")
                self.signStack.setCurrentIndex(2)
            except Exception:
                self.signStack.setCurrentIndex(0)


        def on_forgetPassword_clicked():
            # go to forget password page
            self.signStack.setCurrentIndex(1)


        def on_sendEmail_clicked():
            print("send email clicked")
            gmail=self.login_id_2.text()
            login_details = db.checkEmailValidity(gmail)
            if not(login_details):
                QMessageBox.warning(self,"Forget Password","Invalid Email Id")
            else:
                id,email,pswd=login_details[0][0],login_details[0][6],login_details[0][-1]
                mygmail.sendForgetPasswordMail(id,email,pswd)
                QMessageBox.information(self,"Forget Password","Email has been sent to you\nwith your login details")
                """
                -connect to database
                --check if that email exists
                ---import gmail module
                ----send email to reqselfred ward
                """

        # sign up page functions
        self.signup.setAutoDefault(True)
        self.signup.clicked.connect(on_signup_clicked)
        self.browse.setAutoDefault(True)
        self.browse.clicked.connect(on_browse_clicked)
        self.signin_2.setAutoDefault(True)
        self.signin_2.clicked.connect(on_signin_2_clicked)

        # sign in page functions
        self.signin.setAutoDefault(True)
        self.signin.clicked.connect(on_signin_clicked)
        self.signup_2.setAutoDefault(True)
        self.signup_2.clicked.connect(on_signup_2_clicked)
        self.forgetPassword.setAutoDefault(True)
        self.forgetPassword.clicked.connect(on_forgetPassword_clicked)

        # forget password functions
        self.signin_3.setAutoDefault(True)
        self.signin_3.clicked.connect(on_signin_2_clicked)
        self.sendEmail.setAutoDefault(True)
        self.sendEmail.clicked.connect(on_sendEmail_clicked)




    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(614, 668)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        MainWindow.setMaximumSize(QtCore.QSize(1366, 768))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("sw_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.signinBox = QtWidgets.QGroupBox(self.centralWidget)
        self.signinBox.setGeometry(QtCore.QRect(10, 10, 591, 641))
        self.signinBox.setMinimumSize(QtCore.QSize(0, 0))
        self.signinBox.setMaximumSize(QtCore.QSize(1366, 768))
        self.signinBox.setStyleSheet("QLineEdit,QGroupBox,QPushButton{\n"
" background:transparent;\n"
"color: rgb(23, 109, 2);\n"
"      border: 2px solid gray;\n"
"      border-radius: 10px;\n"
"}")
        self.signinBox.setTitle("")
        self.signinBox.setObjectName("signinBox")
        self.sw_logo_ = QtWidgets.QLabel(self.signinBox)
        self.sw_logo_.setGeometry(QtCore.QRect(140, 10, 311, 191))
        self.sw_logo_.setStyleSheet("border:none;\n"
"border-radius:0px;\n"
"border-image:url(:/pic/sw_logo.png)")
        self.sw_logo_.setText("")
        self.sw_logo_.setObjectName("sw_logo_")
        self.signStack = QtWidgets.QStackedWidget(self.signinBox)
        self.signStack.setGeometry(QtCore.QRect(10, 180, 571, 441))
        self.signStack.setMinimumSize(QtCore.QSize(0, 0))
        self.signStack.setMaximumSize(QtCore.QSize(1366, 768))
        self.signStack.setStyleSheet("\n"
"background:transparent;\n"
"")
        self.signStack.setObjectName("signStack")
        self.signupPage = QtWidgets.QWidget()
        self.signupPage.setObjectName("signupPage")
        self.municipality = QtWidgets.QLineEdit(self.signupPage)
        self.municipality.setGeometry(QtCore.QRect(30, 60, 351, 31))
        self.municipality.setStyleSheet("background:transparent")
        self.municipality.setText("")
        self.municipality.setObjectName("municipality")
        self.address = QtWidgets.QLineEdit(self.signupPage)
        self.address.setGeometry(QtCore.QRect(30, 110, 351, 31))
        self.address.setStyleSheet("background:transparent")
        self.address.setObjectName("address")
        self.phoneNo = QtWidgets.QLineEdit(self.signupPage)
        self.phoneNo.setGeometry(QtCore.QRect(30, 160, 351, 31))
        self.phoneNo.setStyleSheet("background:transparent")
        self.phoneNo.setText("")
        self.phoneNo.setObjectName("phoneNo")
        self.email = QtWidgets.QLineEdit(self.signupPage)
        self.email.setGeometry(QtCore.QRect(30, 200, 351, 31))
        self.email.setStyleSheet("background:transparent")
        self.email.setObjectName("email")
        self.wardno = QtWidgets.QLineEdit(self.signupPage)
        self.wardno.setGeometry(QtCore.QRect(400, 60, 141, 31))
        self.wardno.setStyleSheet("background:transparent")
        self.wardno.setObjectName("wardno")
        self.mun_logo = QtWidgets.QLineEdit(self.signupPage)
        self.mun_logo.setGeometry(QtCore.QRect(30, 250, 351, 31))
        self.mun_logo.setStyleSheet("background:transparent")
        self.mun_logo.setEchoMode(QtWidgets.QLineEdit.Password)
        self.mun_logo.setObjectName("mun_logo")
        self.password = QtWidgets.QLineEdit(self.signupPage)
        self.password.setGeometry(QtCore.QRect(30, 300, 251, 31))
        self.password.setStyleSheet("background:transparent")
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")
        self.confirmpassword = QtWidgets.QLineEdit(self.signupPage)
        self.confirmpassword.setGeometry(QtCore.QRect(300, 300, 251, 31))
        self.confirmpassword.setStyleSheet("background:transparent")
        self.confirmpassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirmpassword.setObjectName("confirmpassword")
        self.signup = QtWidgets.QPushButton(self.signupPage)
        self.signup.setGeometry(QtCore.QRect(200, 370, 191, 41))
        self.signup.setStyleSheet("border: 2px solid #8f8f91;\n"
"border-radius: 6px;\n"
"background:blue;\n"
"color:white;\n"
"")
        self.signup.setObjectName("signup")
        self.signin_2 = QtWidgets.QPushButton(self.signupPage)
        self.signin_2.setGeometry(QtCore.QRect(310, 420, 261, 25))
        self.signin_2.setStyleSheet("border:none;")
        self.signin_2.setObjectName("signin_2")
        self.browse = QtWidgets.QPushButton(self.signupPage)
        self.browse.setGeometry(QtCore.QRect(390, 250, 41, 31))
        self.browse.setStyleSheet("border: 2px solid black;\n"
"border-radius:0px;\n"
"border-image:url(:/pic/browse.png);\n"
"\n"
"")
        self.browse.setText("")
        self.browse.setObjectName("browse")
        self.label_3 = QtWidgets.QLabel(self.signupPage)
        self.label_3.setGeometry(QtCore.QRect(180, 10, 181, 41))
        self.label_3.setStyleSheet("background:transparent;\n"
"color: rgb(223, 101, 21);\n"
"    ")
        self.label_3.setObjectName("label_3")
        self.state = QtWidgets.QLineEdit(self.signupPage)
        self.state.setGeometry(QtCore.QRect(400, 110, 141, 31))
        self.state.setObjectName("state")
        self.signStack.addWidget(self.signupPage)
        self.forgetPasswordPage = QtWidgets.QWidget()
        self.forgetPasswordPage.setObjectName("forgetPasswordPage")
        self.label_2 = QtWidgets.QLabel(self.forgetPasswordPage)
        self.label_2.setGeometry(QtCore.QRect(150, 20, 241, 41))
        self.label_2.setStyleSheet("background:transparent;\n"
"color: rgb(223, 101, 21);\n"
"    ")
        self.label_2.setObjectName("label_2")
        self.signin_3 = QtWidgets.QPushButton(self.forgetPasswordPage)
        self.signin_3.setGeometry(QtCore.QRect(420, 390, 121, 25))
        self.signin_3.setStyleSheet("border:none;")
        self.signin_3.setObjectName("signin_3")
        self.label = QtWidgets.QLabel(self.forgetPasswordPage)
        self.label.setGeometry(QtCore.QRect(130, 70, 291, 61))
        self.label.setStyleSheet("background:transparent;\n"
"color: rgb(223, 101, 21);\n"
"    ")
        self.label.setObjectName("label")
        self.login_id_2 = QtWidgets.QLineEdit(self.forgetPasswordPage)
        self.login_id_2.setGeometry(QtCore.QRect(70, 160, 471, 41))
        self.login_id_2.setStyleSheet("background:transparent")
        self.login_id_2.setObjectName("login_id_2")
        self.sendEmail = QtWidgets.QPushButton(self.forgetPasswordPage)
        self.sendEmail.setGeometry(QtCore.QRect(230, 240, 141, 41))
        self.sendEmail.setStyleSheet("border: 2px solid #8f8f91;\n"
"border-radius: 6px;\n"
"background:blue;\n"
"color:white;\n"
"")
        self.sendEmail.setObjectName("sendEmail")
        self.signStack.addWidget(self.forgetPasswordPage)
        self.signinPage = QtWidgets.QWidget()
        self.signinPage.setObjectName("signinPage")
        self.login_id = QtWidgets.QLineEdit(self.signinPage)
        self.login_id.setGeometry(QtCore.QRect(50, 110, 471, 41))
        self.login_id.setStyleSheet("background:transparent")
        self.login_id.setObjectName("login_id")
        self.login_password = QtWidgets.QLineEdit(self.signinPage)
        self.login_password.setGeometry(QtCore.QRect(50, 200, 471, 41))
        self.login_password.setStyleSheet("background:transparent;")
        self.login_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.login_password.setObjectName("login_password")
        self.signin = QtWidgets.QPushButton(self.signinPage)
        self.signin.setGeometry(QtCore.QRect(170, 290, 211, 41))
        self.signin.setStyleSheet("border: 2px solid #8f8f91;\n"
"border-radius: 6px;\n"
"background:blue;\n"
"color:white;\n"
"")
        self.signin.setObjectName("signin")
        self.forgetPassword = QtWidgets.QPushButton(self.signinPage)
        self.forgetPassword.setGeometry(QtCore.QRect(340, 380, 151, 25))
        self.forgetPassword.setStyleSheet("border:none;")
        self.forgetPassword.setObjectName("forgetPassword")
        self.signup_2 = QtWidgets.QPushButton(self.signinPage)
        self.signup_2.setGeometry(QtCore.QRect(490, 380, 61, 25))
        self.signup_2.setStyleSheet("border:none;\n"
"border-left:50px;\n"
"")
        self.signup_2.setObjectName("signup_2")
        self.label_4 = QtWidgets.QLabel(self.signinPage)
        self.label_4.setGeometry(QtCore.QRect(240, 30, 61, 41))
        self.label_4.setStyleSheet("background:transparent;\n"
"color: rgb(223, 101, 21);\n"
"    ")
        self.label_4.setObjectName("label_4")
        self.signStack.addWidget(self.signinPage)
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        self.window_functions(MainWindow)
        self.signStack.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Smartवडा"))
        self.municipality.setPlaceholderText(_translate("MainWindow", "(Rural) Municipality/(Sub) Metropolitan City"))
        self.address.setPlaceholderText(_translate("MainWindow", "Address"))
        self.phoneNo.setPlaceholderText(_translate("MainWindow", "Phone No"))
        self.email.setPlaceholderText(_translate("MainWindow", "E-mail ID"))
        self.wardno.setPlaceholderText(_translate("MainWindow", "Ward No."))
        self.mun_logo.setPlaceholderText(_translate("MainWindow", "Municipality/VDC Logo"))
        self.password.setPlaceholderText(_translate("MainWindow", "Password"))
        self.confirmpassword.setPlaceholderText(_translate("MainWindow", "Re-Type your Password"))
        self.signup.setText(_translate("MainWindow", "Sign Up"))
        self.signin_2.setText(_translate("MainWindow", "Already have account,Sign In Instead"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">REGISTER NEW WARD</span></p></body></html>"))
        self.state.setPlaceholderText(_translate("MainWindow", "State"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">FORGOTTEN YOUR PASSWORD</span></p></body></html>"))
        self.signin_3.setText(_translate("MainWindow", "Sign In Instead"))
        self.label.setText(_translate("MainWindow", "We would send email to your account to \n"
"give your login details."))
        self.login_id_2.setPlaceholderText(_translate("MainWindow", "Enter email id for your account"))
        self.sendEmail.setText(_translate("MainWindow", "Send E-mail"))
        self.login_id.setPlaceholderText(_translate("MainWindow", "Id or Gmail"))
        self.login_password.setPlaceholderText(_translate("MainWindow", "Password"))
        self.signin.setText(_translate("MainWindow", "Sign In"))
        self.forgetPassword.setText(_translate("MainWindow", "Forgot your password"))
        self.signup_2.setText(_translate("MainWindow", "|Sign Up"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">LOGIN</span></p></body></html>"))
import sw_rc
