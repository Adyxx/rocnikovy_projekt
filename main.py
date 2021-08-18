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
    pieces = ["wh", "bl"]
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

                                if move == 1:
                                    if (gameState.board[pos1][pos2] == "wh"):
                                        gameState.board[row][col] = "wh"#create new white piece
                                        gameState.board[pos1][pos2] = "--" #remove piece
                                        move = 0
                                        print("Black to move")
                                else:
                                    if (gameState.board[pos1][pos2] == "bl"):
                                        gameState.board[row][col] = "bl"#create new black piece
                                        gameState.board[pos1][pos2] = "--" #remove piece
                                        move = 1
                                        print("White to move")
                                        
                                          
                        clicks = []
                if len(clicks) == 1:#fixes problem with pieces not moving if clicked as second click
                    if (gameState.board[row][col] == "--"):
                        clicks = []


                selectedSquare = (row, col)

        drawGameState(screen, gameState, selectedSquare, move)
        clock.tick(30)
        p.display.flip()


def changeColor(screen, gameState, selectedSquare, move):
 
        if selectedSquare != ():
            r, c = selectedSquare

            if (gameState.board[r][c] != "--"):
                if ( (move == 1 and gameState.board[r][c] != "bl") or (move == 0 and gameState.board[r][c] != "wh") ):
                    s = p.Surface((WIDTH/DIMENSTIONS, WIDTH/DIMENSTIONS))
                    s.set_alpha(170)
                    s.fill(p.Color('red'))
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