iimport networkx as nx
import matplotlib.pyplot as plt
import random

G_1 = nx.erdos_renyi_graph(250,0.4)
G_2 = nx.erdos_renyi_graph(100,0.8)
G_3 = nx.erdos_renyi_graph(150,0.05)


def draw_graph(G):
    nx.draw(G, with_labels=True)
    plt.show()


def avg_degree(G):
    return nx.average_degree_connectivity(G)


def avg_clustering(G):
    return nx.average_clustering(G)


def avg_pathlen(G):
    return nx.average_shortest_path_length(G)


def degree_dis(G):
    deg = {}
    for n in G.nodes():
        degree = G.degree(n)
        if degree not in deg:
            deg[degree] = 0
        deg[degree] += 1
    x = sorted(deg.items())

    plt.plot([k for (k, v) in x], [v for (k, v) in x]) 
    plt.xlabel('k')
    plt.ylabel('p(k)')
    plt.show()
    return x

