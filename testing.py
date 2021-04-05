import numpy as np
import agents
import environment

DEBUG = 0

def search_landscape(agent, landscape):
    while (True):
        pos = agent.choose_next_query()
        response = landscape.query_board(pos)
        if (response == 1):
            return agent.n_searches + agent.distance
        else:
            agent.update_kb(pos)
            if (DEBUG): print(agent.belief)
            if (DEBUG): print("")
    return -1

def compare_basic_agents(dim, n_tests):
    agent1_scores = []
    agent2_scores = []
    for i in range(n_tests):
        test_landscape = environment.Landscape(dim)
        test_agent1 = agents.BasicAgent1(dim, test_landscape.board)
        test_agent2 = agents.BasicAgent2(dim, test_landscape.board)
        score1 = search_landscape(test_agent1, test_landscape)
        score2 = search_landscape(test_agent2, test_landscape)
        agent1_scores.append(score1)
        agent2_scores.append(score2)

        (x, y) = test_landscape.target
        print("Board {} of {}: Size {}x{}. False negative chance: {}.".format(i+1, n_tests, dim, dim, test_landscape.board[x][y]))
        print("Basic agent 1 Scored {}.".format(score1))
        print("Basic agent 2 Scored {}.".format(score2))

    print("Final results:")
    print("Basic agent 1 average score: {}".format(sum(agent1_scores)/len(agent1_scores)))
    print("Basic agent 2 average score: {}".format(sum(agent2_scores)/len(agent2_scores)))

def compare_basic_and_advanced(dim, n_tests):
    agent1_scores = []
    agent2_scores = []
    for i in range(n_tests):
        test_landscape = environment.Landscape(dim)
        basic = agents.BasicAgent1(dim, test_landscape.board)
        advanced = agents.AdvancedAgent(dim, test_landscape.board)
        score1 = search_landscape(basic, test_landscape)
        score2 = search_landscape(advanced, test_landscape)
        agent1_scores.append(score1)
        agent2_scores.append(score2)

        (x, y) = test_landscape.target
        print("Board {} of {}: Size {}x{}. False negative chance: {}.".format(i+1, n_tests, dim, dim, test_landscape.board[x][y]))
        print("Basic agent 1 Scored {}.".format(score1))
        print("Advanced agent Scored {}.".format(score2))

    print("Final results:")
    print("Basic agent 1 average score: {}".format(sum(agent1_scores)/len(agent1_scores)))
    print("Advanced agent average score: {}".format(sum(agent2_scores)/len(agent2_scores)))


dim = 50
n_tests = 10
compare_basic_and_advanced(dim, n_tests)