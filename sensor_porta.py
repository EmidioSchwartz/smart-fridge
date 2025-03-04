import socket
import json
import time
import random

class SensorPorta:
    def __init__(self, id, host='localhost', port=5000):
        self.id = id
        self.host = host
        self.port = port

    def start(self):
        while True:
            estado = random.choice([True, False])
            mensagem = f"SENSOR_PORTA:{json.dumps({'id': self.id, 'estado': estado})}"
            self.enviar_mensagem(mensagem)
            time.sleep(5)

    def enviar_mensagem(self, mensagem):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((self.host, self.port))
            s.sendall(mensagem.encode('utf-8'))

if __name__ == "__main__":
    sensor = SensorPorta(id=2)
    sensor.start()