class Circle:
    def __init__(self, radius):
        self.radius = radius

    def resize(self, factor):
        self.radius *= factor

    def __str__(self):
        return f'A circle of radius {self.radius}'


class Square:
    def __init__(self, side):
        self.side = side

    def __str__(self):
        return f'A square with side {self.side}'


class ColoredShape:
    def __init__(self, shape, color):
        self.color = color
        self.shape = shape

    def resize(self, factor):
        if hasattr(self.shape, 'side'):
            self.shape.side = self.shape.side * factor
        else:
            self.shape.resize(factor)

    def __str__(self):
        if isinstance(self.shape, Circle):
            return (f'A circle of radius {self.shape.radius} '
                    f'has the color {self.color}')
        else:
            return (f'A square with side {self.shape.side} '
                    f'has the color {self.color}')


if __name__ == '__main__':
    shape, size, color = input().split()
    if shape == 'c':
        circle = ColoredShape(Circle(int(size)), color)
        result1 = str(circle)
        circle.resize(2)
        result2 = str(circle)
        print(f'{result1} {result2}')

    if shape == 's':
        square = ColoredShape(Square(int(size)), color)
        result1 = str(square)
        square.resize(2)
        result2 = str(square)
        print(f'{result1} {result2}')
