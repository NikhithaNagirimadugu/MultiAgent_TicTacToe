class Game():
    boardvalues = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
    def board(self):
        count = 0
        for i in range(0,3):
            print("|",end = " ")
            for j in range(0,3):
                print(self.boardvalues[i+j+count], "|",end = " "),
            count +=2
            print("\n____________")


    def gameState(self):
        agents = ["Agent1","Agent2"]
        nextTurn = 'Test'
        for i in range(0,9):
            if(i%2==0):
                currentAgent = agent1
                nextTurn = 'X'
            else:
                currentAgent = agent2
                nextTurn ='O'
            print("Hey " + currentAgent + " Agent! Where do you wanna place " + nextTurn + " at?")
            self.board()
            print("\n")
            if nextTurn == 'X':
                if currentAgent == "QLearning":
                    number = self.trainedMove(game)
                else:
                    number = finalMove(game, currentAgent)
            else:
                if currentAgent == "QLearning":
                    number = self.trainedMove(game)
                else:
                    number = finalMove(game, currentAgent)
            if self.boardvalues[number] == " ":
                self.boardvalues[number] = nextTurn
                if self.isEnd() == 'X':
                    self.board()
                    print("OMG! We have a winner.Congratulations " + agent1)
                    break
                elif self.isEnd() == 'O':
                    self.board()
                    print("OMG! We have a winner.Congratulations "+ agent2)
                    break
                elif self.isEnd() == 0:
                    self.board()
                    print("OOPS! Unfortunatly we don't have a winner this time. Better luck next time.")
                    break
                else:
                    continue

    def placeAgent(self, position, curAgent):
        player = None
        if(curAgent == " "):
            self.boardvalues[position] = " "
        else:
            if (curAgent == agent1):
                player = 'X'
            else:
                player = 'O'
            self.boardvalues[position] = player

    def tempGameOver(self,node, curAgent):
        if(curAgent == agent1):
            if self.gameOver(node) == 'X':
                return 1
            elif self.gameOver(node) == 'O':
                return -1
            elif self.gameOver(node) == 0:
                return 0
            else:
                return -10
        elif(curAgent == agent2):
            if self.gameOver(node) == 'X':
                return -1
            elif self.gameOver(node) == 'O':
                return 1
            elif self.gameOver(node) == 0:
                return 0
            else:
                return -10


    def gameOver(self, node):
        if (node.boardvalues[0] == node.boardvalues[1] == node.boardvalues[2] != " "):
            return node.boardvalues[2]
        elif (node.boardvalues[3] == node.boardvalues[4] == node.boardvalues[5] != " "):
            return node.boardvalues[5]
        elif (node.boardvalues[6] == node.boardvalues[7] == node.boardvalues[8] != " "):
            return node.boardvalues[8]
        elif (node.boardvalues[0] == node.boardvalues[3] == node.boardvalues[6] != " "):
            return node.boardvalues[6]
        elif (node.boardvalues[1] == node.boardvalues[4] == node.boardvalues[7] != " "):
            return node.boardvalues[7]
        elif (node.boardvalues[2] == node.boardvalues[5] == node.boardvalues[8] != " "):
            return node.boardvalues[8]
        elif (node.boardvalues[0] == node.boardvalues[4] == node.boardvalues[8] != " "):
            return node.boardvalues[8]
        elif (node.boardvalues[2] == node.boardvalues[4] == node.boardvalues[6] != " "):
            return node.boardvalues[6]
        else:
            for i in range(0,9):
                if(node.boardvalues[i] == " "):
                    return 1
            return 0

    def isEnd(self):
        if (self.boardvalues[0] == self.boardvalues[1] == self.boardvalues[2] != " "):
            return self.boardvalues[2]
        elif (self.boardvalues[3] == self.boardvalues[4] == self.boardvalues[5] != " "):
            return self.boardvalues[5]
        elif (self.boardvalues[6] == self.boardvalues[7] == self.boardvalues[8] != " "):
            return self.boardvalues[8]
        elif (self.boardvalues[0] == self.boardvalues[3] == self.boardvalues[6] != " "):
            return self.boardvalues[6]
        elif (self.boardvalues[1] == self.boardvalues[4] == self.boardvalues[7] != " "):
            return self.boardvalues[7]
        elif (self.boardvalues[2] == self.boardvalues[5] == self.boardvalues[8] != " "):
            return self.boardvalues[8]
        elif (self.boardvalues[0] == self.boardvalues[4] == self.boardvalues[8] != " "):
            return self.boardvalues[8]
        elif (self.boardvalues[2] == self.boardvalues[4] == self.boardvalues[6] != " "):
            return self.boardvalues[6]
        else:
            flag = False
            for i in range(0,9):
                if(self.boardvalues[i] == " "):
                    flag = True
                else:
                    continue
            if(flag==True):
                return 1
            else:
                return 0
    def positionsLeft(self):
        pl = []
        for i in range(len(self.boardvalues)):
            if self.boardvalues[i] == " ":
                pl.append(int(i))
        return pl

    def gameOverValue(self, agent):
        if (agent == 'X'):
            return -1
        elif (agent == 'O'):
            return 1
        else:
            return 0

    def minimax(self, node, curAgent):
        '''
        Minimax algorithm for choosing the best possible move towards
        winning the game
        '''
        if node.tempGameOver(node, curAgent)== -1 or node.tempGameOver(node, curAgent) == 1 or node.tempGameOver(node, curAgent) == 0:
            return node.tempGameOver(node, curAgent)
        else:
            maxValue = 0
            if curAgent == "Minimax":
                for move in node.positionsLeft():
                    node.placeAgent(move, curAgent)
                    newValue = self.minimax(node, getOtherAgent(curAgent))
                    node.placeAgent(move, " ")
                    if (newValue > maxValue):
                        maxValue = newValue
                return maxValue
            else:
                for move in node.positionsLeft():
                    node.placeAgent(move, curAgent)
                    newValue = self.minimax(node, getOtherAgent(curAgent))
                    node.placeAgent(move, " ")
                    if (newValue < maxValue):
                        maxValue = newValue
                return maxValue

    def alphabeta(self, node, curAgent, alpha, beta):
        '''
        Alphabeta pruning minimax algorithm for choosing the best possible move towards
        winning the game
        '''
        if node.tempGameOver(node, curAgent)== -1 or node.tempGameOver(node, curAgent) == 1 or node.tempGameOver(node, curAgent) == 0:
            return node.tempGameOver(node, curAgent)
        else:
            maxValue = 0
            if curAgent == "Alphabeta_Minimax":
                for move in node.positionsLeft():
                    node.placeAgent(move, curAgent)
                    newValue = self.alphabeta(node, getOtherAgent(curAgent), alpha, beta)
                    node.placeAgent(move, " ")
                    if (newValue > maxValue):
                        maxValue = newValue
                    if (maxValue > beta):
                        return maxValue
                    else:
                        alpha = max(alpha, maxValue)
                return maxValue
            else:
                for move in node.positionsLeft():
                    node.placeAgent(move, curAgent)
                    newValue = self.alphabeta(node, getOtherAgent(curAgent), alpha, beta)
                    node.placeAgent(move, " ")
                    if (newValue < maxValue):
                        maxValue = newValue
                    if (maxValue < alpha):
                        return maxValue
                    else:
                        beta = min(beta, maxValue)
                return maxValue

    def expectimax(self, node, curAgent):
        '''
        Minimax algorithm for choosing the best possible move towards
        winning the game
        '''
        if node.tempGameOver(node, curAgent)== -1 or node.tempGameOver(node, curAgent) == 1 or node.tempGameOver(node, curAgent) == 0:
            return node.tempGameOver(node, curAgent)
        else:
            maxValue = 0
            if curAgent == "Expectimax":
                for move in node.positionsLeft():
                    node.placeAgent(move, curAgent)
                    newValue = self.expectimax(node, getOtherAgent(curAgent))
                    node.placeAgent(move, " ")
                    if (newValue > maxValue):
                        maxValue = newValue
                return maxValue
            else:
                NoofPossibilities = len(node.positionsLeft())
                probability = 1/NoofPossibilities
                expectiValue = 0
                for move in node.positionsLeft():
                    node.placeAgent(move, curAgent)
                    newValue = self.expectimax(node, getOtherAgent(curAgent))
                    node.placeAgent(move, " ")
                    expectiValue = expectiValue + (newValue * probability)
                return expectiValue

    def QLwin(self, board, Ql_key):
        """ If we have two in a row and the 3rd is available, take it. """
        # Check for diagonal wins
        diag1 = [self.boardvalues[0], self.boardvalues[4], self.boardvalues[8]]
        diag2 = [self.boardvalues[2], self.boardvalues[4], self.boardvalues[6]]
        if diag1.count(" ") == 1 and diag1.count(Ql_key) == 2:
            ind = diag1.index(" ")
            if ind == 0:
                return 0
            elif ind == 1:
                return 4
            else:
                return 8
        elif diag2.count(" ") == 1 and diag2.count(Ql_key) == 2:
            ind = diag2.index(" ")
            if ind == 0:
                return 2
            elif ind == 1:
                return 4
            else:
                return 6
        for i in range(3):
            count = 0
            rows = [self.boardvalues[count], self.boardvalues[count+1], self.boardvalues[count+2]]
            if rows.count(" ") == 1 and rows.count(Ql_key) == 2:
                ind = rows.index(" ")
                if ind == 0:
                    return count
                elif ind == 1:
                    return count+1
                else:
                    return count+2
            count = count + 3

        for j in range(3):
            count = 0
            cols = [self.boardvalues[count], self.boardvalues[count+3], self.boardvalues[count+6]]
            if cols.count(" ") == 1 and cols.count(Ql_key) == 2:
                ind = cols.index(" ")
                if ind == 0:
                    return count
                elif ind == 1:
                    return count+3
                else:
                    return count+6
            count = count + 1
        return None

    def blockWin(self, board, enemyKey):
        """ Block the opponent if she has a win available. """
        return self.QLwin(board, enemyKey)



    def pickcenter(self, board):
        """ Pick the center if it is available. """
        if self.boardvalues[4] == " ":
            return 4
        return None

    def pickcorner(self, board, enemyKey):

        corner = [self.boardvalues[0],self.boardvalues[2],self.boardvalues[6],self.boardvalues[8]]
        if corner.count(" ") == 4:
            return random.choice(corner)
        else:
            if self.boardvalues[0] == enemyKey and self.boardvalues[8] == " ":
                return 8
            elif self.boardvalues[2] == enemyKey and self.boardvalues[6] == " ":
                return 6
            elif self.boardvalues[8] == enemyKey and self.boardvalues[0] == " ":
                return 0
            elif self.boardvalues[6] == enemyKey and self.boardvalues[2] == " ":
                return 2
        return None

    def diamondside(self, board):
        """ Pick an empty side. """
        diamond = [self.boardvalues[1], self.boardvalues[3], self.boardvalues[5], self.boardvalues[7]]
        if diamond.count(" ") == 4:
            return random.choice(diamond)
        else:
            count = 1
            for i in range(0,3):
                if(diamond[i] == " "):
                    return count
                count = count + 2
        return None


    def trainedMove(self, board):
        """
        trained move for Q-Learning Agent
        """
        if(agent1 == "QLearning"):
            Ql_key = 'X'
            enemyKey = 'O'
        elif(agent2 == "QLearning"):
            Ql_key = 'O'
            enemyKey = 'X'
        # Chose randomly with some probability so that the teacher does not always win
        if random.random() > 0.9:
            return random.choice(game.positionsLeft())
        # Follow optimal strategy
        if(self.QLwin(board,Ql_key) != None and self.QLwin(board,Ql_key) != ' '):
            return self.QLwin(board,Ql_key)
        elif(self.blockWin(board, enemyKey) != None and self.blockWin(board, enemyKey) != ' '):
            return self.blockWin(board, enemyKey)
        elif(self.pickcenter(board) != None and self.pickcenter(board) != ' '):
            return self.pickcenter(board)
        elif(self.pickcorner(board, enemyKey) != None and self.pickcorner(board, enemyKey) != ' '):
            return self.pickcorner(board, enemyKey)
        elif(self.diamondside(board) != None and self.diamondside(board) != ' '):
            return self.diamondside(board)
        else:
            return random.choice(game.positionsLeft())

