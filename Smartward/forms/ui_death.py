# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'deathregistrationform.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(694, 801)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, -200, 649, 1051))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.districtLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.districtLabel.setObjectName("districtLabel")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.districtLabel)
        self.districtLineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.districtLineEdit.setObjectName("districtLineEdit")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.districtLineEdit)
        self.mubicipalityLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.mubicipalityLabel.setObjectName("mubicipalityLabel")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.mubicipalityLabel)
        self.mubicipalityLineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.mubicipalityLineEdit.setObjectName("mubicipalityLineEdit")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.mubicipalityLineEdit)
        self.wardNoLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.wardNoLabel.setObjectName("wardNoLabel")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.wardNoLabel)
        self.wardNoLineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.wardNoLineEdit.setObjectName("wardNoLineEdit")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.wardNoLineEdit)
        self.roadLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.roadLabel.setObjectName("roadLabel")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.roadLabel)
        self.roadLineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.roadLineEdit.setObjectName("roadLineEdit")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.roadLineEdit)
        self.houseNoLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.houseNoLabel.setObjectName("houseNoLabel")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.houseNoLabel)
        self.houseNoLineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.houseNoLineEdit.setObjectName("houseNoLineEdit")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.houseNoLineEdit)
        self.villageLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.villageLabel.setObjectName("villageLabel")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.villageLabel)
        self.villageLineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.villageLineEdit.setObjectName("villageLineEdit")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.villageLineEdit)
        self.gridLayout_2.addLayout(self.formLayout_2, 3, 0, 1, 1)
        self.formLayout_5 = QtWidgets.QFormLayout()
        self.formLayout_5.setObjectName("formLayout_5")
        self.districtLabel_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.districtLabel_2.setObjectName("districtLabel_2")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.districtLabel_2)
        self.districtLineEdit_2 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.districtLineEdit_2.setObjectName("districtLineEdit_2")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.districtLineEdit_2)
        self.municipalityLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.municipalityLabel.setObjectName("municipalityLabel")
        self.formLayout_5.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.municipalityLabel)
        self.municipalityLineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.municipalityLineEdit.setObjectName("municipalityLineEdit")
        self.formLayout_5.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.municipalityLineEdit)
        self.wardNoLabel_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.wardNoLabel_2.setObjectName("wardNoLabel_2")
        self.formLayout_5.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.wardNoLabel_2)
        self.roadtLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.roadtLabel.setObjectName("roadtLabel")
        self.formLayout_5.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.roadtLabel)
        self.roadStreetLineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.roadStreetLineEdit.setObjectName("roadStreetLineEdit")
        self.formLayout_5.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.roadStreetLineEdit)
        self.houseNoLabel_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.houseNoLabel_2.setObjectName("houseNoLabel_2")
        self.formLayout_5.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.houseNoLabel_2)
        self.houseNoLineEdit_2 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.houseNoLineEdit_2.setObjectName("houseNoLineEdit_2")
        self.formLayout_5.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.houseNoLineEdit_2)
        self.villageLabel_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.villageLabel_2.setObjectName("villageLabel_2")
        self.formLayout_5.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.villageLabel_2)
        self.villageCommunityLineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.villageCommunityLineEdit.setObjectName("villageCommunityLineEdit")
        self.formLayout_5.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.villageCommunityLineEdit)
        self.wardNoLineEdit_2 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.wardNoLineEdit_2.setObjectName("wardNoLineEdit_2")
        self.formLayout_5.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.wardNoLineEdit_2)
        self.gridLayout_2.addLayout(self.formLayout_5, 5, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 6, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 2, 0, 1, 1)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.birthRegistrationNoLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.birthRegistrationNoLabel.setObjectName("birthRegistrationNoLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.birthRegistrationNoLabel)
        self.birthRegistrationNoLineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.birthRegistrationNoLineEdit.setObjectName("birthRegistrationNoLineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.birthRegistrationNoLineEdit)
        self.nameLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.nameLabel.setObjectName("nameLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.nameLabel)
        self.nameLineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.nameLineEdit.setObjectName("nameLineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.nameLineEdit)
        self.dateOfBirthLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.dateOfBirthLabel.setObjectName("dateOfBirthLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.dateOfBirthLabel)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.dateEdit_2 = QtWidgets.QDateEdit(self.scrollAreaWidgetContents)
        self.dateEdit_2.setObjectName("dateEdit_2")
        self.horizontalLayout.addWidget(self.dateEdit_2)
        self.dateEdit = QtWidgets.QDateEdit(self.scrollAreaWidgetContents)
        self.dateEdit.setObjectName("dateEdit")
        self.horizontalLayout.addWidget(self.dateEdit)
        self.formLayout.setLayout(2, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout)
        self.dateOfDeathLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.dateOfDeathLabel.setObjectName("dateOfDeathLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.dateOfDeathLabel)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.dateEdit_4 = QtWidgets.QDateEdit(self.scrollAreaWidgetContents)
        self.dateEdit_4.setObjectName("dateEdit_4")
        self.horizontalLayout_2.addWidget(self.dateEdit_4)
        self.dateEdit_3 = QtWidgets.QDateEdit(self.scrollAreaWidgetContents)
        self.dateEdit_3.setObjectName("dateEdit_3")
        self.horizontalLayout_2.addWidget(self.dateEdit_3)
        self.formLayout.setLayout(3, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_2)
        self.placeOfDeathLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.placeOfDeathLabel.setObjectName("placeOfDeathLabel")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.placeOfDeathLabel)
        self.placeOfDeathLineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.placeOfDeathLineEdit.setObjectName("placeOfDeathLineEdit")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.placeOfDeathLineEdit)
        self.gridLayout_2.addLayout(self.formLayout, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 4, 0, 1, 1)
        self.formLayout_6 = QtWidgets.QFormLayout()
        self.formLayout_6.setObjectName("formLayout_6")
        self.citizenshipNoLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.citizenshipNoLabel.setObjectName("citizenshipNoLabel")
        self.formLayout_6.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.citizenshipNoLabel)
        self.citizenshipNoLineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.citizenshipNoLineEdit.setObjectName("citizenshipNoLineEdit")
        self.formLayout_6.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.citizenshipNoLineEdit)
        self.issueDistrictLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.issueDistrictLabel.setObjectName("issueDistrictLabel")
        self.formLayout_6.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.issueDistrictLabel)
        self.issueDistrictLineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.issueDistrictLineEdit.setObjectName("issueDistrictLineEdit")
        self.formLayout_6.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.issueDistrictLineEdit)
        self.issueDateLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.issueDateLabel.setObjectName("issueDateLabel")
        self.formLayout_6.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.issueDateLabel)
        self.dateEdit_5 = QtWidgets.QDateEdit(self.scrollAreaWidgetContents)
        self.dateEdit_5.setObjectName("dateEdit_5")
        self.formLayout_6.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.dateEdit_5)
        self.forForeignerLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.forForeignerLabel.setObjectName("forForeignerLabel")
        self.formLayout_6.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.forForeignerLabel)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_3.addWidget(self.lineEdit_2)
        self.lineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_3.addWidget(self.lineEdit)
        self.formLayout_6.setLayout(3, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_3)
        self.qualificationLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.qualificationLabel.setObjectName("qualificationLabel")
        self.formLayout_6.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.qualificationLabel)
        self.qualificationLineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.qualificationLineEdit.setObjectName("qualificationLineEdit")
        self.formLayout_6.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.qualificationLineEdit)
        self.mothersTongueLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.mothersTongueLabel.setObjectName("mothersTongueLabel")
        self.formLayout_6.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.mothersTongueLabel)
        self.mothersTongueLineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.mothersTongueLineEdit.setObjectName("mothersTongueLineEdit")
        self.formLayout_6.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.mothersTongueLineEdit)
        self.casteLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.casteLabel.setObjectName("casteLabel")
        self.formLayout_6.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.casteLabel)
        self.casteLineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.casteLineEdit.setObjectName("casteLineEdit")
        self.formLayout_6.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.casteLineEdit)
        self.religionLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.religionLabel.setObjectName("religionLabel")
        self.formLayout_6.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.religionLabel)
        self.religionLineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.religionLineEdit.setObjectName("religionLineEdit")
        self.formLayout_6.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.religionLineEdit)
        self.grandFatherLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.grandFatherLabel.setObjectName("grandFatherLabel")
        self.formLayout_6.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.grandFatherLabel)
        self.grandFatherLineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.grandFatherLineEdit.setObjectName("grandFatherLineEdit")
        self.formLayout_6.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.grandFatherLineEdit)
        self.fatherLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.fatherLabel.setObjectName("fatherLabel")
        self.formLayout_6.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.fatherLabel)
        self.fatherLineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.fatherLineEdit.setObjectName("fatherLineEdit")
        self.formLayout_6.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.fatherLineEdit)
        self.motherLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.motherLabel.setObjectName("motherLabel")
        self.formLayout_6.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.motherLabel)
        self.motherLineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.motherLineEdit.setObjectName("motherLineEdit")
        self.formLayout_6.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.motherLineEdit)
        self.spouseLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.spouseLabel.setObjectName("spouseLabel")
        self.formLayout_6.setWidget(11, QtWidgets.QFormLayout.LabelRole, self.spouseLabel)
        self.spouseLineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.spouseLineEdit.setObjectName("spouseLineEdit")
        self.formLayout_6.setWidget(11, QtWidgets.QFormLayout.FieldRole, self.spouseLineEdit)
        self.causeOfDeathLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.causeOfDeathLabel.setObjectName("causeOfDeathLabel")
        self.formLayout_6.setWidget(12, QtWidgets.QFormLayout.LabelRole, self.causeOfDeathLabel)
        self.causeOfDeathLineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.causeOfDeathLineEdit.setObjectName("causeOfDeathLineEdit")
        self.formLayout_6.setWidget(12, QtWidgets.QFormLayout.FieldRole, self.causeOfDeathLineEdit)
        self.gridLayout_2.addLayout(self.formLayout_6, 7, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.districtLabel.setText(_translate("MainWindow", "District"))
        self.mubicipalityLabel.setText(_translate("MainWindow", "Municopality"))
        self.wardNoLabel.setText(_translate("MainWindow", "Ward No"))
        self.roadLabel.setText(_translate("MainWindow", "Road/Route/street"))
        self.houseNoLabel.setText(_translate("MainWindow", "House No:"))
        self.villageLabel.setText(_translate("MainWindow", "Village/Community"))
        self.districtLabel_2.setText(_translate("MainWindow", "District"))
        self.municipalityLabel.setText(_translate("MainWindow", "Municipality"))
        self.wardNoLabel_2.setText(_translate("MainWindow", "Ward No"))
        self.roadtLabel.setText(_translate("MainWindow", "Road/street"))
        self.houseNoLabel_2.setText(_translate("MainWindow", "House No"))
        self.villageLabel_2.setText(_translate("MainWindow", "Village/Community"))
        self.label_4.setText(_translate("MainWindow", "Deatils Of Deceased"))
        self.label_2.setText(_translate("MainWindow", "Place Of Birth"))
        self.birthRegistrationNoLabel.setText(_translate("MainWindow", "Birth Registration No"))
        self.nameLabel.setText(_translate("MainWindow", "Name"))
        self.dateOfBirthLabel.setText(_translate("MainWindow", "Date Of Birth"))
        self.dateOfDeathLabel.setText(_translate("MainWindow", "Date Of Death"))
        self.placeOfDeathLabel.setText(_translate("MainWindow", "Place of Death"))
        self.label.setText(_translate("MainWindow", "Details Of Deceased\'s"))
        self.label_3.setText(_translate("MainWindow", "Adress Of Deceased"))
        self.citizenshipNoLabel.setText(_translate("MainWindow", "Citizenship No"))
        self.issueDistrictLabel.setText(_translate("MainWindow", "Issue District"))
        self.issueDateLabel.setText(_translate("MainWindow", "Issue Date"))
        self.forForeignerLabel.setText(_translate("MainWindow", "For Foreigner"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "Country"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Passport No"))
        self.qualificationLabel.setText(_translate("MainWindow", "Qualification"))
        self.mothersTongueLabel.setText(_translate("MainWindow", "Mothers Tongue"))
        self.casteLabel.setText(_translate("MainWindow", "Caste"))
        self.religionLabel.setText(_translate("MainWindow", "Religion"))
        self.grandFatherLabel.setText(_translate("MainWindow", "GrandFather"))
        self.fatherLabel.setText(_translate("MainWindow", "Father"))
        self.motherLabel.setText(_translate("MainWindow", "Mother"))
        self.spouseLabel.setText(_translate("MainWindow", "Spouse"))
        self.causeOfDeathLabel.setText(_translate("MainWindow", "Cause Of Death"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
