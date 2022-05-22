# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Confirmation_suppresion_client2.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_ConfirmerDelWindow(object):
    def setupUi(self, ConfirmerDelWindow):
        if not ConfirmerDelWindow.objectName():
            ConfirmerDelWindow.setObjectName(u"ConfirmerDelWindow")
        ConfirmerDelWindow.resize(800, 600)
        self.menuDel = QAction(ConfirmerDelWindow)
        self.menuDel.setObjectName(u"menuDel")
        self.centralwidget = QWidget(ConfirmerDelWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.CreationClient = QFrame(self.centralwidget)
        self.CreationClient.setObjectName(u"CreationClient")
        self.CreationClient.setGeometry(QRect(120, 100, 351, 261))
        self.CreationClient.setFrameShape(QFrame.StyledPanel)
        self.CreationClient.setFrameShadow(QFrame.Raised)
        self.confirmDelOk = QPushButton(self.CreationClient)
        self.confirmDelOk.setObjectName(u"confirmDelOk")
        self.confirmDelOk.setGeometry(QRect(40, 150, 93, 29))
        self.confirmDelCancel = QPushButton(self.CreationClient)
        self.confirmDelCancel.setObjectName(u"confirmDelCancel")
        self.confirmDelCancel.setGeometry(QRect(150, 150, 93, 29))
        self.label_3 = QLabel(self.CreationClient)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(0, 70, 63, 20))
        self.confirmDelCourriel = QLabel(self.CreationClient)
        self.confirmDelCourriel.setObjectName(u"confirmDelCourriel")
        self.confirmDelCourriel.setGeometry(QRect(50, 70, 63, 20))
        self.label_7 = QLabel(self.CreationClient)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(0, 40, 63, 20))
        self.confirmDelPrenom = QLabel(self.CreationClient)
        self.confirmDelPrenom.setObjectName(u"confirmDelPrenom")
        self.confirmDelPrenom.setGeometry(QRect(50, 40, 63, 20))
        self.label_9 = QLabel(self.CreationClient)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(0, 10, 63, 20))
        self.confirmDelNom = QLabel(self.CreationClient)
        self.confirmDelNom.setObjectName(u"confirmDelNom")
        self.confirmDelNom.setGeometry(QRect(50, 10, 63, 20))
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(190, 50, 221, 20))
        ConfirmerDelWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(ConfirmerDelWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        self.menuMenu = QMenu(self.menubar)
        self.menuMenu.setObjectName(u"menuMenu")
        ConfirmerDelWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(ConfirmerDelWindow)
        self.statusbar.setObjectName(u"statusbar")
        ConfirmerDelWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuMenu.menuAction())
        self.menuMenu.addAction(self.menuDel)

        self.retranslateUi(ConfirmerDelWindow)

        QMetaObject.connectSlotsByName(ConfirmerDelWindow)
    # setupUi

    def retranslateUi(self, ConfirmerDelWindow):
        ConfirmerDelWindow.setWindowTitle(QCoreApplication.translate("ConfirmerDelWindow", u"MainWindow", None))
        self.menuDel.setText(QCoreApplication.translate("ConfirmerDelWindow", u"Se deconecter", None))
        self.confirmDelOk.setText(QCoreApplication.translate("ConfirmerDelWindow", u"Supprimer", None))
        self.confirmDelCancel.setText(QCoreApplication.translate("ConfirmerDelWindow", u"Annuler", None))
        self.label_3.setText(QCoreApplication.translate("ConfirmerDelWindow", u"Courriel:", None))
        self.confirmDelCourriel.setText(QCoreApplication.translate("ConfirmerDelWindow", u"TextLabel", None))
        self.label_7.setText(QCoreApplication.translate("ConfirmerDelWindow", u"Prenom", None))
        self.confirmDelPrenom.setText(QCoreApplication.translate("ConfirmerDelWindow", u"TextLabel", None))
        self.label_9.setText(QCoreApplication.translate("ConfirmerDelWindow", u"Nom", None))
        self.confirmDelNom.setText(QCoreApplication.translate("ConfirmerDelWindow", u"TextLabel", None))
        self.label_5.setText(QCoreApplication.translate("ConfirmerDelWindow", u"Vous etes sur de supprimer le client", None))
        self.menuMenu.setTitle(QCoreApplication.translate("ConfirmerDelWindow", u"Menu", None))
    # retranslateUi

