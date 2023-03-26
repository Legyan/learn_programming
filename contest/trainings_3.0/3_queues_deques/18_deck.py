from collections import deque
deq = deque()
while True:
    command = input().split()
    if command[0] == "push_front":
        deq.appendleft(int(command[1]))
        print("ok")
    elif command[0] == "push_back":
        deq.append(int(command[1]))
        print("ok")
    elif command[0] == "pop_front":
        if len(deq) == 0:
            print("error")
        else:
            print(deq.popleft())
    elif command[0] == "pop_back":
        if len(deq) == 0:
            print("error")
        else:
            print(deq.pop())
    elif command[0] == "front":
        if len(deq) == 0:
            print("error")
        else:
            print(deq[0])
    elif command[0] == "back":
        if len(deq) == 0:
            print("error")
        else:
            print(deq[-1])
    elif command[0] == "size":
        print(len(deq))
    elif command[0] == "clear":
        deq.clear()
        print("ok")
    elif command[0] == "exit":
        print("bye")
        break
