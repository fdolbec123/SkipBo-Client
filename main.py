from PyQt5.QtWidgets import *
# import sys


class Menu(QMainWindow):
    def __init__(self):
        super(Menu, self).__init__()
        self.bouton = QPushButton(self)
        self.label = QLabel(self)
        self.init_ui()
        self.setGeometry(100, 100, 1280, 720)
        self.setWindowTitle("Bienvenue dans SkipBo!")

    def clicked(self):
        print("cliqué")
        self.label.setText("cliqué")
        self.label.repaint()

    def init_ui(self):
        self.label.setText("Coucou")
        self.label.move(100, 100)
        self.bouton.setText("Clique!")
        self.bouton.move(200, 200)
        self.bouton.clicked.connect(self.clicked)


def main():
    app = QApplication([])
    menu = Menu()
    menu.show()
    app.exec_()


main()
