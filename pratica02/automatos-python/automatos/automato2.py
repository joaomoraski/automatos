from automata.fa.nfa import NFA

automato02 = NFA(
    states={'q0', 'q1', 'q2', 'q3', 'q4'},
    input_symbols={'0', '1'},
    transitions={
        'q0': {'0': {'q1'}, '1': {'q1'}},
        'q1': {'0': {'q0'}, '1': {'q2'}},
        'q2': {'0': {'q3'}, '1': {'q1'}},
        'q3': {'0': {'q0'}, '1': {'q4'}},
        'q4': {'0': {'q3'}, '1': {'q1'}},
    },
    initial_state='q0',
    final_states={'q3', 'q4'}
)