import socket
from sys import argv

class EnvioArchivo:

    target = ""
    file = ""

    def __init__(self,target,file):
        self.target=target
        self.file=file

    def Send(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        #target = input("Enviar a: ")
        #file = input("Direccion del archivo: ")
        # main program
        try:
            # Open file
            try:
                print("Leyendo archivo ...", end=" ")
                data = open(self.file, "rb").read()
                print("Hecho")
            except FileNotFoundError:
                print("Error de lectura")
                s.close()
                exit()
        # send file
            print("Enviando archivo ...", end=" ")
            # "s.sendto()" This method transmits UDP message
            s.sendto(data, (self.target, 50002))
            print("Hecho")
        finally:
            s.close()


#a= "127.0.0.1"
#arch="C:\\Users\\japb1\\OneDrive - Universidad Autonoma de Yucatan\\repositorios\\udp\\TareaUDP\\ejemplo.txt"
#ejemplo=EnvioArchivo(a,arch)
#ejemplo.Send()