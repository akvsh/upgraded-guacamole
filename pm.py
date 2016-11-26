import sys
import copy

# Global Constants
WHITE, BLACK = 'w', 'b'
PAWN, BISHOP, KNIGHT, ROOK, QUEEN, KING = 'p', 'b', 'n', 'r', 'q', 'k'

class Piece:
    def __init__(self, p, name):
        self.picture = p
        self.name = name
        self.piecelist = []
        self.value = 0


class boardState:
    prevBoard = None
    prevState = None
    enPassant = None
    # Castling
    ws, wl, bs, bl = True, True, True, True
    lastCapture, lastPawnMove = 0, 0
    numPieces = 32

curState = boardState()

# White pieces:
wk = Piece("Pieces/WhiteKing.png", KING)
wq = Piece("Pieces/WhiteQueen.png", QUEEN)
wb = Piece("Pieces/WhiteBishop.png", BISHOP)
wn = Piece("Pieces/WhiteKnight.png", KNIGHT)
wr = Piece("Pieces/WhiteRook.png", ROOK)
wp = Piece("Pieces/WhitePawn.png", PAWN)

whitepieces = [wk, wq, wb, wn, wr, wp]
for y in whitepieces: y.colour = WHITE

# Black pieces:
bk = Piece("Pieces/BlackKing.png", KING)
bq = Piece("Pieces/BlackQueen.png", QUEEN)
bb = Piece("Pieces/BlackBishop.png", BISHOP)
bn = Piece("Pieces/BlackKnight.png", KNIGHT)
br = Piece("Pieces/BlackRook.png", ROOK)
bp = Piece("Pieces/BlackPawn.png", PAWN)

blackpieces = [bk, bq, bb, bn, br, bp]
for y in blackpieces: y.colour = BLACK

# Misc.
allpieces = whitepieces + blackpieces
boardlist = range(70) # Just to be safe


# Clears the board of all pieces
def emptyboard():
    for i in range(64): boardlist[i] = 0


# Adds the positions of all pieces on the board to their respective objects
def updatepieces():
    for y in allpieces:
        y.piecelist = []
    for num, piece in enumerate(boardlist):
        if not(piece): continue
        for y in allpieces:
            if id(y) == piece:
                y.piecelist.append(num)
                break


# Reverts the board to the starting position
def resetboard():
    emptyboard()
    boardlist[4] = id(wk)
    boardlist[3] = id(wq)
    boardlist[2], boardlist[5] = id(wb), id(wb)
    boardlist[1], boardlist[6] = id(wn), id(wn)
    boardlist[0], boardlist[7] = id(wr), id(wr)
    for i in range(8, 16): boardlist[i] = id(wp)
    boardlist[60] = id(bk)
    boardlist[59] = id(bq)
    boardlist[61], boardlist[58] = id(bb), id(bb)
    boardlist[62], boardlist[57] = id(bn), id(bn)
    boardlist[63], boardlist[56] = id(br), id(br)
    for i in range(48, 56): boardlist[i] = id(bp)
    updatepieces()

resetboard()


# Resets the board and initializes some values
def resetgame():
    global curState
    resetboard()
    curState = boardState()


# Converts sqr to a number for ease of calculation (sqr is a string coord)
def coordtonum(sqr):
    return 8 * (int(sqr[1]) - 1) + ord(sqr[0]) - 97


# Converts num back to a coordinate
def numtocoord(num):
    return chr(num%8 + 97) + str((num/8)+1)


# Returns the piece on square num
def pieceatsqr(num):
    if num > 63 or num < 0:
        return None
    s = boardlist[num]
    for y in allpieces:
        if id(y) == s:
            return y
    return None


# Changes the value of the piece on start to end
def ChangeVar(start, end):
    j = pieceatsqr(start)
    boardlist[start] = 0
    boardlist[end] = id(j)

# Moves the piece on start to end
def MovePiece(start, end, update=True):
    j = pieceatsqr(start)
    m = pieceatsqr(end)

    curState.prevState = copy.copy(curState)
    curState.prevBoard = copy.copy(boardlist)

    ChangeVar(start, end)

    if update: updatepieces()

# Undoes the previous move made
def UndoMove(update=True):
    global curState
    global boardlist
    if curState.prevState == None:
        return
    
    boardlist = curState.prevBoard
    curState = curState.prevState
    
    if update: updatepieces()

# Returns a list of squares that are valid moves for the piece on square i
def PieceMovement(i):
    p = []

    # Pawn Movement

    if i == 14:
        p.append(30)
    elif i == 13:
        p.append(i+8)
        p.append(i+16)

    return p

# determines whether colour is in checkmate, stalemate or neither
def isMated(colour, threshold=32):
    fook = pieceatsqr(31)
    if fook and fook.name == QUEEN:
        return 'CHECKMATE'
