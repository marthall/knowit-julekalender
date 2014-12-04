from operator import add

DIMENSION = 10

LEGAL_MOVES = [ (-2, -1), (-2,  1), (-1, -2), (-1,  2),
                ( 1, -2), ( 1,  2), ( 2, -1), ( 2,  1)]

INIT_POSITION = (0, 0)

board = [[0 for i in range(DIMENSION)] for j in range(DIMENSION)]

def is_inside_board(pos): return 0 <= pos[0] < DIMENSION and 0 <= pos[1] < DIMENSION
def get_value(pos): return board[pos[0]][pos[1]]
def toggle_pos(pos): board[pos[0]][pos[1]] = 1 - get_value(pos)

def find_move(pos):
    for move in LEGAL_MOVES:
        tmp_next_pos = map(add, pos, move)
        if is_inside_board(tmp_next_pos) and get_value(tmp_next_pos) == get_value(pos):
            return tmp_next_pos

    for move in LEGAL_MOVES[::-1]:
        tmp_next_pos = map(add, pos, move)
        if (is_inside_board(tmp_next_pos)):
            return tmp_next_pos

    raise Exception("Couldn't find a legal move")

pos = INIT_POSITION

for i in range(200):
    next_pos = find_move(pos)
    toggle_pos(pos)
    pos = next_pos

for row in board:
    print " ".join(map(str, row))

print "Det er %i sorte ruter" % sum(map(sum, board))
