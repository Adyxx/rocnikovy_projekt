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
    i=1
    bestValue =0
    boardValue =0
    bestBoardValue =-999
    bMove = []
    gameCopy = copy.deepcopy(gameState)
    whatPawn=0
    pawn =0
    numStred=0
    numStredn=0
    movedd=0
    #testing values
    #make values random, change 1 value at a time, change it for x amount of time, save values somewhere
    #Not sure if it counts as AI but it should do what I want it to

    #boardValue = numFriendly - numEnemy
    king = 10
    pieceOnSide = 1
    protectingPiece = 2
    willBeEaten = -20
    #if boardValue <0 -> randomly change all values
    #if boardValue >0 -> slightly change 1 value, if better, keep value
    for x in possibleMoves:
        if x==";":
            numStred += 1
    for u in range (len(possibleMoves) - numStred):
        if (possibleMoves[pawn] == ";"):
            pawn +=1
        for r in range(man.DIMENSIONS):
            for c in range(man.DIMENSIONS):


                #print(man.main.possibleMovesW)
                #gameCopy.board[man.main.possibleMovesW[1][0]][man.main.possibleMovesW[1][1]] = "--"
                #gameCopy.board[man.main.possibleMovesW[2][0]][man.main.possibleMovesW[2][1]] = "wh"
                if gameCopy.board[r][c] == "blk":
                    boardValue+=king
                    if ((c == man.DIMENSIONS-1) or (c == 0)):
                        boardValue+=pieceOnSide
                    if ((r + 1 < man.DIMENSIONS) and (c + 1 < man.DIMENSIONS) and r - 1 > 0 and c - 1 > 0 and (
                            (gameCopy.board[r + 1][c + 1].startswith("bl")) or (gameCopy.board[r + 1][c - 1].startswith("bl")) or (
                            gameCopy.board[r - 1][c + 1].startswith("bl")) or (gameCopy.board[r - 1][c - 1].startswith("bl")))):
                        boardValue += protectingPiece


                elif gameCopy.board[r][c] == "whk":
                    boardValue -= king
                    if ((c == man.DIMENSIONS-1) or (c == 0)):
                        boardValue-=pieceOnSide
                    if ((r + 1 < man.DIMENSIONS) and (c + 1 < man.DIMENSIONS) and (r - 1 > 0) and (c - 1 > 0) and (
                            (gameCopy.board[r + 1][c + 1].startswith("bl")) or (gameCopy.board[r + 1][c - 1].startswith("bl")) or (
                            gameCopy.board[r - 1][c + 1].startswith("bl")) or (gameCopy.board[r - 1][c - 1].startswith("bl")))):
                        boardValue += protectingPiece


                elif gameCopy.board[r][c] == "bl":
                    boardValue +=2
                    if ((c == man.DIMENSIONS-1) or (c == 0)):
                        boardValue+=pieceOnSide

                    if ((r + 1 < man.DIMENSIONS) and (c + 1 < man.DIMENSIONS) and r - 1 > 0 and c - 1 > 0 and (
                            (gameCopy.board[r + 1][c + 1].startswith("bl")) or (gameCopy.board[r + 1][c - 1].startswith("bl")) or (
                            gameCopy.board[r - 1][c + 1].startswith("bl")) or (gameCopy.board[r - 1][c - 1].startswith("bl")))):
                        boardValue += protectingPiece

                    if ((r + 1 < man.DIMENSIONS) and (c + 1 < man.DIMENSIONS) and r - 1 > 0 and c - 1 > 0 and (
                            (gameCopy.board[r + 1][c + 1].startswith("wh")) or (
                    gameCopy.board[r + 1][c - 1].startswith("wh")) or (
                                    gameCopy.board[r - 1][c + 1].startswith("wh")) or (
                            gameCopy.board[r - 1][c - 1].startswith("wh")))):
                        boardValue+=willBeEaten


                elif gameCopy.board[r][c] == "wh":
                    boardValue -=2
                    if ((c == man.DIMENSIONS-1) or (c == 0)):
                        boardValue-=pieceOnSide
                    if ((r + 1 < man.DIMENSIONS) and (c + 1 < man.DIMENSIONS) and r - 1 > 0 and c - 1 > 0 and (
                            (gameCopy.board[r + 1][c + 1].startswith("bl")) or (gameCopy.board[r + 1][c - 1].startswith("bl")) or (
                    gameCopy.board[r - 1][c + 1].startswith("bl")) or (gameCopy.board[r - 1][c - 1].startswith("bl")))):
                        boardValue += protectingPiece





        if (possibleMoves[0] == 0):
            print("black cannot move")
        if(movedd>0):
            if (bestBoardValue <= boardValue):
                bestBoardValue = boardValue
                bMove = []
                bMove.append(possibleMoves[pawn])
                bMove.append(possibleMoves[pawn + i])
            i += 1
            if (((len(possibleMoves)>i+1)) and possibleMoves[pawn+i] == ";"):
                pawn = pawn+i+1
                i=1

                print("out of range")
            if ((len(possibleMoves)==3) or (len(possibleMoves)==4) ):
                bMove = []
                bMove.append(possibleMoves[1])
                bMove.append(possibleMoves[2])
                return bMove

            gameCopy = copy.deepcopy(gameState)


            if (possibleMoves[pawn+i] == ";"):
                pawn = pawn+i+1
                i=1
        if (possibleMoves[pawn + i] == 0):
            return bMove
        if (gameCopy.board[possibleMoves[pawn][0]][possibleMoves[pawn][1]] =="bl"):
            gameCopy.board[possibleMoves[pawn][0]][possibleMoves[pawn][1]] = "--"
            gameCopy.board[possibleMoves[pawn+i][0]][possibleMoves[pawn+i][1]] = "bl"
        else:
            gameCopy.board[possibleMoves[pawn + i][0]][possibleMoves[pawn + i][1]] = "blk"
        movedd+=1

        #man.allPossibleMoves(gameCopy)

        #gameCopy.board[man.main.possibleMovesW[1][0]][man.main.possibleMovesW[1][1]] = "--"
        #gameCopy.board[man.main.possibleMovesW[2][0]][man.main.possibleMovesW[2][1]] = "wh"


        print(possibleMoves[pawn+1][0])
        boardValue =0
        if (possibleMoves[pawn+1][0] == man.DIMENSIONS - 1):
            gameCopy.board[possibleMoves[pawn+1][0]][possibleMoves[pawn+1][1]] = "blk"

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
def whiteMove(gameState):
    possibleMoves = man.allPossibleMoves(gameState)


