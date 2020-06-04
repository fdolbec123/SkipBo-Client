from PyQt5.QtWidgets import *
# from PyQt5.QtCore import *
# from PyQt5.QtGui import QRegion, QPalette, QPixmap, QBrush


class NouvellePartie(QMainWindow):
    def __init__(self):
        super(NouvellePartie, self).__init__()
        self.init_ui()
        self.fenetre_creer_une_partie = None
        self.setWindowTitle("Fenêtre 2")

    def init_ui(self):
        # --------------- Paramètres de la fenêtre --------------------
        self.resize(600, 360)
        self.center()

    def center(self):
        frame = self.frameGeometry()
        ecran_actif = QApplication.desktop().screenNumber(QApplication.desktop().cursor().pos())
        point_central = QApplication.desktop().screenGeometry(ecran_actif).center()
        frame.moveCenter(point_central)
        self.move(frame.topLeft())


if __name__ == '__main__':
    app = QApplication([])
    nouvelle_partie = NouvellePartie()
    nouvelle_partie.show()
    app.exec_()
