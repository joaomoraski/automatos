from automata.fa.dfa import DFA

automato09 = DFA(
    states={'q0', 'q1', 'q2', 'q3', 'q4', 'q5'},
    input_symbols={'a', 'b'},
    transitions={
        'q0': {'a': 'q3', 'b': 'q1'},
        'q1': {'a': 'q4', 'b': 'q2'},
        'q2': {'a': 'q5', 'b': 'q0'},
        'q3': {'a': 'q0', 'b': 'q4'},
        'q4': {'a': 'q1', 'b': 'q5'},
        'q5': {'a': 'q2', 'b': 'q3'},
    },
    initial_state='q0',
    final_states={'q3'}
)
