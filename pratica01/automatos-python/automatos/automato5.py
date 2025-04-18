from automata.fa.dfa import DFA

automato05 = DFA(
    states={'q0', 'q1', 'q2', 'q3'},
    input_symbols={'a', 'b'},
    transitions={
        'q0': {'a': 'q1', 'b': 'q2'},
        'q1': {'a': 'q0', 'b': 'q3'},
        'q2': {'a': 'q3', 'b': 'q0'},
        'q3': {'a': 'q2', 'b': 'q1'},
    },
    initial_state='q0',
    final_states={'q0'}
)