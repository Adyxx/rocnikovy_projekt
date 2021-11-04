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
        IMAGES[piece] = p.transform.scale(p.image.load("images/" + piece + ".png"), (squareSize, squareSize))


'''
    main
'''


def main():

    p.init()
    screen = p.display.set_mode((WIDTH, HEIGHT))
    screen.fill(p.Color("white"))
    clock = p.time.Clock()
    main.move = 1
    main.exTurn = 0
    main.exTurnPiece = []
    main.canBeTaken = []
    gameState = board.GameState()
    loadImages()
    running = True
    selectedSquare = ()  # memory
    clicks = []
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
            elif e.type == p.MOUSEBUTTONDOWN:
                location = p.mouse.get_pos()
                col = location[0] // squareSize  # location 2. click
                row = location[1] // squareSize  # location 2. click

                if (gameState.board[row][
                    col] != "--"):  # if there is piece on the location of the player's second click...
                    clicks = []  # then remove click memory
                # this fixes problem where player clicks a piece and then other piece that wouldn't move

                if selectedSquare == (row, col):  # reset when clicked same position
                    selectedSquare = ()
                    clicks = []
                else:
                    clicks.append(selectedSquare)
                    if len(clicks) == 2:
                        pos1 = selectedSquare[0]  # location 1. click
                        pos2 = selectedSquare[1]  # location 1. click
                        if (gameState.board[pos1][pos2] != "--"):  # does 1. position have piece?
                            if (gameState.board[row][col] == "--"):  # is 2. position empty?
                                piece = gameState.board[pos1][pos2]

                                if (hungaryPawns(gameState, pos1, pos2, row, col) == True):
                                    movePiece(gameState, piece, pos1, pos2, row, col)
                                elif(gameState.board[pos1][pos2].endswith("k") and hungaryPawns(gameState, pos1, pos2, row, col)):
                                    movePiece(gameState, piece, pos1, pos2, row, col)
                                isItFinallyOver(gameState)

                        clicks = []
                selectedSquare = (row, col)

        drawGameState(screen, gameState, selectedSquare)
        clock.tick(30)
        p.display.flip()

def hungaryKings(gameState, pos1, pos2, row, col,r,c, piece):

    for plus in range(DIMENSIONS):
        plus= plus+1
        if (r - plus >= 0):
            try:
                if ((gameState.board[r - plus][c + plus] != "--" and
                     gameState.board[r - plus - 1][c + plus + 1] != "--")):
                    return True

                elif ((gameState.board[r + plus][c + plus] != "--" and
                       gameState.board[r + plus + 1][c + plus + 1] != "--")):
                    return True
                elif ((gameState.board[r - plus][c - plus] != "--" and
                       gameState.board[r - plus - 1][c - plus - 1] != "--")):
                    return True
                elif ((gameState.board[r + plus][c + plus] != "--" and
                       gameState.board[r + plus + 1][c + plus + 1] != "--")):
                    return True

                if (row > pos1 and col > pos2):
                    if ((gameState.board[r + plus][c + plus] != "--" and
                         gameState.board[r + plus + 1][c + plus + 1] == "--") and not
                    gameState.board[r + plus][c + plus].startswith(piece) and (
                            main.move == 1 and piece.startswith("wh") or (
                            main.move == 0 and piece.startswith(
                        "bl")))):
                        print("KA: Mmm... yummy" + str(r + plus) + "," + str(c + plus))
                        main.canBeTaken.append(r + plus)
                        main.canBeTaken.append(c + plus)
                        return True
                if (row > pos1 and col < pos2):
                    if ((gameState.board[r + plus][c - plus] != "--" and
                         gameState.board[r + plus + 1][c - plus - 1] == "--") and not
                    gameState.board[r + plus][c - plus].startswith(piece) and (
                            main.move == 1 and piece.startswith("wh") or (
                            main.move == 0 and piece.startswith(
                        "bl")))):
                        print("KAA: Mmm... yummy" + str(r + plus) + "," + str(c - plus))
                        main.canBeTaken.append(r + plus)
                        main.canBeTaken.append(c - plus)
                        return True

                if (row < pos1 and col > pos2):
                    if ((gameState.board[r - plus][c + plus] != "--" and
                         gameState.board[r - plus - 1][c + plus + 1] == "--") and not
                    gameState.board[r - plus][c + plus].startswith(piece) and (
                            main.move == 1 and piece.startswith("wh") or (
                            main.move == 0 and piece.startswith(
                        "bl")))):
                        print("KAAAA: Mmm... yummy" + str(r - plus) + "," + str(c + plus))
                        main.canBeTaken.append(r - plus)
                        main.canBeTaken.append(c + plus)
                        return True

                if (row < pos1 and col < pos2):
                    if ((gameState.board[r - plus][c - plus] != "--" and
                         gameState.board[r - plus - 1][c - plus - 1] == "--") and not
                    gameState.board[r - plus][c - plus].startswith(piece) and (
                            main.move == 1 and piece.startswith("wh") or (
                            main.move == 0 and piece.startswith(
                        "bl")))):
                        print("KAAAAA: Mmm... yummy" + str(r - plus) + "," + str(c - plus))
                        main.canBeTaken.append(r - plus)
                        main.canBeTaken.append(c - plus)
                        return True


            except:
                print("out of range")

    return False


