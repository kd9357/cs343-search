# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    #Successor in the form of: [((x, y), 'Direction', 'Cost'), ...]

    #Should try to use stack instead of default list
    #though it won't make a difference due to the way this recursion works
    visited, actions = set(), []
    start = (problem.getStartState(), None, 0)
    actions = dfsHelper(problem, start, visited, actions)
    return actions

#Should keep track of already expanded states
def dfsHelper(problem, currentState, visited, actions):
    visited.add(currentState[0])
    if problem.isGoalState(currentState[0]):
        #actions.append(currentState[1])
        return actions
    successors = problem.getSuccessors(currentState[0])
    for s in successors:
        if s[0] not in visited:
            possiblePath = actions + [s[1]]
            path = dfsHelper(problem, s, visited, possiblePath)
            if path is not None:
                return path
    return None
    
def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    # Because of cornersProblem and using a list to keep
    # track of hit corners, can no longer use set for visited
    visited, fringe = [], util.Queue()
    start = (problem.getStartState(), None, 0)
    visited.append(problem.getStartState())
    fringe.push((start, [])) 
    while not fringe.isEmpty():
        (currentState, actions) = fringe.pop()
        if problem.isGoalState(currentState[0]):
            return actions
        successors = problem.getSuccessors(currentState[0])
        for s in successors:
            if s[0] not in visited:
                visited.append(s[0])
                possiblePath = actions + [s[1]]
                fringe.push((s, possiblePath))
    return None

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    visited, fringe = {}, util.PriorityQueue()
    start = (problem.getStartState(), None, 0)
    fringe.push((start, []), 0)
    visited[problem.getStartState()] = 0
    while not fringe.isEmpty():
        (currentState, actions) = fringe.pop()
        if problem.isGoalState(currentState[0]):
            return actions
        cost = problem.getCostOfActions(actions)
        successors = problem.getSuccessors(currentState[0])
        for s in successors:
            possibleCost = cost + s[2]
            if not visited.has_key(s[0]) or possibleCost < visited[s[0]]:
                visited[s[0]] = possibleCost
                possiblePath = actions + [s[1]]
                fringe.update((s, possiblePath), possibleCost)
    return None

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    visited, fringe = {}, util.PriorityQueue()
    start = (problem.getStartState(), None, 0)
    fringe.push((start, []), 0)
    visited[problem.getStartState()] = 0
    while not fringe.isEmpty():
        (currentState, actions) = fringe.pop()
        if problem.isGoalState(currentState[0]):
            return actions
        cost = problem.getCostOfActions(actions)
        successors = problem.getSuccessors(currentState[0])
        for s in successors:
            g = cost + s[2]
            h = heuristic(s[0], problem)
            totalScore = g + h
            if not visited.has_key(s[0]) or g < visited[s[0]]:
                visited[s[0]] = g
                possiblePath = actions + [s[1]]
                fringe.update((s, possiblePath), totalScore)
    return None


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
