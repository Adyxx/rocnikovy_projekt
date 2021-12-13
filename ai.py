#Use this branch to make AI
import pygame as p
import board
import random
import oop as man
#import tensorflow as tf
#import mysql.connector

howManyTurns = 2

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

def intoTheFuture(gameState, howManyTurns, value):
    game_copy = gameState

    while(howManyTurns >0):

        howManyTurns = howManyTurns - 1


def bValue(moves, gameState):
    i=0
    bestValue =0
    boardValue =0
    bestBoardValue =0
    bestMov = []
    gameCopy = gameState
    whatPawn=0
    pawn =0
    #testing values
    #make values random, change 1 value at a time, change it for x amount of time, save values somewhere
    #Not sure if it counts as AI but it should do what I want it to

    #boardValue = numFriendly - numEnemy
    king = 10
    pieceOnSide = 1

    #if boardValue <0 -> randomly change all values
    #if boardValue >0 -> slightly change 1 value, if better, keep value

    while (len(possibleMoves)):
        for r in range(man.DIMENSIONS):
            for c in range(man.DIMENSIONS):
                if gameCopy.board[r][c] == "blk":
                    boardValue+=king
                if gameCopy.board[r][c] == "whk":
                    boardValue -= king
                if gameCopy.board[r][c] == "bl":
                    boardValue +=1

                if gameCopy.board[r][c] == "wh":
                    boardValue -=1
                if (bestBoardValue < boardValue):
                    bestBoardValue = boardValue
                    whatPawn = pawn

        gameCopy = gameState
        gameCopy.board[possibleMoves[0+pawn]][possibleMoves[1+pawn]] = "bl"
        gameCopy.board[possibleMoves[2+pawn]][possibleMoves[3+pawn]] = "--"
        pawn +=1

    #database(r,c)
    print("Current value:")
    return bestMov
'''
def database(r,c):
    mydb = mysql.connector.connect(
        host="localhost",
        user="eidam",
        password="cheese",
        database="cheesecake"
    )
    moves = mydb.cursor()
    moves.execute("CREATE DATABASE mydatabase")
    sql = "INSERT INTO moves (row, col) VALUES (%s, %s)"
    vall = (r, c)
    moves.execute(sql, vall)
    mydb.commit()
    print("arghhhhh")
'''

def move(gameState, piece, pos1, pos2, row, col):

    print("testAI")

def bestMove(gameState):
    bestMov = []
    possibleMoves = man.allPossibleMoves(gameState)
    bestMov = bValue(possibleMoves, gameState)

    gameState.board[bestMov[0]][bestMov[1]] = "bl"
    gameState.board[bestMov[2]][bestMov[3]] = "--"
    print(bestMov)
