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
    return [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem):
    # we are using Stack, the search explores from the last explored node
    frontier = util.Stack()
    # Make an empty list of explored nodes
    exploredNode = []
    # Make an empty list of actions
    actionList = []
    # Place the starting point in the stack
    node = {'state': problem.getStartState(), 'cost': actionList}
    frontier.push(node.values())
    while frontier:
        node, activities = frontier.pop()
        if not node in exploredNode:
            exploredNode.append(node)
            if problem.isGoalState(node):
                return activities
            successors = problem.getSuccessors(node)
            for successor in successors:
                coordinate, path, cost = successor
                nextActions = activities + [path]
                frontier.push((coordinate, nextActions))
    return []


def breadthFirstSearch(problem):
    frontier = util.Queue()
    # # Make an empty list of actions costed
    explorednodes = []  # keep track of visited nodes

    startState = problem.getStartState()  # get the start state
    startNode = (startState, [], 0)  # start node

    frontier.push(startNode)  # push start node onto a queue

    while not frontier.isEmpty():
        # explore first pushed node

        currentState, actions, currentCost = frontier.pop()

        if currentState not in explorednodes:

            explorednodes.append(currentState)

            if problem.isGoalState(currentState):
                return actions
            else:
                # getting successors of the current state
                successors = problem.getSuccessors(currentState)

                for succState, succAction, succCost in successors:
                    newAction = actions + [succAction]
                    newCost = currentCost + succCost
                    newNode = (succState, newAction, newCost)
                    #
                    #         for successor in successors:
                    #             position, route, cost = successor
                    #             nextMove = actions + [route]
                    #             frontier.push((position, nextMove))

                    frontier.push(newNode)

    return actions


def uniformCostSearch(problem):
    # Use a PriorityQueue, so the cost of actions is calculated with a provided heuristic
    frontier = util.PriorityQueue()
    # Make an empty list of explored nodes
    visited = []
    # Make an empty list of actions
    actionList = []
    # Place the starting point in the priority queue
    node = {'state': problem.getStartState(), 'cost': actionList}
    frontier.push((node.values()), problem)
    while frontier:
        node, actions = frontier.pop()
        if not node in visited:
            visited.append(node)
            if problem.isGoalState(node):
                return actions
            successors = problem.getSuccessors(node)
            for successor in successors:
                coordinate, direction, cost = successor
                nextActions = actions + [direction]
                nextCost = problem.getCostOfActions(nextActions)
                frontier.push((coordinate, nextActions), nextCost)
    return []


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    # Use a priority queue, so the cost of actions is calculated with a provided heuristic
    frontier = util.PriorityQueue()
    # Make an empty list of explored nodes
    exporedNodes = []
    # Make an empty list of actions
    actionList = []
    # Place the starting point in the priority queue
    frontier.push((problem.getStartState(), actionList), heuristic(problem.getStartState(), problem))
    while frontier:
        node, activities = frontier.pop()
        if not node in exporedNodes:
            exporedNodes.append(node)
            if problem.isGoalState(node):
                return activities
            for successor in problem.getSuccessors(node):
                position, routes, cost = successor
                nextActions = activities + [routes]
                nextCost = problem.getCostOfActions(nextActions) + heuristic(position, problem)
                frontier.push((position, nextActions), nextCost)
    return []



# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
