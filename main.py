# Connect 4 AI

import numpy as np
import random as rd

def isValid(board): # Check if the board is valid
    if isinstance(board, np.ndarray) and board.shape == (7,7):
        return True
    else:
        return False 

def isFull(arr): # Check if the passed array contains empty spaces
    if empty in arr:
        return False
    else:
        return True

def opp(turn): # Returns opposite player
    if turn == pieces[0]:
        return pieces[1]
    else:
        return pieces[0]

def printBoard(board): # Print the board if it is valid
    # Check if the board is valid, if so store the number of rows and columns
    if isValid(board):
        nRows, nCols = board.shape
    else:
        print("The board is not valid!")
        return

    # If it is valid, print the board
    for i in np.arange(nRows):
        for j in np.arange(nCols):
            if j < nCols-1:
                print(str(board[i, j])[0] + ' | ', end='')
            else:
                print(str(board[i, j])[0])
        if i < nRows-1:
            print('--+---+---+---+---+---+--')
        
    print('0   1   2   3   4   5   6')

def isWinner(board): # If there is a winner, return winner; otherwise, return None
    if isValid(board):
        nRows, nCols = board.shape
    else:
        print("The board is not valid!")
        return

    toWin = 4
    
    for i in np.arange(nRows):
        for j in np.arange(nCols):
            if board[i, j] == empty: # if space isn't occupied by a piece, continue
                    continue
            if nRows-i >= toWin: # check for vertical wins
                checkArr = board[i:(i+toWin), j]
                if np.all(checkArr == board[i, j]):
                    return board[i, j]
            if nCols-j >= toWin: # check for horizontal wins
                checkArr = board[i, j:(j+toWin)]
                if np.all(checkArr == board[i, j]):
                    return board[i, j]
            if nRows-i >= toWin and nCols-j >= toWin: # check for down-and-right diagonal wins
                checkArr = np.array([])
                for k in np.arange(toWin):
                    checkArr = np.append(checkArr, board[i-k, j+k])
                if np.all(checkArr == board[i, j]):
                    return board[i, j]
            if nRows-i <= toWin and nCols-j >= toWin: # check for up-and-right diagonal wins
                checkArr = np.array([])
                for k in np.arange(toWin):
                    checkArr = np.append(checkArr, board[i-k, j+k])
                if np.all(checkArr == board[i, j]):
                    return board[i, j]

def placePiece(board, move, turn): # Adjust board to reflect move
    
    try:
        col = board[:, move]
    except:
        return board, False

    for i in np.arange(len(col)-1, -1, -1):
        if col[i] == empty:
            board[i, move] = turn
            return board, True
    
    return board, False

def chooseMove(board, turn): # Choose a move
    return rd.randint(0, board.shape[1]-1)

def minimax(board, turn, depth): # Given a board, returns 1, -1, or 0

    # Check if depth has exceeded 3; if so, return 0
    if depth > 3:
        return 0

    # Check if board is full; if so, return 0
    if isFull(board):
        return 0

    bestScore = -2

    for i in np.arange(np.shape[1]):
        if isFull(board[:,i]):
            dummyBoard = placePiece(board[i], i, turn)

            # First, check if the move will result in a win for the player; if so, return score of 1
            if isWinner(board) == True:
                bestScore = 1
            
            # Otherwise, find the minimax score of opponent
            else:
                if -minimax(dummyBoard, opp(turn), depth+1) > bestScore:
                    bestScore = -minimax(dummyBoard, opp(turn), depth+1)
    
    return bestScore

def game():
    # Initiate the game board
    board = np.full((7,7), empty) 

    # Ask the user which side they would like to be
    while True:
        print("Would you like to be " + pieces[0] + " or " + pieces[1] + "?")
        user = input()
        if user in pieces:
            break
        print("That is not a valid entry.")

    # Begin gameplay
    turn = pieces[0]

    while not isFull(board):
        # Prompt the user for a move
        if turn == user:
            printBoard(board)
            print("It's your turn, " + turn + ". Move to which place?")

        # Add move to board (if it's valid)
        while True:
            if turn == user:
                move = int(input())
            else:
                move = chooseMove(board, turn)
                print("Computer chooses " + str(move))
    
            board, validMove = placePiece(board[:], move, turn)
            if validMove:
                break
            print("That is not a valid move. Try again!")

        # Check for winner
        if isWinner(board) != None:
            printBoard(board)
            print("Game over. " + isWinner(board) + " has won.")
            break

        # Switch sides
        turn = opp(turn)

if __name__ == "__main__":
    
    empty = ' '
    pieces = ['X', 'O']

    game()
