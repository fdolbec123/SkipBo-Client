from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QPixmap, QBrush, QPalette, QFont, QIcon


class Jeu(QMainWindow):
    def __init__(self, nbre_de_joueur, nom, couleur, cartes_de_depart):
        super(Jeu, self).__init__()
        self.nbre_de_joueur = nbre_de_joueur
        self.nom = nom
        self.couleur = couleur
        self.cartes_de_depart = cartes_de_depart
        self.couleur_id = str()
        self.label_nom_local = QLabel(self)
        self.test = str()
        self.background = QPixmap()
        self.palette = QPalette()
        self.icon_joueur = QPixmap()
        self.label_icon_joueur = QLabel(self)
        self.label_count = QLabel(self)
        self.commande_defausser = QCheckBox(self)
        self.deck = QPushButton(self)
        self.main1 = QPushButton(self)
        self.main2 = QPushButton(self)
        self.main3 = QPushButton(self)
        self.main4 = QPushButton(self)
        self.main5 = QPushButton(self)
        self.talon = []
        self.cartes_deck = []
        self.cartes_main = []
        self.count = 30
        self.carte_deck_j1 = None
        self.carte_deck_j2 = None
        self.carte_deck_j3 = None
        self.nbre_cartes_main_j1 = 5
        self.count_j1 = 30
        self.nbre_cartes_main_j2 = 5
        self.count_j2 = 30
        self.nbre_cartes_main_j3 = 5
        self.count_j3 = 30
        self.c1 = QIcon("cartes/1.png")
        self.c2 = QIcon("cartes/2.png")
        self.c3 = QIcon("cartes/3.png")
        self.c4 = QIcon("cartes/4.png")
        self.c5 = QIcon("cartes/5.png")
        self.c6 = QIcon("cartes/6.png")
        self.c7 = QIcon("cartes/7.png")
        self.c8 = QIcon("cartes/8.png")
        self.c9 = QIcon("cartes/9.png")
        self.c10 = QIcon("cartes/10.png")
        self.c11 = QIcon("cartes/11.png")
        self.c12 = QIcon("cartes/12.png")
        self.sb = QIcon("cartes/sb.png")
        self.icon_deck = None
        self.icon_m1 = None
        self.icon_m2 = None
        self.icon_m3 = None
        self.icon_m4 = None
        self.icon_m5 = None
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
        self.commande_defausser.setText("Défausser")
        self.commande_defausser.setStyleSheet("color:white")
        self.commande_defausser.setFont(QFont('Arial', 24))
        self.commande_defausser.adjustSize()
        self.commande_defausser.move(1519.5, 1000)
        self.label_count.setStyleSheet("color:white")
        self.label_count.setFont(QFont('Arial', 24))
        self.label_count.move(425, 718)
        # print(self.cartes_de_depart)
        if self.nbre_de_joueur == 2:
            (self.talon, self.cartes_deck, self.cartes_main, self.count, self.carte_deck_j1, self.nbre_cartes_main_j1,
             self.count_j1) = self.cartes_de_depart
            print(self.cartes_deck)
            self.icon_deck = self.set_icon(self.cartes_deck[0])
            # print(self.icon_deck)
            self.icon_m1 = self.set_icon(self.cartes_main[0])
            self.icon_m2 = self.set_icon(self.cartes_main[1])
            self.icon_m3 = self.set_icon(self.cartes_main[2])
            self.icon_m4 = self.set_icon(self.cartes_main[3])
            self.icon_m5 = self.set_icon(self.cartes_main[4])
            self.deck.setIcon(self.icon_deck)
            self.main1.setIcon(self.icon_m1)
            self.main2.setIcon(self.icon_m2)
            self.main3.setIcon(self.icon_m3)
            self.main4.setIcon(self.icon_m4)
            self.main5.setIcon(self.icon_m5)
            self.main1.setIconSize(QSize(135, 210))
            self.main2.setIconSize(QSize(135, 210))
            self.main3.setIconSize(QSize(135, 210))
            self.main4.setIconSize(QSize(135, 210))
            self.main5.setIconSize(QSize(135, 210))
            self.deck.setIconSize(QSize(135, 210))
            self.deck.resize(135,210)
            self.main1.resize(135,210)
            self.main2.resize(135,210)
            self.main3.resize(135,210)
            self.main4.resize(135,210)
            self.main5.resize(135,210)
            self.deck.move(365, 830)
            self.main1.move(612.5, 945)
            self.main2.move(752.5, 945)
            self.main3.move(892.5, 945)
            self.main4.move(1032.5, 945)
            self.main5.move(1172.5, 945)
            self.label_count.setText(str(self.count))
        elif self.nbre_de_joueur == 3:
            (self.talon, self.cartes_deck, self.cartes_main, self.count, self.carte_deck_j1,
             self.nbre_cartes_main_j1, self.count_j1, self.carte_deck_j2,
             self.nbre_cartes_main_j2, self.count_j2) = self.cartes_de_depart
            print(self.cartes_deck)
            self.icon_deck = self.set_icon(self.cartes_deck[0])
            # print(self.icon_deck)
            self.icon_m1 = self.set_icon(self.cartes_main[0])
            self.icon_m2 = self.set_icon(self.cartes_main[1])
            self.icon_m3 = self.set_icon(self.cartes_main[2])
            self.icon_m4 = self.set_icon(self.cartes_main[3])
            self.icon_m5 = self.set_icon(self.cartes_main[4])
            self.deck.setIcon(self.icon_deck)
            self.main1.setIcon(self.icon_m1)
            self.main2.setIcon(self.icon_m2)
            self.main3.setIcon(self.icon_m3)
            self.main4.setIcon(self.icon_m4)
            self.main5.setIcon(self.icon_m5)
            self.main1.setIconSize(QSize(135, 210))
            self.main2.setIconSize(QSize(135, 210))
            self.main3.setIconSize(QSize(135, 210))
            self.main4.setIconSize(QSize(135, 210))
            self.main5.setIconSize(QSize(135, 210))
            self.deck.setIconSize(QSize(135, 210))
            self.deck.resize(135, 210)
            self.main1.resize(135, 210)
            self.main2.resize(135, 210)
            self.main3.resize(135, 210)
            self.main4.resize(135, 210)
            self.main5.resize(135, 210)
            self.deck.move(365, 830)
            self.main1.move(612.5, 945)
            self.main2.move(752.5, 945)
            self.main3.move(892.5, 945)
            self.main4.move(1032.5, 945)
            self.main5.move(1172.5, 945)
            self.label_count.setText(str(self.count))
        elif self.nbre_de_joueur == 4:
            (self.talon, self.cartes_deck, self.cartes_main, self.count, self.carte_deck_j1,
             self.nbre_cartes_main_j1, self.count_j1, self.carte_deck_j2,
             self.nbre_cartes_main_j2, self.count_j2, self.carte_deck_j3,
             self.nbre_cartes_main_j3, self.count_j3) = self.cartes_de_depart
            print(self.cartes_deck)
            self.icon_deck = self.set_icon(self.cartes_deck[0])
            # print(self.icon_deck)
            self.icon_m1 = self.set_icon(self.cartes_main[0])
            self.icon_m2 = self.set_icon(self.cartes_main[1])
            self.icon_m3 = self.set_icon(self.cartes_main[2])
            self.icon_m4 = self.set_icon(self.cartes_main[3])
            self.icon_m5 = self.set_icon(self.cartes_main[4])
            self.deck.setIcon(self.icon_deck)
            self.main1.setIcon(self.icon_m1)
            self.main2.setIcon(self.icon_m2)
            self.main3.setIcon(self.icon_m3)
            self.main4.setIcon(self.icon_m4)
            self.main5.setIcon(self.icon_m5)
            self.main1.setIconSize(QSize(135, 210))
            self.main2.setIconSize(QSize(135, 210))
            self.main3.setIconSize(QSize(135, 210))
            self.main4.setIconSize(QSize(135, 210))
            self.main5.setIconSize(QSize(135, 210))
            self.deck.setIconSize(QSize(135, 210))
            self.deck.resize(135, 210)
            self.main1.resize(135, 210)
            self.main2.resize(135, 210)
            self.main3.resize(135, 210)
            self.main4.resize(135, 210)
            self.main5.resize(135, 210)
            self.deck.move(365, 830)
            self.main1.move(612.5, 945)
            self.main2.move(752.5, 945)
            self.main3.move(892.5, 945)
            self.main4.move(1032.5, 945)
            self.main5.move(1172.5, 945)
            self.label_count.setText(str(self.count))
            # self.label_count.adjustSize()

    def center(self):
        frame = self.frameGeometry()
        ecran_actif = QApplication.desktop().screenNumber(QApplication.desktop().cursor().pos())
        point_central = QApplication.desktop().screenGeometry(ecran_actif).center()
        frame.moveCenter(point_central)
        self.move(frame.topLeft())

    def set_icon(self, carte):
        if carte == 1:
            return self.c1
        elif carte == 2:
            return self.c2
        elif carte == 3:
            return self.c3
        elif carte == 4:
            return self.c4
        elif carte == 5:
            return self.c5
        elif carte == 6:
            return self.c6
        elif carte == 7:
            return self.c7
        elif carte == 8:
            return self.c8
        elif carte == 9:
            return self.c9
        elif carte == 10:
            return self.c10
        elif carte == 11:
            return self.c11
        elif carte == 12:
            return self.c12
        elif carte == "SB":
            return self.sb


if __name__ == '__main__':
    app = QApplication([])
    jeu = Jeu()
    print("2")
    jeu.show()
    app.exec_()
