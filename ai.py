#Use this branch to make AI
import pygame as p
import board
import random
import main as man
#import mysql.connector



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

def bValue(moves, gameState):
    i=0
    value = 0
    bestValue =0
    for r in range(man.DIMENSIONS):
        for c in range(man.DIMENSIONS):
            if gameState.board[r][c] == "bl":
                while(moves[i] != ";"):
                    value = 0
                    row = moves[i]
                    col = moves[i + 1]
                    if ((col == 0) or (col == man.DIMENSIONS -1)):
                        value = value + 4
                    if ((col == 1) or (col == man.DIMENSIONS -2)):
                        value = value + 3

                    if (value >= bestValue):
                        bestMov = []
                        bestMov.append(row)
                        bestMov.append(col)
                        bestMov.append(r)
                        bestMov.append(c)
                        bestValue = value


                    i=i+2
                i = i + 1


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
