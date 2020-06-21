import socket
import pickle
server = "192.168.100.195"
port = 5555
address = (server, port)

socket_de_connexion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
couleurs = []


def connecter():
    socket_de_connexion.connect(address)