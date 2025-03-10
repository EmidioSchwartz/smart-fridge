﻿smart-fridge
# 🧊 Trabalho de Redes - Gerenciador de Geladeira

## 📌 Sobre o Projeto
Este projeto é um sistema de gerenciamento de geladeira utilizando sensores e atuadores. Ele simula um ambiente onde diferentes componentes da geladeira interagem através de comunicação em rede.

## ⚙️ Funcionalidades
- **Sensores**:
  - `sensor_temperatura.py`: Monitora a temperatura interna.
  - `sensor_porta.py`: Detecta abertura e fechamento da porta.
  - `sensor_estoque.py`: Controla o estoque de produtos dentro da geladeira.
- **Atuadores**:
  - `atuador_refrigerador.py`: Controla o sistema de refrigeração.
  - `atuador_luz.py`: Liga e desliga a luz interna.
  - `atuador_alarme.py`: Aciona um alarme caso haja problemas.
- **Cliente**:
  - `cliente.py`: Simula a interação do usuário com a geladeira.
- **Gerenciador**:
  - `GERENCIADOR.PY`: Responsável por orquestrar os componentes do sistema.

## 🛠️ Tecnologias Utilizadas
- **Python**
- **Sockets para comunicação entre os dispositivos**

## 🚀 Como Executar
1. Clone este repositório:
   ```sh
   git clone https://github.com/seu-usuario/seu-repositorio.git
   ```
2. Acesse o diretório do projeto:
   ```sh
   cd Trabalho-Redes-Geladeira
   ```
3. Execute o gerenciador para iniciar o sistema:
   ```sh
   python GERENCIADOR.PY
   ```
4. Para interagir com o sistema, execute o cliente:
   ```sh
   python cliente.py
   ```

## 📄 Licença
Este projeto é apenas para fins educacionais.

---
Se precisar de mais detalhes ou ajustes no README, é só avisar! 🚀


