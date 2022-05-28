##Appel des librairies que j'utilise pour executer mes fênetres

import sys
import json
import PySide2.QtWidgets as qtw
import PySide2.QtCore as qtw_core
from UI.main import Ui_LoginWindow as UI_login
from UI.Creation_Client2 import Ui_CreateClientWindow as UI_UserAdd
from UI.Modifier_Client2 import Ui_CreationWindow as UI_UserMod
from UI.Confirmation_suppresion_client2 import Ui_ConfirmerDelWindow as UI_UserDel
from UI.principal import Ui_MainWindow
import images.image_users


class Usager():
    ## initializacion des variables
    def __init__(self, username):
        self.username = username
        self.nom = None
        self.prenom = None
        self.password = None
        self.courriel = None
        self.acces_type = None
        self.user_exist = False

    ##validation d'usager avec le dictionnaire ou les informations d'usagers sont enregistrées
    def get_user(self):
        try:
            with open("usager.json", 'r', encoding='utf-8') as f:
                usager_dict = json.load(f)
            self.password = usager_dict[self.username]['password']
            self.nom = usager_dict[self.username]['nom']
            self.prenom = usager_dict[self.username]['prenom']
            self.prenom = usager_dict[self.username]['courriel']
            self.acess_type = usager_dict[self.username]['type']
            self.user_exist = True
        except KeyError:
            self.user_exist = False


class LoginWindow(qtw.QMainWindow, UI_login):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self._user_verified = False
        self.loginOk.clicked.connect(self.load_main_wd)
        self.loginDecon.triggered.connect(sys.exit)
        self.main_window = None
        self.user = None

    def verify_user(self) -> bool:
        usager = self.loginUser.text()
        password = self.loginPassword.text()
        access_type = self.loginType.currentText()
        self.user = Usager(usager)
        self.user.get_user()
        self._user_verified = False
        if self.user.user_exist:
            if password == self.user.password:
                if access_type == self.user.acess_type:
                    self._user_verified = True
        if not self._user_verified:
            self.loginInfo.setText("Le usager, le password ou le type d'access ne sont pas valides")

    def load_main_wd(self):
        self.verify_user()
        if self._user_verified:
            self.main_window = MainWindow(user=self.user)
            self.main_window.show()
            self.close()
## création classe MainWindow lequel a une fonction init qui amene les informations de parent
## fonction show que a une if pour verifier l'accées du usager, en cas que soit accées lecture
## user accées type lecture donc mettre les buttons invisible

