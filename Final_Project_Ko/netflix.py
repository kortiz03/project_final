import sys
import PySide2.QtWidgets as qtw
from logic import LoginWindow
from UI.main import Ui_LoginWindow as UI_login
from UI.Creation_Client2 import Ui_CreateClientWindow
from UI.Modifier_Client2 import Ui_CreationWindow
from UI.Confirmation_suppresion_client2 import Ui_ConfirmerDelWindow
from UI.principal import Ui_MainWindow
import images.image_users




if __name__ == "__main__":
    app = qtw.QApplication([])
    window = LoginWindow()
    window.show()
    print(window._user_verified)
    sys.exit(app.exec_())

