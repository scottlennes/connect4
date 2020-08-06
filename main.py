# Connect 4 AI

import numpy as np
import random as rd


def isValid(board): # Check if the board is valid
    if isinstance(board, np.ndarray) and board.shape == (7,7):
        return True
    else:
        return False 

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

def isWinner(board): # If there is a winner, return winner; otherwise, return None
    if isValid(board):
        nRows, nCols = board.shape
    else:
        print("The board is not valid!")
        return

    toWin = 4
    
    for i in np.arange(nRows):
        for j in np.arange(nCols):
            if board[i, j] == ' ': # if space isn't occupied by a piece, continue
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
        if col[i] == ' ':
            board[i, move] = turn
            return board, True
    
    return board, False

def chooseMove(board, turn):
    return rd.randint(0, board.shape[1]-1)

def game():
    
    pieces = (' ','X','O')
    boardSize = (7,7)

    board = np.full(boardSize, pieces[0]) 
    turn = pieces[1]

    # Ask the user which side they would like to be
    while True:
        print("Would you like to be " + pieces[1] + " or " + pieces[2] + "?")
        user = input()
        if user in pieces[1:3]:
            break
        print("That is not a valid entry.")

    for i in np.arange(boardSize[0] * boardSize[1]):
        
        if turn == user:
            printBoard(board)
            print("It's your turn, " + turn + ". Move to which place?")

        while True:
            if turn == user:
                move = int(input())
            else:
                move = chooseMove(board, turn)
                print("Computer chooses " + str(move))
    
            # Add move to board, check for invalid move
            board, validMove = placePiece(board[:], move, turn)
            if validMove:
                break
            print("That is not a valid move. Try again!")

        # Check for win
        if isWinner(board) != None:
            printBoard(board)
            print("Game over. " + isWinner(board) + " has won.")
            break

        if turn == pieces[1]:
            turn = pieces[2]
        else:
            turn = pieces[1]    


if __name__ == "__main__":
    game()