import pygame as p

import ai
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
        main.allPossibleJumps = []
        v, p, eK = 0, 0, 0
        pawn, king = False, False
        if len(main.clicks) == 2:
            dist1, dist2, dist3, dist4 = 0, 0, 0, 0
            oo1, oo2, oo3, oo4 = 0, 0, 0, 0
            orientation = -1 if gameState.board[main.clicks[0][0]][main.clicks[0][1]].startswith("b") else 1
            opPiece = "wh" if orientation != 1 else "bl"
            if(gameState.board[main.clicks[0][0]][main.clicks[0][1]] != "--" and gameState.board[main.clicks[1][0]][main.clicks[1][1]] == "--" and (orientation == 1 and main.whiteToMove == True or orientation == -1 and main.whiteToMove == False)):           
                for r in range(DIMENSIONS):
                    for c in range(DIMENSIONS):
                        if (not gameState.board[r][c].startswith(opPiece) and gameState.board[r][c] != "--" and not gameState.board[r][c].endswith("k") ):
                            main.allPossibleJumps.append(";")
                            main.allPossibleJumps.append((r, c))
                            if((c+2)<DIMENSIONS):                            
                                if(gameState.board[r-orientation][c+1].startswith(opPiece) and gameState.board[r-(orientation*2)][c+2] == "--"): # RIGHT
                                    main.allPossibleJumps.append((r-(orientation*2), c+2))
                                    v+=1
                                        
                            if((c-2)>=0):
                                if(gameState.board[r-orientation][c-1].startswith(opPiece) and gameState.board[r-(orientation*2)][c-2] == "--"): # LEFT
                                    main.allPossibleJumps.append((r-(orientation*2), c-2))
                                    v+=1
                                                    
                if(v==0 and not gameState.board[main.clicks[0][0]][main.clicks[0][1]].endswith("k")):
                    if (main.clicks[0][0] == main.clicks[1][0]+orientation and (main.clicks[0][1] == main.clicks[1][1]+1 or main.clicks[0][1] == main.clicks[1][1]-1)):
                        pawn = True
                elif(v==0 and gameState.board[main.clicks[0][0]][main.clicks[0][1]].endswith("k")):
                    pawn = True
                                                                
                if (main.clicks[0][0] == main.clicks[1][0]+(orientation*2)):
                    if(main.clicks[0][1] == main.clicks[1][1]+2):
                        if(gameState.board[main.clicks[0][0]-orientation][main.clicks[0][1]-1].startswith(opPiece)):
                            gameState.board[main.clicks[0][0]-orientation][main.clicks[0][1]-1] = "--"
                            main.validMove = True
                            Piece().extraMove(orientation, opPiece)

                    if(main.clicks[0][1] == main.clicks[1][1]-2):
                        if(gameState.board[main.clicks[0][0]-orientation][main.clicks[0][1]+1].startswith(opPiece)):
                            gameState.board[main.clicks[0][0]-orientation][main.clicks[0][1]+1] = "--"
                            main.validMove = True
                            Piece().extraMove(orientation, opPiece)
                
                for r in range(DIMENSIONS):
                    for c in range(DIMENSIONS):
                        if (not gameState.board[r][c].startswith(opPiece) and gameState.board[r][c] != "--" and gameState.board[r][c].endswith("k") ):
                            eK+=1
                            for n in range(DIMENSIONS): 
                                if(n>0):                      
                                    if(((r + n + 1) < (DIMENSIONS)) and ((c + n + 1) < (DIMENSIONS))):
                                        if(oo1 == 0 and ((not gameState.board[r + n][c + n].startswith(opPiece) and not gameState.board[r + n][c + n] == "--") or (not gameState.board[r + n][c + n] == "--" and not gameState.board[r + n + 1][c + n + 1] == "--"))):
                                            oo1 = n
                                        elif(oo1 == 0 and gameState.board[r + n][c + n].startswith(opPiece) and gameState.board[r + n + 1][c + n + 1] == "--"):
                                            p+=1      
                                            dist1 = n  
                                    if(((r - n - 1) >= 0) and ((c + n + 1) < (DIMENSIONS))):
                                        if(oo2 == 0 and ((not gameState.board[r - n][c + n].startswith(opPiece) and not gameState.board[r - n][c + n] == "--") or (not gameState.board[r - n][c + n] == "--" and not gameState.board[r - n - 1][c + n + 1] == "--"))):
                                            oo2 = n
                                        elif(oo2 == 0 and gameState.board[r - n][c + n].startswith(opPiece) and gameState.board[r - n - 1][c + n + 1] == "--"):
                                            p+=1
                                            dist2 = n                                                                                                                                                    
                                    if(((r + n + 1) < (DIMENSIONS)) and (c - n - 1 >= 0) ):
                                        if(oo3 == 0 and ((not gameState.board[r + n][c - n].startswith(opPiece) and not gameState.board[r + n][c - n] == "--") or (not gameState.board[r + n][c - n] == "--" and not gameState.board[r + n + 1][c - n - 1] == "--"))):
                                            oo3 = n                         
                                        elif(oo3 == 0 and gameState.board[r + n][c - n].startswith(opPiece) and gameState.board[r + n + 1][c - n - 1] == "--"):
                                            p+=1
                                            dist3 = n  
                                    if(((r - n - 1) >= 0) and ((c - n - 1) >= 0)):
                                        if(oo4 == 0 and ((not gameState.board[r - n][c - n].startswith(opPiece) and not gameState.board[r - n][c - n] == "--") or (not gameState.board[r - n][c - n] == "--" and not gameState.board[r - n - 1][c - n - 1] == "--"))):
                                            oo4 = n
                                        elif(oo4 == 0 and gameState.board[r - n][c - n].startswith(opPiece) and gameState.board[r - n - 1][c - n - 1] == "--"):
                                            p+=1
                                            dist4 = n                                                              
                if (p == 0):
                    for n in range(DIMENSIONS):
                        if ( (main.clicks[1][0] == main.clicks[0][0] - n) and (main.clicks[1][1] == main.clicks[0][1] - n) and (((main.clicks[1][0] > (main.clicks[0][0] - oo4) ) and (main.clicks[1][1] > (main.clicks[0][1] - oo4) )) or oo4 == 0)):
                            king = True
                        if ( (main.clicks[1][0] == main.clicks[0][0] - n) and (main.clicks[1][1] == main.clicks[0][1] + n) and (((main.clicks[1][0] > (main.clicks[0][0] - oo2) ) and (main.clicks[1][1] < (main.clicks[0][1] + oo2) )) or oo2 == 0)):
                            king = True
                        if ( (main.clicks[1][0] == main.clicks[0][0] + n) and (main.clicks[1][1] == main.clicks[0][1] + n) and (((main.clicks[1][0] < (main.clicks[0][0] + oo1) ) and (main.clicks[1][1] < (main.clicks[0][1] + oo1) )) or oo1 == 0)):
                            king = True
                        if ( (main.clicks[1][0] == main.clicks[0][0] + n) and (main.clicks[1][1] == main.clicks[0][1] - n) and (((main.clicks[1][0] < (main.clicks[0][0] + oo3) ) and (main.clicks[1][1] > (main.clicks[0][1] - oo3) )) or oo3 == 0)):
                            king = True
                else:
                    for n in range(DIMENSIONS):
                        if ((main.clicks[1][0] == main.clicks[0][0] - n) and (main.clicks[1][1] == main.clicks[0][1] - n) and dist4 > 0 and main.clicks[1][0] < (main.clicks[0][0] - dist4) and main.clicks[1][1] < (main.clicks[0][1] - dist4) and (((main.clicks[1][0] > (main.clicks[0][0] - oo4) ) and (main.clicks[1][1] > (main.clicks[0][1] - oo4) )) or oo4 == 0)):
                            for d in range(dist4+1):
                                if d>0:
                                    gameState.board[main.clicks[0][0] - d][main.clicks[0][1] - d] = "--"
                            main.validMove = True
                        if ((main.clicks[1][0] == main.clicks[0][0] - n) and (main.clicks[1][1] == main.clicks[0][1] + n) and dist2 > 0 and (main.clicks[1][0] < main.clicks[0][0] - dist2) and (main.clicks[1][1] > main.clicks[0][1] + dist2) and (((main.clicks[1][0] > (main.clicks[0][0] - oo2) ) and (main.clicks[1][1] < (main.clicks[0][1] + oo2) )) or oo2 == 0)):
                            for d in range(dist2+1):
                                if d>0:
                                    gameState.board[main.clicks[0][0] - d][main.clicks[0][1] + d] = "--"                        
                            main.validMove = True
                        if ((main.clicks[1][0] == main.clicks[0][0] + n) and (main.clicks[1][1] == main.clicks[0][1] + n) and dist1 > 0 and main.clicks[1][0] > (main.clicks[0][0] + dist1) and main.clicks[1][1] > (main.clicks[0][1] + dist1) and (((main.clicks[1][0] < (main.clicks[0][0] + oo1) ) and (main.clicks[1][1] < (main.clicks[0][1] + oo1) )) or oo1 == 0)):
                            for d in range(dist1+1):
                                if d>0:
                                    gameState.board[main.clicks[0][0] + d][main.clicks[0][1] + d] = "--"
                            main.validMove = True            
                        if ((main.clicks[1][0] == main.clicks[0][0] + n) and (main.clicks[1][1] == main.clicks[0][1] - n) and dist3 > 0 and main.clicks[1][0] > (main.clicks[0][0] + dist3) and main.clicks[1][1] < (main.clicks[0][1] - dist3) and (((main.clicks[1][0] < (main.clicks[0][0] + oo3) ) and (main.clicks[1][1] > (main.clicks[0][1] - oo3) )) or oo3 == 0)):
                            for d in range(dist3+1):
                                if d>0:
                                    gameState.board[main.clicks[0][0] + d][main.clicks[0][1] - d] = "--"
                            main.validMove = True

                king = True if (eK == 0 or king == True or (p==0 and pawn == True and not gameState.board[main.clicks[0][0]][main.clicks[0][1]].endswith("k"))) else False
                main.validMove = True if ( (king == True and pawn == True) or main.validMove == True) else False

    def extraMove(self, orientation, opPiece):
        if(not gameState.board[main.clicks[0][0]][main.clicks[0][1]].endswith("k")):
            x = 0
            while(x == 0):
                y = 0
                if((main.clicks[1][1] - 2 )>=0 and (main.clicks[1][1] + 2)<DIMENSIONS and main.clicks[1][0] - orientation*2 >= 0 and main.clicks[1][0] - orientation*2 < DIMENSIONS): # BOTH
                    print(main.clicks[1][1] - 2 , main.clicks[1][1] + 2)
                    if((gameState.board[main.clicks[1][0] - orientation ][main.clicks[1][1] + 1].startswith(opPiece) and gameState.board[main.clicks[1][0] - orientation*2 ][main.clicks[1][1] + 2] == "--") and (gameState.board[main.clicks[1][0] - orientation ][main.clicks[1][1] - 1].startswith(opPiece) and gameState.board[main.clicks[1][0] - orientation*2 ][main.clicks[1][1] - 2] == "--")):             
                        main.whiteToMove = False if main.whiteToMove != False else True
                        main.exPiece.append(main.clicks[1]) 
                        break
                if(y == 0 and (main.clicks[1][1] + 2)<DIMENSIONS and main.clicks[1][0] - orientation*2 >= 0 and main.clicks[1][0] - orientation*2 < DIMENSIONS): # RIGHT
                    if(gameState.board[main.clicks[1][0] - orientation][main.clicks[1][1] + 1].startswith(opPiece) and gameState.board[main.clicks[1][0] - orientation*2 ][main.clicks[1][1] + 2] == "--"):
                        y = 1
                        gameState.board[main.clicks[1][0] - orientation][main.clicks[1][1] + 1] = "--"
                        main.clicks[1] = (main.clicks[1][0] - orientation*2, main.clicks[1][1] + 2)
                if(y == 0 and (main.clicks[1][1] - 2 )>=0 and main.clicks[1][0] - orientation*2 >= 0 and main.clicks[1][0] - orientation*2 < DIMENSIONS): # LEFT
                    if(gameState.board[main.clicks[1][0] - orientation ][main.clicks[1][1] - 1].startswith(opPiece) and gameState.board[main.clicks[1][0] - orientation*2 ][main.clicks[1][1] - 2] == "--"):
                        y = 1
                        gameState.board[main.clicks[1][0] - orientation][main.clicks[1][1] - 1] = "--"
                        main.clicks[1] = (main.clicks[1][0] - orientation*2, main.clicks[1][1] - 2)
                if (y == 0): # NONE
                    break
            
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

