import middleware as md

lista_cosas = [
    "iniciar programa",
    "terminar programa",
    "monitoreo",
    "procesos actuales",
    "terminar"
]  # lista de las 4 cosas que puede hacer el servidor.

orden_d = None #

middleware = md.conexion()

class Cosas_para_hacer:  # organizacion de las cosas para hacer.

    def __init__(self, orden = ""):
        self.orden = orden
        pass

    def iniciar_programa(self):
        modo = "iniciar"
        with open("Historial.txt", "a") as guardado:  # guarda las cosas en un documento para mantener seguimiento, como un historial.
            guardado.write(f"\n{str(self.orden)} {modo}\n")
        return modo

    def matar_programa(self):
        modo = "terminando"
        with open("Historial.txt", "a") as guardado:
            guardado.write(f"\n{str(self.orden)} {modo}\n")
        return modo

    def monitorear_RAM_CPU(self):
        print("Monitoreando:")
        return "monitorea"

    def procesos(self):  # monitorea procesos en uso.
        print("Procesos en ejecución:")
        return "procesos"

  
while True:
    
   host_seleccionada = middleware.IP_Seleccionada()

   conexion = middleware.conectar(host_seleccionada)

   while conexion == "postivo":
      
    try:
        print("¿Qué quieres hacer ahora?\n")

        for indice, cosas in enumerate(lista_cosas, start=1):
            print(indice, cosas)

        elección = int(input("\nR//"))

        match elección:

            case 1: #iniciar programas
                orden = input("\nEscribe:> ")
                seleccion = Cosas_para_hacer(orden).iniciar_programa()
                print(seleccion, orden)
                middleware.enviar_comando(f"{seleccion}/{orden}")

            case 2: #detener programas
                middleware.enviar_comando(f"{seleccion}/{orden}")
                middleware.data()   # Recibe lista

            case 3:#monitorear RAM CPU
                seleccion = Cosas_para_hacer().monitorear_RAM_CPU() 
                middleware.enviar_comando(f"{seleccion}/{orden_d}")

            case 4: #Procesos
                seleccion = Cosas_para_hacer().procesos()
                middleware.enviar_comando(f"{seleccion}/{orden_d}")

            case 5: #desconeta el server y crea más cosas
                middleware.enviar_comando("salir")
                middleware.data()
                middleware.terminar_transmision()
                conexion = "negativo"
                break

            case _:
                print("Selecciona las opciones dadas")
                

        print(f"\n{seleccion}\n")
        print(f"{middleware.data()}\n")

    except (ValueError, IndexError):  # por si hay errores.
        print("\nSelecciona una opción válida\n")
   else: pass
