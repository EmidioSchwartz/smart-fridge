import socket
import json
import time
import random

class SensorEstoque:
    def __init__(self, id, host='localhost', port=5000):
        self.id = id
        self.host = host
        self.port = port

    def start(self):
        while True:
            estoque = random.randint(0, 100)
            mensagem = f"SENSOR_ESTOQUE:{json.dumps({'id': self.id, 'estoque': estoque})}"
            self.enviar_mensagem(mensagem)
            time.sleep(15)

    def enviar_mensagem(self, mensagem):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((self.host, self.port))
            s.sendall(mensagem.encode('utf-8'))

if __name__ == "__main__":
    sensor = SensorEstoque(id=3)
    sensor.start()