def hungaryPawns(gameState, pos1, pos2, row, col):

    if(main.exTurn == 1):
        try:
            piece = gameState.board[main.exTurnPiece[0]][main.exTurnPiece[1]]
            direction1 = -1 if piece == "wh" else 1

            if ((gameState.board[main.exTurnPiece[0] + direction1][main.exTurnPiece[1] + 1] != "--" and
                 gameState.board[main.exTurnPiece[0] + (direction1 * 2)][main.exTurnPiece[1] + 2] == "--") and not
            gameState.board[main.exTurnPiece[0] + direction1][main.exTurnPiece[1] + 1].startswith(piece) and (
                    main.move == 1 and piece.startswith("wh") or (main.move == 0 and piece.startswith(
                "bl")))):
                print("test")

                return True
        except:
            print("ex")
        try:
            if ((gameState.board[main.exTurnPiece[0] + direction1][main.exTurnPiece[1] - 1] != "--" and
                   gameState.board[main.exTurnPiece[0] + (direction1 * 2)][main.exTurnPiece[1] - 2] == "--") and not
                  gameState.board[main.exTurnPiece[0] + direction1][main.exTurnPiece[1] - 1].startswith(piece) and (
                          main.move == 1 and piece.startswith("wh") or (main.move == 0 and piece.startswith(
                      "bl")))):
                print("Test")
                return True
            else:
                main.exTurn = 0
                return False
        except:
            print("ex")
            main.exTurn = 0
            return False


    else:
        main.canBeTaken = []

        for r in range(DIMENSIONS):
            for c in range(DIMENSIONS):
                r=7
                if gameState.board[r][c] != "--":
                    piece = gameState.board[r][c]
                    direction1 = -1 if piece == "wh" else 1
                    if (not piece.endswith("k")):
                        try:
                            # and ((r+(direction1*2))>=0 and (r+(direction1*2))<DIMENSIONS and (c-2)>=0 and (c-2)<DIMENSIONS)
                            if ((gameState.board[r + direction1][c + 1] != "--" and
                                 gameState.board[r + (direction1 * 2)][c + 2] == "--") and not
                            gameState.board[r + direction1][c + 1].startswith(piece) and (
                                    main.move == 1 and piece.startswith("wh") or (main.move == 0 and piece.startswith(
                                    "bl")))):
                                print("A: Mmm... yummy" + str(r + direction1) + "," + str(c + 1))
                                main.canBeTaken.append(r + direction1)
                                main.canBeTaken.append(c + 1)
                                if ((pos1 + 2 == row and pos2 + 2 == col) or (pos1 + 2 == row and pos2 - 2 == col) or (
                                        pos1 - 2 == row and pos2 + 2 == col) or (pos1 - 2 == row and pos2 - 2 == col)):

                                    return True
                                else:
                                    return False
                            elif ((gameState.board[r + direction1][c - 1] != "--" and
                                 gameState.board[r + (direction1 * 2)][c - 2] == "--") and not
                            gameState.board[r + direction1][c - 1].startswith(piece) and (
                                    main.move == 1 and piece.startswith("wh") or (main.move == 0 and piece.startswith(
                                    "bl"))) ):
                                print("B: Mmm... yummy" + str(r + direction1) + "," + str(c - 1))
                                main.canBeTaken.append(r + direction1)
                                main.canBeTaken.append(c - 1)
                                if ((pos1 + 2 == row and pos2 + 2 == col) or (pos1 + 2 == row and pos2 - 2 == col) or (
                                        pos1 - 2 == row and pos2 + 2 == col) or (pos1 - 2 == row and pos2 - 2 == col)):

                                    return True
                                else:
                                    return False
                        except:
                            print("out of range")
                    else:

                        if (hungaryKings(gameState, pos1, pos2, row, col, r, c, piece)):
                            if(gameState.board[pos1][pos2].endswith("k")):
                                return True
                            else:
                                return False

                        else:
                            if (gameState.board[pos1][pos2].endswith("k")):
                                return False
                            else:
                                return True
        return True



