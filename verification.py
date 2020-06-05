from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QRegion, QPalette, QPixmap, QBrush, QRegExpValidator

class Verification(QDialog):
    def __init__(self):
        super(Verification, self).__init__()
        self.boite_texte_code = QLineEdit(self)
        self.bouton_verifier = QPushButton(self)
        self.bouton_annuler2 = QPushButton(self)
        self.invite_code = QLabel(self)
        self.accept_local_test = "Ok"
        self.init_ui()

    def init_ui(self):
        self.resize(290, 110)
        self.center()
        self.setWindowTitle("Veuillez saisir le code d'invitation:")
        self.regex2 = QRegExp("^[0-9]{4}")
        self.validator2 = QRegExpValidator(self.regex2)
        self.boite_texte_code.setValidator(self.validator2)
        self.boite_texte_code.setGeometry(150, 20, 100, 25)
        self.bouton_annuler2.setText("Annuler")
        self.bouton_annuler2.setGeometry(157, 60, 100, 40)
        self.bouton_annuler2.clicked.connect(self.annuler2)
        self.bouton_verifier.setDefault(True)
        self.bouton_verifier.setEnabled(False)
        self.bouton_verifier.setText("Confirmer")
        self.bouton_verifier.setGeometry(57, 60, 100, 40)
        self.bouton_verifier.clicked.connect(self.confirmer2)
        self.invite_code.setText("Code d'invitation:")
        self.invite_code.adjustSize()
        self.invite_code.move(30, 25)
        self.boite_texte_code.textChanged.connect(self.texte_change)

    def center(self):
        frame = self.frameGeometry()
        ecran_actif = QApplication.desktop().screenNumber(QApplication.desktop().cursor().pos())
        point_central = QApplication.desktop().screenGeometry(ecran_actif).center()
        frame.moveCenter(point_central)
        self.move(frame.topLeft())

    def annuler2(self):
        self.close()

    def confirmer2(self):
        if self.accept_local_test == "Ok":
            if self.boite_texte_code.text() != "":
                self.accept()
        else:
            print("Nope!")

    def texte_change(self):
        if self.boite_texte_code != "":
            if len(self.boite_texte_code.text()) == 4:
                self.bouton_verifier.setEnabled(True)
        if self.boite_texte_code.text() == "":
            self.bouton_verifier.setEnabled(False)


if __name__ == '__main__':
    app = QDialog()
    verification = Verification()
    verification.show()
    app.exec_()
