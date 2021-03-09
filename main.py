import socket
import os
import hashlib
from datetime import datetime

host = 'localhost'
port = 8050
path_archivos = "./ArchivosRecibidos"
path_logs = "./Logs"

BLOCK_SIZE = 65536
conexiones=25

obj = socket.socket()

obj.connect((host, port))
obj.listen(conexiones)

archivolog = os.path.join(path_logs, datetime.now())
file = open(archivolog, "w")

#No se me ocurrió otra manera de identificar el cliente
cliente=obj.__getattribute__('name')

print("Conectado al servidor")


while True:
    mens = input("Mensaje de confirmacion. Listo para recibir un archivo")
    obj.send(mens.encode('ascii'))
    recibido = obj.recv(4096)
#    log="nombre del archivo: "
#    log=log+" Tamaño: "+os.stat(recibido).st_size
#    log=log+"\n Cliente: "+cliente
    nombre_archivo = cliente+"-Prueba"+conexiones
    archivoPorEscribir = os.path.join(path_archivos, nombre_archivo)
    file1 = open(archivoPorEscribir, "w")
    file1.write(recibido)
    file1.close()
#    log=log+"\n Entrega exitosa: "


    file_hash = hashlib.sha256()
    with open(archivoPorEscribir, 'rb') as f:
        fb = f.read(BLOCK_SIZE)
        while len(fb) > 0:
            file_hash.update(fb)
            fb = f.read(BLOCK_SIZE)
    resultadoHash = file_hash.hexdigest()
#log=log+"\n Tiempo de transferencia: "
#log=log+"\n Número de paquetes recibidos: "++" número de bytes recibidos: "
obj.close()
print("Conexión cerrada")


if __name__ == '__main__':
    print_hi('Cliente')


