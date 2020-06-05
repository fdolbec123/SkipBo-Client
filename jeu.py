from PyQt5.QtWidgets import *


class Jeu(QMainWindow):
    def __init__(self):
        super(Jeu, self).__init__()
        self.init_ui()

    def init_ui(self):
        # --------------- Paramètres de la fenêtre --------------------
        self.resize(1280, 720)


if __name__ == '__main__':
    app = QApplication([])
    jeu = Jeu()
    print("2")
    jeu.show()
    app.exec_()
