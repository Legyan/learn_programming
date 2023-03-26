import sys

_string = ''

while True:
    line = sys.stdin.readline()
    _string += line
    if line == '':
        break
_string = _string.replace(' ', '').replace('\n', '')
set_of_string = set(_string)
symbols = sorted(list(set_of_string))
symbols_len = len(symbols)
symbols = {sym: zero for sym, zero in zip(symbols, [0] * symbols_len)}
for symbol in _string:
    symbols[symbol] += 1
result = []
for x in range(max(symbols.values()), 0, -1):
    tmp = [' '] * symbols_len
    i = 0
    for y in symbols:
        if symbols[y] >= x:
            tmp[i] = '#'
        i += 1
    result.append(tmp)
result.append(symbols.keys())
for x in result:
    print(''.join(x))
