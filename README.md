# Implementation of Multiple Tic Tac Toe Agents in a Tournament setting
## Introduction:
Tic Tac Toe is a two player game which is played in any square grid. Tic Tac Toe is a Zero sum game where win of player1 is a loss of player2. Usually it is playing putting either X or O in the grid. If Player1 gets key X then player2 gets key O. If any player achieves their key in any all the cells of any row or column or diagonal then that player wins.

! [Tic Tac Toe] (https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.wayfair.com%2Ffurniture%2Fpdx%2Fbreakwater-bay-schumaker-wood-large-spring-tic-tac-toe-game-w000931690.html&psig=AOvVaw2i4TVEnyLese5TECkpBXfe&ust=1607664837171000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCJiLsq7Ywu0CFQAAAAAdAAAAABAE)
 
## Algorithms used:
We have created four Agents to play against each other.
* Minimax Agent
* Alpha beta Minimax Agent
* Expectimax Agent
* Q-Learning Agent
## Minimax Algorithm:
Minimax is a backtracking algorithm which is commonly used in decision making and game theory especially in 2-player zero sum games to make an optimal move. In Minimax tree representation each node will be a game state upon some action performed. It has recursive layers of max and min layers where maximizer tries to maximize the outcome for player and minimizer tries to sabotages the outcome of the player


## Alpha Beta Minimax Algorithm:
This is very much similar to Minimax with the only difference where the algorithm decides which child nodes or other game states the algorithm have to check further before returning best value. This is done using alpha and beta values. Alpha holds best value for maximizer and Beta holds best value for minimizer

## Expectimax Algorithm:
This is also similar to Minimax but other than Minimizer we have chance node which is the average of all available nodes which is the expected utility. This Algorithm does not assume that opponent may always play optimally rather it assumes that their next move is based on chance

## Q-Learning Algorithm:
Q-Learning is reinforcement-based algorithm where initially agent has no idea about the environment. It learns about the environment by playing few games and getting rewards. By obtaining rewards agent realise which move is good and which is not. This Agent should be trained with game environment before it can be played with other players in tournament.

## Instructions to run code:
* Run the file multiagent_tictactoe.py 
*	Enter agent1 and agent2 as shown in the console (without typos) and see how the agents play. 
*	Run multiple times and check with multiple agents to compare which agent plays the game better.
*	Make sure you select 2 different agents for Tic-Tac-Toe game.
