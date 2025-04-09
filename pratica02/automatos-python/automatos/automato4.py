from automata.fa.nfa import NFA

automato04 = NFA(
    states={'q0', 'q1', 'q2'},
    input_symbols={'a', 'b', 'c'},
    transitions={
        'q0': {'a': {'q0'}, 'b': {'q1'}, 'c': {'q0'}},
        'q1': {'c': {'q2'}},
        'q2': {'a': {'q2'}, 'c': {'q2'}, '': {'q0'}},
    },
    initial_state='q0',
    final_states={'q2'}
)
