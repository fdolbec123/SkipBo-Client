from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QRegion, QPalette, QPixmap, QBrush
import creation_partie
import verification
import join


class Menu(QMainWindow):
    def __init__(self):
        super(Menu, self).__init__()
        self.background_picture = QGraphicsView()
        self.scene = QGraphicsScene()
        self.grp = QGroupBox("Mon Groupe")
        self.palette = QPalette()
        self.proxy = QGraphicsProxyWidget()
        self.background_picture2 = QPixmap()
        # self.setStyleSheet("background-color: yellow;")
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

    def center(self):
        frame = self.frameGeometry()
        ecran_actif = QApplication.desktop().screenNumber(QApplication.desktop().cursor().pos())
        point_central = QApplication.desktop().screenGeometry(ecran_actif).center()
        frame.moveCenter(point_central)
        self.move(frame.topLeft())

    def quitter(self):
        self.close()

    def creer_nouvelle_partie(self):
        self.fenetre_creer_une_partie = creation_partie.NouvellePartie()
        self.fenetre_creer_une_partie.setModal(True)
        self.fenetre_creer_une_partie.show()
        self.rsp = self.fenetre_creer_une_partie.exec_()
        if self.rsp == QDialog.Accepted:
            self.close()
        else:
            print("Cancel")

    def joindre_partie(self):
        self.verification = verification.Verification()
        self.verification.setModal(True)
        self.verification.show()
        self.rsp2 = self.verification.exec_()
        if self.rsp2 == QDialog.Accepted:
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

    def init_ui(self):
        # --------------- Paramètres de la fenêtre --------------------
        self.resize(1280, 720)
        self.center()
        self.background_picture2.load('background_menu2.png')
        self.palette.setBrush(self.backgroundRole(), QBrush(self.background_picture2))
        self.setPalette(self.palette)
        # self.background_picture.setStyleSheet("background-image: url(background_menu.png);")
        # self.setCentralWidget(self.background_picture)
        # self.background_picture.setScene(self.scene)
        # # --------------- Fin des paramètres -------------------------
        #
        # # --------------- Paramètres pour le groupbox ------------------
        # self.grp.setLayout(QVBoxLayout())
        # self.grp.layout().addWidget(self.bouton_help)
        # self.grp.layout().addWidget(self.bouton_creer)
        # self.grp.layout().addWidget(self.bouton_rejoindre)
        # self.grp.layout().addWidget(self.bouton_quitter)
        # self.palette.setColor(QPalette.Background, Qt.transparent)
        # self.grp.setPalette(self.palette)
        # self.proxy.setWidget(self.grp)
        # self.scene.addItem(self.proxy)
        # --------------- Fin des paramètres -------------------------

        # --------------- Éléments présents dans la fenêtre ----------
        self.hauteur = int(self.frameGeometry().height())
        self.quart_hauteur = int(self.hauteur / 4)
        self.longueur = int(self.frameGeometry().width())
        self.quart_longueur = int(self.longueur/4)
        self.label.setText("* Skip-Bo est une marque déposée de Mattel Inc.")
        self.label.move(20, 690)
        self.label.adjustSize()
        self.bouton_creer.setText("Créer une partie")
        self.bouton_creer.setGeometry((self.quart_longueur-160), (3*self.quart_hauteur), self.quart_longueur,
                                      int(self.quart_hauteur / 2))
        self.bouton_creer.clicked.connect(self.creer_nouvelle_partie)
        self.bouton_rejoindre.setText("Rejoindre une partie")
        self.bouton_rejoindre.setGeometry(((2*self.quart_longueur)-160), (3*self.quart_hauteur), self.quart_longueur,
                                          int(self.quart_hauteur / 2))
        self.bouton_rejoindre.clicked.connect(self.joindre_partie)
        self.bouton_help.setText("?")
        self.bouton_help.setFixedHeight(100)
        self.bouton_help.setFixedWidth(100)
        self.bouton_help.move(self.longueur-int(self.quart_longueur / (4/2)), -10)
        self.test_rect = QRect(20, 20, 60, 60)
        self.test_region = QRegion(self.test_rect, QRegion.Ellipse)
        self.test_region.boundingRect().size()
        self.bouton_help.setMask(self.test_region)
        self.bouton_quitter.setText("Quitter")
        self.bouton_quitter.setGeometry(((3*self.quart_longueur)-160), (3*self.quart_hauteur), self.quart_longueur,
                                        int(self.quart_hauteur / 2))
        self.bouton_quitter.clicked.connect(self.quitter)


if __name__ == '__main__':
    app = QApplication([])
    menu = Menu()
    menu.show()
    app.exec_()
