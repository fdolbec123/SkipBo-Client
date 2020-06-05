from PyQt5.QtWidgets import *


class Jeu(QMainWindow):
    def __init__(self):
        super(Jeu, self).__init__()
        self.init_ui()

    def init_ui(self):
        # --------------- Paramètres de la fenêtre --------------------
        self.resize(1920, 1080)
        self.center()

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
