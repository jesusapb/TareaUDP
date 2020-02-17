import socket

class valores:
    ubicacionIP = ""
    Archivo = ""

    def is_valid_ipv4_address(self,address):
        try:
            socket.inet_pton(socket.AF_INET, address)
        except AttributeError:  # no inet_pton here, sorry
            try:
                socket.inet_aton(address)
            except socket.error:
                return False
            return address.count('.') == 3
        except socket.error: # not a valid address
            return False
        return True

#este metodo es para direcciones ip version 6 puede
# que no se use, pero resultara muy util

    def is_valid_ipv6_address(self,address):
        try:
            socket.inet_pton(socket.AF_INET6, address)
        except socket.error:  # not a valid address
            return False
        return True


#val= valores()
#print(val.is_valid_ipv4_address("100.0.0.300"))


#Fuente: https://www.iteramos.com/pregunta/14002/como-validar-la-direccion-ip-en-python
