import sys

from automatos.automato1 import automato01
from automatos.automato2 import automato02
from automatos.automato3 import automato03
from automatos.automato4 import automato04
from automatos.automato5 import automato05
from automatos.automato6 import automato06
from automatos.automato7 import automato07
from automatos.automato8 import automato08
from automatos.automato9 import automato09
import user_input

def main():
    arg = int(sys.argv[1])
    print(arg)
    if arg == 1:
        print("Executando automato 1")
        automato01.show_diagram()
        user_input.user_input(automato01)
    elif arg == 2:
        print("Executando automato 2")
        user_input.user_input(automato02)
    elif arg == 3:
        print("Executando automato 3")
        user_input.user_input(automato03)
    elif arg == 4:
        print("Executando automato 4")
        user_input.user_input(automato04)
    elif arg == 5:
        print("Executando automato 5")
        user_input.user_input(automato05)
    elif arg == 6:
        print("Executando automato 6")
        user_input.user_input(automato06)
    elif arg == 7:
        print("Executando automato 7")
        user_input.user_input(automato07)
    elif arg == 8:
        print("Executando automato 8")
        user_input.user_input(automato08)
    elif arg == 9:
        print("Executando automato 9")
        user_input.user_input(automato09)


if __name__ == "__main__":
    main()