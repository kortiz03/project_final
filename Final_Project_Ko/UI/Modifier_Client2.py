# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Modifier_Client2.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_CreationWindow(object):
    def setupUi(self, CreationWindow):
        if not CreationWindow.objectName():
            CreationWindow.setObjectName(u"CreationWindow")
        CreationWindow.resize(800, 600)
        self.menuCreation = QAction(CreationWindow)
        self.menuCreation.setObjectName(u"menuCreation")
        self.centralwidget = QWidget(CreationWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.CreationClient = QFrame(self.centralwidget)
        self.CreationClient.setObjectName(u"CreationClient")
        self.CreationClient.setGeometry(QRect(110, 120, 351, 261))
        self.CreationClient.setFrameShape(QFrame.StyledPanel)
        self.CreationClient.setFrameShadow(QFrame.Raised)
        self.layoutWidget = QWidget(self.CreationClient)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 100, 273, 24))
        self.horizontalLayout_4 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_4.addWidget(self.label_4)

        self.modifierPassword = QLineEdit(self.layoutWidget)
        self.modifierPassword.setObjectName(u"modifierPassword")

        self.horizontalLayout_4.addWidget(self.modifierPassword)

        self.layoutWidget_2 = QWidget(self.CreationClient)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(0, 70, 183, 24))
        self.horizontalLayout_3 = QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.layoutWidget_2)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.modifierCourriel = QLineEdit(self.layoutWidget_2)
        self.modifierCourriel.setObjectName(u"modifierCourriel")

        self.horizontalLayout_3.addWidget(self.modifierCourriel)

        self.layoutWidget_3 = QWidget(self.CreationClient)
        self.layoutWidget_3.setObjectName(u"layoutWidget_3")
        self.layoutWidget_3.setGeometry(QRect(0, 10, 168, 24))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget_3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.layoutWidget_3)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.modifierNom = QLineEdit(self.layoutWidget_3)
        self.modifierNom.setObjectName(u"modifierNom")

        self.horizontalLayout.addWidget(self.modifierNom)

        self.layoutWidget_4 = QWidget(self.CreationClient)
        self.layoutWidget_4.setObjectName(u"layoutWidget_4")
        self.layoutWidget_4.setGeometry(QRect(0, 40, 183, 24))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget_4)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.layoutWidget_4)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.modifierPrenom = QLineEdit(self.layoutWidget_4)
        self.modifierPrenom.setObjectName(u"modifierPrenom")

        self.horizontalLayout_2.addWidget(self.modifierPrenom)

        self.modifierOk = QPushButton(self.CreationClient)
        self.modifierOk.setObjectName(u"modifierOk")
        self.modifierOk.setGeometry(QRect(40, 170, 93, 29))
        self.modifierCancel = QPushButton(self.CreationClient)
        self.modifierCancel.setObjectName(u"modifierCancel")
        self.modifierCancel.setGeometry(QRect(150, 170, 93, 29))
        self.layoutWidget_5 = QWidget(self.CreationClient)
        self.layoutWidget_5.setObjectName(u"layoutWidget_5")
        self.layoutWidget_5.setGeometry(QRect(0, 130, 331, 24))
        self.horizontalLayout_5 = QHBoxLayout(self.layoutWidget_5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.layoutWidget_5)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_5.addWidget(self.label_6)

        self.modifierPasswordVerify = QLineEdit(self.layoutWidget_5)
        self.modifierPasswordVerify.setObjectName(u"modifierPasswordVerify")

        self.horizontalLayout_5.addWidget(self.modifierPasswordVerify)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(200, 70, 111, 20))
        CreationWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(CreationWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        self.menuMenu = QMenu(self.menubar)
        self.menuMenu.setObjectName(u"menuMenu")
        CreationWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(CreationWindow)
        self.statusbar.setObjectName(u"statusbar")
        CreationWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuMenu.menuAction())
        self.menuMenu.addAction(self.menuCreation)

        self.retranslateUi(CreationWindow)

        QMetaObject.connectSlotsByName(CreationWindow)
    # setupUi

    def retranslateUi(self, CreationWindow):
        CreationWindow.setWindowTitle(QCoreApplication.translate("CreationWindow", u"MainWindow", None))
        self.menuCreation.setText(QCoreApplication.translate("CreationWindow", u"Se deconecter", None))
        self.label_4.setText(QCoreApplication.translate("CreationWindow", u"Tapez votre mot de passe", None))
        self.label_3.setText(QCoreApplication.translate("CreationWindow", u"Courriel", None))
        self.label.setText(QCoreApplication.translate("CreationWindow", u"Nom", None))
        self.label_2.setText(QCoreApplication.translate("CreationWindow", u"Prenom", None))
        self.modifierOk.setText(QCoreApplication.translate("CreationWindow", u"Modifier", None))
        self.modifierCancel.setText(QCoreApplication.translate("CreationWindow", u"Annuler", None))
        self.label_6.setText(QCoreApplication.translate("CreationWindow", u"Ecrire a nouveau votre mot de passe", None))
        self.label_5.setText(QCoreApplication.translate("CreationWindow", u"Modifier Client", None))
        self.menuMenu.setTitle(QCoreApplication.translate("CreationWindow", u"Menu", None))
    # retranslateUi

