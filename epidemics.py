import random as rnd
import society


def initialize_state(agents):
    """
    Randomely select initially infected agents from non-vaccinators and
    determine the agents who get perfect immunity from vaccinators
    """

    x = [i for i, agent in enumerate(agents)]
    rand = rnd.choice(x)
    agents[rand].state = 'I'


def disease_spreading(agents, beta, gamma):
    """Calculate SIR dynamics until I agents disappear"""

    list_s = []
    list_i = []
    list_r = []
    list_s.append(500)
    list_i.append(1)
    list_r.append(0)
    for day in range(1, 100000):
        # Only S or I state agents change their state, IM or R don't change their state!
        state_changeable_agents = [
            agent for agent in agents if agent.state in ['S', 'I']]
        next_states = ['S' for i in range(len(state_changeable_agents))]

        for i, agent in enumerate(state_changeable_agents):
            if agent.state == 'S':
                num_infected_neighbors = len(
                    [agents[agent_id] for agent_id in agent.neighbors_id if agents[agent_id].state == 'I'])
                if num_infected_neighbors != 0:
                    if rnd.random() <= beta:
                        next_states[i] = 'I'
                else:
                    pass

            elif agent.state == 'I':
                if rnd.random() <= gamma:
                    next_states[i] = 'R'
                else:
                    next_states[i] = 'I'

        # Update state
        # 新旧リストを同時にループして代入
        for agent, next_state in zip(state_changeable_agents, next_states):
            agent.state = next_state

        list_s.append(society.count_num_s(agents))
        list_i.append(society.count_num_i(agents))
        list_r.append(society.count_num_r(agents))
        num_i = society.count_num_i(state_changeable_agents)

        if num_i == 0:
            break

    return list_s, list_i, list_r
