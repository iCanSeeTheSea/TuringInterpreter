class TuringMachine:

    def __init__(self):

        self._mapping_table = {
            'b': self._move_head('b', '>'),
            'b+': self._assign_operator('o', '+', '>'),
        }
        self._tape = input('').split(' ')
        print(self._tape)

        self._head = 0
        self._state = 'B'
        self._operand = '0000'
        self._operator = ''
        self._cache = {'operator': '', 'operand': '', 'head': 0}
        self._step = True

    def _move_head(self, state, direction):
        self._state = state
        match direction:
            case '<':
                self._head -= 1
                if self._head < 0:
                    self._head = 0
            case '>':
                self._head += 1
                if self._head >= len(self._tape):
                    self._tape += ['  ']

    def _assign_operator(self, state, operator, direction):
        self._state = state
        self._operator = operator
        if direction:
            self._move_head(state, direction)

    def _assign_operand(self, state, operand, direction):
        self._state = state
        self.operand = operand
        if direction:
            self._move_head(state, direction)

    def process(self):
        self.output_head()
        while self._state != 'T':
            if self._step:
                _ = input('')
            self.output_head()

    def output_tape(self):
        print(
            f"S{self._state}\n ━┳━{'━┳━'.join(['━━━━' for _ in range(len(self._tape))])}━┳━"
        )
        print(f"{' ┃ '.join([' '] + [c + ' '*(4-len(c)) for c in self._tape])} ┃  ")
        print(
            f" ━┻━{'━┻━'.join(['━━━━' for _ in range(len(self._tape))])}━┻━"
        )
        print(
            f"    {''.join(['       ' for _ in range(self._head)])}↑"
        )

    def output_head(self):

        print(f"S{self._state}\n {'━┳━━'.join(['' for _ in range(10)])}━┳━")
        print(
            f"  ┃ {' ┃ '.join(self._tape[self._head - 4: self._head + 5] + [' ' for _ in range(5 - (len(self._tape) - self._head)) if len(self._tape) - self._head < 5])} ┃  ")
        print(f" {'━┻━━'.join(['' for _ in range(10)])}━┻━")
        print("                    ↑")


machine = TuringMachine()