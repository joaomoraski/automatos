from automata.fa.dfa import DFA

automato04 = DFA(
    states={'q0', 'q1', 'q2'},
    input_symbols={'a', 'b'},
    transitions={
        'q0': {'a': 'q1', 'b': 'q1'},
        'q1': {'a': 'q2', 'b': 'q2'},
        'q2': {'a': 'q0', 'b': 'q0'},
    },
    initial_state='q0',
    final_states={'q0'}
)