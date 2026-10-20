import socket

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    cliente.connect(("localhost", 5000))
except socket.error as e:
    print(f"Error al conectar con el servidor: {e}")
    exit()

while True:
    print("si quiere desconectarse escriba: salir")
    mensaje = input("Escriba su mensaje:")
    cliente.send(mensaje.encode())
    if mensaje.lower().strip() == "salir":
        print("Se ha desconectado exitosamente")
        cliente.close()
        break
    respuesta = cliente.recv(1024)
    print("Servidor:", respuesta.decode())
