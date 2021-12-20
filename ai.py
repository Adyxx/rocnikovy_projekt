#Use this branch to make AI
import pygame as p
import board
import random
import oop as man
import copy

#import tensorflow as tf
#import mysql.connector

howManyTurns = 2

def eidam(gameState):#main

    bestMove(gameState)


def intoTheFuture(gameState, howManyTurns, value):
    game_copy = gameState

    while(howManyTurns >0):

        howManyTurns = howManyTurns - 1


def bValue(possibleMoves, gameState):
    i=0
    bestValue =0
    boardValue =0
    bestBoardValue =0
    bMove = []
    gameCopy = copy.deepcopy(gameState.board)
    whatPawn=0
    pawn =0
    numStred=0
    #testing values
    #make values random, change 1 value at a time, change it for x amount of time, save values somewhere
    #Not sure if it counts as AI but it should do what I want it to

    #boardValue = numFriendly - numEnemy
    king = 10
    pieceOnSide = 1
    protectingPiece = 2
    #if boardValue <0 -> randomly change all values
    #if boardValue >0 -> slightly change 1 value, if better, keep value
    for x in possibleMoves:
        numStred += 1
    while (i<numStred):
        if (possibleMoves[i] == ";"):
            pawn +=1
        for r in range(man.DIMENSIONS):
            for c in range(man.DIMENSIONS):
                if gameCopy[r][c] == "blk":
                    boardValue+=king
                    if ((c == man.DIMENSIONS-1) or (c == 0)):
                        boardValue+=pieceOnSide
                    if ((r + 1 < man.DIMENSIONS) and (c + 1 < man.DIMENSIONS) and r - 1 > 0 and c - 1 > 0 and (
                            (gameCopy[r + 1][c + 1].startswith("bl")) or (gameCopy[r + 1][c - 1].startswith("bl")) or (
                            gameCopy[r - 1][c + 1].startswith("bl")) or (gameCopy[r - 1][c - 1].startswith("bl")))):
                        boardValue += protectingPiece


                elif gameCopy[r][c] == "whk":
                    boardValue -= king
                    if ((c == man.DIMENSIONS-1) or (c == 0)):
                        boardValue-=pieceOnSide
                    if ((r + 1 < man.DIMENSIONS) and (c + 1 < man.DIMENSIONS) and r - 1 > 0 and c - 1 > 0 and (
                            (gameCopy[r + 1][c + 1].startswith("bl")) or (gameCopy[r + 1][c - 1].startswith("bl")) or (
                            gameCopy[r - 1][c + 1].startswith("bl")) or (gameCopy[r - 1][c - 1].startswith("bl")))):
                        boardValue += protectingPiece


                elif gameCopy[r][c] == "bl":
                    boardValue +=1
                    if ((c == man.DIMENSIONS-1) or (c == 0)):
                        boardValue+=pieceOnSide

                    if ((r + 1 < man.DIMENSIONS) and (c + 1 < man.DIMENSIONS) and r - 1 > 0 and c - 1 > 0 and (
                            (gameCopy[r + 1][c + 1].startswith("bl")) or (gameCopy[r + 1][c - 1].startswith("bl")) or (
                            gameCopy[r - 1][c + 1].startswith("bl")) or (gameCopy[r - 1][c - 1].startswith("bl")))):
                        boardValue += protectingPiece


                elif gameCopy[r][c] == "wh":
                    boardValue -=1
                    if ((c == man.DIMENSIONS-1) or (c == 0)):
                        boardValue-=pieceOnSide
                    if ((r + 1 < man.DIMENSIONS) and (c + 1 < man.DIMENSIONS) and r - 1 > 0 and c - 1 > 0 and (
                            (gameCopy[r + 1][c + 1].startswith("bl")) or (gameCopy[r + 1][c - 1].startswith("bl")) or (
                    gameCopy[r - 1][c + 1].startswith("bl")) or (gameCopy[r - 1][c - 1].startswith("bl")))):
                        boardValue += protectingPiece

                
                

        if (possibleMoves[i] == ";"):
            pawn = i+1
        i+=1

        gameCopy = copy.deepcopy(gameState.board)

        if (bestBoardValue <= boardValue):
            bestBoardValue = boardValue
            bMove = []
            bMove.append(possibleMoves[pawn])
            bMove.append(possibleMoves[pawn+1])

        gameCopy[possibleMoves[pawn][0]][possibleMoves[pawn][1]] = "--"
        gameCopy[possibleMoves[pawn+1][0]][possibleMoves[pawn+1][1]] = "bl"

    if (bMove == []):
        bestBoardValue = boardValue
        bMove.append(possibleMoves[pawn])
        bMove.append(possibleMoves[pawn + 1])

    print("Current value:")
    return bMove
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
    gameState.board[bestMov[0][0]][bestMov[0][1]] = "--"
    gameState.board[bestMov[1][0]][bestMov[1][1]] = "bl"

    print(bestMov)
