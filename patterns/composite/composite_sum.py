from abc import ABC
from collections.abc import Iterable


class BaseValues(Iterable, ABC):
    value = 0

    @property
    def sum(self):
        res = 0
        if self.value != 0:
            res += self.value
        else:
            for s in self:
                if isinstance(s, BaseValues):
                    res += s.sum
                else:
                    res += s
        return res


class SingleValue(BaseValues):
    def __init__(self, value):
        self.value = value

    def __iter__(self):
        yield self


class ManyValues(list, BaseValues):
    pass


if __name__ == '__main__':
    single_value = SingleValue(11)
    other_values = ManyValues()
    other_values.append(22)
    other_values.append(33)

    all_values = ManyValues()
    all_values.append(single_value)
    all_values.append(other_values)

    assert all_values.sum == 66
