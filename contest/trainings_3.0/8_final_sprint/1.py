def train_rides(n):
    counts = {}
    items = []
    args = []

    for _ in range(n):
        args.append(input().split())

    for command, *args in args:
        if command == "add":
            count, item = int(args[0]), args[1]
            counts[item] = counts.get(item, 0) + count
            if item not in items:
                items.append(item)
        elif command == "delete":
            count = int(args[0])
            for _ in range(count):
                item = items.pop()
                counts[item] -= 1
                if counts[item] == 0:
                    del counts[item]
        elif command == "get":
            item = args[0]
            print(counts.get(item, 0))


if __name__ == "__main__":
    n = int(input())
    train_rides(n)
