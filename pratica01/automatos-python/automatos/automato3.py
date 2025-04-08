from automata.fa.dfa import DFA

automato03 = DFA(
    states={'q0', 'q1', 'q2', 'q3', 'q4'},
    input_symbols={'a', 'b'},
    transitions={
        'q0': {'b': 'q1', 'a': 'q4'},
        'q1': {'b': 'q2', 'a': 'q1'},
        'q2': {'a': 'q3', 'b': 'q4'},
        'q3': {'b': 'q4', 'a': 'q4'},
        'q4': {'a': 'q4', 'b': 'q4'},
    },
    initial_state='q0',
    final_states={'q3'}
)