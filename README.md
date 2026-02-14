<div align="center">
  <h1>🔍 Simple TCP Port Scanner</h1>
  
  <p>
    <strong>Scanner de portas TCP leve e didático feito em Python</strong><br>
    Perfeito para quem está começando em redes, pentest e cibersegurança.
  </p>

  <p>
    <img src="https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
    <img src="https://img.shields.io/badge/Status-Em%20desenvolvimento-success?style=for-the-badge" alt="Status"/>
    <img src="https://img.shields.io/github/license/matheuss-dsr/scanner-portas?style=for-the-badge" alt="License MIT"/>
    <img src="https://img.shields.io/github/stars/matheuss-dsr/scanner-portas?style=for-the-badge" alt="Stars"/>
  </p>
</div>

<br>

## 📌 Sobre o projeto

Este é um **scanner de portas TCP simples** que verifica se portas específicas ou um intervalo de portas estão abertas em um host alvo, utilizando conexão TCP completa (connect scan).

**Funcionalidades atuais**
- Escaneia intervalo de portas (ex: 1-1024)
- Escaneia portas específicas (ex: 22,80,443)
- Usa threads para acelerar o scan
- Timeout configurável
- Saída clara com portas abertas destacadas

<br>

## 🚀 Como usar (rápido)

```bash
# 1. Clone o repositório
git clone https://github.com/matheuss-dsr/scanner-portas.git
cd scanner-portas

# 2. (opcional) Ambiente virtual
python -m venv venv
source venv/bin/activate          # Linux / macOS
# ou no Windows: venv\Scripts\activate

# 3. Instale dependências (quase nenhuma)
pip install -r requirements.txt

# 4. Exemplos de uso

# Scan de portas comuns em um host público de teste
python main.py scanme.nmap.org -p 21,22,80,443,3389

# Scan de portas baixas (1-1000) em máquina local
python main.py 127.0.0.1 -p 1-1000 --threads 150

# Scan completo com mais velocidade
python main.py 192.168.1.254 -p 1-65535 -t 300 --timeout 0.8

# Ver todos os argumentos
python main.py --help