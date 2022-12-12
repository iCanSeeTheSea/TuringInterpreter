class TransitionFunction:

    def __init__(self):
        self._mapping_table = {}

    def transition(self, state, operand):
        key = state + operand
        return self._mapping_table[key]

    def add_transition(self, key, output):
        self._mapping_table[key] = output

    def output(self):
        print(self._mapping_table)


class TuringMachine:

    def __init__(self):
        self._transf = TransitionFunction()
        self._tape = input('').split(' ')
        print(self._tape)

        self._head = 0
        self._state = 'B'
        self._memory = '0000'
        self._step = True

    def _execute(self):
        (state, output, direction) = (c for c in self._transf.transition(
            self._state, self._tape[self._head]))
        self._state = state
        self._tape[self._head] = output
        if direction == '<':
            self._head -= 1
            if self._head < 0:
                self._tape = [' '] + self._tape
                self._head = 0
        if direction == '>':
            self._head += 1
            if self._head >= len(self._tape):
                self._tape += ['  ']

    def process(self):
        self.output_head()
        while self._state != 'T':
            if self._step:
                _ = input('')
            self._execute()
            self.output_head()

    def output_tape(self):
        print(
            f"S{self._state}\n {'━┳━━'.join(['' for _ in range(len(self._tape) + 2)])}━┳━"
        )
        print(f"{' ┃ '.join([' '] + self._tape + [' '])} ┃  ")
        print(f" {'━┻━━'.join(['' for _ in range(len(self._tape) + 2)])}━┻━")
        print(f"    {''.join(['    ' for _ in range(self._head)])}↑")

    def output_head(self):

        print(f"S{self._state}\n {'━┳━━'.join(['' for _ in range(10)])}━┳━")
        print(
            f"  ┃ {' ┃ '.join(self._tape[self._head - 4: self._head + 5] + [' ' for _ in range(5 - (len(self._tape) - self._head)) if len(self._tape) - self._head < 5])} ┃  ")
        print(f" {'━┻━━'.join(['' for _ in range(10)])}━┻━")
        print("                    ↑")


machine = TuringMachine()