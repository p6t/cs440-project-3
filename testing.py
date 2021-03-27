import numpy as np
import agents
import environment

def search_landscape(agent, landscape):
    moves = 0
    while (True):
        pos = agent.choose_next_query()
        response = landscape.query_board(pos)
        moves += 1
        if (response == 1):
            return moves
        else:
            agent.update_kb(pos, response)
    return -1

dim = 10

test_agent = agents.BasicAgent1(dim)
test_landscape = environment.Landscape(dim)
score = search_landscape(test_agent, test_landscape)

print(score)