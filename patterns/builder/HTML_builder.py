class HtmlElement:
    indent_size = 2

    def __init__(self, name: str = '', text: str = '') -> None:
        self.name = name
        self.text = text
        self.elements = []

    def __str(self, indent: int) -> str:
        lines = []
        i = ' ' * (indent * self.indent_size)
        lines.append(f'{i}<{self.name}>')

        if self.text:
            i1 = ' ' * ((indent + 1) * self.indent_size)
            lines.append(f'{i1}{self.text}')

        for e in self.elements:
            lines.append(e.__str(indent + 1))

        lines.append(f'{i}</{self.name}>')
        return '\n'.join(lines)

    def __str__(self):
        return self.__str(0)

    @staticmethod
    def create(name: str) -> 'HtmlBuilder':
        return HtmlBuilder(name)


class HtmlBuilder:
    def __init__(self, root_name: str) -> None:
        self.root_name = root_name
        self.__root = HtmlElement(root_name)

    def add_child(self, child_name: str, child_text: str) -> None:
        self.__root.elements.append(
            HtmlElement(name=child_name, text=child_text)
        )

    def __str__(self) -> str:
        return str(self.__root)


if __name__ == '__main__':
    builder = HtmlElement.create('ul')
    builder.add_child('li', 'hello')
    builder.add_child('li', 'world')
    print(builder)
