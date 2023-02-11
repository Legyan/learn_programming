from enum import Enum, auto


class Token:
    class Type(Enum):
        INTEGER = auto()
        PLUS = auto()
        MINUS = auto()
        LPAREN = auto()
        RPAREN = auto()

    def __init__(self, type, text):
        self.type = type
        self.text = text

    def __str__(self):
        return f'`{self.text}`'


def lex(input_string):
    result = []
    i = 0
    while i < len(input_string):
        if input_string[i] == '+':
            result.append(Token(Token.Type.PLUS, '+'))
        elif input_string[i] == '-':
            result.append(Token(Token.Type.MINUS, '-'))
        elif input_string[i] == '(':
            result.append(Token(Token.Type.LPAREN, '('))
        elif input_string[i] == ')':
            result.append(Token(Token.Type.RPAREN, ')'))
        else:
            digits = [input_string[i]]
            for j in range(i + 1, len(input_string)):
                if input_string[j].isdigit():
                    digits.append(input_string[j])
                    i += 1
                else:
                    result.append(Token(Token.Type.INTEGER, ''.join(digits)))
                    break
        i += 1
    return result


class Integer:
    def __init__(self, value):
        self.value = value


class BinaryExpression:
    class Type(Enum):
        ADDITION = auto()
        SUBTRACTION = auto()

    def __init__(self):
        self.type = None
        self.left = None
        self.right = None

    @property
    def value(self):
        if self.type == self.Type.ADDITION:
            return self.left.value + self.right.value
        else:
            return self.left.value - self.right.value


def parse(tokens):
    result = BinaryExpression()
    have_ihs = False
    i = 0
    while i < len(tokens):
        token = tokens[i]
        if token.type == Token.Type.INTEGER:
            integer = Integer(int(token.text))
            if not have_ihs:
                result.left = integer
                have_ihs = True
            else:
                result.right = integer
        elif token.type == Token.Type.PLUS:
            result.type = BinaryExpression.Type.ADDITION
        elif token.type == Token.Type.MINUS:
            result.type = BinaryExpression.Type.SUBTRACTION
        elif token.type == Token.Type.LPAREN:
            j = i
            while j < len(tokens):
                if tokens[j].type == Token.Type.RPAREN:
                    break
                j += 1
            subexpression = tokens[i+1:j]
            element = parse(subexpression)
            if not have_ihs:
                result.left = element
                have_ihs = True
            else:
                result.right = element
            i = j
        i += 1
    return result


def calc(input_string):
    tokens = lex(input_string)
    print(' '.join((map(str, tokens))))
    parsed = parse(tokens)
    print(f'{input_string} = {parsed.value}')


if __name__ == '__main__':
    calc('(13+4)-(12+1)')
