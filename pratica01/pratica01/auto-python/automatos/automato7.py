from automata.fa.dfa import DFA

automato07 = DFA(
    states={'q1', 'q2'},
    input_symbols={'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'},
    transitions={
        'q1': {
            '0': 'q1', '2': 'q1', '4': 'q1', '6': 'q1', '8': 'q1',
            '1': 'q2', '3': 'q2', '5': 'q2', '7': 'q2', '9': 'q2'
        },
        'q2': {
            '1': 'q2', '3': 'q2', '5': 'q2', '7': 'q2', '9': 'q2',
            '0': 'q1', '2': 'q1', '4': 'q1', '6': 'q1', '8': 'q1'
        },
    },
    initial_state='q1',
    final_states={'q1'}
)
