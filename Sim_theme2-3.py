import numpy as np
import pandas as pd
import random as rnd
import society
import epidemics
import matplotlib.pyplot as plt
import networkx as nx


def main():
    ### Calcualtion setting ###
    num_agent = 500                      # Number of agent
    neighbors = 20  # average degree of the social network
    p = 0
    beta = 0.8                            # Infection probability
    gamma = 0.1                           # Recovery probability

    G_smallnet = nx.watts_strogatz_graph(num_agent, neighbors, p)

    agents = society.generate_agents(G_smallnet, num_agent, neighbors)
    epidemics.initialize_state(agents)
    s, i, r = epidemics.disease_spreading(agents, beta, gamma)

    i_len = len(i)
    x = np.arange(0, i_len)
    plt.figure(figsize=(20, 14))
    plt.xlabel('Time', fontsize=30)
    plt.plot(x, s, color='blue', label='Susceptible')
    plt.plot(x, i, color='red', label='Infected')
    plt.plot(x, r, color='green', label='Recovered')
    plt.legend(fontsize=24)
    plt.tick_params(labelsize=26)
    plt.grid()
    plt.show()


if __name__ == '__main__':
    main()
