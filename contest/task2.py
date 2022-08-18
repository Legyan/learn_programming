n = int(input())

rows = []

for number_of_row in range(n):
    row = list(input())
    rows.append(row)

groups = int(input())

left_places = [0, 1, 2]
right_places = [4, 5, 6]

places = {'left':
              {'window': left_places,
               'aisle': left_places[::-1]},
          'right':
              {'window': right_places[::-1],
               'aisle': right_places}}

alphabet = 'ABC_DEF'


def find_in_row(num, side, position, row):
    places_nearby = 0
    for place in places[side][position]:
        if rows[row][place] == "#":
            return None
        places_nearby += 1
        if places_nearby == num:
            sought_places = places[side][position][0:num]
            for place in sought_places:
                rows[row][place] = "X"
            print_answer(row, sought_places)
            for place in sought_places:
                rows[row][place] = '#'
            return True
    return None


def print_answer(row, sought_places):
    message = f"Passengers can take seats:"
    for place in sorted(sought_places):
        message += f' {row+1}{alphabet[place]}'
    print(message)
    for i in rows:
        print(''.join(i))


for number_of_group in range(groups):
    num, side, position = input().split(' ')
    for i in range(n):
        if find_in_row(int(num), side,position, i):
            break
    else:
        print('Cannot fulfill passengers requirements')
