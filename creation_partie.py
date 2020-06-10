from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import jeu
import socket
import pickle
server = "192.168.100.195"
port = 5555
socket_de_connexion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
address = (server, port)

class NouvellePartie(QDialog):
    def __init__(self):
        super(NouvellePartie, self).__init__()
        self.une_partie = None
        self.msg = QMessageBox()
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
        self.invite_nbre_joueur = QLabel(self)
        self.choix_de_couleur = QComboBox(self)
        self.choix_nbre_joueur = QComboBox(self)
        self.cartes_de_depart = ()
        self.init_ui()

    def init_ui(self):
        # --------------- Paramètres de la fenêtre --------------------
        self.resize(640, 325)
        self.center()
        self.invite_username.setText("Nom d'utilisateur à afficher durant la partie: ")
        self.invite_couleur.setText("Veuillez choisir une couleur:")
        self.invite_nbre_joueur.setText("Le nombre de joueurs pour la partie")
        self.invite_username.adjustSize()
        self.invite_couleur.adjustSize()
        self.invite_nbre_joueur.adjustSize()
        self.invite_username.move(30, 75)
        self.invite_couleur.move(30, 120)
        self.invite_nbre_joueur.move(30, 175)
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
        self.choix_de_couleur.addItems(["Rouge", "Bleu", "Vert", "Jaune"])
        self.choix_nbre_joueur.setGeometry(307, 170, 300, 25)
        self.choix_nbre_joueur.addItems(["2", "3", "4"])
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

    def send(self):
        print("Trying to send informations to server...")
        socket_de_connexion.connect(address)
        msg = socket_de_connexion.recv(2048)
        message = pickle.loads(msg)
        print(message)
        if message == "Connecté!":
            data_to_send = pickle.dumps("create")
            socket_de_connexion.send(data_to_send)
            code = socket_de_connexion.recv(2048)
            code_invitation = pickle.loads(code)
            print(code_invitation)
            self.code = code_invitation
            player_info = {"username": self.boite_texte_username.text(), "couleur": self.choix_de_couleur.currentText()}
            nbre_de_joueur = int(self.choix_nbre_joueur.currentText())
            joueurs = pickle.dumps((nbre_de_joueur, player_info))
            socket_de_connexion.send(joueurs)
            depart = socket_de_connexion.recv(2048)
            self.cartes_de_depart = pickle.loads(depart)
            # print(self.cartes_de_depart)

    def confirmer(self):
        self.send()
        # self.code = 1234
        print("Voici les cartes de départs: " + str(self.cartes_de_depart))
        self.msg.setIcon(QMessageBox.Information)
        self.msg.setText("Voici votre code d'invitation: " + str(self.code))
        self.msg.setInformativeText("Garder ce code en note, il permettra aux autres joueurs de se joindre à vous.")
        self.msg.setWindowTitle("Code d'invitation")
        self.msg.setStandardButtons(QMessageBox.Ok)
        self.msg.exec_()
        self.accept()
        if not self.isVisible():
            # jeu.Game()
            self.une_partie = jeu.Jeu(int(self.choix_nbre_joueur.currentText()), self.boite_texte_username.text(),
                                      self.choix_de_couleur.currentText())
            self.une_partie.show()


if __name__ == '__main__':
    app = QDialog()
    nouvelle_partie = NouvellePartie()
    nouvelle_partie.show()
    app.exec_()
