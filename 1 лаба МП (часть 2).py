import networkx as nx
x = open('Для лабы МП(2).txt','r')
a = int(''.join([chr(int(s, 2)) for s in x.readline().split()]))  # из двоичной в обычную
b = int(''.join([chr(int(s, 2)) for s in x.readline().split()]))  # из двоичной в обычную
c = int(''.join([chr(int(s, 2)) for s in x.readline().split()]))  # из двоичной в обычную
spisok = []

for line in x:
    d = ''.join([chr(int(s, 2)) for s in line.split()])  # из двоичной в обычную
    spisok.append([int(z) for z in d.split()])
print("spisok = ",spisok)

G = nx.DiGraph()
nodes = []

for i in range(a):
    for j in range(2):
        nodes.append(spisok[i][j])
print(nodes)

G.add_nodes_from(nodes)

for i in range(a):
    G.add_edge(spisok[i][0],spisok[i][1],weight=spisok[i][2])

print(nx.dijkstra_path(G, b, c))
print(nx.dijkstra_path_length(G, b, c))






