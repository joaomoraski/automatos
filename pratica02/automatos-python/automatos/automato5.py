from automata.fa.nfa import NFA

automato05 = NFA(
    states={'q0', 'q1', 'q2'},
    input_symbols={'0', '1'},
    transitions={
        'q0': {'1': {'q0'}, '0': {'q0', 'q1'}},
        'q1': {'0': {'q2'}},
    },
    initial_state='q0',
    final_states={'q2'}
)
