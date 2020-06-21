from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QRegExpValidator
import socket
import pickle
import connexion
import sys
server = "192.168.100.195"
port = 5555


class Verification(QDialog):
    def __init__(self):
        super(Verification, self).__init__()
        self.boite_texte_code = QLineEdit(self)
        self.bouton_verifier = QPushButton(self)
        self.bouton_annuler2 = QPushButton(self)
        self.invite_code = QLabel(self)
        self.accept_local_test = "Ok"
        self.regex2 = QRegExp()
        self.validator2 = QRegExpValidator()
        self.msg = QMessageBox()
        # self.socket_de_connexion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.init_ui()

    def init_ui(self):
        connexion.connecter()
        # address = (server, port)
        # self.socket_de_connexion.connect(address)
        # print(self.socket_connexion)
        self.resize(290, 110)
        self.center()
        self.setWindowTitle("Veuillez saisir le code d'invitation:")
        self.regex2 = QRegExp("^[0-9]{4}")
        self.validator2 = QRegExpValidator(self.regex2)
        self.boite_texte_code.setValidator(self.validator2)
        self.boite_texte_code.setGeometry(150, 20, 100, 25)
        self.bouton_annuler2.setText("Annuler")
        self.bouton_annuler2.setGeometry(157, 60, 100, 40)
        self.bouton_annuler2.clicked.connect(self.annuler2)
        self.bouton_verifier.setDefault(True)
        self.bouton_verifier.setEnabled(False)
        self.bouton_verifier.setText("Confirmer")
        self.bouton_verifier.setGeometry(57, 60, 100, 40)
        self.bouton_verifier.clicked.connect(self.confirmer2)
        self.invite_code.setText("Code d'invitation:")
        self.invite_code.adjustSize()
        self.invite_code.move(30, 25)
        self.boite_texte_code.textChanged.connect(self.texte_change)

    def center(self):
        frame = self.frameGeometry()
        ecran_actif = QApplication.desktop().screenNumber(QApplication.desktop().cursor().pos())
        point_central = QApplication.desktop().screenGeometry(ecran_actif).center()
        frame.moveCenter(point_central)
        self.move(frame.topLeft())

    def annuler2(self):
        # self.socket_de_connexion.close()
        connexion.socket_de_connexion.close()
        self.close()

    def confirmer2(self):
        print("Trying to send informations to server...")
        msg = connexion.socket_de_connexion.recv(2048)
        # msg = self.socket_de_connexion.recv(2048)
        message = pickle.loads(msg)
        print(message)
        if message == "Connecté!":
            print("in...")
            data_to_send = pickle.dumps("join")
            connexion.socket_de_connexion.send(data_to_send)
            # self.socket_de_connexion.send(data_to_send)
            verif_pickled = connexion.socket_de_connexion.recv(2048)
            # verif_pickled = self.socket_de_connexion.recv(2048)
            verif = pickle.loads(verif_pickled)
            if verif == "code?":
                print("asked")
                code_to_send = pickle.dumps(self.boite_texte_code.text())
                connexion.socket_de_connexion.send(code_to_send)
                # self.socket_de_connexion.send(code_to_send)
                answer_pickled = connexion.socket_de_connexion.recv(2048)
                # answer_pickled = self.socket_de_connexion.recv(2048)
                answer = pickle.loads(answer_pickled)
                print(answer)
                if answer == "No":
                    print("Oups!")
                    self.msg.setIcon(QMessageBox.Critical)
                    self.msg.setText("Erreur! Le code est invalide!")
                    self.msg.setInformativeText(
                        "Veuillez vérifier la validité du code. Le programme va maintenant quitter.")
                    self.msg.setWindowTitle("Oups!")
                    self.msg.setStandardButtons(QMessageBox.Ok)
                    self.msg.exec_()
                    # add msg box here
                    # self.close()
                    # socket_de_connexion.shutdown()
                    # socket_de_connexion.close()
                    sys.exit()
                elif answer == "Yes":
                    print("yes")
                    une_commande = pickle.dumps("couleurs")
                    print(une_commande)
                    connexion.socket_de_connexion.send(une_commande)
                    couleurs_pickled = connexion.socket_de_connexion.recv(2048)
                    couleurs_restantes = pickle.loads(couleurs_pickled)
                    print(couleurs_restantes)
                    connexion.couleurs = couleurs_restantes
                    #return self.socket_de_connexion
                    self.accept()
        if self.accept_local_test == "Ok":
            if self.boite_texte_code.text() != "":
                pass
                # self.accept()
        else:
            print("Nope!")

    def texte_change(self):
        if self.boite_texte_code != "":
            if len(self.boite_texte_code.text()) == 4:
                self.bouton_verifier.setEnabled(True)
            else:
                self.bouton_verifier.setEnabled(False)
        if self.boite_texte_code.text() == "":
            self.bouton_verifier.setEnabled(False)


if __name__ == '__main__':
    app = QDialog()
    verification = Verification()
    verification.show()
    app.exec_()
