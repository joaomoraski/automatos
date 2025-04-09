import sys

from automatos.automato1 import automato01
from automatos.automato2 import automato02
from automatos.automato3 import automato03
from automatos.automato3_1 import automato03_1
from automatos.automato4 import automato04
from automatos.automato5 import automato05
from automatos.automato6 import automato06
from automatos.automato7 import automato07
from user_input import user_input

automatos: dict = {
    1: automato01,
    2: automato02,
    3: automato03,
    31: automato03_1,
    4: automato04,
    5: automato05,
    6: automato06,
    7: automato07,
}

def main():
    arg = int(sys.argv[1])
    print(f"Executando automato {arg}")

    automato = automatos.get(arg)

    if automato:
        user_input(automato)
    else:
        print("Número de automato inválido")

if __name__ == "__main__":
    main()
