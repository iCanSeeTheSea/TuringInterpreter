class TuringMachine:
    def __init__(self):
        self._tape = input('').split(' ')
        self._head = 0
        self._state = 'b'
        self._operand = '0000'
        self._jump = 0
        self._step = True
        self._state_to_function = {
            'b': self._assign_operand,
            'o': self._assign_operator,
            'c': self._recognise_input,
            '+': self._add,
            '*': self._prod,
            '-': self._sub,
            '/': self._div,
        }

    def _move_head(self, direction):
        match direction:
            case '<':
                self._head -= 1
                if self._head < 0:
                    self._head = 0
            case '>':
                self._head += 1
                if self._head >= len(self._tape):
                    self._tape += [' ']
            case '~':
                pass

    def _recognise_input(self, cell):
        if cell in ('*', '+', '-', '/'):
            return self._assign_operator(cell)
        elif cell == ' ':
            self._state = 'T'
            return self._operand, '~'
        else:
            return self._assign_operand(cell)

    def _assign_operator(self, operator):
        self._state = operator
        return operator, '>'

    def _assign_operand(self, operand):
        self._state = 'o'
        self._operand = operand
        return operand, '>'

    def _add(self, cell):
        self._state = 'c'
        self._operand = f'{int(self._operand) + int(cell)}'
        return cell, '>'

    def _prod(self, cell):
        self._state = 'c'
        self._operand = f'{int(self._operand) * int(cell)}'
        return cell, '>'

    def _div(self, cell):
        self._state = 'c'
        self._operand = f'{int(self._operand) // int(cell)}'
        return cell, '>'

    def _sub(self, cell):
        self._state = 'c'
        self._operand = f'{int(self._operand) - int(cell)}'
        return cell, '>'

    def process(self):
        self.output_tape()
        while self._state != 'T':
            if self._step:
                _ = input('')
            cell = self._tape[self._head]
            self._tape[self._head], direction = self._state_to_function[self._state](cell)
            self._move_head(direction)
            self.output_tape()

    def output_tape(self):
        print(
            f"S{self._state}X{self._operand}\n ━┳━{'━┳━'.join(['━━━━' for _ in range(len(self._tape))])}━┳━"
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
machine.process()
