import pygame as p
import board

WIDTH = 512
HEIGHT = WIDTH
DIMENSIONS = 8
squareSize = WIDTH // DIMENSIONS
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
    main.move = 1
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
                                piece = gameState.board[pos1][pos2]

                                movePiece(gameState, piece, pos1, pos2, row, col)
                                
                        clicks = []
                selectedSquare = (row, col)

        drawGameState(screen, gameState, selectedSquare)
        clock.tick(30)
        p.display.flip()

def changeColor(screen, gameState, selectedSquare):
 
        if selectedSquare != (): # if square is clicked.... (if square is not empty)
            r, c = selectedSquare

            if (gameState.board[r][c] != "--"): # if selected square has a piece....
                if ( (main.move == 1 and gameState.board[r][c] != "bl" and gameState.board[r][c] != "blk") or (main.move == 0 and gameState.board[r][c] != "wh" and gameState.board[r][c] != "whk") ): # highlight only black pieces if it's Black's turn or only white pieces if it's White's turn
                    s = p.Surface((WIDTH/DIMENSIONS, WIDTH/DIMENSIONS))
                    s.set_alpha(170) #set opacity
                    s.fill(p.Color('red')) # set color
                    screen.blit(s, (c*(WIDTH/DIMENSIONS), (r*WIDTH/DIMENSIONS)))

def movePiece(gameState, piece, pos1, pos2, row, col):
    direction1 = 1 if piece == "wh" else -1

    #for r in range (DIMENSIONS):  #musí brát
     #   for c in range (DIMENSIONS):
      #      if (gameState.board[r][c]):
       #         print (gameState.board[r][c])


    if ( main.move == 1 and piece=="wh" and (pos1 == row + 1) and ((pos2 == col + 1) or (pos2 == col - 1)) or ( main.move == 0 and piece=="bl" and (pos1 == row - 1) and ( (pos2 == col + 1) or (pos2 == col - 1)))):                                                            
        gameState.board[row][col] = piece # create new white piece
        gameState.board[pos1][pos2] = "--" # remove piece
        main.move = 1 if main.move != 1 else 0

    elif (  main.move == 1 and piece=="wh" and ((pos1 == row + 2) and (pos2 == col - 2)) and (gameState.board[row+1][col-1] != "--") and ( not gameState.board[row+1][col-1].startswith("wh") ) or ( main.move == 0 and piece=="bl" and ((pos1 == row - 2) and (pos2 == col - 2)) and (gameState.board[row-1][col-1] != "--") and ( not gameState.board[row-1][col-1].startswith("bl") )) ):                     
        gameState.board[row][col] = piece # create new piece
        gameState.board[row+direction1][col-1] = "--"
        gameState.board[pos1][pos2] = "--" # remove piece
        main.move = 1 if main.move != 1 else 0
                 
    elif ( main.move == 1 and piece=="wh" and ((pos1 == row + 2) and (pos2 == col + 2)) and (gameState.board[row+1][col+1] != "--") and ( not gameState.board[row+1][col+1].startswith("wh") ) or ( main.move == 0 and piece=="bl" and ((pos1 == row - 2) and (pos2 == col + 2)) and (gameState.board[row-1][col+1] != "--") and ( not gameState.board[row-1][col+1].startswith("bl"))  )) :
        gameState.board[row][col] = piece # create new white piece
        gameState.board[row+direction1][col+1] = "--"
        gameState.board[pos1][pos2] = "--" # remove piece
        main.move = 1 if main.move != 1 else 0

    elif (piece.endswith("k")):

        if (row < pos1):
            direction1 = 1 #UP
        else:
            direction1 = -1 #DOWN
        if (col < pos2):
            direction2 = 1 #LEFT
        else:
            direction2 = -1 #RIGHT


        jump =0
        for n in range(DIMENSIONS):
            if ( (((pos1 == row + n) or (pos1 == row - n)) and ((pos2 == col + n) or (pos2 == col - n))) and ( (piece == "blk" and main.move == 0) or (piece == "whk" and main.move == 1) ) ):
                if ((direction1 == 1 and direction2 == 1)):
                    for i in range(pos1 - row):
                        i = i + 1
                        if ((gameState.board[pos1 - i][pos2 - i] != "--")):
                            print("přeskok")
                            jump = jump+1

                            if (jump ==1):
                                gameState.board[row][col] = piece  # create new white piece
                                gameState.board[pos1 - direction1][pos2 - direction2] = "--"
                                gameState.board[pos1][pos2] = "--"  # remove piece
                                main.move = 1 if main.move != 1 else 0

                            else:
                                print("ill eagle move")




                if ((direction1 == -1 and direction2 == 1)):
                    for i in range(row - pos1):
                        i = i + 1
                        if ((gameState.board[pos1 + i][pos2 - i] != "--")):
                            print("přeskok")
                            jump = jump + 1

                            if (jump ==1):
                                gameState.board[row][col] = piece  # create new white piece
                                gameState.board[pos1 - direction1][pos2 - direction2] = "--"
                                gameState.board[pos1][pos2] = "--"  # remove piece
                                main.move = 1 if main.move != 1 else 0

                            else:
                                print("ill eagle move")


                if ((direction1 == 1 and direction2 == -1)):
                    for i in range(pos1 - row):
                        i = i + 1
                        if ((gameState.board[pos1 - i][pos2 + i] != "--")):
                            print("přeskok")
                            jump = jump + 1

                            if (jump ==1):
                                gameState.board[row][col] = piece  # create new white piece
                                gameState.board[pos1 - direction1][pos2 - direction2] = "--"
                                gameState.board[pos1][pos2] = "--"  # remove piece
                                main.move = 1 if main.move != 1 else 0

                            else:
                                print("ill eagle move")


                if ((direction1 == -1 and direction2 == -1)):
                    for i in range(row - pos1):
                        i = i + 1
                        if ((gameState.board[pos1 + i][pos2 + i] != "--")):
                            print("přeskok")
                            jump = jump + 1

                            if (jump ==1):
                                gameState.board[row][col] = piece  # create new white piece
                                gameState.board[pos1 - direction1][pos2 - direction2] = "--"
                                gameState.board[pos1][pos2] = "--"  # remove piece
                                main.move = 1 if main.move != 1 else 0


                            else:
                                print("ill eagle move")

                if (jump ==0):
                    gameState.board[row][col] = piece  # create new white piece
                    gameState.board[pos1][pos2] = "--"  # remove piece
                    main.move = 1 if main.move != 1 else 0







    if ((row == 0) and (gameState.board[row][col] == "wh") or (row == DIMENSIONS -1) and (gameState.board[row][col] == "bl") ): # promotion 
        gameState.board[row][col] = str(piece)+"k"

def drawBoard(screen):
    colors = [p.Color(235, 235, 208), p.Color(120, 188, 227)]
    for r in range(DIMENSIONS):
        for c in range(DIMENSIONS):
            color = colors[((r+c)%2)]
            p.draw.rect(screen, color, p.Rect(c*squareSize, r*squareSize, squareSize, squareSize))

def drawPieces(screen, board):
    for r in range(DIMENSIONS):
        for c in range(DIMENSIONS):
            piece = board[r][c]
            if piece != "--":
                screen.blit(IMAGES[piece], p.Rect(c*squareSize, r*squareSize, squareSize, squareSize))

def drawGameState(screen, gameState, selectedSquare):
    drawBoard(screen)
    changeColor(screen, gameState, selectedSquare)
    drawPieces(screen, gameState.board)

if __name__ == "__main__":
    main()
