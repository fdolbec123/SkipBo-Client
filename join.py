from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import jeu
import connexion
import socket
import pickle
# server = "192.168.100.195"
# port = 5555
# address = (server, port)


class JoinPartie(QDialog):
    def __init__(self):
        super(JoinPartie, self).__init__()
        # self.socket_de_connexion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.une_partie = None
        self.code = int
        self.setWindowTitle("Veuillez remplir les éléments suivants")
        self.boite_texte_username = QLineEdit(self)
        self.regex = QRegExp("^\w[\w|\s|\.]+")
        self.validator = QRegExpValidator(self.regex)
        self.boite_texte_username.setValidator(self.validator)
        self.bouton_creer = QPushButton(self)
        self.bouton_annuler = QPushButton(self)
        self.invite_username = QLabel(self)
        self.invite_couleur = QLabel(self)
        self.choix_de_couleur = QComboBox(self)
        self.init_ui()

    def init_ui(self):
        # --------------- Paramètres de la fenêtre --------------------
        self.resize(640, 325)
        self.center()
        print(connexion.couleurs)
        self.invite_username.setText("Nom d'utilisateur à afficher durant la partie: ")
        self.invite_couleur.setText("Veuillez choisir une couleur:")
        self.invite_username.adjustSize()
        self.invite_couleur.adjustSize()
        self.invite_username.move(30, 75)
        self.invite_couleur.move(30, 120)
        self.boite_texte_username.setGeometry(300, 70, 300, 25)
        self.bouton_annuler.setText("Annuler")
        self.bouton_annuler.setGeometry(530, 275, 100, 40)
        self.bouton_annuler.clicked.connect(self.annuler)
        self.bouton_creer.setDefault(True)
        self.bouton_creer.setText("Confirmer")
        self.bouton_creer.setGeometry(430, 275, 100, 40)
        self.bouton_creer.setEnabled(False)
        self.bouton_creer.clicked.connect(self.confirmer)
        self.choix_de_couleur.setGeometry(307, 115, 300, 25)
        self.choix_de_couleur.addItems(connexion.couleurs)
        self.boite_texte_username.textChanged.connect(self.texte_change)

    def texte_change(self):
        if self.boite_texte_username != "":
            self.bouton_creer.setEnabled(True)
        if self.boite_texte_username.text() == "":
            self.bouton_creer.setEnabled(False)

    def center(self):
        frame = self.frameGeometry()
        ecran_actif = QApplication.desktop().screenNumber(QApplication.desktop().cursor().pos())
        point_central = QApplication.desktop().screenGeometry(ecran_actif).center()
        frame.moveCenter(point_central)
        self.move(frame.topLeft())

    def annuler(self):
        self.close()

    def confirmer(self):
        infos = {"username": self.boite_texte_username.text(), "couleur": self.choix_de_couleur.currentText()}
        infos_du_joueur = pickle.dumps(infos)
        connexion.socket_de_connexion.send(infos_du_joueur)
        cartes_joueur_pickled = connexion.socket_de_connexion.recv(2048)
        cartes_joueur = pickle.loads(cartes_joueur_pickled)
        self.accept()
        if not self.isVisible():
            self.une_partie = jeu.Jeu(2, self.boite_texte_username.text(),  self.choix_de_couleur.currentText(),
                                      cartes_joueur)
            self.une_partie.show()


if __name__ == '__main__':
    app = QDialog()
    join_partie = JoinPartie()
    join_partie.show()
    app.exec_()
