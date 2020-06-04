from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QRegion, QPalette, QPixmap, QBrush
# import sys


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

    def quitter(self):
        self.close()

    def init_ui(self):
        # --------------- Paramètres de la fenêtre --------------------
        self.setGeometry(100, 100, 1280, 720)
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
        self.bouton_rejoindre.setText("Rejoindre une partie")
        self.bouton_rejoindre.setGeometry(((2*self.quart_longueur)-160), (3*self.quart_hauteur), self.quart_longueur,
                                          int(self.quart_hauteur / 2))
        self.bouton_help.setText("?")
        self.bouton_help.setFixedHeight(100)
        self.bouton_help.setFixedWidth(100)
        self.bouton_help.move(self.longueur-int(self.quart_longueur / (4/2)), -10)
        # self.bouton_help.setGeometry(200, 150, 100, 100)
        self.test_rect = QRect(20, 20, 60, 60)
        self.test_region = QRegion(self.test_rect, QRegion.Ellipse)
        self.test_region.boundingRect().size()
        self.bouton_help.setMask(self.test_region)
        self.bouton_quitter.setText("Quitter")
        self.bouton_quitter.setGeometry(((3*self.quart_longueur)-160), (3*self.quart_hauteur), self.quart_longueur,
                                        int(self.quart_hauteur / 2))
        self.bouton_quitter.clicked.connect(self.quitter)


def main():
    app = QApplication([])
    menu = Menu()
    menu.show()
    app.exec_()


main()
