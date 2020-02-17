import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#main program
file = input("Guardar los datos recibidos como: ")
try:
        #receive data
        # To create a socket, you must use the socket.socket() function available in socket module, which has
        # the general syntax:
        r = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # "r.bind()" This method binds address (hostname, port number pair) to socket.
        r.bind(("", 50002))
        # "r.recvfrom()" This method receives UDP message
        data, ip = r.recvfrom(524300000)
        print("Recibido de: ", ip)
        #write data to file
        try:
                print("Escribiendo archivo ...", end=" ")
                open(file, "xb").write(data)
                print("Hecho")
        except FileExistsError:
                print("File already exists!")
                r.close()
                exit()
finally:
    r.close()