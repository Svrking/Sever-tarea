import socket 
HOST = ["192.168.0.28", "192.168.0.29"] #seleccion entre las ips de los servers
PORT = 9999 

class conexion: #creamos una class para internconexión entre recursos
 
 def IP_Seleccionada(self): # selecciona la ip
    print("\nA que servidor desea conectarse?\n")
    for index, hosts in enumerate(HOST, start=1):
       print(index, hosts)
    return int(input("\nQue servidor deseas usar? "))
    
 def conectar(self, ip_seleccionada): #conecta y crea clientes constantemente
    self.cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
     print(HOST[ip_seleccionada-1], "\n")
     self.cliente.connect((HOST[ip_seleccionada-1], PORT))
     return "postivo"
    
    except (socket.gaierror, IndexError, ConnectionRefusedError, ValueError):
      print("\nNo se establecio la conexion")
    
 def enviar_comando(self, comando): 
    self.cliente.sendall(f"{comando}".encode())

 def data(self): #recibe la informacion de cualquiera de los servidores
    data = self.cliente.recv(10000000).decode()
    return data
 def terminar_transmision(self): #cierra la transmision
    self.cliente.close()
    

