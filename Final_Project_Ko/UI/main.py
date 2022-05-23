# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_LoginWindow(object):
    def setupUi(self, LoginWindow):
        if not LoginWindow.objectName():
            LoginWindow.setObjectName(u"LoginWindow")
        LoginWindow.resize(800, 441)
        self.loginDecon = QAction(LoginWindow)
        self.loginDecon.setObjectName(u"loginDecon")
        self.centralwidget = QWidget(LoginWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(170, 50, 561, 281))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.loginOk = QPushButton(self.frame)
        self.loginOk.setObjectName(u"loginOk")
        self.loginOk.setGeometry(QRect(110, 220, 93, 29))
        self.loginCancel = QPushButton(self.frame)
        self.loginCancel.setObjectName(u"loginCancel")
        self.loginCancel.setGeometry(QRect(230, 220, 93, 29))
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(380, 10, 161, 221))
        self.layoutWidget = QWidget(self.frame)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(130, 90, 225, 24))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.loginUser = QLineEdit(self.layoutWidget)
        self.loginUser.setObjectName(u"loginUser")

        self.horizontalLayout.addWidget(self.loginUser)

        self.layoutWidget1 = QWidget(self.frame)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(130, 130, 191, 24))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.layoutWidget1)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.loginPassword = QLineEdit(self.layoutWidget1)
        self.loginPassword.setObjectName(u"loginPassword")
        self.loginPassword.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_2.addWidget(self.loginPassword)

        self.layoutWidget2 = QWidget(self.frame)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(130, 170, 165, 24))
        self.horizontalLayout_3 = QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.layoutWidget2)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.loginType = QComboBox(self.layoutWidget2)
        self.loginType.addItem("")
        self.loginType.addItem("")
        self.loginType.setObjectName(u"loginType")

        self.horizontalLayout_3.addWidget(self.loginType)

        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(220, 40, 71, 16))
        self.loginInfo = QLabel(self.frame)
        self.loginInfo.setObjectName(u"loginInfo")
        self.loginInfo.setGeometry(QRect(78, 60, 301, 20))
        LoginWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(LoginWindow)
        self.statusbar.setObjectName(u"statusbar")
        LoginWindow.setStatusBar(self.statusbar)
        self.menubar = QMenuBar(LoginWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        self.menuMenu = QMenu(self.menubar)
        self.menuMenu.setObjectName(u"menuMenu")
        self.menuView = QMenu(self.menubar)
        self.menuView.setObjectName(u"menuView")
        LoginWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuMenu.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menuMenu.addAction(self.loginDecon)
        self.menuMenu.addSeparator()

        self.retranslateUi(LoginWindow)
        self.loginCancel.clicked.connect(self.loginPassword.clear)
        self.loginCancel.clicked.connect(self.loginUser.clear)
        self.loginCancel.clicked.connect(self.loginInfo.clear)

        QMetaObject.connectSlotsByName(LoginWindow)
    # setupUi

    def retranslateUi(self, LoginWindow):
        LoginWindow.setWindowTitle(QCoreApplication.translate("LoginWindow", u"MainWindow", None))
        self.loginDecon.setText(QCoreApplication.translate("LoginWindow", u"Quitter", None))
#if QT_CONFIG(tooltip)
        self.loginDecon.setToolTip(QCoreApplication.translate("LoginWindow", u"Quitter", None))
#endif // QT_CONFIG(tooltip)
        self.loginOk.setText(QCoreApplication.translate("LoginWindow", u"Ok", None))
        self.loginCancel.setText(QCoreApplication.translate("LoginWindow", u"Effacer", None))
        self.label_4.setText(QCoreApplication.translate("LoginWindow", u"<html><head/><body><p><img src=\":/images/icone.jpg\"/></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("LoginWindow", u"Code Utilisateur", None))
        self.label_2.setText(QCoreApplication.translate("LoginWindow", u"Password", None))
        self.label_3.setText(QCoreApplication.translate("LoginWindow", u"Type Acc\u00e8s", None))
        self.loginType.setItemText(0, QCoreApplication.translate("LoginWindow", u"Acc\u00e8s Lecture", None))
        self.loginType.setItemText(1, QCoreApplication.translate("LoginWindow", u"Acc\u00e8s Total", None))

        self.label_5.setText(QCoreApplication.translate("LoginWindow", u"Projet Final", None))
        self.loginInfo.setText("")
        self.menuMenu.setTitle(QCoreApplication.translate("LoginWindow", u"Menu", None))
        self.menuView.setTitle(QCoreApplication.translate("LoginWindow", u"View", None))
    # retranslateUi

