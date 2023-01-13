from abc import ABC


class Renderer(ABC):
    def render_circle(self, radius):
        pass

    def render_square(self, side):
        pass


class VectorRenderer(Renderer):
    def render_circle(self, radius):
        print(f'Drawing a circle of radius {radius}')

    def render_square(self, side):
        print(f'Drawing a square of side {side}')


class RasterRenderer(Renderer):
    def render_circle(self, radius):
        print(f'Drawing pixels for a circle of radius {radius}')

    def render_square(self, side):
        print(f'Drawing pixels for a square of side {side}')


class Shape:
    def __init__(self, renderer):
        self.renderer = renderer

    def draw(self):
        pass


class Circle(Shape):
    def __init__(self, renderer, radius):
        super().__init__(renderer)
        self.radius = radius

    def draw(self):
        self.renderer.render_circle(self.radius)


class Square(Shape):
    def __init__(self, renderer, size):
        super().__init__(renderer)
        self.size = size

    def draw(self):
        self.renderer.render_square(self.size)


if __name__ == '__main__':
    raster = RasterRenderer()
    vector = VectorRenderer()
    circle1 = Circle(vector, 2)
    circle2 = Circle(raster, 4)
    square1 = Square(vector, 3)
    square2 = Square(raster, 6)
    circle1.draw()
    circle2.draw()
    square1.draw()
    square2.draw()
