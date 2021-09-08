import pygame as p
import board

WIDTH = 512
HEIGHT = WIDTH
DIMENSTIONS = 8
squareSize = WIDTH // DIMENSTIONS
IMAGES = {}

'''
    images
'''

def loadImages():
    pieces = ["wh", "bl", "whk", "blk"]
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("images/" + piece + ".png"),(squareSize, squareSize))

'''
    main
'''
def main():
    p.init()
    screen = p.display.set_mode((WIDTH, HEIGHT))
    screen.fill(p.Color("white"))
    clock = p.time.Clock()
    move = 1
    gameState = board.GameState()
    #print(gameState.board)
    loadImages()
    running =  True
    selectedSquare = () #memory
    clicks = []
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
            elif e.type == p.MOUSEBUTTONDOWN:
                location = p.mouse.get_pos()
                col = location[0]//squareSize#location 2. click
                row = location[1]//squareSize#location 2. click

                if (gameState.board[row][col] != "--"):# if there is piece on the location of the player's second click...          
	                clicks = [] # then remove click memory
                    # this fixes problem where player clicks a piece and then other piece that wouldn't move

                if selectedSquare == (row, col):# reset when clicked same position
                    selectedSquare = ()
                    clicks = []
                else:
                    
                    clicks.append(selectedSquare)
                    if len(clicks) == 2:
                        pos1 = selectedSquare[0] #location 1. click
                        pos2 = selectedSquare[1] #location 1. click
                        if (gameState.board[pos1][pos2] != "--"): #does 1. position have piece?
                            if (gameState.board[row][col] == "--"): # is 2. position empty?
                                #what color am I moving?
                                if move == 1: # if it's White's turn
                                    if ((pos1 == row + 1) and ((pos2 == col + 1) or (pos2 == col - 1))):

                                        piece = "wh" if gameState.board[pos1][pos2] == "wh" else "whk" # if there is white piece...
                                        gameState.board[row][col] = piece # create new white piece
                                        gameState.board[pos1][pos2] = "--" # remove piece
                                        move = 0

                                    elif (((pos1 == row + 2) and (pos2 == col - 2)) and ((gameState.board[row+1][col-1] != "--") and (gameState.board[row+1][col-1] != "wh") and (gameState.board[row+1][col-1] != "whk") )) : # or ((pos1 == row - 2) and (pos2 == col - 2) and (gameState.board[row - 1][col - 1] != "--"))
                                                                       
                                        piece = "wh" if gameState.board[pos1][pos2] == "wh" else "whk" # if there is white piece...
                                        gameState.board[row][col] = piece # create new white piece
                                        gameState.board[row+1][col-1] = "--"
                                        gameState.board[pos1][pos2] = "--" # remove piece
                                        move = 0
                                        
                                    elif (((pos1 == row + 2) and (pos2 == col + 2)) and ((gameState.board[row+1][col+1] != "--") and (gameState.board[row+1][col-1] != "wh") and (gameState.board[row+1][col-1] != "whk") )) : # or ((pos1 == row - 2) and (pos2 == col - 2) and (gameState.board[row - 1][col - 1] != "--"))
                                                                           
                                        piece = "wh" if gameState.board[pos1][pos2] == "wh" else "whk" # if there is white piece...
                                        gameState.board[row][col] = piece # create new white piece
                                        gameState.board[row+1][col+1] = "--"
                                        gameState.board[pos1][pos2] = "--" # remove piece
                                        move = 0                             

                                    if ((row == 0) and (gameState.board[row][col] == "wh")): #promoce
                                        gameState.board[row][col] = "whk"

                                else:
                                    if (pos1 == row - 1) and ((pos2 == col + 1) or (pos2 == col - 1)):

                                        piece = "bl" if gameState.board[pos1][pos2] == "bl" else "blk" # if there is black piece...
                                        gameState.board[row][col] = piece # create new black piece
                                        gameState.board[pos1][pos2] = "--" # remove piece
                                        move = 1
      
                                    elif (((pos1 == row - 2) and (pos2 == col - 2)) and ((gameState.board[row-1][col-1] != "--") and (gameState.board[row+1][col-1] != "bl") and (gameState.board[row+1][col-1] != "blk") )) : # or ((pos1 == row - 2) and (pos2 == col - 2) and (gameState.board[row - 1][col - 1] != "--"))
                                        
                                        piece = "bl" if gameState.board[pos1][pos2] == "bl" else "blk" # if there is black piece...
                                        gameState.board[row][col] = piece # create new black piece
                                        gameState.board[row-1][col-1] = "--" # delete white piece
                                        gameState.board[pos1][pos2] = "--" # remove piece
                                        move = 1
      
                                    elif (((pos1 == row - 2) and (pos2 == col + 2)) and ((gameState.board[row-1][col+1] != "--") and (gameState.board[row+1][col-1] != "bl") and (gameState.board[row+1][col-1] != "blk") )) : # or ((pos1 == row - 2) and (pos2 == col - 2) and (gameState.board[row - 1][col - 1] != "--"))
                                        
                                        piece = "bl" if gameState.board[pos1][pos2] == "bl" else "blk" # if there is black piece...
                                        gameState.board[row][col] = piece # create new black piece
                                        gameState.board[row-1][col+1] = "--" # delete white piece
                                        gameState.board[pos1][pos2] = "--" # remove piece
                                        move = 1    

                                    if ((row == DIMENSTIONS -1) and (gameState.board[row][col] == "bl")): #promoce
                                        gameState.board[row][col] = "blk"

                        clicks = []

                selectedSquare = (row, col)

        drawGameState(screen, gameState, selectedSquare, move)
        clock.tick(30)
        p.display.flip()


def changeColor(screen, gameState, selectedSquare, move):
 
        if selectedSquare != (): # if square is clicked.... (if square is not empty)
            r, c = selectedSquare

            if (gameState.board[r][c] != "--"): # if selected square has a piece....
                if ( (move == 1 and gameState.board[r][c] != "bl" and gameState.board[r][c] != "blk") or (move == 0 and gameState.board[r][c] != "wh" and gameState.board[r][c] != "whk") ): # highlight only black pieces if it's Black's turn or only white pieces if it's White's turn
                    s = p.Surface((WIDTH/DIMENSTIONS, WIDTH/DIMENSTIONS))
                    s.set_alpha(170) #set opacity
                    s.fill(p.Color('red')) # set color
                    screen.blit(s, (c*(WIDTH/DIMENSTIONS), (r*WIDTH/DIMENSTIONS)))


def drawGameState(screen, gameState, selectedSquare, move):
    drawBoard(screen)
    changeColor(screen, gameState, selectedSquare, move)
    drawPieces(screen, gameState.board)


def drawBoard(screen):
    colors = [p.Color(235, 235, 208), p.Color(120, 188, 227)]
    for r in range(DIMENSTIONS):
        for c in range(DIMENSTIONS):
            color = colors[((r+c)%2)]
            p.draw.rect(screen, color, p.Rect(c*squareSize, r*squareSize, squareSize, squareSize))


def drawPieces(screen, board):
    for r in range(DIMENSTIONS):
        for c in range(DIMENSTIONS):
            piece = board[r][c]
            if piece != "--":
                screen.blit(IMAGES[piece], p.Rect(c*squareSize, r*squareSize, squareSize, squareSize))


if __name__ == "__main__":
    main()