def move(gameState, piece, pos1, pos2, row, col):

    print("testAI")

def bestMove(gameState):
    bestMov = []
    possibleMoves = man.allPossibleMoves(gameState)
    bestMov = bValue(possibleMoves, gameState)

    if ((gameState.board[bestMov[0][0]][bestMov[0][1]] == "bl") and ((bestMov[0][1] - bestMov[1][1] ==2))):
        gameState.board[bestMov[0][0]][bestMov[0][1]] = "--"
        gameState.board[bestMov[0][0]+1][bestMov[0][1]-1] = "--"
        gameState.board[bestMov[1][0]][bestMov[1][1]] = "bl"
    elif ((bestMov[1][1] - bestMov[0][1] ==2)):
        gameState.board[bestMov[0][0]][bestMov[0][1]] = "--"
        gameState.board[bestMov[0][0]+1][bestMov[0][1]+1] = "--"
        gameState.board[bestMov[1][0]][bestMov[1][1]] = "bl"

    elif ((bestMov[0][1] - bestMov[1][1] >= 2) or (bestMov[0][1] - bestMov[1][1] <= 2) and
              gameState.board[bestMov[0][0]][bestMov[0][1]] == "blk"):
        gameState.board[bestMov[0][0]][bestMov[0][1]] = "--"
        gameState.board[bestMov[1][0] - 1][bestMov[1][1] - 1] = "--"
        gameState.board[bestMov[1][0]][bestMov[1][1]] = "blk"
    elif (gameState.board[bestMov[0][0]][bestMov[0][1]] == "bl" ):
        gameState.board[bestMov[0][0]][bestMov[0][1]] = "--"
        gameState.board[bestMov[1][0]][bestMov[1][1]] = "bl"

    elif (gameState.board[bestMov[0][0]][bestMov[0][1]] == "blk" and ((bestMov[0][1] - bestMov[1][1] !=2) or (bestMov[0][1] - bestMov[1][1] !=-2))):
        gameState.board[bestMov[0][0]][bestMov[0][1]] = "--"
        gameState.board[bestMov[1][0]][bestMov[1][1]] = "blk"







    if (bestMov[1][0] == man.DIMENSIONS-1):
        gameState.board[bestMov[1][0]][bestMov[1][1]] = "blk"

    print(bestMov)
