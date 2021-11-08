#Use this branch to make AI
import pygame as p
import board
import random
import main as man

def eidam(gameState):#main

    whatMove(gameState)
    return gameState

def whatMove(gameState):
    pos1=random.randint(0, man.DIMENSIONS-1)
    pos2=random.randint(0, man.DIMENSIONS-1)
    row=1+pos1
    col=1+pos2
    piece="bl"
    gameState.board[pos1][pos2] = piece
    return gameState
    #man.movePiece(gameState, piece, pos1, pos2, row, col)

def value():
    print("Current value:")

def move(gameState, piece, pos1, pos2, row, col):

    print("testAI")