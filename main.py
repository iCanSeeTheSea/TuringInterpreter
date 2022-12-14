class TuringMachine:
    def __init__(self):
        self._operations = ('*', '+', '-', '/', '?=', '?<', '?>')
        self._tape = [''] * 3 + input('').split(' ')
        self._head = 3
        self._state = 'bgn'
        self._operand = '000'
        self._step = True
        self._state_to_function = {
            'bgn': self._check_start,
            'opr': self._assign_operator,
            'cnt': self._recognise_input,
            'gtv': self._go_to_vars,
            'prs': self._parse_tape,
            'chk': self._check_var,
            'rd': self._read_var,
            'wrt': self._write_var,
            '?=': self._if_equal,
            '?>': self._if_greater,
            '?<': self._if_less,
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
            case '>>':
                self._head = int(self._tape[0])
            case '~':
                pass

    def _check_start(self, cell):
        if cell == ':':
            return 'cnt', cell, '>'
        return 'bgn', cell, '>'

    def _recognise_input(self, cell):
        if cell in self._operations:
            return self._assign_operator(cell)
        elif cell == ' ':
            return 'T', self._operand, '~'
        elif cell.isalpha():
            return self._get_var(cell)
        elif cell == '=':
            ...
        else:
            return self._assign_operand(cell)

    def _assign_operator(self, operator):
        if operator in self._operations:
            return operator, operator, '>'

    def _assign_operand(self, operand):
        self._operand = operand
        return 'opr', operand, '>'

    def _get_var(self, cell):
        self._tape[0] = str(self._head)
        self._tape[1] = self._state
        self._tape[2] = self._operand
        self._operand = cell
        return 'gtv', cell, '<'

    def _if_equal(self, cell):
        if cell.isalpha():
            return self._get_var(cell)
        if int(self._operand) == int(cell):
            self._operand = 'tru'
            return 'cnt', cell, '>'
        else:
            self._operand = 'fls'
            return 'cnt', cell, '>'

    def _if_greater(self, cell):
        if cell.isalpha():
            return self._get_var(cell)
        if int(self._operand) > int(cell):
            self._operand = 'tru'
            return 'cnt', cell, '>'
        else:
            self._operand = 'fls'
            return 'cnt', cell, '>'

    def _if_less(self, cell):
        if cell.isalpha():
            return self._get_var(cell)
        if int(self._operand) < int(cell):
            self._operand = 'tru'
            return 'cnt', cell, '>'
        else:
            self._operand = 'fls'
            return 'cnt', cell, '>'

    def _add(self, cell):
        if cell.isalpha():
            return self._get_var(cell)
        self._operand = f'{int(self._operand) + int(cell)}'
        return 'cnt', cell, '>'

    def _prod(self, cell):
        if cell.isalpha():
            return self._get_var(cell)
        self._operand = f'{int(self._operand) * int(cell)}'
        return 'cnt', cell, '>'

    def _div(self, cell):
        if cell.isalpha():
            return self._get_var(cell)
        self._operand = f'{int(self._operand) // int(cell)}'
        return 'cnt', cell, '>'

    def _sub(self, cell):
        if cell.isalpha():
            return self._get_var(cell)
        self._operand = f'{int(self._operand) - int(cell)}'
        return 'cnt', cell, '>'

    def _go_to_vars(self, cell):
        if cell == ':':
            return 'prs', cell, '<'
        return 'gtv', cell, '<'

    def _parse_tape(self, cell):
        if cell == self._operand:
            return 'chk', cell, '>'
        else:
            return 'prs', cell, '<'

    def _check_var(self, cell):
        if cell == '=':
            return 'rd', cell, '>'
        else:
            self._move_head('<')
            return 'prs', cell, '<'

    def _read_var(self, var):
        self._operand = var
        return 'wrt', var, '>>'

    def _write_var(self, cell):
        temp = self._operand
        self._operand = self._tape[2]
        return self._tape[1], temp, '~'

    def process(self):
        self.output_tape()
        while self._state != 'T':
            if self._step:
                _ = input('')
            cell = self._tape[self._head]
            self._state, self._tape[self._head], direction = self._state_to_function[self._state](cell)
            self._move_head(direction)
            self.output_tape()

    def output_tape(self):
        print(
            f"S{self._state}X{self._operand}\n ━┳━{'━┳━'.join(['━━━' for _ in range(len(self._tape))])}━┳━"
        )
        print(f"{' ┃ '.join([' '] + [(lambda c: c if len(c) == 3 else f'{c} ' if len(c) == 2 else f' {c} ' if len(c) == 1 else '   ')(c) for c in self._tape])} ┃  ")
        print(
            f" ━┻━{'━┻━'.join(['━━━' for _ in range(len(self._tape))])}━┻━"
        )
        print(
            f"     {''.join(['      ' for _ in range(self._head)])}↑"
        )


machine = TuringMachine()
machine.process()