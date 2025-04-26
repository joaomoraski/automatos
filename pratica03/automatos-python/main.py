from sys import argv

from automatos.moore_exemplo import moore as moore_exemplo
from automatos.moore import moore
from automatos.mealy import mealy

maquinas: dict = {
    "moore_exemplo": moore_exemplo,
    "moore": moore,
    "mealy": mealy,
}

def main():
    if len(argv) < 3:
        raise IOError("Use Moore.py file.cm")

    arg = argv[1]
    print(f"Executando máquina de {arg}")

    # python3 main.py mealy teste_mealy01.cm

    aux = argv[2].split('.')

    if aux[-1] != 'cm':
        raise IOError("Not a .cm file!")

    data = open(argv[2])
    source_file = data.read()

    maquina = maquinas[argv[1]]

    # Printa a definição da máquina.
    print(maquina)

    # Entrada lida do arquivo.
    print(f"Input: {source_file}")

    # Mostra a saida.
    print(f"Output: {maquina.get_output_from_string(source_file)}")


if __name__ == "__main__":
    main()


