# le piece movement

class Piece:
    def __init__(self, p, lst):
        self.picture = p
        self.piecelist = lst

# White pieces:
wk = Piece("WhiteKing.png", [4])
wq = Piece("WhiteQueen.png", [3])
wb = Piece("WhiteBishop.png", [2, 5])
wn = Piece("WhiteKnight.png", [1, 6])
wr = Piece("WhiteRook.png", [0, 7])
wp = Piece("WhitePawn.png", range(8,16))

whitepieces = [wk, wq, wb, wn, wr, wp]

# Black pieces:
bk = Piece("BlackKing.png", [60])
bq = Piece("BlackQueen.png", [59])
bb = Piece("BlackBishop.png", [58, 61])
bn = Piece("BlackKnight.png", [57, 62])
br = Piece("BlackRook.png", [56, 63])
bp = Piece("BlackPawn.png", range(48, 56))

blackpieces = [bk, bq, bb, bn, br, bp]

# Misc.
allpieces = whitepieces + blackpieces
boardlist = range(70) # Just to be safe

# Clears the board of all pieces
def emptyboard():
    for i in range(64): boardlist[i] = 0

# Adds the positions of all pieces on the board to their respective objects
def updatepiece(piece, old, newsqr):
    for num, i in enumerate(piece.piecelist):
        if i == old:
            piece.piecelist[num] = newsqr 

# Reverts the board to the starting position
def resetboard():
    wp.piecelist = range(8, 16)
    bp.piecelist = range(48, 56)
    bq.piecelist = [59]

# Returns the piece on square num
def pieceatsqr(num):
    for y in wp, bp, bq:
        for j in y.piecelist:
            if j == num:
                return y
    return None

# Moves the piece on start to end
def MovePiece(start, end):
    j = pieceatsqr(start)
    updatepiece(j, start, end)

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

# determines whether the user has been checkmated
def isMated(): 
    if bq.piecelist == [31]: return 'CHECKMATE'
