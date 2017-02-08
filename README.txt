Name: Kevin Du
UTEID: kd9357

Q1: Depth First Search uses recursion to backtrace steps
Q2: Breadth First Search is iterative, keeping track of the current path to the position for each position. Instead of a set, a list is used to compensate for CornersProblem, although this was later rectified
Q3: Uniform Cost Search is the same as breadth first search, with three exceptions: A priority queue is used to track the fringe, the cost of the path is calculated, and the fringe is updated if either the state hasn't been visited or the new path is cheaper than what has been seen so far.
Q4: A* search is Uniform Cost Search, but with the addition of the heuristic along with the cost calculation.
Q5: Added the available four corners to the state representation, so that each state position will also know what corners it already hit
Q6: The heuristic returns the furthest distance dot/corner the agent has yet to hit
Q7: Calculate the distance between the currentState's position and the dot furthest away. Use a dictionary to cache calculations to speed up the lookup time.
Q8: Use BFS for findPathToClosestDot. To check goal, simply see if the current state position is over an existing food location.