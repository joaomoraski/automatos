def user_input(my_automaton):
    try:
        while True:
            if my_automaton.accepts_input(input("Manda o input ai: ")):
                print("Aceito")
            else:
                print("Rejeitado")
    except KeyboardInterrupt:
        print("")