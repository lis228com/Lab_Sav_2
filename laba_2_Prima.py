import math
import itertools

import networkx as nx
import numpy.random as rnd
import matplotlib.pyplot as plt
graph = nx.Graph()
for i in range(1,7):
    graph.add_node(i)
print(graph.nodes())



def get_min(R, U):
    rm = (math.inf, -1, -1)
    for v in U:
        rr = min(R, key=lambda x: x[0] if (x[1] == v or x[2] == v) and (x[1] not in U or x[2] not in U) else math.inf)
        if rm[0] > rr[0]:
            rm = rr

    return rm


# список ребер графа (длина, вершина 1, вершина 2)
# первое значение возвращается, если нет минимальных ребер
R = [(math.inf, -1, -1), (13, 1, 2), (18, 1, 3), (17, 1, 4), (14, 1, 5), (22, 1, 6),
     (26, 2, 3), (19, 2, 5), (30, 3, 4), (22, 4, 6)]

N = 6     # число вершин в графе
U = {1}   # множество соединенных вершин
T = []    # список ребер остова

while len(U) < N:
    r = get_min(R, U)       # ребро с минимальным весом
    if r[0] == math.inf:    # если ребер нет, то остов построен
        break

    T.append(r)             # добавляем ребро в остов
    U.add(r[1])             # добавляем вершины в множество U
    U.add(r[2])

print(T)
for i in range(len(T)):
    graph.add_edge(T[i][1],T[i][2],weight = T[i][0])
nx.draw_circular(graph,
         node_color='red',
         node_size=1000,
         with_labels=True)
plt.show()
