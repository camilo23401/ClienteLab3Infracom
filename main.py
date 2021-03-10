import socket
import os
import hashlib
from datetime import datetime
import threading


def conexion():
    host = 'localhost'
    port = 8050
    path_archivos = "./ArchivosRecibidos"
    path_logs = "./Logs"

    BLOCK_SIZE = 65536
    conexiones = 25
    obj = socket.socket()

    obj.connect((host, port))
    obj.listen(conexiones)

    year=datetime.now().year
    mes = datetime.now().month
    dia = datetime.now().day
    hora= datetime.now().hour
    min = datetime.now().minute
    seg = datetime.now().second

    fecha= "/"+str(year)+"-"+str(mes)+"-"+str(dia)+"-"+str(hora)+"-"+str(min)+"-"+str(seg)+"log"
    print(fecha)
    archivolog = path_logs+fecha+".txt"
    file = open(archivolog, "w")

    cliente= threading.currentThread().getName()
    print("Cliente "+cliente)
    print("Conectado al servidor")

    while (True):
        mens = input("Mensaje de confirmacion. Listo para recibir un archivo")
        obj.send(mens.encode('ascii'))
        recibido = obj.recv(4096)
        log = "nombre del archivo: "
        log=log+" Tamaño: "+os.stat(recibido).st_size
        log = log+"\n Cliente: "+cliente
        nombre_archivo = cliente + "-Prueba" + str(conexiones)
        print(nombre_archivo)
        archivoPorEscribir = os.path.join(path_archivos, nombre_archivo)
        file1 = open(archivoPorEscribir, "w")
        file1.write(recibido)
        file1.close()
        log = log+"\n Entrega exitosa: "

        file_hash = hashlib.sha256()
        with open(archivoPorEscribir, 'rb') as f:
            fb = f.read(BLOCK_SIZE)
            while len(fb) > 0:
                file_hash.update(fb)
                fb = f.read(BLOCK_SIZE)
        resultadoHash = file_hash.hexdigest()
        log=log+"\n Tiempo de transferencia: "
        log=log+"\n Número de paquetes recibidos: "+" número de bytes recibidos: "
        file.write(log)
        file.close()
    obj.close()
    print("Conexión cerrada")


NUM_HILOS = 25

for num_hilo in range(NUM_HILOS):
    hilo = threading.Thread(target=conexion,name='Cliente'+str(num_hilo))
    hilo.start()

