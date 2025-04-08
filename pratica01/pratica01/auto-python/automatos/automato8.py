from automata.fa.dfa import DFA

automato08 = DFA(
    states={'q1', 'q2'},
    input_symbols={'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'},
    transitions={
        'q1': {
            '0': 'q1', '5': 'q1',
            '1': 'q2', '3': 'q2', '5': 'q2',
            '7': 'q2', '9': 'q2', '2': 'q2',
            '4': 'q2', '6': 'q2', '8': 'q2',
        },
        'q2': {
            '1': 'q2', '3': 'q2', '5': 'q2',
            '7': 'q2', '9': 'q2', '2': 'q2',
            '0': 'q1', '5': 'q1', '4': 'q2',
            '6': 'q2', '8': 'q2'
        },
    },
    initial_state='q1',
    final_states={'q1'}
)
