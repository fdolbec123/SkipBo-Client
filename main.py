from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QRegion, QPalette, QPixmap, QBrush, QIcon
import creation_partie
import verification
import join


class Menu(QMainWindow):
    # ------------------------- Init ----------------------------------
    def __init__(self):
        super(Menu, self).__init__()
        self.background_picture = QGraphicsView()
        self.scene = QGraphicsScene()
        self.grp = QGroupBox("Mon Groupe")
        self.palette = QPalette()
        self.proxy = QGraphicsProxyWidget()
        self.background_picture2 = QPixmap()
        self.fenetre_creer_une_partie = None
        self.bouton_creer = QPushButton(self)
        self.bouton_rejoindre = QPushButton(self)
        self.bouton_quitter = QPushButton(self)
        self.bouton_help = QPushButton(self)
        self.label = QLabel(self)
        self.init_ui()
        self.setWindowTitle("Bienvenue dans Skip-Bo!")
        self.hauteur = int
        self.quart_hauteur = int
        self.longueur = int
        self.quart_longueur = int
        self.test_rect = QRect()
        self.test_region = QRegion()
        self.rsp = None
        self.rsp2 = None
        self.rsp3 = None
        self.join = QDialog()
        self.verification = QDialog()
        self.quitter_icon = QIcon()
        self.join_icon = QIcon()
        self.creer_icon = QIcon()
        self.help_icon = QIcon()
        self.msg_help = QMessageBox()
        # self.socket_connexion = None
    # ---------------------- Fin du Init ------------------------------

    # ---------------------- Fonction pour centrer la fenêtre dans l'écran ----------------------
    def center(self):
        frame = self.frameGeometry()
        ecran_actif = QApplication.desktop().screenNumber(QApplication.desktop().cursor().pos())
        point_central = QApplication.desktop().screenGeometry(ecran_actif).center()
        frame.moveCenter(point_central)
        self.move(frame.topLeft())
    # --------------------- Fin de la fonction --------------------------------------------------

    # --------------------- Fonction quitter ----------------------------------------------------
    def quitter(self):
        self.close()
    # --------------------- Fin de la fonction --------------------------------------------------

    # --------------------- Fonction pour créer une partie --------------------------------------
    def creer_nouvelle_partie(self):
        self.fenetre_creer_une_partie = creation_partie.NouvellePartie()
        self.fenetre_creer_une_partie.setModal(True)
        self.fenetre_creer_une_partie.show()
        self.rsp = self.fenetre_creer_une_partie.exec_()
        if self.rsp == QDialog.Accepted:
            self.close()
        else:
            print("Cancel")
    # --------------------- Fin de la fonction -------------------------------------------------

    # --------------------- Fonction pour joindre une partie -----------------------------------
    def joindre_partie(self):
        self.verification = verification.Verification()
        self.verification.setModal(True)
        self.verification.show()
        self.rsp2 = self.verification.exec_()
        # print(self.verification.socket_de_connection)
        if self.rsp2 == QDialog.Accepted:
            # print(self.socket_connexion)
            self.join = join.JoinPartie()
            self.join.setModal(True)
            self.join.show()
            self.rsp3 = self.join.exec_()
            if self.rsp3 == QDialog.Accepted:
                self.close()
            else:
                print("Join canceled")
        else:
            print("Cancel")
    # --------------------- Fin de la fonction -------------------------------------------------

    # --------------------- Fonction d'aide ----------------------------------------------------
    def help(self):
        self.msg_help.setIcon(QMessageBox.Information)
        self.msg_help.setText("Bienvenue dans la rubrique d'aide")
        self.msg_help.setInformativeText('Pour créer une partie, cliquez sur le bouton "Créer une partie".\n \nPour '
                                         'joindre une partie, ayez d\'abord votre code d\'invitation en main, puis '
                                         'cliquez sur joindre une partie.')
        self.msg_help.setWindowTitle("Rubrique d'aide")
        self.msg_help.setStandardButtons(QMessageBox.Ok)
        self.msg_help.exec_()
    # --------------------- Fin de la fonction -------------------------------------------------

    # --------------------- Initialisation de la fenêtre et des éléments graphique -------------
    def init_ui(self):
        # --------------- Paramètres de la fenêtre --------------------
        self.resize(1280, 720)
        self.setMaximumSize(1280, 720)
        self.setMinimumSize(1280, 720)
        self.center()
        self.background_picture2.load('backgroundmenu3.png')
        self.palette.setBrush(self.backgroundRole(), QBrush(self.background_picture2))
        self.setPalette(self.palette)

        # --------------- Éléments présents dans la fenêtre ----------
        self.hauteur = int(self.frameGeometry().height())
        self.quart_hauteur = int(self.hauteur / 4)
        self.longueur = int(self.frameGeometry().width())
        self.quart_longueur = int(self.longueur/4)
        self.label.setText("* Skip-Bo est une marque déposée de Mattel Inc.")
        self.label.move(20, 690)
        self.label.adjustSize()
        self.bouton_creer.setText("")
        self.creer_icon = QIcon("bouton_creer.png")
        self.bouton_creer.setIcon(self.creer_icon)
        self.bouton_creer.setIconSize(QSize(320, 90))
        self.bouton_creer.setGeometry((self.quart_longueur-160), (3*self.quart_hauteur), self.quart_longueur,
                                      int(self.quart_hauteur / 2))
        self.bouton_creer.clicked.connect(self.creer_nouvelle_partie)
        self.bouton_rejoindre.setText("")
        self.join_icon = QIcon("bouton_join.png")
        self.bouton_rejoindre.setIcon(self.join_icon)
        self.bouton_rejoindre.setIconSize(QSize(318, 88))
        self.bouton_rejoindre.setGeometry(((2*self.quart_longueur)-160), (3*self.quart_hauteur), self.quart_longueur,
                                          int(self.quart_hauteur / 2))
        self.bouton_rejoindre.clicked.connect(self.joindre_partie)
        self.bouton_help.setText("")
        self.help_icon = QIcon("bouton_help.png")
        self.bouton_help.setIcon(self.help_icon)
        self.bouton_help.setIconSize(QSize(65, 65))
        self.bouton_help.setFixedHeight(100)
        self.bouton_help.setFixedWidth(100)
        self.bouton_help.move(self.longueur-int(self.quart_longueur / (4/2)), -10)
        self.bouton_help.clicked.connect(self.help)
        self.test_rect = QRect(20, 20, 60, 60)
        self.test_region = QRegion(self.test_rect, QRegion.Ellipse)
        self.test_region.boundingRect().size()
        self.bouton_help.setMask(self.test_region)
        self.bouton_quitter.setText("")
        self.quitter_icon = QIcon("bouton_quitter.png")
        self.bouton_quitter.setIcon(self.quitter_icon)
        self.bouton_quitter.setIconSize(QSize(318, 88))
        self.bouton_quitter.setGeometry(((3*self.quart_longueur)-160), (3*self.quart_hauteur), self.quart_longueur,
                                        int(self.quart_hauteur / 2))
        self.bouton_quitter.clicked.connect(self.quitter)
    # ---------------------------- Fin de l'initialisation ---------------------------------------------------------

# -------------------------------- Main loop -----------------------------------------------------------------------


if __name__ == '__main__':
    app = QApplication([])
    menu = Menu()
    menu.show()
    app.exec_()
