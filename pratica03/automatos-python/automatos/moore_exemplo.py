from automata.fa.Moore import Moore

moore = Moore(['q0', 'q1', 'q2', 'q3'],
              ['a', 'b'],
              ['0', '1'],
              {
                  'q0': {
                      'a': 'q1',
                      'b': 'q3'
                  },
                  'q1': {
                      'a': 'q3',
                      'b': 'q1'
                  },
                  'q2': {
                      'a': 'q0',
                      'b': 'q3'
                  },
                  'q3': {
                      'a': 'q3',
                      'b': 'q2'
                  }
              },

              'q0',
              {
                  'q0': '1',
                  'q1': '0',
                  'q2': '0',
                  'q3': '1'
              }
              )
