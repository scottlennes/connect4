# Connect 4 AI

import numpy as np

def isValid(board):
    if isinstance(board, np.ndarray) and board.shape == (7,7):
        return True
    else:
        return False 

def printBoard(board):
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

def isWinner(board):
    if isValid(board):
        nRows, nCols = board.shape
    else:
        print("The board is not valid!")
        return

    toWin = 4
    
    for i in np.arange(nRows):
        for j in np.arange(nCols):
            if board[i, j] in [' ', 0]: # if space isn't occupied by a piece, continue
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
                checkArr = np.zeros(toWin)
                for k in np.arange(toWin):
                    checkArr[k] = board[i+k, j+k]
                if np.all(checkArr == board[i, j]):
                    return board[i, j]
            if nRows-i <= toWin and nCols-j >= toWin: # check for up-and-right diagonal wins
                checkArr = np.zeros(toWin)
                for k in np.arange(toWin):
                    checkArr[k] = board[i-k, j+k]
                if np.all(checkArr == board[i, j]):
                    return board[i, j]

if __name__ == "__main__":
    board = np.array([0,0,0,0,0,0,0,
                      0,0,0,0,0,0,0,
                      0,0,1,1,1,0,0,
                      0,0,0,0,1,0,0,
                      0,0,0,0,0,1,0,
                      0,0,0,0,0,0,1,
                      0,0,0,0,0,0,0])
    board = board.reshape(7,7)
    printBoard(board)
    print(isWinner(board))