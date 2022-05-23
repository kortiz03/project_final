# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'principal.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1313, 622)
        self.mainDecon = QAction(MainWindow)
        self.mainDecon.setObjectName(u"mainDecon")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 270, 441, 281))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.mainListeUser = QTreeWidget(self.frame)
        QTreeWidgetItem(self.mainListeUser)
        self.mainListeUser.setObjectName(u"mainListeUser")
        self.mainListeUser.setGeometry(QRect(10, 20, 431, 192))
        self.mainUserAdd = QPushButton(self.frame)
        self.mainUserAdd.setObjectName(u"mainUserAdd")
        self.mainUserAdd.setGeometry(QRect(40, 250, 51, 29))
        self.mainUserMod = QPushButton(self.frame)
        self.mainUserMod.setObjectName(u"mainUserMod")
        self.mainUserMod.setGeometry(QRect(110, 250, 61, 29))
        self.mainUserDel = QPushButton(self.frame)
        self.mainUserDel.setObjectName(u"mainUserDel")
        self.mainUserDel.setGeometry(QRect(200, 250, 91, 29))
        self.mainInfo = QLabel(self.frame)
        self.mainInfo.setObjectName(u"mainInfo")
        self.mainInfo.setGeometry(QRect(18, 220, 411, 20))
        self.mainInfo.setAlignment(Qt.AlignCenter)
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(470, 280, 401, 221))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.mainListeFIlms = QTreeWidget(self.frame_2)
        QTreeWidgetItem(self.mainListeFIlms)
        self.mainListeFIlms.setObjectName(u"mainListeFIlms")
        self.mainListeFIlms.setGeometry(QRect(10, 10, 401, 192))
        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(900, 260, 411, 231))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.mainListeFilmsCat = QTreeWidget(self.frame_3)
        QTreeWidgetItem(self.mainListeFilmsCat)
        self.mainListeFilmsCat.setObjectName(u"mainListeFilmsCat")
        self.mainListeFilmsCat.setGeometry(QRect(0, 30, 401, 191))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(950, 60, 191, 191))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(510, 80, 311, 171))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(110, 60, 241, 211))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1313, 22))
        self.menuMenu = QMenu(self.menubar)
        self.menuMenu.setObjectName(u"menuMenu")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuMenu.menuAction())
        self.menuMenu.addAction(self.mainDecon)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.mainDecon.setText(QCoreApplication.translate("MainWindow", u"Se deconecter", None))
#if QT_CONFIG(tooltip)
        self.mainDecon.setToolTip(QCoreApplication.translate("MainWindow", u"Se deconecter", None))
#endif // QT_CONFIG(tooltip)
        ___qtreewidgetitem = self.mainListeUser.headerItem()
        ___qtreewidgetitem.setText(4, QCoreApplication.translate("MainWindow", u"Type d'Access", None));
        ___qtreewidgetitem.setText(3, QCoreApplication.translate("MainWindow", u"Courriel", None));
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("MainWindow", u"Prenom", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("MainWindow", u"Nom", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", u"usager", None));

        __sortingEnabled = self.mainListeUser.isSortingEnabled()
        self.mainListeUser.setSortingEnabled(False)
        ___qtreewidgetitem1 = self.mainListeUser.topLevelItem(0)
        ___qtreewidgetitem1.setText(3, QCoreApplication.translate("MainWindow", u"Kortiz1522@limoilou.local", None));
        ___qtreewidgetitem1.setText(2, QCoreApplication.translate("MainWindow", u"Kellin", None));
        ___qtreewidgetitem1.setText(1, QCoreApplication.translate("MainWindow", u"Ortiz", None));
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("MainWindow", u"kortiz", None));
        self.mainListeUser.setSortingEnabled(__sortingEnabled)

        self.mainUserAdd.setText(QCoreApplication.translate("MainWindow", u"Ajouter", None))
        self.mainUserMod.setText(QCoreApplication.translate("MainWindow", u"Modifier", None))
        self.mainUserDel.setText(QCoreApplication.translate("MainWindow", u"Supprimer", None))
        self.mainInfo.setText("")
        ___qtreewidgetitem2 = self.mainListeFIlms.headerItem()
        ___qtreewidgetitem2.setText(2, QCoreApplication.translate("MainWindow", u"Categorie Film", None));
        ___qtreewidgetitem2.setText(1, QCoreApplication.translate("MainWindow", u"Dur\u00e9e Film", None));
        ___qtreewidgetitem2.setText(0, QCoreApplication.translate("MainWindow", u" Nom Film", None));

        __sortingEnabled1 = self.mainListeFIlms.isSortingEnabled()
        self.mainListeFIlms.setSortingEnabled(False)
        ___qtreewidgetitem3 = self.mainListeFIlms.topLevelItem(0)
        ___qtreewidgetitem3.setText(2, QCoreApplication.translate("MainWindow", u"Fiction", None));
        ___qtreewidgetitem3.setText(1, QCoreApplication.translate("MainWindow", u"2:30", None));
        ___qtreewidgetitem3.setText(0, QCoreApplication.translate("MainWindow", u"Avatar", None));
        self.mainListeFIlms.setSortingEnabled(__sortingEnabled1)

        ___qtreewidgetitem4 = self.mainListeFilmsCat.headerItem()
        ___qtreewidgetitem4.setText(2, QCoreApplication.translate("MainWindow", u"Categorie Film", None));
        ___qtreewidgetitem4.setText(1, QCoreApplication.translate("MainWindow", u"Nom Acteur", None));
        ___qtreewidgetitem4.setText(0, QCoreApplication.translate("MainWindow", u" Nom Film", None));

        __sortingEnabled2 = self.mainListeFilmsCat.isSortingEnabled()
        self.mainListeFilmsCat.setSortingEnabled(False)
        ___qtreewidgetitem5 = self.mainListeFilmsCat.topLevelItem(0)
        ___qtreewidgetitem5.setText(2, QCoreApplication.translate("MainWindow", u"Animation", None));
        ___qtreewidgetitem5.setText(1, QCoreApplication.translate("MainWindow", u"Mirabel", None));
        ___qtreewidgetitem5.setText(0, QCoreApplication.translate("MainWindow", u"Encanto", None));
        self.mainListeFilmsCat.setSortingEnabled(__sortingEnabled2)

        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><img src=\":/images/users-principal.jpg\"/></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><img src=\":/images/films-principal.jpg\"/></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><img src=\":/images/actors-principal.jpg\"/></p></body></html>", None))
        self.menuMenu.setTitle(QCoreApplication.translate("MainWindow", u"Menu", None))
    # retranslateUi

