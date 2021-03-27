# cs440-project-3

CS 440: Assignment 3 - Probabilistic Search (and Destroy)

## Problem structure

The landscape is a map of cells. The cells can have onr of four different terrain types depending on how hard they are to search.

$$P(target\:in\:cell) = \frac{1}{n-cells}$$

False negative chances per terrain type:

- 0.1 if cell is **flat**
- 0.3 if cell is **hilly**
- 0.7 if cell is **forested**
- 0.9 if cell is **a maze of caves**

False positive chance is always 0.

The algorithm is done when it finds the target. The goal is to do so in as few searches as possible.

## Implementation

Board state:

- Use a 50x50 grid.
- The cells are split 4 ways evenly between the different terrain types.
- The target is selected randomly.

Agent knowledge base:

- Use a 50x50 array of values for belief state 

$$belief(cell_i) = P(target\:in\:cell_i | observations\:through\:time\:t)$$


Agent decision-making:

- At t=0, belief in all cells is 1/2500
- At any time t, an agent needs to select a cell to serach
- If the cell does not contain the target, the environment will return failure
- If the cell does contain the target, the environment will return either failure or success with the above probabilities
- Use observations about the selected cell to update belief state for all cells (using Bayes' Theorem)
- If the search returns success, return the number of searches taken to locate the target

## Problems

### 1) 

### 2)


### 3)

- Basic agent 1: iteratively travel to the cell with the highest probability of contianing the target, search that cell. Repeat until target found.
- Basic agent 2: Iteratively travel to the cell with the highest probability of finding the target in that cell, search, repeat until found.

### 4)

## Bonus: a moving target
