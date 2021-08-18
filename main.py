
import pygame as p
import board


WIDTH = 512
HEIGHT = WIDTH
DIMENSTIONS = 8
squareSize = WIDTH // DIMENSTIONS
IMAGES = {}
colorr=(120, 188, 227)


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
                                if (gameState.board[pos1][pos2] == "wh"):
                                    gameState.board[row][col] = "wh"#create new white piece
                                elif (gameState.board[pos1][pos2] == "bl"):
                                    gameState.board[row][col] = "bl"#create new black piece
                                gameState.board[pos1][pos2] = "--" #remove piece

                        clicks = []



                selectedSquare = (row, col)

        drawGameState(screen, gameState, selectedSquare)
        clock.tick(30)
        p.display.flip()


def changeColor(screen, gameState, selectedSquare):
        if selectedSquare != ():
            r, c = selectedSquare
            if (gameState.board[r][c] != "--"):
                s = p.Surface((WIDTH/8, WIDTH/8))
                s.set_alpha(170)
                s.fill(p.Color('red'))
                screen.blit(s, (c*(WIDTH/8), (r*WIDTH/8)))


def drawGameState(screen, gameState, selectedSquare):
    drawBoard(screen, colorr)
    changeColor(screen, gameState, selectedSquare)
    drawPieces(screen, gameState.board)


def drawBoard(screen, colorr):
    colors = [p.Color(235, 235, 208), p.Color(colorr)]
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