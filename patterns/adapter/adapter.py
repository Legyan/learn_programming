class Square:
    def __init__(self, side=0):
        self.side = side


def calculate_area(rc):
    return rc.width * rc.height


class SquareToRectangleAdapter:
    def __init__(self, square):
        self.square = square

    @property
    def width(self):
        return self.square.side

    @property
    def height(self):
        return self.square.side


if __name__ == '__main__':
    x, y = input().split()
    sq = Square(int(x))
    adapter = SquareToRectangleAdapter(sq)
    res1 = calculate_area(adapter)
    sq.side = int(y)
    res2 = calculate_area(adapter)
    print(f'{res1} {res2}')
