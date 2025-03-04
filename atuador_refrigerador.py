import socket
import json

class AtuadorRefrigerador:
    def __init__(self, id, host='localhost', port=5000):
        self.id = id
        self.host = host
        self.port = port

    def start(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((self.host, self.port))
            while True:
                data = s.recv(1024).decode('utf-8')
                if data:
                    header, dados = data.split(':', 1)
                    dados = json.loads(dados)
                    if header == 'REFRIGERADOR':
                        print(f"Refrigerador {dados['acao']}")

if __name__ == "__main__":
    atuador = AtuadorRefrigerador(id=1)
    atuador.start()