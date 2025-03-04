import socket
import json

class Cliente:
    def __init__(self, host='localhost', port=5000):
        self.host = host
        self.port = port

    def consultar_estado(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((self.host, self.port))
            s.sendall("CLIENTE_CONSULTA:{}".encode('utf-8'))
            data = s.recv(1024).decode('utf-8')
            return json.loads(data)

    def configurar_temperatura(self, temperatura_ideal):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((self.host, self.port))
            mensagem = f"CLIENTE_CONFIG:{json.dumps({'temperatura_ideal': temperatura_ideal})}"
            s.sendall(mensagem.encode('utf-8'))

if __name__ == "__main__":
    cliente = Cliente()
    estado = cliente.consultar_estado()
    print("Estado atual da geladeira:", estado)
    cliente.configurar_temperatura(5)  # Configura a temperatura ideal para 5°C