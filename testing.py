import numpy as np
import agents
import environment

DEBUG = 0

def search_landscape(agent, landscape):
    while (True):
        pos = agent.choose_next_query()
        response = landscape.query_board(pos)
        if (response == 1):
            return agent.n_searches
        else:
            agent.update_kb(pos)
            if (DEBUG): print(agent.belief)
            if (DEBUG): print("")
    return -1

dim = 10
n_tests = 100

agent1_scores = []
for i in range(n_tests):
    test_landscape = environment.Landscape(dim)
    test_agent = agents.BasicAgent1(dim, test_landscape.board)
    score = search_landscape(test_agent, test_landscape)
    agent1_scores.append(score)

    #(x, y) = test_landscape.target
    #print("Scored {} on one {}x{} board. False negative chance was {}.".format(score, test_landscape.d, test_landscape.d, test_landscape.board[x][y]))
    #print("Adjusted score: {}\n".format(score * (1-test_landscape.board[x][y])))

agent2_scores = []
for i in range(n_tests):
    test_landscape = environment.Landscape(dim)
    test_agent = agents.BasicAgent2(dim, test_landscape.board)
    score = search_landscape(test_agent, test_landscape)
    agent2_scores.append(score)

    #(x, y) = test_landscape.target
    #print("Scored {} on one {}x{} board. False negative chance was {}.".format(score, test_landscape.d, test_landscape.d, test_landscape.board[x][y]))
    #print("Adjusted score: {}\n".format(score * (1-test_landscape.board[x][y])))

print("Basic agent 1 average score: {}".format(sum(agent1_scores)/len(agent1_scores)))
print("Basic agent 2 average score: {}".format(sum(agent2_scores)/len(agent2_scores)))