def isItFinallyOver(gameState):
    white = False
    black = False
    for r in range(DIMENSIONS):
        for c in range(DIMENSIONS):
            if (gameState.board[r][c].startswith("wh")):
                white = True
            elif (gameState.board[r][c].startswith("bl")):
                black = True

    if (white == False):
        print("Black Wins!!!")
    elif (black == False):
        print("White Wins!!!")


def changeColor(screen, gameState, selectedSquare):
    if selectedSquare != ():  # if square is clicked.... (if square is not empty)
        r, c = selectedSquare

        if (gameState.board[r][c] != "--"):  # if selected square has a piece....
            if ((main.move == 1 and gameState.board[r][c] != "bl" and gameState.board[r][c] != "blk") or (
                    main.move == 0 and gameState.board[r][c] != "wh" and gameState.board[r][
                c] != "whk")):  # highlight only black pieces if it's Black's turn or only white pieces if it's White's turn
                s = p.Surface((WIDTH / DIMENSIONS, WIDTH / DIMENSIONS))
                s.set_alpha(170)  # set opacity
                s.fill(p.Color('red'))  # set color
                screen.blit(s, (c * (WIDTH / DIMENSIONS), (r * WIDTH / DIMENSIONS)))


def movePiece(gameState, piece, pos1, pos2, row, col):
    direction1 = 1 if piece == "wh" else -1

    print(main.exTurnPiece)
    if (main.exTurnPiece != [] and (pos1 != main.exTurnPiece[0] or pos2 != main.exTurnPiece[1])):
        print("wrong piece")




    elif (main.move == 1 and piece == "wh" and ((pos1 == row + 2) and (pos2 == col - 2)) and (
            gameState.board[row + 1][col - 1] != "--") and (not gameState.board[row + 1][col - 1].startswith("wh")) or (
                  main.move == 0 and piece == "bl" and ((pos1 == row - 2) and (pos2 == col - 2)) and (
                  gameState.board[row - 1][col - 1] != "--") and (
                  not gameState.board[row - 1][col - 1].startswith("bl")))):
        gameState.board[row][col] = piece  # create new piece
        gameState.board[row + direction1][col - 1] = "--"
        gameState.board[pos1][pos2] = "--"  # remove piece
        main.exTurnPiece.append(row)
        main.exTurnPiece.append(col)
        main.exTurn = 1


        if (hungaryPawns(gameState, pos1, pos2, row, col) == False):
            if (main.exTurn ==0):
                main.exTurnPiece = []
                main.move = 1 if main.move != 1 else 0

    elif (main.move == 1 and piece == "wh" and ((pos1 == row + 2) and (pos2 == col + 2)) and (
            gameState.board[row + 1][col + 1] != "--") and (not gameState.board[row + 1][col + 1].startswith("wh")) or (
                  main.move == 0 and piece == "bl" and ((pos1 == row - 2) and (pos2 == col + 2)) and (
                  gameState.board[row - 1][col + 1] != "--") and (
                  not gameState.board[row - 1][col + 1].startswith("bl")))):
        gameState.board[row][col] = piece  # create new white piece
        gameState.board[row + direction1][col + 1] = "--"
        gameState.board[pos1][pos2] = "--"  # remove piece

        main.exTurn = 1
        main.exTurnPiece.append(row)
        main.exTurnPiece.append(col)

        if (hungaryPawns(gameState, pos1, pos2, row, col) == False):
            if (main.exTurn == 0):
                main.exTurnPiece = []
                main.move = 1 if main.move != 1 else 0

    elif (main.exTurn == 0 and (main.move == 1 and piece == "wh" and (pos1 == row + 1) and ((pos2 == col + 1) or (pos2 == col - 1)) or (
            main.move == 0 and piece == "bl" and (pos1 == row - 1) and ((pos2 == col + 1) or (pos2 == col - 1))) )):

        gameState.board[row][col] = piece  # create new white piece
        gameState.board[pos1][pos2] = "--"  # remove piece
        main.move = 1 if main.move != 1 else 0

    elif (piece.endswith("k")):

        if (row < pos1):
            direction1 = 1  # UP
        else:
            direction1 = -1  # DOWN
        if (col < pos2):
            direction2 = 1  # LEFT
        else:
            direction2 = -1  # RIGHT

        jump = 0
        for n in range(DIMENSIONS):
            if ((((pos1 == row + n) or (pos1 == row - n)) and ((pos2 == col + n) or (pos2 == col - n))) and (
                    (piece == "blk" and main.move == 0) or (piece == "whk" and main.move == 1))):
                if ((direction1 == 1 and direction2 == 1)):
                    for i in range(pos1 - row):
                        i = i + 1
                        if ((gameState.board[pos1 - i][pos2 - i] != "--")):
                            print("přeskok")
                            skip1 = pos1 - i
                            skip2 = pos2 - i
                            jump = jump + 1

                    if (jump == 1):
                        gameState.board[row][col] = piece  # create new white piece
                        gameState.board[skip1][skip2] = "--"
                        gameState.board[pos1][pos2] = "--"  # remove piece
                        main.move = 1 if main.move != 1 else 0

                if ((direction1 == -1 and direction2 == 1)):
                    for i in range(row - pos1):
                        i = i + 1
                        if ((gameState.board[pos1 + i][pos2 - i] != "--")):
                            print("přeskok")
                            skip1 = pos1 + i
                            skip2 = pos2 - i
                            jump = jump + 1

                    if (jump == 1):
                        gameState.board[row][col] = piece  # create new white piece
                        gameState.board[skip1][skip2] = "--"
                        gameState.board[pos1][pos2] = "--"  # remove piece
                        main.move = 1 if main.move != 1 else 0

                if ((direction1 == 1 and direction2 == -1)):
                    for i in range(pos1 - row):
                        i = i + 1
                        if ((gameState.board[pos1 - i][pos2 + i] != "--")):
                            print("přeskok")
                            skip1 = pos1 - i
                            skip2 = pos2 + i
                            jump = jump + 1

                    if (jump == 1):
                        gameState.board[row][col] = piece  # create new white piece
                        gameState.board[skip1][skip2] = "--"
                        gameState.board[pos1][pos2] = "--"  # remove piece
                        main.move = 1 if main.move != 1 else 0

                if ((direction1 == -1 and direction2 == -1)):
                    for i in range(row - pos1):
                        i = i + 1
                        if ((gameState.board[pos1 + i][pos2 + i] != "--")):
                            print("přeskok")
                            skip1 = pos1 + i
                            skip2 = pos2 + i
                            jump = jump + 1

                    if (jump == 1):
                        gameState.board[row][col] = piece  # create new white piece
                        gameState.board[skip1][skip2] = "--"
                        gameState.board[pos1][pos2] = "--"  # remove piece
                        main.move = 1 if main.move != 1 else 0

                elif (jump == 0 and  hungaryPawns(gameState, pos1, pos2, row, col) == False):
                    gameState.board[row][col] = piece  # create new white piece
                    gameState.board[pos1][pos2] = "--"  # remove piece
                    main.move = 1 if main.move != 1 else 0

    if ((row == 0) and (gameState.board[row][col] == "wh") or (row == DIMENSIONS - 1) and (
            gameState.board[row][col] == "bl")):  # promotion
        gameState.board[row][col] = str(piece) + "k"

    print(main.canBeTaken)
    print(main.exTurnPiece)
    print(main.exTurn)
def drawBoard(screen):
    colors = [p.Color(235, 235, 208), p.Color(120, 188, 227)]
    for r in range(DIMENSIONS):
        for c in range(DIMENSIONS):
            color = colors[((r + c) % 2)]
            p.draw.rect(screen, color, p.Rect(c * squareSize, r * squareSize, squareSize, squareSize))


def drawPieces(screen, board):
    for r in range(DIMENSIONS):
        for c in range(DIMENSIONS):
            piece = board[r][c]
            if piece != "--":
                screen.blit(IMAGES[piece], p.Rect(c * squareSize, r * squareSize, squareSize, squareSize))


def drawGameState(screen, gameState, selectedSquare):
    drawBoard(screen)
    changeColor(screen, gameState, selectedSquare)
    drawPieces(screen, gameState.board)


if __name__ == "__main__":
    main()
