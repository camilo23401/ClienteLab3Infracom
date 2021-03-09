import socket
import os
import hashlib

host = 'localhost'
port = 8050
path_archivos = "./ArchivosRecibidos"
nombre_archivo =  "Cliente1-Prueba-5.txt"
BLOCK_SIZE = 65536


obj = socket.socket()

obj.connect((host, port))
obj.listen(25)
print("Conectado al servidor")


while True:
    mens = input("Mensaje de confirmacion. Listo para recibir un archivo")
    obj.send(mens.encode('ascii'))
    recibido = obj.recv(4096)
    archivoPorEscribir = os.path.join(path_archivos, nombre_archivo)
    file1 = open(archivoPorEscribir, "w")
    file1.write(recibido)
    file1.close()


    file_hash = hashlib.sha256()
    with open(archivoPorEscribir, 'rb') as f:
        fb = f.read(BLOCK_SIZE)
        while len(fb) > 0:
            file_hash.update(fb)
            fb = f.read(BLOCK_SIZE)
    resultadoHash = file_hash.hexdigest()
obj.close()
print("Conexión cerrada")


if __name__ == '__main__':
    print_hi('Cliente')


