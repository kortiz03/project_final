# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Creation_Client2.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_CreateClientWindow(object):
    def setupUi(self, CreateClientWindow):
        if not CreateClientWindow.objectName():
            CreateClientWindow.setObjectName(u"CreateClientWindow")
        CreateClientWindow.resize(800, 600)
        self.createDecon = QAction(CreateClientWindow)
        self.createDecon.setObjectName(u"createDecon")
        self.centralwidget = QWidget(CreateClientWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.CreationClient = QFrame(self.centralwidget)
        self.CreationClient.setObjectName(u"CreationClient")
        self.CreationClient.setGeometry(QRect(190, 130, 391, 311))
        self.CreationClient.setFrameShape(QFrame.StyledPanel)
        self.CreationClient.setFrameShadow(QFrame.Raised)
        self.layoutWidget_5 = QWidget(self.CreationClient)
        self.layoutWidget_5.setObjectName(u"layoutWidget_5")
        self.layoutWidget_5.setGeometry(QRect(0, 160, 331, 24))
        self.horizontalLayout_5 = QHBoxLayout(self.layoutWidget_5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.layoutWidget_5)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_5.addWidget(self.label_6)

        self.createPasswordVerify = QLineEdit(self.layoutWidget_5)
        self.createPasswordVerify.setObjectName(u"createPasswordVerify")
        self.createPasswordVerify.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_5.addWidget(self.createPasswordVerify)

        self.layoutWidget_6 = QWidget(self.CreationClient)
        self.layoutWidget_6.setObjectName(u"layoutWidget_6")
        self.layoutWidget_6.setGeometry(QRect(0, 130, 331, 24))
        self.horizontalLayout_6 = QHBoxLayout(self.layoutWidget_6)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.layoutWidget_6)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_6.addWidget(self.label_7)

        self.createPassword = QLineEdit(self.layoutWidget_6)
        self.createPassword.setObjectName(u"createPassword")
        self.createPassword.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_6.addWidget(self.createPassword)

        self.layoutWidget_7 = QWidget(self.CreationClient)
        self.layoutWidget_7.setObjectName(u"layoutWidget_7")
        self.layoutWidget_7.setGeometry(QRect(0, 100, 331, 24))
        self.horizontalLayout_7 = QHBoxLayout(self.layoutWidget_7)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.layoutWidget_7)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_7.addWidget(self.label_8)

        self.createCourriel = QLineEdit(self.layoutWidget_7)
        self.createCourriel.setObjectName(u"createCourriel")
        self.createCourriel.setEchoMode(QLineEdit.Normal)

        self.horizontalLayout_7.addWidget(self.createCourriel)

        self.layoutWidget_8 = QWidget(self.CreationClient)
        self.layoutWidget_8.setObjectName(u"layoutWidget_8")
        self.layoutWidget_8.setGeometry(QRect(0, 70, 331, 24))
        self.horizontalLayout_8 = QHBoxLayout(self.layoutWidget_8)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_9 = QLabel(self.layoutWidget_8)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_8.addWidget(self.label_9)

        self.createPrenom = QLineEdit(self.layoutWidget_8)
        self.createPrenom.setObjectName(u"createPrenom")
        self.createPrenom.setEchoMode(QLineEdit.Normal)

        self.horizontalLayout_8.addWidget(self.createPrenom)

        self.layoutWidget_9 = QWidget(self.CreationClient)
        self.layoutWidget_9.setObjectName(u"layoutWidget_9")
        self.layoutWidget_9.setGeometry(QRect(0, 40, 331, 24))
        self.horizontalLayout_9 = QHBoxLayout(self.layoutWidget_9)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.label_10 = QLabel(self.layoutWidget_9)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_9.addWidget(self.label_10)

        self.createNom = QLineEdit(self.layoutWidget_9)
        self.createNom.setObjectName(u"createNom")
        self.createNom.setEchoMode(QLineEdit.Normal)

        self.horizontalLayout_9.addWidget(self.createNom)

        self.layoutWidget_10 = QWidget(self.CreationClient)
        self.layoutWidget_10.setObjectName(u"layoutWidget_10")
        self.layoutWidget_10.setGeometry(QRect(0, 10, 331, 24))
        self.horizontalLayout_10 = QHBoxLayout(self.layoutWidget_10)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.label_11 = QLabel(self.layoutWidget_10)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_10.addWidget(self.label_11)

        self.createUsager = QLineEdit(self.layoutWidget_10)
        self.createUsager.setObjectName(u"createUsager")
        self.createUsager.setEchoMode(QLineEdit.Normal)

        self.horizontalLayout_10.addWidget(self.createUsager)

        self.widget = QWidget(self.CreationClient)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(90, 190, 165, 24))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.type_lbl = QLabel(self.widget)
        self.type_lbl.setObjectName(u"type_lbl")

        self.horizontalLayout.addWidget(self.type_lbl)

        self.createType = QComboBox(self.widget)
        self.createType.addItem("")
        self.createType.addItem("")
        self.createType.setObjectName(u"createType")

        self.horizontalLayout.addWidget(self.createType)

        self.widget1 = QWidget(self.CreationClient)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(90, 250, 158, 26))
        self.horizontalLayout_2 = QHBoxLayout(self.widget1)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.createOk = QPushButton(self.widget1)
        self.createOk.setObjectName(u"createOk")

        self.horizontalLayout_2.addWidget(self.createOk)

        self.createCancel = QPushButton(self.widget1)
        self.createCancel.setObjectName(u"createCancel")

        self.horizontalLayout_2.addWidget(self.createCancel)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(310, 80, 91, 20))
        self.createInfo = QLabel(self.centralwidget)
        self.createInfo.setObjectName(u"createInfo")
        self.createInfo.setGeometry(QRect(190, 110, 331, 20))
        self.createInfo.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        CreateClientWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(CreateClientWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        self.menuMenu = QMenu(self.menubar)
        self.menuMenu.setObjectName(u"menuMenu")
        CreateClientWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(CreateClientWindow)
        self.statusbar.setObjectName(u"statusbar")
        CreateClientWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuMenu.menuAction())
        self.menuMenu.addAction(self.createDecon)

        self.retranslateUi(CreateClientWindow)

        QMetaObject.connectSlotsByName(CreateClientWindow)
    # setupUi

    def retranslateUi(self, CreateClientWindow):
        CreateClientWindow.setWindowTitle(QCoreApplication.translate("CreateClientWindow", u"MainWindow", None))
        self.createDecon.setText(QCoreApplication.translate("CreateClientWindow", u"Se deconecter", None))
        self.label_6.setText(QCoreApplication.translate("CreateClientWindow", u"Ecrire a nouveau votre mot de passe", None))
        self.label_7.setText(QCoreApplication.translate("CreateClientWindow", u"Ecrire votre mot de passe", None))
        self.label_8.setText(QCoreApplication.translate("CreateClientWindow", u"Courriel", None))
        self.label_9.setText(QCoreApplication.translate("CreateClientWindow", u"Prenom", None))
        self.label_10.setText(QCoreApplication.translate("CreateClientWindow", u"Nom", None))
        self.label_11.setText(QCoreApplication.translate("CreateClientWindow", u"Usager", None))
        self.type_lbl.setText(QCoreApplication.translate("CreateClientWindow", u"Type Acc\u00e8s", None))
        self.createType.setItemText(0, QCoreApplication.translate("CreateClientWindow", u"Acc\u00e8s Lecture", None))
        self.createType.setItemText(1, QCoreApplication.translate("CreateClientWindow", u"Acc\u00e8s Total", None))

        self.createOk.setText(QCoreApplication.translate("CreateClientWindow", u"Ajouter", None))
        self.createCancel.setText(QCoreApplication.translate("CreateClientWindow", u"Annuler", None))
        self.label_5.setText(QCoreApplication.translate("CreateClientWindow", u"Creation Client", None))
        self.createInfo.setText("")
        self.menuMenu.setTitle(QCoreApplication.translate("CreateClientWindow", u"Menu", None))
    # retranslateUi

