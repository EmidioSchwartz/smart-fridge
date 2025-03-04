import socket
import json
import time
import random

class SensorTemperatura:
    def __init__(self, id, host='localhost', port=5000):
        self.id = id
        self.host = host
        self.port = port

    def start(self):
        while True:
            temperatura = random.randint(0, 10)
            mensagem = f"SENSOR_TEMP:{json.dumps({'id': self.id, 'temperatura': temperatura})}"
            self.enviar_mensagem(mensagem)
            time.sleep(10)

    def enviar_mensagem(self, mensagem):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((self.host, self.port))
            s.sendall(mensagem.encode('utf-8'))

if __name__ == "__main__":
    sensor = SensorTemperatura(id=1)
    sensor.start()