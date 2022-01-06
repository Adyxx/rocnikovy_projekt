#Use this branch to make AI
import oop as man
import copy

howManyTurns = 2

def eidam(gameState):#main
    bestMov = []
    possibleMoves = man.allPossibleMoves(gameState)
    bestMov = bValue(gameState)
    print(bestMov)
    return bestMov

def bValue(gameState):
    i = 1
    boardValue = 0
    bestBoardValue = -999
    bMove = []
    possibleMoves = man.allPossibleMoves(gameState)
    gameCopy = copy.deepcopy(gameState)
    pawn = 0
    numStred = 0
    movedd = 0
    king = 10
    pieceOnSide = 1
    protectingPiece = 2
    willBeEaten = -2
    print(possibleMoves)
    for x in possibleMoves:
        if x==";":
            numStred += 1
    for u in range (len(possibleMoves) - numStred):
        if (possibleMoves[pawn] == ";"):
            pawn +=1
        for o in range(howManyTurns):
            if o >1:
                gameCopy = copy.deepcopy(gameState)
                print("Awdawdawdawdawdawd")
                print(bMove)
                gameCopy.board[bMove[0][0]][bMove[0][1]] = "--"
                gameCopy.board[bMove[1][0]][bMove[1][1]] = "bl"
                gameCopy1 = copy.deepcopy(gameCopy)
            for r in range(man.DIMENSIONS):
                for c in range(man.DIMENSIONS):
                    if gameCopy.board[r][c] == "blk":
                        boardValue+=king
                        if ((c == man.DIMENSIONS-1) or (c == 0)):
                            boardValue+=pieceOnSide
                        if ((r + 1 < man.DIMENSIONS) and (c + 1 < man.DIMENSIONS) and r - 1 > 0 and c - 1 > 0 and (
                                (gameCopy.board[r + 1][c + 1].startswith("bl")) or (gameCopy.board[r + 1][c - 1].startswith("bl")) or (
                                gameCopy.board[r - 1][c + 1].startswith("bl")) or (gameCopy.board[r - 1][c - 1].startswith("bl")))):
                            boardValue += protectingPiece

                        if ((r + 1 < man.DIMENSIONS) and (c + 1 < man.DIMENSIONS) and r - 1 > 0 and c - 1 > 0 and (
                                (gameCopy.board[r + 1][c + 1].startswith("wh")) or (
                        gameCopy.board[r + 1][c - 1].startswith("wh")) or (
                                        gameCopy.board[r - 1][c + 1].startswith("wh")) or (
                                gameCopy.board[r - 1][c - 1].startswith("wh")))):
                            boardValue+=willBeEaten

                    elif gameCopy.board[r][c] == "whk":
                        boardValue -= king
                        if ((c == man.DIMENSIONS-1) or (c == 0)):
                            boardValue-=pieceOnSide
                        if ((r + 1 < man.DIMENSIONS) and (c + 1 < man.DIMENSIONS) and (r - 1 > 0) and (c - 1 > 0) and (
                                (gameCopy.board[r + 1][c + 1].startswith("bl")) or (gameCopy.board[r + 1][c - 1].startswith("bl")) or (
                                gameCopy.board[r - 1][c + 1].startswith("bl")) or (gameCopy.board[r - 1][c - 1].startswith("bl")))):
                            boardValue += protectingPiece

                    elif gameCopy.board[r][c] == "bl":
                        boardValue +=2
                        if ((c == man.DIMENSIONS-1) or (c == 0)):
                            boardValue+=pieceOnSide

                        if ((r + 1 < man.DIMENSIONS) and (c + 1 < man.DIMENSIONS) and r - 1 > 0 and c - 1 > 0 and (
                                (gameCopy.board[r + 1][c + 1].startswith("bl")) or (gameCopy.board[r + 1][c - 1].startswith("bl")) or (
                                gameCopy.board[r - 1][c + 1].startswith("bl")) or (gameCopy.board[r - 1][c - 1].startswith("bl")))):
                            boardValue += protectingPiece

                        if ((r + 1 < man.DIMENSIONS) and (c + 1 < man.DIMENSIONS) and r - 1 > 0 and c - 1 > 0 and (
                                (gameCopy.board[r + 1][c + 1].startswith("wh")) or (
                        gameCopy.board[r + 1][c - 1].startswith("wh")) or (
                                        gameCopy.board[r - 1][c + 1].startswith("wh")) or (
                                gameCopy.board[r - 1][c - 1].startswith("wh")))):
                            boardValue+=willBeEaten

                    elif gameCopy.board[r][c] == "wh":
                        boardValue -=2
                        if ((c == man.DIMENSIONS-1) or (c == 0)):
                            boardValue-=pieceOnSide
                        if ((r + 1 < man.DIMENSIONS) and (c + 1 < man.DIMENSIONS) and r - 1 > 0 and c - 1 > 0 and (
                                (gameCopy.board[r + 1][c + 1].startswith("bl")) or (gameCopy.board[r + 1][c - 1].startswith("bl")) or (
                        gameCopy.board[r - 1][c + 1].startswith("bl")) or (gameCopy.board[r - 1][c - 1].startswith("bl")))):
                            boardValue += protectingPiece

            if (possibleMoves[0] == 0):
                print("black cannot move")
            if(movedd>0):
                if (bestBoardValue <= boardValue):
                    bestBoardValue = boardValue
                    bMove = []
                    bMove.append(possibleMoves[pawn])
                    bMove.append(possibleMoves[pawn + i])
                i += 1
                if (((len(possibleMoves)>i+1)) and possibleMoves[pawn+i] == ";"):
                    pawn = pawn+i+1
                    i=1

                    print("out of range")
                if ((len(possibleMoves)==3) or (len(possibleMoves)==4) ):
                    bMove = []
                    bMove.append(possibleMoves[1])
                    bMove.append(possibleMoves[2])
                    return bMove

                gameCopy = copy.deepcopy(gameState)

                if (possibleMoves[pawn+i] == ";"):
                    pawn = pawn+i+1
                    i=1
            if (possibleMoves[pawn + i] == 0):
                return bMove
            if (gameCopy.board[possibleMoves[pawn][0]][possibleMoves[pawn][1]] =="bl"):
                gameCopy.board[possibleMoves[pawn][0]][possibleMoves[pawn][1]] = "--"
                gameCopy.board[possibleMoves[pawn+i][0]][possibleMoves[pawn+i][1]] = "bl"
            else:
                gameCopy.board[possibleMoves[pawn + i][0]][possibleMoves[pawn + i][1]] = "blk"
            movedd+=1

            print(possibleMoves[pawn+1][0])
            boardValue =0
            if (possibleMoves[pawn+1][0] == man.DIMENSIONS - 1):
                gameCopy.board[possibleMoves[pawn+1][0]][possibleMoves[pawn+1][1]] = "blk"

        if (bMove == []):
            bestBoardValue = boardValue
            bMove.append(possibleMoves[pawn])
            bMove.append(possibleMoves[pawn + 1])

        return bMove
