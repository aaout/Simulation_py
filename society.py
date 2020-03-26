import matplotlib.pyplot as plt
import networkx as nx
import random
import numpy as np


class Agent:

    def __init__(self):
        """
        state = ['S', I', 'R'] (S: Susceptible, I: Infectious, R: Recovered)
        """
        self.state = 'S'
        self.neighbors_id = None


def generate_agents(G, num_agent, neighbors):
    # グラフの作成

    # Agentをnum_agent人分作成
    agents = [Agent() for agent_id in range(num_agent)]

    #　neighbors_idの更新
    # 隣接しているnodeをリストで格納
    for agent_id, agent in enumerate(agents):
        agent.neighbors_id = list(G[agent_id])

    return agents


def count_state_fraction(agents):
    """Count the fraction of S/IM/I/R state agents"""

    fs = len([agent for agent in agents if agent.state == 'S'])/len(agents)
    fi = len([agent for agent in agents if agent.state == 'I'])/len(agents)
    fr = 1 - fs - fi

    return fs, fi, fr


def count_num_s(agents):
    """Count the number of infected agents"""

    num_s = len([agent for agent in agents if agent.state == 'S'])

    return num_s


def count_num_i(agents):
    """Count the number of infected agents"""

    num_i = len([agent for agent in agents if agent.state == 'I'])

    return num_i


def count_num_r(agents):
    """Count the number of infected agents"""

    num_r = len([agent for agent in agents if agent.state == 'R'])

    return num_r
