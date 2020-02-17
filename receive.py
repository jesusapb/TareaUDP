import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#main program
file = input("Save received data as: ")
try:
        #receive data
        r = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        r.bind(("", 50002))
        data, ip = r.recvfrom(524300000)
        print("Received from ", ip)
        #write data to file
        try:
                print("Writing file...", end=" ")
                open(file, "xb").write(data)
                print("done")
        except FileExistsError:
                print("File already exists!")
                r.close()
                exit()
finally:
    r.close()