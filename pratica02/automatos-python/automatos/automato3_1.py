from automata.fa.nfa import NFA

automato03_1 = NFA(
    states={'q4', 'q5'},
    input_symbols={'1', '0'},
    transitions={
        'q4': {'0': {'q5'}, '1': {'q5'}},
        'q5': {'0': {'q4'}, '1': {'q4'}},
    },
    initial_state='q4',
    final_states={'q5'}
)
