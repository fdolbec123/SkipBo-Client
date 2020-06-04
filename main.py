from PyQt5.QtWidgets import *
# import sys


class Menu(QMainWindow):
    def __init__(self):
        super(Menu, self).__init__()
        self.bouton_quitter = QPushButton(self)
        self.label = QLabel(self)
        self.init_ui()
        self.setGeometry(100, 100, 1280, 720)
        self.setWindowTitle("Bienvenue dans SkipBo!")

    def quitter(self):
        self.close()
        # self.label.setText("cliqué")
        # self.label.repaint()

    def init_ui(self):
        self.label.setText("Coucou")
        self.label.move(100, 100)
        self.bouton_quitter.setText("Quitter")
        self.bouton_quitter.move(200, 200)
        self.bouton_quitter.clicked.connect(self.quitter)


def main():
    app = QApplication([])
    menu = Menu()
    menu.show()
    app.exec_()


main()
