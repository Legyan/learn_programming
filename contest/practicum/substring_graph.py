T = int(input())

meeting_rooms_names = [input() for name in range(T)]

graph = {}

for name in meeting_rooms_names:
    first_substring = name[0: 3]
    for substring_number in range(1, len(name) - 2):
        second_substring = name[substring_number: substring_number + 3]
        if first_substring not in graph:
            graph[first_substring] = {second_substring: 1}
        elif second_substring not in graph[first_substring]:
            graph[first_substring][second_substring] = 1
        else:
            graph[first_substring][second_substring] += 1
        first_substring = second_substring


message = ''
number_of_vertices = 0
for node in graph:
    for edge in graph[node]:
        weight = graph[node][edge]
        message += f'{node} {edge} {weight}\n'
        number_of_vertices += 1

message = message[:-1]

print(len(graph))
print(number_of_vertices)
print(message)
