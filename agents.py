import numpy as np
import random

class BasicAgent1:
    # Iteratively travel to the cell with the highest chance of containing the target

    def __init__(self, d):
        self.d = d
        self.belief = np.full((d, d), 1 / (d ** 2))

    def choose_next_query(self):
        options = []
        max_belief = 0
        for i in range(self.d):
            for j in range(self.d):
                if (max_belief < self.belief[i][j]):
                    max_belief = self.belief[i][j]
                    options = []
                    options.append((i, j))
                elif (max_belief == self.belief[i][j]):
                    options.append((i, j))
        return random.choice(options)

    def update_kb(self, pos, data):
        (x, y) = pos
        hypothesis = self.belief[x][y]

        # P(hypothesis | data) =
        # P(data | hypothesis) * P(hypothesis) / P(data)

        

        posterior_prob = 0
        return None