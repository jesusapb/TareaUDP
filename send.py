#! /usr/bin/python3
#

import socket
from sys import argv
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
target = input("Send to: ")
file = input("File to send: ")
#main program
try:
        #Open file
        try:
                print("Reading file...", end=" ")
                data = open(file, "rb").read()
                print("done")
        except FileNotFoundError:
                print("No such File")
                s.close()
                exit()
        #send file
        print("Sending file...", end=" ")
        s.sendto(data, (target, 50002))
        print("done")
finally:
        s.close()