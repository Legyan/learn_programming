import random
import string


class User:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return ''.join(self.name)


class UserFlyweight:
    strings = []

    def __init__(self, full_name):
        self.names = [self._get_or_add(x) for x in full_name.split()]

    def __str__(self):
        return ' '.join([self.strings[x] for x in self.names])

    def _get_or_add(self, s):
        if s in self.strings:
            return self.strings.index(s)
        else:
            self.strings.append(s)
            return len(self.strings) - 1


def random_string():
    chars = string.ascii_lowercase
    return ''.join([random.choice(chars) for x in range(8)])


if __name__ == '__main__':
    users = []
    first_names = [random_string() for x in range(100)]
    last_names = [random_string() for x in range(100)]

    for first in first_names:
        for last in last_names:
            # users.append(User(f'{first} {last}'))
            users.append(UserFlyweight(f'{first} {last}'))
    print('Имен в памяти', len(UserFlyweight.strings))
    print('Всего пользователей', len(users))
