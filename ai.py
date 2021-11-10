#Use this branch to make AI
import pygame as p
import board
import random
import main as man

def eidam(gameState):#main

    bestMove(gameState)
    whatMove(gameState)
    return gameState

def whatMove(gameState):
    '''
    pos1=random.randint(0, man.DIMENSIONS-1)
    pos2=random.randint(0, man.DIMENSIONS-1)
    row=1+pos1
    col=1+pos2
    piece="bl"
    gameState.board[pos1][pos2] = piece
    '''
    return gameState
    #man.movePiece(gameState, piece, pos1, pos2, row, col)

def value():
    print("Current value:")

def move(gameState, piece, pos1, pos2, row, col):

    print("testAI")

def bestMove(gameState):
    i =0
    value = 0
    bestValue = 0
    bestMov = []
    possibleMoves = man.allPossibleMoves(gameState)
    for r in range(man.DIMENSIONS):
        for c in range(man.DIMENSIONS):
            if gameState.board[r][c] == "bl":
                while(possibleMoves[i] != ";"):
                    possibleMoves[i]
                    possibleMoves[i+1]
                    i= i+2
                i = i+1
                    #if()
                        #value = x+y+z


                if (value > bestValue):
                    bestMov = []
                    bestMov.append(r)
                    bestMov.append(r)
                    bestValue = value


        print(bestMov)
