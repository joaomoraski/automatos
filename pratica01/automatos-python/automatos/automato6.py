from automata.fa.dfa import DFA

automato06 = DFA(
    states={'q0', 'q1', 'q2', 'q3', 'q4'},
    input_symbols={'a', 'b'},
    transitions={
        'q0': {'a': 'q1', 'b': 'q2'},
        'q1': {'a': 'q0', 'b': 'q3'},
        'q2': {'a': 'q4', 'b': 'q3'},
        'q3': {'a': 'q4', 'b': 'q2'},
        'q4': {'a': 'q4', 'b': 'q4'},
    },
    initial_state='q0',
    final_states={'q0'}
)