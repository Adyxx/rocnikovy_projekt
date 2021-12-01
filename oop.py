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
            orientation = -1 if gameState.board[main.clicks[0][0]][main.clicks[0][1]].startswith("b") else 1
            if (gameState.board[main.clicks[0][0]][main.clicks[0][1]] != "--" and (orientation == 1 and main.whiteToMove == True or orientation == -1 and main.whiteToMove == False)):
                s = p.Surface((WIDTH / DIMENSIONS, WIDTH / DIMENSIONS))
                s.set_alpha(200)  # set opacity
                s.fill(p.Color('deepskyblue3'))  # set color
                self.screen.blit(s, (main.clicks[-1][1] * (WIDTH / DIMENSIONS), (main.clicks[-1][0] * WIDTH / DIMENSIONS)))

class Piece:
    def __init__(self):
        pass

    def getPosition(self):
        main.clicks = [] if (gameState.board[p.mouse.get_pos()[1] // squareSize][p.mouse.get_pos()[0] // squareSize] != "--") else main.clicks
        main.clicks.append((p.mouse.get_pos()[1] // squareSize, p.mouse.get_pos()[0] // squareSize))

    def getValidMoves(self):
        v=0
        p=0
        eK=0
        pawn=False
        king=False
        if len(main.clicks) == 2:
            orientation = -1 if gameState.board[main.clicks[0][0]][main.clicks[0][1]].startswith("b") else 1
            opPiece = "wh" if orientation != 1 else "bl"

            if(gameState.board[main.clicks[0][0]][main.clicks[0][1]] != "--" and gameState.board[main.clicks[1][0]][main.clicks[1][1]] == "--" and (orientation == 1 and main.whiteToMove == True or orientation == -1 and main.whiteToMove == False)):
                if (main.clicks[0][0] == main.clicks[1][0]+orientation and (main.clicks[0][1] == main.clicks[1][1]+1 or main.clicks[0][1] == main.clicks[1][1]-1)):
                    for r in range(DIMENSIONS):
                        for c in range(DIMENSIONS):
                            if (not gameState.board[r][c].startswith(opPiece) and gameState.board[r][c] != "--" and not gameState.board[r][c].endswith("k") ):
                                if((c+2)<DIMENSIONS):
                                    if(gameState.board[r-orientation][c+1].startswith(opPiece) and gameState.board[r-(orientation*2)][c+2] == "--"): # RIGHT
                                        v+=1
                                        
                                if((c-2)>=0):
                                    if(gameState.board[r-orientation][c-1].startswith(opPiece) and gameState.board[r-(orientation*2)][c-2] == "--"): # LEFT
                                        v+=1
                    if(v==0):
                        pawn = True
                                                                
                if (main.clicks[0][0] == main.clicks[1][0]+(orientation*2)):
                    if(main.clicks[0][1] == main.clicks[1][1]+2):
                        if(gameState.board[main.clicks[0][0]-orientation][main.clicks[0][1]-1].startswith(opPiece)):
                            gameState.board[main.clicks[0][0]-orientation][main.clicks[0][1]-1] = "--"
                            pawn= True
                    if(main.clicks[0][1] == main.clicks[1][1]-2):
                        if(gameState.board[main.clicks[0][0]-orientation][main.clicks[0][1]+1].startswith(opPiece)):
                            gameState.board[main.clicks[0][0]-orientation][main.clicks[0][1]+1] = "--"
                            pawn = True

                for r in range(DIMENSIONS):
                    for c in range(DIMENSIONS):
                        if (not gameState.board[r][c].startswith(opPiece) and gameState.board[r][c] != "--" and gameState.board[r][c].endswith("k") ):
                            eK+=1
                            for n in range(DIMENSIONS): 
                                if(n>0):                      
                                    if(((r + n + 1) < (DIMENSIONS)) and ((c + n + 1) < (DIMENSIONS))):                      
                                        if(gameState.board[r + n][c + n].startswith(opPiece) and gameState.board[r + n + 1][c + n + 1] == "--"):
                                            p+=1      
                                                    
                                    if(((r - n - 1) >= 0) and ((c + n + 1) < (DIMENSIONS))):
                                        if(gameState.board[r - n][c + n].startswith(opPiece) and gameState.board[r - n - 1][c + n + 1] == "--"):
                                            p+=1                                 
                                                                                    
                                    if(((r + n + 1) < (DIMENSIONS)) and (c - n - 1 >= 0) ):
                                        if(gameState.board[r + n][c - n].startswith(opPiece) and gameState.board[r + n + 1][c - n - 1] == "--"):
                                            p+=1

                                    if(((r - n - 1) >= 0) and ((c - n - 1) >= 0)):
                                        if(gameState.board[r - n][c - n].startswith(opPiece) and gameState.board[r - n - 1][c - n - 1] == "--"):
                                            p+=1
                                                            
                if (p == 0):
                    for n in range(DIMENSIONS):
                        if ((main.clicks[0][0] == main.clicks[1][0] + n) or (main.clicks[0][0] == main.clicks[1][0] - n)) and ((main.clicks[0][1] == main.clicks[1][1] + n) or (main.clicks[0][1] == main.clicks[1][1] - n)):                                       
                            king = True
                elif ():
                    pass
                    # king must eat

                king = True if (eK == 0 or king == True) else False
                main.validMove = True if (king == True and pawn == True) else False

    def move(self):
        if len(main.clicks) == 2:
            if (main.validMove):
                gameState.board[main.clicks[1][0]][main.clicks[1][1]] = gameState.board[main.clicks[0][0]][main.clicks[0][1]]
                gameState.board[main.clicks[0][0]][main.clicks[0][1]] = "--"
                # check for promotion
                if ((main.clicks[1][0] == 0) and (gameState.board[main.clicks[1][0]][main.clicks[1][1]] == "wh") or (main.clicks[1][0] == DIMENSIONS - 1) and (gameState.board[main.clicks[1][0]][main.clicks[1][1]] == "bl")):  # promotion
                    gameState.board[main.clicks[1][0]][main.clicks[1][1]] = str(gameState.board[main.clicks[1][0]][main.clicks[1][1]]) + "k"
                # ------------------
                main.validMove = False
                main.whiteToMove = False if main.whiteToMove != False else True
            main.clicks = []

def loadImages():
    pieces = ["wh", "bl", "whk", "blk"]
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("images/" + piece + ".png"), (squareSize, squareSize))

def main():
    p.init()
    loadImages()
    clock = p.time.Clock()
    main.whiteToMove = True
    main.validMove = False
    main.clicks = []
    board = Board((200, 200, 200), (100, 100, 100), p.display.set_mode((WIDTH, HEIGHT)))
    piece = Piece()
    running = True
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
            elif e.type == p.MOUSEBUTTONDOWN:
                piece.getPosition()
                piece.getValidMoves()
                piece.move()

        board.drawBoard()
        board.drawHighlight()
        board.drawPieces() 
        p.display.flip()
        clock.tick(30)

if __name__ == "__main__":
    main()
