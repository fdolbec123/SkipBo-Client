from PyQt5.QtWidgets import *
# from PyQt5.QtCore import *
# from PyQt5.QtGui import QRegion, QPalette, QPixmap, QBrush
import main
import jeu

class NouvellePartie(QDialog):
    def __init__(self):
        super(NouvellePartie, self).__init__()
        # self.fenetre_creer_une_partie = None
        self.une_partie = None
        self.msg = QMessageBox()
        self.code = int
        self.setWindowTitle("Veuillez remplir les éléments suivants")
        self.boite_texte_username = QLineEdit(self)
        self.bouton_creer = QPushButton(self)
        self.bouton_annuler = QPushButton(self)
        self.invite_username = QLabel(self)
        self.invite_couleur = QLabel(self)
        self.invite_nbre_joueur = QLabel(self)
        self.choix_de_couleur = QComboBox(self)
        self.choix_nbre_joueur = QComboBox(self)
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
        self.choix_de_couleur.addItems(["Couleur 1", "Couleur 2", "Couleur 3", "Couleur 4"])
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

    def confirmer(self):
        self.code = 1234
        self.msg.setIcon(QMessageBox.Information)
        self.msg.setText("Voici votre code d'invitation: " + str(self.code))
        self.msg.setInformativeText("Garder ce code en note, il permettra aux autres joueurs de se joindre à vous.")
        self.msg.setWindowTitle("Code d'invitation")
        # self.msg.setDetailedText("The details are as follows:")
        self.msg.setStandardButtons(QMessageBox.Ok)
        retval = self.msg.exec_()
        self.accept()
        if not self.isVisible():
            self.une_partie = jeu.Jeu()
            self.une_partie.show()





if __name__ == '__main__':
    app = QDialog([])
    nouvelle_partie = NouvellePartie()
    nouvelle_partie.show()
    app.exec_()
