# multiAgents.py
# --------------
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


from util import manhattanDistance
from game import Directions
import random, util

from game import Agent
from pacman import GameState

class ReflexAgent(Agent):
    """
    A reflex agent chooses an action at each choice point by examining
    its alternatives via a state evaluation function.

    The code below is provided as a guide.  You are welcome to change
    it in any way you see fit, so long as you don't touch our method
    headers.
    """


    def getAction(self, gameState: GameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {NORTH, SOUTH, WEST, EAST, STOP}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices) # Pick randomly among the best

        "Add more of your code here if you want to"

        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState: GameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()
        newFood = successorGameState.getFood()
        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]

        
        # Diem co ban sau khi thuc hien hanh dong
        score = successorGameState.getScore()

        # Chuyen danh sach thuc an sang dang danh sach toa do
        foodList = newFood.asList()

        # 1. Khuyen khich Pacman tien gan thuc an
        if foodList:
            foodDistances = [
                manhattanDistance(newPos, food)
                for food in foodList
            ]
            minFoodDistance = min(foodDistances)

            score += 10.0 / (minFoodDistance + 1)

            # Thuong khi an duoc thuc an
            oldFoodCount = len(currentGameState.getFood().asList())
            newFoodCount = len(foodList)
            score += 10 * (oldFoodCount - newFoodCount)

        # 2. Tranh ma va tan dung khi ma dang so hai
        for ghostState in newGhostStates:
            ghostPos = ghostState.getPosition()

            ghostDistance = manhattanDistance(newPos, ghostPos)
            scaredTimer = ghostState.scaredTimer

            if scaredTimer > 0:
                # Chi khuyen khich den gan ma neu co kha nang an ma
                if ghostDistance < scaredTimer:
                    score += 8.0 / (ghostDistance + 1)
            else:
                # Ma khong so hai: tranh cac vi tri nguy hiem
                if ghostDistance == 0:
                    score -= 1000
                elif ghostDistance == 1:
                    score -= 200
                elif ghostDistance == 2:
                    score -= 50
                elif ghostDistance == 3:
                    score -= 10

        # 3. Han che dung yen khi van con thuc an
        if action == Directions.STOP and foodList:
            score -= 10

        return score

def scoreEvaluationFunction(currentGameState: GameState):
    """
    This default evaluation function just returns the score of the state.
    The score is the same one displayed in the Pacman GUI.

    This evaluation function is meant for use with adversarial search agents
    (not reflex agents).
    """
    return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
    """
    This class provides some common elements to all of your
    multi-agent searchers.  Any methods defined here will be available
    to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

    You *do not* need to make any changes here, but you can if you want to
    add functionality to all your adversarial search agents.  Please do not
    remove anything, however.

    Note: this is an abstract class: one that should not be instantiated.  It's
    only partially specified, and designed to be extended.  Agent (game.py)
    is another abstract class.
    """

    def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
        self.index = 0 # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)


class MinimaxAgent(MultiAgentSearchAgent):
    """
    Your minimax agent (question 2)
    """

    def getAction(self, gameState: GameState):
        """
        Returns the minimax action from the current gameState using self.depth
        and self.evaluationFunction.
        """

        numAgents = gameState.getNumAgents()

        def minimax(state, depth, agentIndex):
            # Dung neu Pacman thang hoac thua
            if state.isWin() or state.isLose():
                return self.evaluationFunction(state), None

            # Dung khi da dat do sau yeu cau
            if depth == self.depth:
                return self.evaluationFunction(state), None

            legalActions = state.getLegalActions(agentIndex)

            if not legalActions:
                return self.evaluationFunction(state), None

            # Xac dinh agent tiep theo
            nextAgent = (agentIndex + 1) % numAgents

            # Chi tang depth khi quay lai luot Pacman
            nextDepth = depth + 1 if nextAgent == 0 else depth

            if agentIndex == 0:
                # Pacman la MAX
                bestValue = float("-inf")
                bestAction = None

                for action in legalActions:
                    successor = state.generateSuccessor(agentIndex, action)

                    value, _ = minimax(
                        successor, nextDepth, nextAgent
                    )

                    if value > bestValue:
                        bestValue = value
                        bestAction = action

                return bestValue, bestAction

            else:
                # Ghost la MIN
                bestValue = float("inf")
                bestAction = None

                for action in legalActions:
                    successor = state.generateSuccessor(agentIndex, action)

                    value, _ = minimax(
                        successor, nextDepth, nextAgent
                    )

                    if value < bestValue:
                        bestValue = value
                        bestAction = action

                return bestValue, bestAction

        # Bat dau tim kiem tu Pacman (agent 0), depth = 0
        _, action = minimax(gameState, 0, 0)

        return action


