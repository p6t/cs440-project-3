import numpy as np
import random

# False negative chances
FN_FLAT = 0.1
FN_HILL = 0.3
FN_FOREST = 0.7
FN_CAVE = 0.9

DEBUG = 0

class Landscape:

    def __init__(self, d):

        # Store size of board
        self.d = d

        # Select a target location at random
        self.target = (random.randrange(0, d), random.randrange(0, d))

        # Create board
        self.board = self.create_board(d)

    def create_board(self, d):

        # Create the board
        board = np.zeros(d ** 2)

        # Evenly split terrain type in board
        board[0:int(d ** 2 * 0.25)] = FN_FLAT
        board[int(d ** 2 * 0.25):int(d ** 2 * 0.5)] = FN_HILL
        board[int(d ** 2 * 0.5):int(d ** 2 * 0.75)] = FN_FOREST
        board[int(d ** 2 * 0.75):d ** 2] = FN_CAVE

        # Shuffle board
        np.random.shuffle(board)

        # Reshape from 1d into 2d
        board = np.reshape(board, (d, d))

        return board

    def query_board(self, pos):

        (x, y) = pos

        if (pos == self.target):
            # Positive, check to see if target is found
            false_negative_chance = self.board[x][y]
            roll = random.random()
            if (roll < false_negative_chance):
                # False negative, return 0
                if (DEBUG): print("---> FALSE NEGATIVE AT ({}, {})".format(x, y))
                return 0
            else:
                # True positive, return 1
                if (DEBUG): print("---> TARGET FOUND AT ({}, {})".format(x, y))
                return 1
        else:
            # True negative, return 0
            if (DEBUG): print("---> True negative at ({}, {})".format(x, y))
            return 0

    

