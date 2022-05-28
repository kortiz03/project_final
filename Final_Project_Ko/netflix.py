
##appel des librairies
import sys
import PySide2.QtWidgets as qtw
from logic import LoginWindow

## Creation et affichage de la fênetre principale
if __name__ == "__main__":
    app = qtw.QApplication([])
    window = LoginWindow()
    window.show()
    ##print(window._user_verified)
    sys.exit(app.exec_())

