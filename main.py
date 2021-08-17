
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
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
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