def getOtherAgent(currentAgent):
    if currentAgent == agent1:
        return agent2
    else:
        return agent1

def finalMove(game, currentAgent):
    bestValue = 0
    bestMove = []
    for move in game.positionsLeft():
        game.placeAgent(move, currentAgent)
        if(currentAgent == "Minimax"):
            newValue = game.minimax(game, getOtherAgent(currentAgent))
        elif(currentAgent == "Alphabeta_Minimax"):
            newValue = game.alphabeta(game, getOtherAgent(currentAgent), -1000, 1000)
        elif(currentAgent == "Expectimax"):
            newValue = game.expectimax(game, getOtherAgent(currentAgent))
        game.placeAgent(move, " ")
        if newValue >= bestValue:
            bestValue = newValue
            bestMove.append(move)
            print("Move",bestMove)
    if(len(bestMove) == 0):
        return random.choice(game.positionsLeft())
    else:
        return random.choice(bestMove)


if __name__ == "__main__":
    import random
    import math
    game = Game()
    game.board()
    print("Please Select Agent1 from following:")
    print("1.Minimax,2.Alphabeta_Minimax,3.Expectimax,4.QLearning")
    agent1 = input("Please Enter your choice of Agent1:")
    print(agent1)
    print("Please Select Agent2 from following(other than what you chose for Agent1):")
    print("1.Minimax,2.Alphabeta_Minimax,3.Expectimax,4.QLearning")
    agent2 = input("Please Enter your choice of Agent2:")
    print(agent2)
    game.gameState()

