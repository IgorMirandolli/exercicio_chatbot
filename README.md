# Exercicio Chatbot AIML

Este projeto implementa um chatbot simples em Python usando PyAIML3.

## Arquivos

- `main.py`: programa principal do chatbot.
- `brain.xml`: base de conhecimento em AIML.
- `requirements.txt`: dependencia do PyAIML3.

## Instalar no Windows PowerShell

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Instalar no Prompt de Comando

```bat
python -m venv venv
venv\Scripts\activate.bat
pip install -r requirements.txt
```

Se o comando `python` nao existir, instale o Python em https://www.python.org/downloads/ e marque a opcao **Add python.exe to PATH**. Neste computador, o Python 3.11 foi instalado em `%LOCALAPPDATA%\Programs\Python\Python311`.

## Executar

```powershell
python main.py brain.xml
```

Exemplos de mensagens para testar:

```text
oi
como vai voce
meu nome e Ana
qual e o meu nome
posso comprar uma passagem para Recife
posso pagar com cartao
qual e o meu destino
ajuda
sair
```
