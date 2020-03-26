import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
n = 500  # The number of nodes
k = 4    # nearest neighbors

avg_path_len = []
avg_cluster = []
x = np.arange(0, 1.01, 0.005)
for p in x:
    G = nx.watts_strogatz_graph(n, k, p)
    avg_path_len.append(nx.average_shortest_path_length(G))
    avg_cluster.append(nx.average_clustering(G))

plt.figure()
plt.xlabel('p')
plt.ylabel('L(p)')
plt.xscale("log")
plt.plot(x, avg_path_len)

plt.figure()
plt.xlabel('p')
plt.ylabel('C(p)')
plt.xscale("log")
plt.plot(x, avg_cluster)

plt.show()
