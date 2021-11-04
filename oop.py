import pygame as p
import board

WIDTH = 512
HEIGHT = WIDTH
DIMENSIONS = 8
IMAGES = {}
squareSize = WIDTH // DIMENSIONS
gameState = board.GameState()

class Board:  
    def __init__(self, color1, color2, screen):
        self.color1 = color1
        self.color2 = color2
        self.screen = screen

    def drawBoard(self):
        boardColors = [p.Color(self.color1), p.Color(self.color2)]

        for r in range(DIMENSIONS):
            for c in range(DIMENSIONS):
                color = boardColors[((r + c) % 2)]
                p.draw.rect(self.screen, color, p.Rect(c * squareSize, r * squareSize, squareSize, squareSize))

    def drawPieces(self):
        for r in range(DIMENSIONS):
            for c in range(DIMENSIONS):
                piece = gameState.board[r][c]
                if piece != "--":
                    self.screen.blit(IMAGES[piece], p.Rect(c * squareSize, r * squareSize, squareSize, squareSize))

    def drawHighlight(self):
        if main.clicks != []:
            r = main.clicks[-1][0]
            c = main.clicks[-1][1]
            if (gameState.board[main.clicks[0][0]][main.clicks[0][1]] != "--"):
                s = p.Surface((WIDTH / DIMENSIONS, WIDTH / DIMENSIONS))
                s.set_alpha(150)  # set opacity
                s.fill(p.Color('orange'))  # set color
                self.screen.blit(s, (c * (WIDTH / DIMENSIONS), (r * WIDTH / DIMENSIONS)))

class Piece:
    def __init__(self):
        pass

    def move(self):
        main.clicks = [] if (gameState.board[p.mouse.get_pos()[1] // squareSize][p.mouse.get_pos()[0] // squareSize] != "--") else main.clicks
        main.clicks.append((p.mouse.get_pos()[1] // squareSize, p.mouse.get_pos()[0] // squareSize))
        if len(main.clicks) == 2:
            if (gameState.board[main.clicks[0][0]][main.clicks[0][1]] != "--"):
                if (gameState.board[main.clicks[1][0]][main.clicks[1][1]] == "--"):
                    gameState.board[main.clicks[1][0]][main.clicks[1][1]] = gameState.board[main.clicks[0][0]][main.clicks[0][1]]
                    gameState.board[main.clicks[0][0]][main.clicks[0][1]] = "--"
            main.clicks = []

def loadImages():
    pieces = ["wh", "bl", "whk", "blk"]
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("images/" + piece + ".png"), (squareSize, squareSize))

def main():
    p.init()
    loadImages()
    clock = p.time.Clock()
    main.clicks = []
    board = Board((200, 200, 200), (100, 100, 100), p.display.set_mode((WIDTH, HEIGHT)))
    piece = Piece()
    running = True
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
            elif e.type == p.MOUSEBUTTONDOWN:

                piece.move()

        board.drawBoard()
        board.drawHighlight() 
        board.drawPieces() 
        p.display.flip()
        clock.tick(30)

if __name__ == "__main__":
    main()
