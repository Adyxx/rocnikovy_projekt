#Use this branch to make AI
import pygame as p
import board
import random
import main as man
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
    value = 0
    bestValue =0
    bestMov = []

    #testing values
    #make values random, change 1 value at a time, change it for x amount of time, save values somewhere
    #Not sure if it counts as AI but it should do what I want it to

    #boardValue = numFriendly - numEnemy
    makeKing = 10
    takePiece = 1
    loosePiece = -1
    pieceOnSide = 0,75


    #if boardValue <0 -> randomly change all values
    #if boardValue >0 -> slightly change 1 value, if better, keep value



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
