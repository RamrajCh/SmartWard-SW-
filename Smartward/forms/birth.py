from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import datetime
import nepali_date
import sw_string

table="BirthRegistration"


class Ui_BirthForm(object):
    def setupUi(self, BirthForm):
        BirthForm.setObjectName("BirthForm")
        BirthForm.resize(888, 989)
        self.centralwidget = QtWidgets.QWidget(BirthForm)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 851, 1086))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.formLayout_5 = QtWidgets.QFormLayout()
        self.formLayout_5.setObjectName("formLayout_5")
        self.grandFatherLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.grandFatherLabel.setObjectName("grandFatherLabel")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.grandFatherLabel)
        self.grandFatherLineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.grandFatherLineEdit.setObjectName("grandFatherLineEdit")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.grandFatherLineEdit)
        self.gridLayout_2.addLayout(self.formLayout_5, 4, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 3, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 1, 0, 1, 1)
        self.formLayout_6 = QtWidgets.QFormLayout()
        self.formLayout_6.setObjectName("formLayout_6")
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label.setText("")
        self.label.setObjectName("label")
        self.formLayout_6.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.formLayout_6.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_3)
        self.nameLabel_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.nameLabel_2.setObjectName("nameLabel_2")
        self.formLayout_6.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.nameLabel_2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.horizontalLayout_2.addWidget(self.lineEdit_6)
        self.formLayout_6.setLayout(1, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_2)
        self.label_4 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_4.setObjectName("label_4")
        self.formLayout_6.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.districtLabel_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.districtLabel_2.setObjectName("districtLabel_2")
        self.formLayout_6.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.districtLabel_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.districtLineEdit_3 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.districtLineEdit_3.setObjectName("districtLineEdit_3")
        self.horizontalLayout_4.addWidget(self.districtLineEdit_3)
        self.districtLineEdit_2 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.districtLineEdit_2.setObjectName("districtLineEdit_2")
        self.horizontalLayout_4.addWidget(self.districtLineEdit_2)
        self.formLayout_6.setLayout(3, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_4)
        self.municipalityLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.municipalityLabel.setObjectName("municipalityLabel")
        self.formLayout_6.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.municipalityLabel)
        self.wardNoLabel_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.wardNoLabel_2.setObjectName("wardNoLabel_2")
        self.formLayout_6.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.wardNoLabel_2)
        self.roadLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.roadLabel.setObjectName("roadLabel")
        self.formLayout_6.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.roadLabel)
        self.communityLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.communityLabel.setObjectName("communityLabel")
        self.formLayout_6.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.communityLabel)
        self.houseNoLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.houseNoLabel.setObjectName("houseNoLabel")
        self.formLayout_6.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.houseNoLabel)
        self.ageAtBirthLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.ageAtBirthLabel.setObjectName("ageAtBirthLabel")
        self.formLayout_6.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.ageAtBirthLabel)
        self.motherlandLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.motherlandLabel.setObjectName("motherlandLabel")
        self.formLayout_6.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.motherlandLabel)
        self.countryWithCitizenshipLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.countryWithCitizenshipLabel.setObjectName("countryWithCitizenshipLabel")
        self.formLayout_6.setWidget(11, QtWidgets.QFormLayout.LabelRole, self.countryWithCitizenshipLabel)
        self.citizenshipNoLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.citizenshipNoLabel.setObjectName("citizenshipNoLabel")
        self.formLayout_6.setWidget(12, QtWidgets.QFormLayout.LabelRole, self.citizenshipNoLabel)
        self.issueDateLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.issueDateLabel.setObjectName("issueDateLabel")
        self.formLayout_6.setWidget(13, QtWidgets.QFormLayout.LabelRole, self.issueDateLabel)
        self.issueAdressLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.issueAdressLabel.setObjectName("issueAdressLabel")
        self.formLayout_6.setWidget(14, QtWidgets.QFormLayout.LabelRole, self.issueAdressLabel)
        self.citizenshipNoIfForeignLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.citizenshipNoIfForeignLabel.setObjectName("citizenshipNoIfForeignLabel")
        self.formLayout_6.setWidget(15, QtWidgets.QFormLayout.LabelRole, self.citizenshipNoIfForeignLabel)
        self.qualificationLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.qualificationLabel.setObjectName("qualificationLabel")
        self.formLayout_6.setWidget(16, QtWidgets.QFormLayout.LabelRole, self.qualificationLabel)
        self.occupationLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.occupationLabel.setObjectName("occupationLabel")
        self.formLayout_6.setWidget(17, QtWidgets.QFormLayout.LabelRole, self.occupationLabel)
        self.religionLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.religionLabel.setObjectName("religionLabel")
        self.formLayout_6.setWidget(18, QtWidgets.QFormLayout.LabelRole, self.religionLabel)
        self.motherSTongueLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.motherSTongueLabel.setObjectName("motherSTongueLabel")
        self.formLayout_6.setWidget(19, QtWidgets.QFormLayout.LabelRole, self.motherSTongueLabel)
        self.totalChildrenLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.totalChildrenLabel.setObjectName("totalChildrenLabel")
        self.formLayout_6.setWidget(20, QtWidgets.QFormLayout.LabelRole, self.totalChildrenLabel)
        self.totalChildrenLineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.totalChildrenLineEdit.setObjectName("totalChildrenLineEdit")
        self.formLayout_6.setWidget(20, QtWidgets.QFormLayout.FieldRole, self.totalChildrenLineEdit)
        self.totalChildrenAliveLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.totalChildrenAliveLabel.setObjectName("totalChildrenAliveLabel")
        self.formLayout_6.setWidget(21, QtWidgets.QFormLayout.LabelRole, self.totalChildrenAliveLabel)
        self.totalChildrenAliveLineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.totalChildrenAliveLineEdit.setObjectName("totalChildrenAliveLineEdit")
        self.formLayout_6.setWidget(21, QtWidgets.QFormLayout.FieldRole, self.totalChildrenAliveLineEdit)
        self.marriageRegistrationNoLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.marriageRegistrationNoLabel.setObjectName("marriageRegistrationNoLabel")
        self.formLayout_6.setWidget(22, QtWidgets.QFormLayout.LabelRole, self.marriageRegistrationNoLabel)
        self.marriageRegistrationNoLineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.marriageRegistrationNoLineEdit.setObjectName("marriageRegistrationNoLineEdit")
        self.formLayout_6.setWidget(22, QtWidgets.QFormLayout.FieldRole, self.marriageRegistrationNoLineEdit)
        self.marriageDateLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.marriageDateLabel.setObjectName("marriageDateLabel")
        self.formLayout_6.setWidget(23, QtWidgets.QFormLayout.LabelRole, self.marriageDateLabel)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.districtLineEdit_4 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.districtLineEdit_4.setObjectName("districtLineEdit_4")
        self.horizontalLayout_5.addWidget(self.districtLineEdit_4)
        self.districtLineEdit_5 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.districtLineEdit_5.setObjectName("districtLineEdit_5")
        self.horizontalLayout_5.addWidget(self.districtLineEdit_5)
        self.formLayout_6.setLayout(4, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.districtLineEdit_6 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.districtLineEdit_6.setObjectName("districtLineEdit_6")
        self.horizontalLayout_6.addWidget(self.districtLineEdit_6)
        self.districtLineEdit_7 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.districtLineEdit_7.setObjectName("districtLineEdit_7")
        self.horizontalLayout_6.addWidget(self.districtLineEdit_7)
        self.formLayout_6.setLayout(5, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.districtLineEdit_8 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.districtLineEdit_8.setObjectName("districtLineEdit_8")
        self.horizontalLayout_7.addWidget(self.districtLineEdit_8)
        self.districtLineEdit_9 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.districtLineEdit_9.setObjectName("districtLineEdit_9")
        self.horizontalLayout_7.addWidget(self.districtLineEdit_9)
        self.formLayout_6.setLayout(6, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.districtLineEdit_10 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.districtLineEdit_10.setObjectName("districtLineEdit_10")
        self.horizontalLayout_8.addWidget(self.districtLineEdit_10)
        self.districtLineEdit_11 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.districtLineEdit_11.setObjectName("districtLineEdit_11")
        self.horizontalLayout_8.addWidget(self.districtLineEdit_11)
        self.formLayout_6.setLayout(7, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_8)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.districtLineEdit_12 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.districtLineEdit_12.setObjectName("districtLineEdit_12")
        self.horizontalLayout_9.addWidget(self.districtLineEdit_12)
        self.districtLineEdit_13 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.districtLineEdit_13.setObjectName("districtLineEdit_13")
        self.horizontalLayout_9.addWidget(self.districtLineEdit_13)
        self.formLayout_6.setLayout(8, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_9)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.districtLineEdit_14 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.districtLineEdit_14.setObjectName("districtLineEdit_14")
        self.horizontalLayout_10.addWidget(self.districtLineEdit_14)
        self.districtLineEdit_15 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.districtLineEdit_15.setObjectName("districtLineEdit_15")
        self.horizontalLayout_10.addWidget(self.districtLineEdit_15)
        self.formLayout_6.setLayout(9, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_10)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.districtLineEdit_16 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.districtLineEdit_16.setObjectName("districtLineEdit_16")
        self.horizontalLayout_11.addWidget(self.districtLineEdit_16)
        self.districtLineEdit_17 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.districtLineEdit_17.setObjectName("districtLineEdit_17")
        self.horizontalLayout_11.addWidget(self.districtLineEdit_17)
        self.formLayout_6.setLayout(10, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_11)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.districtLineEdit_18 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.districtLineEdit_18.setObjectName("districtLineEdit_18")
        self.horizontalLayout_12.addWidget(self.districtLineEdit_18)
        self.districtLineEdit_19 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.districtLineEdit_19.setObjectName("districtLineEdit_19")
        self.horizontalLayout_12.addWidget(self.districtLineEdit_19)
        self.formLayout_6.setLayout(11, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_12)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.districtLineEdit_20 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.districtLineEdit_20.setObjectName("districtLineEdit_20")
        self.horizontalLayout_13.addWidget(self.districtLineEdit_20)
        self.districtLineEdit_21 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.districtLineEdit_21.setObjectName("districtLineEdit_21")
        self.horizontalLayout_13.addWidget(self.districtLineEdit_21)
        self.formLayout_6.setLayout(12, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_13)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.districtLineEdit_22 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.districtLineEdit_22.setObjectName("districtLineEdit_22")
        self.horizontalLayout_14.addWidget(self.districtLineEdit_22)
        self.districtLineEdit_23 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.districtLineEdit_23.setObjectName("districtLineEdit_23")
        self.horizontalLayout_14.addWidget(self.districtLineEdit_23)
        self.formLayout_6.setLayout(13, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_14)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.districtLineEdit_24 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.districtLineEdit_24.setObjectName("districtLineEdit_24")
        self.horizontalLayout_15.addWidget(self.districtLineEdit_24)
        self.districtLineEdit_25 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.districtLineEdit_25.setObjectName("districtLineEdit_25")
        self.horizontalLayout_15.addWidget(self.districtLineEdit_25)
        self.formLayout_6.setLayout(14, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_15)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.districtLineEdit_26 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.districtLineEdit_26.setObjectName("districtLineEdit_26")
        self.horizontalLayout_16.addWidget(self.districtLineEdit_26)
        self.districtLineEdit_27 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.districtLineEdit_27.setObjectName("districtLineEdit_27")
        self.horizontalLayout_16.addWidget(self.districtLineEdit_27)
        self.formLayout_6.setLayout(15, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_16)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.districtLineEdit_28 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.districtLineEdit_28.setObjectName("districtLineEdit_28")
        self.horizontalLayout_17.addWidget(self.districtLineEdit_28)
        self.districtLineEdit_29 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.districtLineEdit_29.setObjectName("districtLineEdit_29")
        self.horizontalLayout_17.addWidget(self.districtLineEdit_29)
        self.formLayout_6.setLayout(16, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_17)
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.districtLineEdit_30 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.districtLineEdit_30.setObjectName("districtLineEdit_30")
        self.horizontalLayout_18.addWidget(self.districtLineEdit_30)
        self.districtLineEdit_31 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.districtLineEdit_31.setObjectName("districtLineEdit_31")
        self.horizontalLayout_18.addWidget(self.districtLineEdit_31)
        self.formLayout_6.setLayout(17, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_18)
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.districtLineEdit_32 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.districtLineEdit_32.setObjectName("districtLineEdit_32")
        self.horizontalLayout_19.addWidget(self.districtLineEdit_32)
        self.districtLineEdit_33 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.districtLineEdit_33.setObjectName("districtLineEdit_33")
        self.horizontalLayout_19.addWidget(self.districtLineEdit_33)
        self.formLayout_6.setLayout(18, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_19)
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.districtLineEdit_34 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.districtLineEdit_34.setObjectName("districtLineEdit_34")
        self.horizontalLayout_20.addWidget(self.districtLineEdit_34)
        self.districtLineEdit_35 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.districtLineEdit_35.setObjectName("districtLineEdit_35")
        self.horizontalLayout_20.addWidget(self.districtLineEdit_35)
        self.formLayout_6.setLayout(19, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_20)
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.dateEdit_2 = QtWidgets.QDateEdit(self.scrollAreaWidgetContents)
        self.dateEdit_2.setObjectName("dateEdit_2")
        self.horizontalLayout_21.addWidget(self.dateEdit_2)
        self.dateEdit = QtWidgets.QDateEdit(self.scrollAreaWidgetContents)
        self.dateEdit.setObjectName("dateEdit")
        self.horizontalLayout_21.addWidget(self.dateEdit)
        self.formLayout_6.setLayout(23, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_21)
        self.gridLayout_2.addLayout(self.formLayout_6, 6, 0, 1, 1)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.nameLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.nameLabel.setObjectName("nameLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.nameLabel)
        self.nameLineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.nameLineEdit.setObjectName("nameLineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.nameLineEdit)
        self.dateOfBirthLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.dateOfBirthLabel.setObjectName("dateOfBirthLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.dateOfBirthLabel)
        self.dateOfBirthDateEdit = QtWidgets.QDateEdit(self.scrollAreaWidgetContents)
        self.dateOfBirthDateEdit.setObjectName("dateOfBirthDateEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.dateOfBirthDateEdit)
        self.placeOfBirthLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.placeOfBirthLabel.setObjectName("placeOfBirthLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.placeOfBirthLabel)
        self.placeOfBirthComboBox = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.placeOfBirthComboBox.setObjectName("placeOfBirthComboBox")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.placeOfBirthComboBox)
        self.genderLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.genderLabel.setObjectName("genderLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.genderLabel)
        self.genderComboBox = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.genderComboBox.setObjectName("genderComboBox")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.genderComboBox)
        self.casteLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.casteLabel.setObjectName("casteLabel")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.casteLabel)
        self.casteLineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.casteLineEdit.setObjectName("casteLineEdit")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.casteLineEdit)
        self.birthTypeLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.birthTypeLabel.setObjectName("birthTypeLabel")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.birthTypeLabel)
        self.birthTypeComboBox = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.birthTypeComboBox.setObjectName("birthTypeComboBox")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.birthTypeComboBox)
        self.physicalDisabledLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.physicalDisabledLabel.setObjectName("physicalDisabledLabel")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.physicalDisabledLabel)
        self.physicalDisabledLineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.physicalDisabledLineEdit.setObjectName("physicalDisabledLineEdit")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.physicalDisabledLineEdit)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_6 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_6.setObjectName("label_6")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.districtLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.districtLabel.setObjectName("districtLabel")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.districtLabel)
        self.districtLineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.districtLineEdit.setObjectName("districtLineEdit")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.districtLineEdit)
        self.MunicipalityLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.MunicipalityLabel.setObjectName("MunicipalityLabel")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.MunicipalityLabel)
        self.MunicipalityLineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.MunicipalityLineEdit.setObjectName("MunicipalityLineEdit")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.MunicipalityLineEdit)
        self.wardNoLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.wardNoLabel.setObjectName("wardNoLabel")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.wardNoLabel)
        self.wardNoLineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.wardNoLineEdit.setObjectName("wardNoLineEdit")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.wardNoLineEdit)
        self.countryIfBornInForeignLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.countryIfBornInForeignLabel.setObjectName("countryIfBornInForeignLabel")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.countryIfBornInForeignLabel)
        self.countryIfBornInForeignLineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.countryIfBornInForeignLineEdit.setObjectName("countryIfBornInForeignLineEdit")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.countryIfBornInForeignLineEdit)
        self.formLayout.setLayout(7, QtWidgets.QFormLayout.SpanningRole, self.formLayout_2)
        self.gridLayout_2.addLayout(self.formLayout, 2, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 5, 0, 1, 1)
        self.formLayout_9 = QtWidgets.QFormLayout()
        self.formLayout_9.setObjectName("formLayout_9")
        self.birthRegistrationNoLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.birthRegistrationNoLabel.setObjectName("birthRegistrationNoLabel")
        self.formLayout_9.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.birthRegistrationNoLabel)
        self.birthRegistrationNoLineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.birthRegistrationNoLineEdit.setObjectName("birthRegistrationNoLineEdit")
        self.formLayout_9.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.birthRegistrationNoLineEdit)
        self.gridLayout_2.addLayout(self.formLayout_9, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.centralwidget)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)
        BirthForm.setCentralWidget(self.centralwidget)

        self.retranslateUi(BirthForm)
        QtCore.QMetaObject.connectSlotsByName(BirthForm)

    def retranslateUi(self, BirthForm):
        _translate = QtCore.QCoreApplication.translate
        BirthForm.setWindowTitle(_translate("BirthForm", "Birth Registration Form"))
        self.grandFatherLabel.setText(_translate("BirthForm", "Grand father "))
        self.label_7.setText(_translate("BirthForm", "<b>Grandfather\'s Details</b>"))
        self.label_5.setText(_translate("BirthForm", "<b>Details Of Newly Born</b>"))
        self.label_2.setText(_translate("BirthForm", "Father\'s Details"))
        self.label_3.setText(_translate("BirthForm", "Mother\'s Details"))
        self.nameLabel_2.setText(_translate("BirthForm", "Name"))
        self.label_4.setText(_translate("BirthForm", "Temporay Adress"))
        self.districtLabel_2.setText(_translate("BirthForm", "District"))
        self.municipalityLabel.setText(_translate("BirthForm", "Municipality"))
        self.wardNoLabel_2.setText(_translate("BirthForm", "Ward No"))
        self.roadLabel.setText(_translate("BirthForm", "Road/Route"))
        self.communityLabel.setText(_translate("BirthForm", "Community"))
        self.houseNoLabel.setText(_translate("BirthForm", "House No"))
        self.ageAtBirthLabel.setText(_translate("BirthForm", "Age At Birth"))
        self.motherlandLabel.setText(_translate("BirthForm", "Motherland"))
        self.countryWithCitizenshipLabel.setText(_translate("BirthForm", "Country With Citizenship"))
        self.citizenshipNoLabel.setText(_translate("BirthForm", "Citizenship No"))
        self.issueDateLabel.setText(_translate("BirthForm", "Issue Date"))
        self.issueAdressLabel.setText(_translate("BirthForm", "Issue Adress"))
        self.citizenshipNoIfForeignLabel.setText(_translate("BirthForm", "Citizenship no(If Foreign)"))
        self.qualificationLabel.setText(_translate("BirthForm", "Qualification"))
        self.occupationLabel.setText(_translate("BirthForm", "Occupation"))
        self.religionLabel.setText(_translate("BirthForm", "Religion"))
        self.motherSTongueLabel.setText(_translate("BirthForm", "Mother\'s Tongue"))
        self.totalChildrenLabel.setText(_translate("BirthForm", "Total children"))
        self.totalChildrenAliveLabel.setText(_translate("BirthForm", "Total Children Alive"))
        self.marriageRegistrationNoLabel.setText(_translate("BirthForm", "Marriage Registration No"))
        self.marriageDateLabel.setText(_translate("BirthForm", "Marriage Date"))
        self.nameLabel.setText(_translate("BirthForm", "Name"))
        self.dateOfBirthLabel.setText(_translate("BirthForm", "Date of birth"))
        self.placeOfBirthLabel.setText(_translate("BirthForm", "Place Of Birth"))
        self.genderLabel.setText(_translate("BirthForm", "Gender"))
        self.casteLabel.setText(_translate("BirthForm", "Caste"))
        self.birthTypeLabel.setText(_translate("BirthForm", "Birth Type"))
        self.physicalDisabledLabel.setText(_translate("BirthForm", "Physical Disabled(if any)"))
        self.label_6.setText(_translate("BirthForm", "Adress Of Newly Born"))
        self.districtLabel.setText(_translate("BirthForm", "District"))
        self.MunicipalityLabel.setText(_translate("BirthForm", "Rural Municipality/Municipality"))
        self.wardNoLabel.setText(_translate("BirthForm", "Ward no"))
        self.countryIfBornInForeignLabel.setText(_translate("BirthForm", "Country(if born in foreign)"))
        self.label_8.setText(_translate("BirthForm", "<b>Details of the parents of new born baby</b>"))
        self.birthRegistrationNoLabel.setText(_translate("BirthForm", "<b>Birth Registration No.</b>"))


