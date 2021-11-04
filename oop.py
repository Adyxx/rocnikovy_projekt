import pygame as p
import board

WIDTH = 512
HEIGHT = WIDTH
DIMENSIONS = 8
squareSize = WIDTH // DIMENSIONS
IMAGES = {}

def loadImages():
    pieces = ["wh", "bl", "whk", "blk"]
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("images/" + piece + ".png"), (squareSize, squareSize))

class Board:
    def __init__(self, color1, color2):
        self.color1 = color1
        self.color2 = color2

    def drawBoard(self):
        colors = [p.Color(self.color1), p.Color(self.color2)]
        screen = p.display.set_mode((WIDTH, HEIGHT))
        for r in range(DIMENSIONS):
            for c in range(DIMENSIONS):
                color = colors[((r + c) % 2)]
                p.draw.rect(screen, color, p.Rect(c * squareSize, r * squareSize, squareSize, squareSize))

    def drawPieces(self):
        screen = p.display.set_mode((WIDTH, HEIGHT))
        gameState = board.GameState()
        for r in range(DIMENSIONS):
            for c in range(DIMENSIONS):
                piece = gameState.board[r][c]
                if piece != "--":
                    screen.blit(IMAGES[piece], p.Rect(c * squareSize, r * squareSize, squareSize, squareSize))


class Pawn:
    def __init__(self, color):
        self.color = color

    def moves(self):
        pass

class King:
    def __init__(self, color):
        self.color = color

    def moves(self):
        pass


def main():
    p.init()
    loadImages()
    clock = p.time.Clock()
    running = True
    board = Board((100, 100, 100), (200, 200, 200))
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
            elif e.type == p.MOUSEBUTTONDOWN:
                pass

        board.drawBoard()
        p.display.flip()

        clock.tick(30)

if __name__ == "__main__":
    main()