class MainWindow(qtw.QMainWindow, Ui_MainWindow):
    def __init__(self, user, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.user = user
        self.mainUserAdd.clicked.connect(self.load_add_user_wd)
        self.mainUserMod.clicked.connect(self.load_mod_user_wd)
        self.mainUserDel.clicked.connect(self.load_del_user_wd)
        self.mainDecon.triggered.connect(self.deconnecter)
        self.user_add_wd = None
        self.user_mod_wd = None
        self.user_del_wd = None
        self.login_wd = None

    def deconnecter(self):
        self.login_wd = LoginWindow()
        self.login_wd.show()
        self.close()


    def show(self):
        self.lister_usagers()
        if self.user.acess_type == "Accès Lecture":
            self.mainUserAdd.setVisible(False)
            self.mainUserMod.setVisible(False)
            self.mainUserDel.setVisible(False)
        qtw.QMainWindow.show(self)
## creation fonction lister_usager pour remplir la liste que va afficher les utilisateurs et ses atributes
## ajout variable toplevelitem lequel ajoterais chaque item dans la liste avec son valeur

    def lister_usagers(self):
        self.mainListeUser.clear()
        with open("usager.json", 'r', encoding='utf-8') as f:
            usager_dict = json.load(f)
        compte_usagers = 0
        for key, values in sorted(usager_dict.items()):
            self.mainListeUser.addTopLevelItem(qtw.QTreeWidgetItem(compte_usagers))
            self.mainListeUser.topLevelItem(compte_usagers).setText(0, key)
            self.mainListeUser.topLevelItem(compte_usagers).setText(1, values['nom'])
            self.mainListeUser.topLevelItem(compte_usagers).setText(2, values['prenom'])
            self.mainListeUser.topLevelItem(compte_usagers).setText(3, values['courriel'])
            self.mainListeUser.topLevelItem(compte_usagers).setText(4, values['type'])
            compte_usagers = compte_usagers + 1

    def load_add_user_wd(self):
        self.user_add_wd = UserAddWindow(self.user)
        self.user_add_wd.show()
        self.close()

    def load_mod_user_wd(self):
        item_choisi = self.mainListeUser.currentItem()
        if item_choisi.isSelected():
            self.user_mod_wd = UserModifyWindow(self.user, item_choisi)
            self.user_mod_wd.show()
            self.close()
        else:
            self.mainInfo.setText("Vous devez choisir l'usager a modifier")

    def load_del_user_wd(self):
        item_choisi = self.mainListeUser.currentItem()
        if item_choisi.isSelected():
            self.user_del_wd = UserDeleteWindow(self.user, item_choisi)
            self.user_del_wd.show()
            self.close()
        else:
            self.mainInfo.setText("Vous devez choisir l'usager a supprimer")


class UserAddWindow(qtw.QMainWindow, UI_UserAdd):
    def __init__(self, user, parent=None):
        super().__init__(parent)
        self.user = user
        self.setupUi(self)
        self.main_window = None
        self.createCancel.clicked.connect(self.cancel_add)
        self.createOk.clicked.connect(self.verifier_formulaire)
        self.createDecon.triggered.connect(self.deconnecter)
        self.login_wd = None

    def deconnecter(self):
        self.login_wd = LoginWindow()
        self.login_wd.show()
        self.close()

    def cancel_add(self):
        self.main_window = MainWindow(user=self.user)
        self.main_window.show()
        self.close()

    def verifier_formulaire(self):
        username = self.createUsager.text()
        courriel = self.createCourriel.text()
        nom = self.createNom.text()
        prenom = self.createPrenom.text()
        password = self.createPassword.text()
        password_verify = self.createPasswordVerify.text()
        user_type = self.createType.currentText()

        if username == "":
            self.createInfo.setText("Vous devez founir un nom d'usager")
        elif courriel == "":
            self.createInfo.setText("Vous devez founir un courriel")
        elif password == "":
            self.createInfo.setText("Vous devez founir un mot de passe")
        elif password != password_verify:
            self.createInfo.setText("les password ne sont pas identiques")
        else:
            user_dict = {
                username:
                    {
                        "nom": nom,
                        "prenom": prenom,
                        "password": password,
                        "courriel": courriel,
                        "type": user_type
                    }
            }
            self.ajouter_usager(user_dict)

    def ajouter_usager(self, user_dict):
        with open("usager.json", 'r', encoding='utf-8') as f:
            usager_dict = json.load(f)
        for key, values in user_dict.items():
            if key not in usager_dict.keys():
                usager_dict[key] = values
                with open("usager.json", 'w', encoding='utf-8') as f:
                    json.dump(usager_dict, f)
                self.main_window = MainWindow(user=self.user)
                self.main_window.show()
                self.close()
            else:
                self.createInfo.setText("le nom de usager existe deja")


class UserModifyWindow(qtw.QMainWindow, UI_UserMod):
    def __init__(self, user, item_choisi, parent=None):
        super().__init__(parent)
        self.user = user
        self.setupUi(self)
        self.main_window = None
        self.item_choisi = item_choisi
        self.modifierUsager.setText(self.item_choisi.text(0))
        self.modifierUsager.setDisabled(True)
        self.modifierNom.setText(self.item_choisi.text(1))
        self.modifierPrenom.setText(self.item_choisi.text(2))
        self.modifierCourriel.setText(self.item_choisi.text(3))
        self.modifierCourriel.setDisabled(True)
        combo_index = self.modifierType.findText(self.item_choisi.text(4), qtw_core.Qt.MatchExactly)
        self.modifierType.setCurrentIndex(combo_index)
        self.modifierCancel.clicked.connect(self.cancel_modifier)
        self.modifierOk.clicked.connect(self.verifier_formulaire)
        self.modifierDecon.triggered.connect(self.deconnecter)
        self.login_wd = None

    def deconnecter(self):
        self.login_wd = LoginWindow()
        self.login_wd.show()
        self.close()

    def cancel_modifier(self):
        self.main_window = MainWindow(user=self.user)
        self.main_window.show()
        self.close()

    def verifier_formulaire(self):
        username = self.modifierUsager.text()
        courriel = self.modifierCourriel.text()
        nom = self.modifierNom.text()
        prenom = self.modifierPrenom.text()
        password = self.modifierPassword.text()
        password_verify = self.modifierPasswordVerify.text()
        user_type = self.modifierType.currentText()

        if password != password_verify:
            self.modifierInfo.setText("les password ne sont pas identiques")
        else:
            user_dict = {
                username:
                    {
                        "nom": nom,
                        "prenom": prenom,
                        "password": password,
                        "courriel": courriel,
                        "type": user_type
                    }
            }
            self.ajouter_usager(user_dict)

    def ajouter_usager(self, user_dict):
        with open("usager.json", 'r', encoding='utf-8') as f:
            usager_dict = json.load(f)
        for key, values in user_dict.items():
            if key in usager_dict.keys():
                if user_dict[key]["password"] == "":
                    values["password"] = usager_dict[key]["password"]
                usager_dict[key] = values
                with open("usager.json", 'w', encoding='utf-8') as f:
                    json.dump(usager_dict, f)
                self.main_window = MainWindow(user=self.user)
                self.main_window.show()
                self.close()
            else:
                self.modifierInfo.setText("le nom de usager n'existe pas")

class UserDeleteWindow(qtw.QMainWindow, UI_UserDel):
    def __init__(self, user, item_choisi, parent=None):
        super().__init__(parent)
        self.user = user
        self.setupUi(self)
        self.main_window = None
        self.item_choisi = item_choisi
        self.confirmDelUsager.setText(self.item_choisi.text(0))
        self.confirmDelNom.setText(self.item_choisi.text(1))
        self.confirmDelPrenom.setText(self.item_choisi.text(2))
        self.confirmDelCourriel.setText(self.item_choisi.text(3))
        self.confirmDelCancel.clicked.connect(self.cancel_del)
        self.confirmDelOk.clicked.connect(self.suprimer_usager)
        self.confirmDecon.triggered.connect(self.deconnecter)
        self.login_wd = None

    def deconnecter(self):
        self.login_wd = LoginWindow()
        self.login_wd.show()
        self.close()

    def cancel_del(self):
        self.main_window = MainWindow(user=self.user)
        self.main_window.show()
        self.close()

    def suprimer_usager(self):
        with open("usager.json", 'r', encoding='utf-8') as f:
            usager_dict = json.load(f)
        usager_dict.pop(self.item_choisi.text(0))
        with open("usager.json", 'w', encoding='utf-8') as f:
            json.dump(usager_dict, f)
        self.main_window = MainWindow(user=self.user)
        self.main_window.show()
        self.close()