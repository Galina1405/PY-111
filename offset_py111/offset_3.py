# Назовем связным такой граф, в котором есть путь от любой вершины
# к любой другой вершине.
# Дан граф, состоящий из 2+ связных подграфов, которые не связаны между собой.
# Задача: посчитать число компонент связности графа, т.е. количество таких подграфов.

import networkx as nx

g = nx.Graph()
g.add_nodes_from('ABCDEFG')
# print(g.nodes)

g.add_edges_from([
    ('A', 'B'),
    ('B', 'C'),
    ('C', 'D'),
    ('F', 'G')
])
subgraphs = list(nx.connected_components(g))
print(subgraphs)
connectivities = list(map(lambda x: len(x) - 1, subgraphs))
print(connectivities)
connectivities_max = max(list(map(lambda x: len(x) - 1, subgraphs)))
print(connectivities_max)
