
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
                col = location[0]//squareSize
                row = location[1]//squareSize

                if selectedSquare == (row, col):
                    selectedSquare = ()
                    clicks = []
                else:
                    clicks.append(selectedSquare)
                    if len(clicks) == 2:
                        pos1 = selectedSquare[0]
                        pos2 = selectedSquare[1]
                        if (gameState.board[pos1][pos2] != "--"):
                            if (gameState.board[row][col] == "--"):
                                if (gameState.board[pos1][pos2] == "wh"):
                                    gameState.board[row][col] = "wh"
                                elif (gameState.board[pos1][pos2] == "bl"):
                                    gameState.board[row][col] = "bl"
                                gameState.board[pos1][pos2] = "--"
                        clicks = []



                selectedSquare = (row, col)

        drawGameState(screen, gameState)
        clock.tick(30)
        p.display.flip()


def drawGameState(screen, gameState):
    drawBoard(screen)
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