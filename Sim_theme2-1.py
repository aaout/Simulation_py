import matplotlib.pyplot as plt
import networkx as nx
import random
n = 500  # The number of nodes
k = 4    # nearest neighbors
p = 1  # The probability of rewiring each edge

# nodesの作成
G_smallnet = nx.watts_strogatz_graph(n, k, p)


print('平均頂点間距離:', nx.average_shortest_path_length(G_smallnet))
print('クラスター係数:', nx.average_clustering(G_smallnet))


# show G
plt.figure(figsize=(20, 14))
pos = nx.circular_layout(G_smallnet)
nx.draw_networkx(G_smallnet, pos, node_color='black',
                 alpha=0.2)

plt.show()
