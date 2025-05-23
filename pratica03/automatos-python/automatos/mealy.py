from automata.fa.Mealy import Mealy

mealy = Mealy(
    ['q0', 'q1', 'q2'],
    ['a', 'b', 'c'],
    ['', '1', '2'],
    {
        'q0': {
            'a': ('q0', '1'),
            'b': ('q1', '')
        },

        'q1': {
            'a': ('q0', '1'),
            'b': ('q1', ''),
            'c': ('q2', '2')
        },

        'q2': {
            'a': ('q0', '1'),
            'b': ('q1', ''),
            'c': ('q2', '2')
        },
    },
    'q0'
)
