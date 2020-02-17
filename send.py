#! /usr/bin/python3
#

import socket
from sys import argv
#To create a socket, you must use the socket.socket() function available in socket module, which has
#the general syntax:
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
target = input("Enviar a: ")
file = input("Direccion del archivo: ")
#main program
try:
        #Open file
        try:
                print("Leyendo archivo ...", end=" ")
                data = open(file, "rb").read()
                print("Hecho")
        except FileNotFoundError:
                print("Error de lectura")
                s.close()
                exit()
        #send file
        print("Enviando archivo ...", end=" ")
        # "s.sendto()" This method transmits UDP message
        s.sendto(data, (target, 50002))
        print("Hecho")
finally:
        s.close()