import re
import sys
import unicodedata

import aiml


def filter(text):
    """Remove acentos, pontuacao e padroniza a entrada para o AIML."""
    text = (
        unicodedata.normalize("NFKD", text)
        .encode("ASCII", "ignore")
        .decode("utf-8")
    )
    text = re.sub(r"[^\w\s]", "", text)
    return " ".join(text.upper().split())


def main():
    if len(sys.argv) < 2:
        print("Uso: python main.py brain.xml")
        return

    kb = sys.argv[1]
    k = aiml.Kernel()
    k.learn(kb)

    print("Chatbot iniciado. Digite SAIR para encerrar.")
    while True:
        message = input("> ")
        message = filter(message)

        if message in {"SAIR", "EXIT", "QUIT"}:
            print("Ate logo!")
            break

        response = k.respond(message)
        print(response or "Eu nao entendi. Tente perguntar de outra forma.")


if __name__ == "__main__":
    main()
