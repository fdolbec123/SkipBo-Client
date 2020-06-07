from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QBrush, QPalette, QFont


class Jeu(QMainWindow):
    def __init__(self, nbre_de_joueur, nom, couleur):
        super(Jeu, self).__init__()
        self.nbre_de_joueur = nbre_de_joueur
        self.nom = nom
        self.couleur = couleur
        self.couleur_id = str()
        self.label_nom_local = QLabel(self)
        self.test = str()
        self.background = QPixmap()
        self.palette = QPalette()
        self.icon_joueur = QPixmap()
        self.label_icon_joueur = QLabel(self)
        self.init_ui()

    def init_ui(self):
        # --------------- Paramètres de la fenêtre --------------------
        self.resize(1920, 1080)
        self.setMaximumSize(1920, 1080)
        self.setMinimumSize(1920, 1080)
        self.center()
        self.background.load("background_de_jeu.png")
        self.palette.setBrush(self.backgroundRole(), QBrush(self.background))
        self.setPalette(self.palette)
        print(self.nbre_de_joueur)
        print(self.nom)
        self.label_nom_local.setText("Vous (" + self.nom + ")")
        if self.couleur == "Jaune":
            self.couleur_id = "255, 198, 0, 127"
            self.icon_joueur.load("jaune.jpg")
        elif self.couleur == "Vert":
            self.couleur_id = "0, 159, 0, 127"
            self.icon_joueur.load("vert.jpg")
        elif self.couleur == "Bleu":
            self.couleur_id = "0, 102, 255, 127"
            self.icon_joueur.load("bleu.jpg")
        elif self.couleur == "Rouge":
            self.couleur_id = "195, 0, 0, 127"
            self.icon_joueur.load("rouge.jpg")
        self.label_icon_joueur.setPixmap(self.icon_joueur)
        self.label_icon_joueur.resize(145, 145)
        self.label_icon_joueur.move(1519.5, 795)
        self.test = str("background-color:rgba(" + self.couleur_id + "); color:white;")
        self.label_nom_local.setStyleSheet(self.test)
        self.label_nom_local.setAlignment(Qt.AlignCenter)
        self.label_nom_local.setFont(QFont('Arial', 24))
        self.label_nom_local.adjustSize()
        self.label_nom_local.move(1519.5, 765)

    def center(self):
        frame = self.frameGeometry()
        ecran_actif = QApplication.desktop().screenNumber(QApplication.desktop().cursor().pos())
        point_central = QApplication.desktop().screenGeometry(ecran_actif).center()
        frame.moveCenter(point_central)
        self.move(frame.topLeft())


if __name__ == '__main__':
    app = QApplication([])
    jeu = Jeu()
    print("2")
    jeu.show()
    app.exec_()
