import socket
import json
import threading
import time

class Gerenciador:
    def __init__(self, host='localhost', port=5000):
        self.host = host
        self.port = port
        self.sensores = {
            'temperatura': {'id': 1, 'valor': 0},
            'porta': {'id': 2, 'estado': False, 'tempo_aberta': 0},
            'estoque': {'id': 3, 'valor': 0}
        }
        self.atuadores = {
            'refrigerador': {'id': 1, 'estado': 'desligado'},
            'luz': {'id': 2, 'estado': 'desligado'},
            'alarme': {'id': 3, 'estado': 'desligado'}
        }
        self.lock = threading.Lock()
        self.temperatura_ideal = 5  # Temperatura ideal configurável pelo cliente

    def start(self):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((self.host, self.port))
        server_socket.listen(5)
        print(f"[GERENCIADOR] Iniciado em {self.host}:{self.port}. Aguardando conexões...")

        # Thread para monitorar o tempo que a porta fica aberta
        threading.Thread(target=self.monitorar_porta).start()

        while True:
            client_socket, addr = server_socket.accept()
            print(f"[GERENCIADOR] Nova conexão estabelecida com {addr}.")
            threading.Thread(target=self.handle_client, args=(client_socket,)).start()

    def handle_client(self, client_socket):
        with client_socket:
            while True:
                data = client_socket.recv(1024).decode('utf-8')
                if not data:
                    print(f"[GERENCIADOR] Conexão com o cliente encerrada.")
                    break

                header, dados = data.split(':', 1)
                dados = json.loads(dados)

                if header == 'SENSOR_TEMP':
                    self.sensores['temperatura']['valor'] = dados['temperatura']
                    print(f"[SENSOR TEMPERATURA] Leitura recebida: {dados['temperatura']}°C.")
                    if dados['temperatura'] > self.temperatura_ideal:
                        print(f"[GERENCIADOR] Temperatura acima do ideal ({self.temperatura_ideal}°C). Ligando refrigerador.")
                        self.controlar_atuador('refrigerador', 'ligar')
                    else:
                        print(f"[GERENCIADOR] Temperatura dentro do ideal ({self.temperatura_ideal}°C). Desligando refrigerador.")
                        self.controlar_atuador('refrigerador', 'desligar')

                elif header == 'SENSOR_PORTA':
                    self.sensores['porta']['estado'] = dados['estado']
                    estado_porta = "aberta" if dados['estado'] else "fechada"
                    print(f"[SENSOR PORTA] Porta {estado_porta}.")
                    if dados['estado']:
                        print(f"[GERENCIADOR] Porta aberta. Acendendo luz interna.")
                        self.controlar_atuador('luz', 'ligar')
                    else:
                        print(f"[GERENCIADOR] Porta fechada. Apagando luz interna.")
                        self.controlar_atuador('luz', 'desligar')

                elif header == 'SENSOR_ESTOQUE':
                    self.sensores['estoque']['valor'] = dados['estoque']
                    print(f"[SENSOR ESTOQUE] Leitura recebida: {dados['estoque']}% de estoque.")

                elif header == 'CLIENTE_CONSULTA':
                    print(f"[CLIENTE] Solicitação de consulta recebida.")
                    client_socket.send(json.dumps(self.sensores).encode('utf-8'))
                    print(f"[GERENCIADOR] Estado atual enviado ao cliente.")

                elif header == 'CLIENTE_CONFIG':
                    self.temperatura_ideal = dados['temperatura_ideal']
                    print(f"[CLIENTE] Temperatura ideal configurada para {self.temperatura_ideal}°C.")

                time.sleep(2)  # Aumenta o intervalo entre os logs para 2 segundos

    def controlar_atuador(self, atuador, acao):
        with self.lock:
            if atuador in self.atuadores:
                self.atuadores[atuador]['estado'] = acao
                print(f"[ATUADOR {atuador.upper()}] Comando recebido: {acao}.")
                # Enviar comando ao atuador (simulado aqui, pois os atuadores estão em processos separados)
                if atuador == 'alarme' and acao == 'ligar':
                    print(f"[ALARME] Alarme ativado! Porta aberta por mais de 30 segundos.")

    def monitorar_porta(self):
        while True:
            if self.sensores['porta']['estado']:
                self.sensores['porta']['tempo_aberta'] += 1
                if self.sensores['porta']['tempo_aberta'] >= 30:
                    print(f"[GERENCIADOR] Porta aberta por 30 segundos. Ativando alarme.")
                    self.controlar_atuador('alarme', 'ligar')
            else:
                self.sensores['porta']['tempo_aberta'] = 0
                self.controlar_atuador('alarme', 'desligar')
            time.sleep(1)  # Verifica o estado da porta a cada 1 segundo

if __name__ == "__main__":
    gerenciador = Gerenciador()
    gerenciador.start()