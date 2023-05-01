"""
Реализация алгоритма Дейкстры для поиска кратчайшего пути во взвешенном графе
"""


def dijkstras(graph: dict):
    """
    Получает на вход хеш-таблицу графа, с узлом начальным узлом 'start'
    и конечным узлом 'end'.
    Возвращает длину кратчайшего пути и сам путь от 'start' до 'end'.
    """
    parents = {}  # создание хеш-таблиц родителей
    costs = {}    # создание хеш-таблиц стоимостей
    inf = float('inf')
    nodes_without_start = [node for node in graph.keys() if node != 'start']
    starts_kids = [node for node in graph['start'].keys()]
    for node in nodes_without_start:
        if node in starts_kids:
            parents[node] = 'start'
            costs[node] = graph['start'][node]
        else:
            parents[node] = None
            costs[node] = inf
    processed = []
    node = find_lowest_cost_node(costs, processed)
    while node is not None:
        cost = costs[node]
        neighbours = graph[node]
        for neigh in neighbours:
            new_cost = neighbours[neigh] + cost
            if new_cost < costs[neigh]:
                costs[neigh] = new_cost
                parents[neigh] = node
        processed.append(node)
        node = find_lowest_cost_node(costs, processed)
    squence_nodes = [parents['end']]
    while squence_nodes[-1] != 'start':
        squence_nodes.append(parents[squence_nodes[-1]])
    squence_nodes.reverse()
    squence_nodes.append('end')
    return costs['end'], squence_nodes


def find_lowest_cost_node(costs, processed):
    lowest_cost = float('inf')
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


if __name__ == '__main__':
    graph = {}  # создание хеш-таблицы графа
    graph['start'] = {}
    graph['start']['a'] = 8
    graph['start']['b'] = 6
    graph['start']['c'] = 10
    graph['a'] = {}
    graph['a']['c'] = 0
    graph['a']['d'] = 5
    graph['b'] = {}
    graph['b']['c'] = 3
    graph['b']['e'] = 7
    graph['c'] = {}
    graph['c']['d'] = 4
    graph['c']['end'] = 9
    graph['d'] = {}
    graph['d']['end'] = 6
    graph['e'] = {}
    graph['e']['end'] = 7
    graph['end'] = {}
    print(dijkstras(graph))