def allPossibleMoves(gameState):
    possibleMoves = []
    main.possibleMovesW = []
    q=0
    howManyHungary = 0
    howManyHungaryW = 0
    for r in range(DIMENSIONS):
        for c in range(DIMENSIONS):
            if gameState.board[r][c] == "bl":

                if (((((r+2 < DIMENSIONS) and (c + 2 < DIMENSIONS)) and ((gameState.board[r + 1][c + 1] == "wh") or (gameState.board[r + 1][c + 1] == "whk")) and(gameState.board[r + 2][c + 2] == "--")))      or (((r+2 < DIMENSIONS) and (c - 2 >= 0) and (((gameState.board[r + 1][c - 1] == "wh") or (gameState.board[r + 1][c - 1] == "whk")) and(gameState.board[r + 2][c - 2] == "--"))and(gameState.board[r + 2][c - 2] == "--")))):
                    if (howManyHungary ==0):
                        possibleMoves = []
                    howManyHungary += 1
                    possibleMoves.append(";")
                    possibleMoves.append((r, c))

                    if ((c-2<DIMENSIONS) and (r+2<DIMENSIONS)and(gameState.board[r + 1][c - 1] == "wh") or (gameState.board[r + 1][c - 1] == "whk") and (c - 1 >= 0) and(gameState.board[r + 2][c - 2] == "--")):
                        possibleMoves.append((r + 2, c - 2))
                    if ((c+2<DIMENSIONS) and (r+2<DIMENSIONS)and((gameState.board[r + 1][c + 1] == "wh") or (gameState.board[r + 1][c + 1] == "whk"))and (c + 1 >= 0)and(gameState.board[r + 2][c + 2] == "--")):
                        possibleMoves.append((r + 2, c + 2))
                    print("a")
                    print(possibleMoves)
                if (howManyHungary ==0 and (((c + 1 < DIMENSIONS) and (gameState.board[r + 1][c + 1] == "--")) or ((gameState.board[r + 1][c - 1] == "--") and (c - 1 >= 0)))):
                    possibleMoves.append(";")
                    possibleMoves.append((r, c))

                if (howManyHungary ==0 and ((c + 1 < DIMENSIONS) and (gameState.board[r + 1][c + 1] == "--"))):

                    possibleMoves.append((r + 1, c + 1))

                if (howManyHungary ==0 and ((gameState.board[r + 1][c - 1] == "--") and (c - 1 >= 0))):
                    possibleMoves.append((r + 1, c - 1))


            if gameState.board[r][c] == "blk":
                if (((r + 2 < DIMENSIONS) and (c + 2 < DIMENSIONS)) and (
                        (((gameState.board[r + 1][c + 1] == "wh") or (gameState.board[r + 1][c + 1] == "whk"))) and (
                        gameState.board[r + 2][c + 2] == "--")) or (((r + 2 < DIMENSIONS) and (c - 2 > 0) and (
                        ((gameState.board[r + 1][c - 1] == "wh") or (gameState.board[r + 1][c - 1] == "whk")) and (
                        gameState.board[r + 2][c - 2] == "--") and (gameState.board[r + 2][c - 2] == "--"))))):
                    if (howManyHungary == 0):
                        possibleMoves = []
                    howManyHungary += 1
                    possibleMoves.append(";")
                    possibleMoves.append((r, c))

                    if ((c - 2 < DIMENSIONS) and (r + 2 < DIMENSIONS) and (gameState.board[r + 1][c - 1] == "wh") or (
                            gameState.board[r + 1][c - 1] == "whk") and (c - 1 >= 0) and (
                            gameState.board[r + 2][c - 2] == "--")):
                        possibleMoves.append((r + 2, c - 2))
                    if ((c + 2 < DIMENSIONS) and (r + 2 < DIMENSIONS) and (
                            (gameState.board[r + 1][c + 1] == "wh") or (gameState.board[r + 1][c + 1] == "whk")) and (
                            c + 1 >= 0) and (gameState.board[r + 2][c + 2] == "--")):
                        possibleMoves.append((r + 2, c + 2))
                    print("a")
                    print(possibleMoves)

                possibleMoves.append(";")
                possibleMoves.append((r, c))
                for f in range(DIMENSIONS):
                    try:
                        if (howManyHungary == 0 and ((c + f < DIMENSIONS) and (r+f < DIMENSIONS) and (gameState.board[r + f][c + f] == "--"))):
                            possibleMoves.append((r + f, c + f))

                        for p in range (f):
                            print(p)
                            if (((gameState.board[r + f-p][c + f-p] == "wh")or(gameState.board[r + f-p][c + f-p] == "whk")) and gameState.board[r + f-p+1][c + f-p+1] == "--"):

                                if (howManyHungary == 0):
                                    possibleMoves = []
                                    possibleMoves.append(";")
                                    possibleMoves.append((r, c))
                                howManyHungary+=1


                                possibleMoves.append((r + f-p+1, c + f-p+1))
                    except:
                        print("out of range")
                    try:
                        if (howManyHungary == 0 and ((gameState.board[r + f][c - f] == "--") and (c - f >= 0))):
                            possibleMoves.append((r + f, c - f))

                        for p in range (f):
                            print(p)
                            if (((gameState.board[r + f-p][c - f+p] == "wh")or(gameState.board[r + f-p][c - f-p] == "whk")) and gameState.board[r + f+p+1][c - f-p-1] == "--"):

                                if (howManyHungary == 0):
                                    possibleMoves = []
                                    possibleMoves.append(";")
                                    possibleMoves.append((r, c))
                                howManyHungary+=1


                                possibleMoves.append((r + f-p+1, c - f-p-1))
                    except:
                        print("out of range")
                    try:
                        if (howManyHungary == 0 and (
                                (c + f < DIMENSIONS)and (r-f >= 0) and (gameState.board[r - f][c + f] == "--"))):
                            possibleMoves.append((r - f, c + f))

                        for p in range (f):
                            print(p)
                            if (((gameState.board[r - f+p][c + f-p] == "wh")or(gameState.board[r - f+p][c + f-p] == "whk")) and gameState.board[r - f+p-1][c + f-p+1] == "--"):

                                if (howManyHungary == 0):
                                    possibleMoves = []
                                    possibleMoves.append(";")
                                    possibleMoves.append((r, c))
                                howManyHungary+=1


                                possibleMoves.append((r - f-p-1, c + f-p+1))
                    except:
                        print("out of range")
                    try:
                        if (howManyHungary == 0 and ((gameState.board[r - f][c - f] == "--")and (r-f >= 0) and (c - f >= 0))):
                            possibleMoves.append((r - f, c - f))

                        for p in range (f):
                            print(p)
                            if (r - f+p>=0 and c - f+p >=0(((gameState.board[r - f+p][c - f+p] == "wh")or(gameState.board[r - f+p][c - f+p] == "whk")) and gameState.board[r - f+p-1][c - f+p-1] == "--")):

                                if (howManyHungary == 0):
                                    possibleMoves = []
                                    possibleMoves.append(";")
                                    possibleMoves.append((r, c))
                                howManyHungary+=1


                                possibleMoves.append((r - f+p-1, c - f+p-1))
                    except:
                        print("out of range")

            if gameState.board[r][c] == "wh":

                if (((r-2 < DIMENSIONS) and (c + 2 < DIMENSIONS)) and ((((gameState.board[r - 1][c + 1] == "bl") or (gameState.board[r - 1][c + 1] == "blk") ) ) and(gameState.board[r - 2][c + 2] == "--"))      or (((r-2 < DIMENSIONS) and (c - 2 > 0) and (((gameState.board[r - 1][c - 1] == "bl") or (gameState.board[r - 1][c - 1] == "blk")) and(gameState.board[r - 2][c - 2] == "--")and(gameState.board[r - 2][c - 2] == "--"))))):
                    if (howManyHungaryW ==0):
                        possibleMovesW = []
                    howManyHungaryW += 1
                    main.possibleMovesW.append(";")
                    main.possibleMovesW.append((r, c))

                    if ((c-2<DIMENSIONS) and (r-2<DIMENSIONS)and(gameState.board[r - 1][c - 1] == "bl") or (gameState.board[r - 1][c - 1] == "blk") and (c - 1 >= 0) and(gameState.board[r - 2][c - 2] == "--")):
                        main.possibleMovesW.append((r - 2, c - 2))
                    if ((c+2<DIMENSIONS) and (r+2<DIMENSIONS)and((gameState.board[r - 1][c + 1] == "bl") or (gameState.board[r - 1][c + 1] == "blk"))and (c + 1 >= 0)and(gameState.board[r - 2][c + 2] == "--")):
                        main.possibleMovesW.append((r - 2, c + 2))
                    print("a")
                    print(main.possibleMovesW)
                if (howManyHungaryW ==0 and (((c + 1 < DIMENSIONS) and (gameState.board[r - 1][c + 1] == "--")) or ((gameState.board[r - 1][c - 1] == "--") and (c - 1 >= 0)))):
                    main.possibleMovesW.append(";")
                    main.possibleMovesW.append((r, c))

                if (howManyHungaryW ==0 and ((c + 1 < DIMENSIONS) and (gameState.board[r - 1][c + 1] == "--"))):

                    main.possibleMovesW.append((r - 1, c + 1))

                if (howManyHungaryW ==0 and ((gameState.board[r - 1][c - 1] == "--") and (c - 1 >= 0))):
                    main.possibleMovesW.append((r - 1, c - 1))

    possibleMoves.append(0)
    main.possibleMovesW.append(0)
    print("black")
    print(possibleMoves)
    print("white")
    print(main.possibleMovesW)
    return possibleMoves

def main():
    p.init()
    loadImages()
    clock = p.time.Clock()
    main.whiteToMove = True
    main.validMove = False
    main.exPiece = []
    main.clicks = []
    main.allPossibleJumps = []
    main.possibleMovesW = []
    board = Board((200, 200, 200), (100, 100, 100), p.display.set_mode((WIDTH, HEIGHT)))
    piece = Piece()
    running = True
    while running:
        if (main.whiteToMove == False):

            piece.getValidMoves()
            print(main.allPossibleJumps)
            main.clicks = ai.eidam(gameState)
            piece.getValidMoves()
            piece.move()
            main.whiteToMove = True
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
            elif e.type == p.MOUSEBUTTONDOWN:             
                piece.getPosition()
                piece.getValidMoves()             
                piece.move()
                print(main.allPossibleJumps)
        board.drawBoard()
        board.drawHighlight()
        board.drawPieces() 
        p.display.flip()
        clock.tick(30)

if __name__ == "__main__":
    main()
