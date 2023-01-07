from random import randint


class Generator:
    def generate(self, count):
        return [randint(1, 9) for i in range(count)]


class Splitter:
    def split(self, array):
        result = []
        row_count = len(array)
        col_count = len(array[0])
        for r in range(row_count):
            the_row = []
            for c in range(col_count):
                the_row.append(array[r][c])
            result.append(the_row)
        for c in range(col_count):
            the_col = []
            for r in range(row_count):
                the_col.append(array[r][c])
            result.append(the_col)
        diag1 = []
        diag2 = []
        for c in range(col_count):
            for r in range(row_count):
                if c == r:
                    diag1.append(array[r][c])
                r2 = row_count - r - 1
                if c == r2:
                    diag2.append(array[r][c])
        result.append(diag1)
        result.append(diag2)
        return result


class Verifier:
    def verify(self, arrays):
        first = sum(arrays[0])
        for i in range(1, len(arrays)):
            if sum(arrays[i]) != first:
                return False
        return True


class MagicSquareGenerator:
    def generate(self, size):
        g = Generator()
        s = Splitter()
        v = Verifier()
        res = [[0], [1]]
        count = 0
        while not v.verify(res):
            matrix = []
            for i in range(size):
                line = g.generate(size)
                matrix.append(line)
            res = s.split(matrix)
            count += 1
        return matrix, count


if __name__ == '__main__':
    gen = MagicSquareGenerator()
    square, count = gen.generate(3)
    print(f'{square}\ngenerated from the {count} time')
