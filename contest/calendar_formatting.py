# https://contest.yandex.ru/contest/48733/problems/1/

days_of_week = {
    'Monday': 0, 'Tuesday': 1, 'Wednesday': 2, 'Thursday': 3,
    'Friday': 4, 'Saturday': 5, 'Sunday': 6
}


def main():
    days, day_of_week = input().split()
    first_day = days_of_week[day_of_week]
    result = [7 * [''] for _ in range(6)]
    for i in range(int(days)):
        index = first_day + i
        result[index // 7][index % 7] = str(i + 1)
    for j in range(3):
        for i in range(7):
            result[j][i] = result[j][i].rjust(2, '.')
    for i in range(6):
        result[i] = ' '.join(result[i])
    result = '\n'.join(result)
    print(result)


if __name__ == '__main__':
    main()