class ActualWork():
    def __init__(self):
        import dbconnect
        self.db=dbconnect.database_wardwindow("localhost","root")
        self.BirthForm = QtWidgets.QMainWindow()
        self.ui = Ui_BirthForm()
        self.ui.setupUi(self.BirthForm)
        self.BirthForm.show()
        self.actualWork()

    def actualWork(self):
        self.ui.buttonBox.accepted.connect(self.submitform)
        self.ui.buttonBox.rejected.connect(lambda:self.BirthForm.close())

    def submitform(self):
        self.values=self.getallvalues()
        a=sw_string.generateList(**self.values)
        #a=["RegDate","1","RegNo","2","C","3","D","4","E","5"]
        #b=['RegNo','123-32','detailsofmarriage', "('Social Tradition', ('2000-01-01', '2056/09/17'))", 'locationofmarriage', "('Kavre', 'Namobudda', '04', 'Timal Road', 'Methinkot', '45', '')", 'detailsofspouse', "{'detailsofbride': ('Tandon', 'Rabina', '2057/01/05', 'Kami', '+2', 'Actress', 'Divorcee', ('Rampur', 'Narayanghat', '5', 'Ghandi Street', 'Hariharpur', '78', 'India'), ('India', '27-12398721', '2071/06/09', 'Rampur', '87289398', 'India', 'New Delhi'), ('Fariha Tandon', 'Kanod Tandon', 'Kajol Tandon')), 'detailsofbridegroom': ('Ghimere', 'Tilak', '2051/03/21', 'Brahmin', 'B.Sc.', 'Astrologer', 'Single', ('Solukhumbu', 'Namche Bazar', '9', 'Manila Street', 'Vaisepati', '567', 'Nepal'), ('Nepal', '983-3468', '2067/03/05', 'Solukhumbu', '', '', ''), ('Goshnath Ghimere', 'Farilal Ghimere', 'Nabina Ghimere'))}"]
        #a=['RegDate',,b[0],b[1],b[2],b[3].replace("'","__"),b[4],b[5].replace("'","__"),b[6],b[7].replace("'","__")]
        #print(a)
        self.db.createFormTable(table)
        self.db.addColumns(table,a[4],a[6],a[8])
        self.db.insertValues(table,a)

    def getallvalues(self):
        '''
        self.magRegNo=self.ui.marriageRegistrationNoLineEdit.text()
        self.marriagetype=self.ui.marriageTypeComboBox.currentText()
        date=QDate(self.ui.dateEdit_2.date())
        year,month,day=date.getDate()
        marriage_in_ad=datetime.date(year,month,day)
        marriage_in_bs=nepali_date.NepaliDate.to_nepali_date(marriage_in_ad)
        today=nepali_date.NepaliDate.today()
        registrationdate=str(today)[3:]
        self.marriagedate=(str(marriage_in_ad),str(marriage_in_bs)[3:])
        detailsofmarriage=(self.marriagetype,self.marriagedate)
        locationofmarriage=(self.ui.districtLineEdit.text(),self.ui.municipalityLineEdit.text(),self.ui.wardNoLineEdit.text(),self.ui.roadStreetLineEdit.text(),self.ui.villageLineEdit.text(),self.ui.houseNoLineEdit.text(),self.ui.locationIfMarriageAbroadLineEdit.text())

        self.paddressbride=(self.ui.lineEdit_18.text(),self.ui.lineEdit_20.text(),self.ui.lineEdit_21.text(),self.ui.lineEdit_24.text(),self.ui.lineEdit_26.text(),self.ui.lineEdit_28.text(),self.ui.lineEdit_30.text())
        self.ccbride=(self.ui.lineEdit_32.text(),self.ui.lineEdit_34.text(),self.ui.lineEdit_36.text(),self.ui.lineEdit_38.text(),self.ui.lineEdit_40.text(),self.ui.lineEdit_42.text(),self.ui.lineEdit_44.text())
        self.parentbride=(self.ui.lineEdit_46.text(),self.ui.lineEdit_48.text(),self.ui.lineEdit_50.text())
        self.detailsofbride=(self.ui.lineEdit_4.text(),self.ui.lineEdit_6.text(),self.ui.lineEdit_8.text(),self.ui.lineEdit_10.text(),self.ui.lineEdit_12.text(),self.ui.lineEdit_14.text(),self.ui.lineEdit_16.text(),self.paddressbride,self.ccbride,self.parentbride)

        self.paddressbridegroom=(self.ui.lineEdit_17.text(),self.ui.lineEdit_19.text(),self.ui.lineEdit_22.text(),self.ui.lineEdit_23.text(),self.ui.lineEdit_25.text(),self.ui.lineEdit_27.text(),self.ui.lineEdit_29.text())
        self.ccbridegroom=(self.ui.lineEdit_31.text(),self.ui.lineEdit_33.text(),self.ui.lineEdit_35.text(),self.ui.lineEdit_37.text(),self.ui.lineEdit_39.text(),self.ui.lineEdit_41.text(),self.ui.lineEdit_43.text())
        self.parentbridegroom=(self.ui.lineEdit_45.text(),self.ui.lineEdit_47.text(),self.ui.lineEdit_49.text())
        self.detailsofbridegroom=(self.ui.lineEdit_3.text(),self.ui.lineEdit_5.text(),self.ui.lineEdit_7.text(),self.ui.lineEdit_9.text(),self.ui.lineEdit_11.text(),self.ui.lineEdit_13.text(),self.ui.lineEdit_15.text(),self.paddressbridegroom,self.ccbridegroom,self.parentbridegroom)
        detailsofspouse={'detailsofbride':self.detailsofbride, 'detailsofbridegroom':self.detailsofbridegroom}

        return {"RegDate":registrationdate,"RegNo":self.magRegNo,"detailsofmarriage":str(detailsofmarriage) , "locationofmarriage":str(locationofmarriage) , 'detailsofspouse':str(detailsofspouse)}
        '''
        pass
    def closeActualWork(self):
        self.BirthForm.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    aw=ActualWork()
    """
    MainWindow = QtWidgets.QMainWindow()
    ui = ActualWork()
    ui.setupUi(MainWindow)
    MainWindow.show()
    """
    sys.exit(app.exec_())

