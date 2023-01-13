class CodeBuilder:
    def __init__(self, root_name):
        self.root_name = root_name
        self.indent = 2
        self.elements = [f'class {self.root_name}:']

    def add_field(self, type, name):
        self.elements.append(
            self.indent * 2 * ' ' + f'self.{type} = \'{name}\''
        )
        return self

    def __str__(self):
        if len(self.elements) == 1:
            self.elements.append(self.indent * ' ' + 'pass')
        else:
            init_line = self.indent * ' ' + 'def __init__(self):'
            self.elements.insert(1, init_line)
        return '\n'.join(self.elements)


if __name__ == '__main__':
    cb_empty = CodeBuilder('Foo')
    print(cb_empty)
    cb_full = CodeBuilder('Person').add_field(
        'name', 'Lev').add_field('age', '0')
    print(cb_full)


def preprocess(s=''):
    return s.strip().replace('\r\n', '\n')
