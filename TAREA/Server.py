import psutil
import subprocess
import socket

HOST = "0.0.0.0"  # IP a la que nos conectamos
PORT = 9999  # Puerto abierto
number_connection = 1  # Numero de conexiones

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(number_connection)

class Controladores:

    def __init__(self, name=None, pid=None):
        self.pid = pid
        self.name = name
        pass

    def crear_proceso(self):
        self.process = subprocess.Popen([self.name])
        return self.process

    def matar_proceso(self):
     for proc in psutil.process_iter(['pid', 'name']):
      if proc.info['name'] == self.process:
        proc.kill() # Termina el proceso inmediatamente
        print(f"Proceso {self.process} (PID: {proc.info['pid']}) matado.")

    def ver_estadisticas():
        cpu = psutil.cpu_percent(interval=1)
        mem = psutil.virtual_memory().percent
        metricas = f"CPU {cpu} % || RAM {mem} %"
        return metricas

    def procesos_en_ejecucion():
        lista_procesos = []
        for list in psutil.process_iter(["pid", "name", "username"]):
            print(list.info)
            lista_procesos.append(list.info)
        return lista_procesos
            
while True:
  
  cliente, addr = server.accept()
  print(addr)

  while True: 
    partes = cliente.recv(1024).decode().split("/")
    print(partes)
    modo = partes[0]

    if len(partes)>1:
     
     programa = partes[1]  
    
    print(modo)

    match modo:

        case "monitorea":
            metricas = Controladores.ver_estadisticas()
            print(metricas)
            cliente.sendall(f"{metricas}".encode())

        case "procesos":
            procesos_a_enviar = Controladores.procesos_en_ejecucion()
            print(procesos_a_enviar)
            cliente.sendall(f"{procesos_a_enviar}".encode())
            
        case "terminando":
           Controladores("", programa).matar_proceso()

        case "iniciar":
            metricas = Controladores(programa).crear_proceso()
            print(metricas)
            cliente.sendall(f"{metricas}".encode())

        case "salir":
            print("saliendo")
            cliente.sendall("Terminado, desconenctando del cliente...".encode())
            cliente.close()
            break


