import networkx as nx
import matplotlib.pyplot as plt
import random


def drawG(G):
    nx.draw(G, with_labels=True)
    plt.show()


def avg_degree(G):
    x = 0
    for i in range(30):
        x += nx.average_degree_connectivity(G)
    x = x/30
    return x


def avg_clustering(G):
    x = 0
    for i in range(30):
        x += nx.average_clustering(G)
    x = x/30
    return x


def avg_pathlen(G):
    x = 0
    for i in range(30):
        x += nx.average_shortest_path_length(G)
    x = x/30
    return x


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


def main(n: int, p: float):
    G = nx.erdos_renyi_graph(n,p)
    
    
    print( "The average degree of this network: ", avg_degree(G))
    print( "Average clustering coefficient of this network: " , avg_clustering(G))
    print( "The average path length of this network: " , avg_pathlen(G))
    print( "Degree Distribution of this network: " , degree_dis(G))


main(250, 0.4)
main(100,0.8)
main(150,0.05)
