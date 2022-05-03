import networkx as nx
x = open('Для лабы МП.txt','r')
a =int(x.readline())
b = int(x.readline(2))
c = int(x.readline(3))
spisok = []

for line in x:
    spisok.append([int(z) for z in line.split()])
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