class AlphaBetaAgent(MultiAgentSearchAgent):
    """
    Your minimax agent with alpha-beta pruning (question 3)
    """

    def getAction(self, gameState: GameState):
        """
        Returns the minimax action using self.depth and self.evaluationFunction
        """

        # 1. Lấy số lượng tác nhân
        numAgents = gameState.getNumAgents()

        # 2. Lấy các hành động hợp lệ của Pacman
        legalActions = gameState.getLegalActions(0)

        if not legalActions:
            return Directions.STOP

        # 3. Khởi tạo giá trị tốt nhất và Alpha, Beta
        bestAction = None
        bestValue = float('-inf')

        alpha = float('-inf')
        beta = float('inf')

        # 4. Hàm đệ quy Alpha-Beta
        def alphaBeta(state, agentIndex, depth, alpha, beta):

            # Điều kiện dừng
            if (depth == self.depth or
                    state.isWin() or state.isLose()):
                return self.evaluationFunction(state)

            # Lấy các hành động hợp lệ
            actions = state.getLegalActions(agentIndex)

            if not actions:
                return self.evaluationFunction(state)

            # Xác định tác nhân tiếp theo
            nextAgent = (agentIndex + 1) % numAgents

            # Chỉ tăng depth khi quay lại lượt Pacman
            nextDepth = depth + 1 if nextAgent == 0 else depth

            # 5. Nút MAX - Pacman
            if agentIndex == 0:

                value = float('-inf')

                for action in actions:

                    successor = state.generateSuccessor(
                        agentIndex, action
                    )

                    value = max(
                        value,
                        alphaBeta(
                            successor,
                            nextAgent,
                            nextDepth,
                            alpha,
                            beta
                        )
                    )

                    # Cập nhật Alpha
                    alpha = max(alpha, value)

                    # Cắt tỉa, không cắt khi bằng nhau
                    if value > beta:
                        return value

                return value

            # 6. Nút MIN - Ghost
            else:

                value = float('inf')

                for action in actions:

                    successor = state.generateSuccessor(
                        agentIndex, action
                    )

                    value = min(
                        value,
                        alphaBeta(
                            successor,
                            nextAgent,
                            nextDepth,
                            alpha,
                            beta
                        )
                    )

                    # Cập nhật Beta
                    beta = min(beta, value)

                    # Cắt tỉa, không cắt khi bằng nhau
                    if value < alpha:
                        return value

                return value

        # 7. Duyệt các hành động đầu tiên của Pacman
        for action in legalActions:

            successor = gameState.generateSuccessor(0, action)

            # Xác định tác nhân tiếp theo
            nextAgent = (0 + 1) % numAgents

            # Nếu chỉ có Pacman thì chuyển sang lượt mới
            nextDepth = 1 if nextAgent == 0 else 0

            # Tính giá trị của nhánh
            value = alphaBeta(
                successor,
                nextAgent,
                nextDepth,
                alpha,
                beta
            )

            # Lưu hành động có giá trị tốt nhất
            if value > bestValue:
                bestValue = value
                bestAction = action

            # Cập nhật Alpha tại nút gốc
            alpha = max(alpha, bestValue)

        return bestAction


class ExpectimaxAgent(MultiAgentSearchAgent):
    """
    Your expectimax agent (question 4)
    """

    def getAction(self, gameState: GameState):
        """
        Returns the expectimax action using self.depth and self.evaluationFunction

        All ghosts should be modeled as choosing uniformly at random
        from their legal moves.
        """

        # 1. Lấy số lượng tác nhân
        numAgents = gameState.getNumAgents()

        # 2. Lấy các hành động hợp lệ của Pacman
        legalActions = gameState.getLegalActions(0)

        if not legalActions:
            return Directions.STOP

        # 3. Khởi tạo giá trị tốt nhất
        bestAction = None
        bestValue = float('-inf')

        # 4. Hàm đệ quy Expectimax
        def expectimax(state, agentIndex, depth):

            # Kiểm tra điều kiện dừng
            if (depth == self.depth or
                    state.isWin() or state.isLose()):
                return self.evaluationFunction(state)

            # Lấy danh sách hành động hợp lệ
            actions = state.getLegalActions(agentIndex)

            if not actions:
                return self.evaluationFunction(state)

            # Xác định tác nhân tiếp theo
            nextAgent = (agentIndex + 1) % numAgents

            # Chỉ tăng độ sâu khi quay lại lượt Pacman
            nextDepth = depth + 1 if nextAgent == 0 else depth

            # 5. Nút MAX - Pacman
            if agentIndex == 0:

                value = float('-inf')

                for action in actions:

                    successor = state.generateSuccessor(
                        agentIndex, action
                    )

                    value = max(
                        value,
                        expectimax(
                            successor,
                            nextAgent,
                            nextDepth
                        )
                    )

                return value

            # 6. Nút CHANCE - Ghost
            else:

                totalValue = 0

                # Duyệt tất cả hành động của Ghost
                for action in actions:

                    successor = state.generateSuccessor(
                        agentIndex, action
                    )

                    totalValue += expectimax(
                        successor,
                        nextAgent,
                        nextDepth
                    )

                # Xác suất mỗi hành động bằng nhau
                return totalValue / len(actions)

        # 7. Duyệt các hành động ban đầu của Pacman
        for action in legalActions:

            successor = gameState.generateSuccessor(0, action)

            nextAgent = (0 + 1) % numAgents

            # Nếu chỉ có Pacman thì bắt đầu lượt mới
            nextDepth = 1 if nextAgent == 0 else 0

            value = expectimax(
                successor,
                nextAgent,
                nextDepth
            )

            # Lưu hành động có giá trị kỳ vọng cao nhất
            if value > bestValue:
                bestValue = value
                bestAction = action

        return bestAction

def betterEvaluationFunction(currentGameState: GameState):
    """
    V2: diem, thuc an, khoang cach den ma nguy hiem
    va co hoi an ma dang so.
    """
    score = float(currentGameState.getScore())
    if currentGameState.isWin():
        return score + 1_000_000.0
    if currentGameState.isLose():
        return score - 1_000_000.0

    position = currentGameState.getPacmanPosition()
    foods = currentGameState.getFood().asList()
    score -= 4.0 * len(foods)

    if foods:
        nearest_food = min(manhattanDistance(position, food) for food in foods)
        score += 10.0 / (nearest_food + 1.0)

    for ghost in currentGameState.getGhostStates():
        distance = manhattanDistance(position, ghost.getPosition())
        if ghost.scaredTimer > 0:
            if distance < ghost.scaredTimer:
                score += 20.0 / (distance + 1.0)
        else:
            score -= 12.0 / (distance + 1.0)
            if distance <= 1:
                score -= 200.0

    return score

# Abbreviation
better = betterEvaluationFunction
