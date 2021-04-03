import numpy as np
import random
import math

DEBUG = 0
class BasicAgent1:
    # Iteratively travel to the cell with the highest chance of containing the target

    def __init__(self, d, board):
        self.d = d
        self.cur_pos = (random.randrange(0, d), random.randrange(0, d))
        if (DEBUG): print("Starting position: {}".format(self.cur_pos))
        self.n_searches = 0
        self.belief = np.full((d, d), 1 / (d ** 2))
        self.n_fails = np.full((d, d), 1)
        self.board = board

    def choose_next_query(self):
        self.n_searches += 1

        # Select the most likely options
        options = []
        max_belief = 0
        for i in range(self.d):
            for j in range(self.d):
                if (math.isclose(max_belief, self.belief[i][j])):
                    options.append((i, j))
                elif (max_belief < self.belief[i][j]):
                    max_belief = self.belief[i][j]
                    options = []
                    options.append((i, j))

        # Select the closest of these options
        min_manhattan_distance = self.d * 2
        shortest_options = []
        for i in range(len(options)):
            cur_manhattan_distance = self.calc_manhattan_distance(options[i])
            #print("distance from {} to {}: {}".format(self.cur_pos, options[i], cur_manhattan_distance))
            if (min_manhattan_distance > cur_manhattan_distance):
                shortest_options = []
                min_manhattan_distance = cur_manhattan_distance
                shortest_options.append(options[i])
            elif (min_manhattan_distance == cur_manhattan_distance):
                shortest_options.append(options[i])

        # Select a random choice from the remainder
        ret = random.choice(shortest_options)
        if (DEBUG): print("Curently at {}, moving to {}".format(self.cur_pos, ret))
        self.cur_pos = ret
        return ret

    def calc_manhattan_distance(self, pos):
        (x1, y1) = self.cur_pos
        (x2, y2) = pos
        return abs(x2 - x1) + abs(y2 - y1)

    def nCr(self, n, r):
        f = math.factorial
        return f(n) // f(r) // f(n-r)

    def update_kb(self, pos):
        # This function will run if the agent failed to find the target at pos
        # fn_prob is the probability of false negative at pos

        (x, y) = pos
        fn_prob = self.board[x][y]
        self.n_fails[x][y] += 1

        # P(A | B) = P(B | A) * P(A) / P(B)
        # new_belief = term1 * term2 / term3

        # P(A | B) = chance of target in cell given current observations

        # P(B | A) = chance of current observations given target in cell
        # Uses a binomial distribution
        # Chance of false negatives
        p = math.pow(fn_prob, self.n_fails[x][y])
        # Chance of true negatives
        q = math.pow(1-fn_prob, 0)
        # Ways to get n false negatives in n trials (always 1)
        ncr = self.nCr(self.n_fails[x][y], self.n_fails[x][y])
        term1 = ncr * p * q

        # P(A) = chance of target in cell
        term2 = self.belief[x][y]

        # P(B) = chance of current observations
        term3 = fn_prob

        
        new_belief = (term1 * term2) / term3
        if (DEBUG): print("{} = {} * {} / {}".format(new_belief, term1, term2, term3))
        delta_belief = new_belief - self.belief[x][y]
        self.belief[x][y] = new_belief

        # Updating belief in all other cells
        delta_belief_others = (-1) * delta_belief / ((self.d ** 2) - 1)
        for i in range(self.d):
            for j in range(self.d):
                if (x == i) and (y == j):
                    continue
                else:
                    self.belief[i][j] += delta_belief_others

        return None

class BasicAgent2:
    # Iteratively travel to the cell with the highest chance of giving a positive

    def __init__(self, d, board):
        self.d = d
        self.cur_pos = (random.randrange(0, d), random.randrange(0, d))
        if (DEBUG): print("Starting position: {}".format(self.cur_pos))
        self.n_searches = 0
        self.belief = np.full((d, d), 1 / (d ** 2))
        self.n_fails = np.full((d, d), 1)
        self.board = board

    def choose_next_query(self):
        self.n_searches += 1

        # Select the most likely options
        options = []
        max_chance = 0
        for i in range(self.d):
            for j in range(self.d):
                if (math.isclose(max_chance, self.belief[i][j] * self.board[i][j])):
                    options.append((i, j))
                elif (max_chance < self.belief[i][j] * self.board[i][j]):
                    max_chance = self.belief[i][j] * self.board[i][j]
                    options = []
                    options.append((i, j))

        # Select the closest of these options
        min_manhattan_distance = self.d * 2
        shortest_options = []
        for i in range(len(options)):
            cur_manhattan_distance = self.calc_manhattan_distance(options[i])
            #print("distance from {} to {}: {}".format(self.cur_pos, options[i], cur_manhattan_distance))
            if (min_manhattan_distance > cur_manhattan_distance):
                shortest_options = []
                min_manhattan_distance = cur_manhattan_distance
                shortest_options.append(options[i])
            elif (min_manhattan_distance == cur_manhattan_distance):
                shortest_options.append(options[i])

        # Select a random choice from the remainder
        ret = random.choice(shortest_options)
        if (DEBUG): print("Curently at {}, moving to {}".format(self.cur_pos, ret))
        self.cur_pos = ret
        return ret

    def calc_manhattan_distance(self, pos):
        (x1, y1) = self.cur_pos
        (x2, y2) = pos
        return abs(x2 - x1) + abs(y2 - y1)

    def nCr(self, n, r):
        f = math.factorial
        return f(n) // f(r) // f(n-r)

    def update_kb(self, pos):
        # This function will run if the agent failed to find the target at pos
        # fn_prob is the probability of false negative at pos

        (x, y) = pos
        fn_prob = self.board[x][y]
        self.n_fails[x][y] += 1

        # P(A | B) = P(B | A) * P(A) / P(B)
        # new_belief = term1 * term2 / term3

        # P(A | B) = chance of target in cell given current observations

        # P(B | A) = chance of current observations given target in cell
        # Uses a binomial distribution
        # Chance of false negatives
        p = math.pow(fn_prob, self.n_fails[x][y])
        # Chance of true negatives
        q = math.pow(1-fn_prob, 0)
        # Ways to get n false negatives in n trials (always 1)
        ncr = self.nCr(self.n_fails[x][y], self.n_fails[x][y])
        term1 = ncr * p * q

        # P(A) = chance of target in cell
        term2 = self.belief[x][y]

        # P(B) = chance of current observations
        term3 = fn_prob

        
        new_belief = (term1 * term2) / term3
        if (DEBUG): print("{} = {} * {} / {}".format(new_belief, term1, term2, term3))
        delta_belief = new_belief - self.belief[x][y]
        self.belief[x][y] = new_belief

        # Updating belief in all other cells
        delta_belief_others = (-1) * delta_belief / ((self.d ** 2) - 1)
        for i in range(self.d):
            for j in range(self.d):
                if (x == i) and (y == j):
                    continue
                else:
                    self.belief[i][j] += delta_belief_others

        return None