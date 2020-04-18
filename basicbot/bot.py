import random

DEBUG = 1
def dlog(str):
    return
    if DEBUG > 0:
        log(str)

ADVANCED_MULTIPLIER = 1
CHAINS_MULTIPLIER = 1
COUNT_MULTIPLIER = 1
HORIZONTAL_MULTIPLIER = 1
THREATS_MULTIPLIER = 1
VERTICAL_MULTIPLIER = 1
WEDGES_MULTIPLIER = 1


def check_space_wrapper(r, c, board_size, team=Team.WHITE, opp_team=Team.BLACK):
    # check space, except doesn't hit you with game errors
    if r < 0 or c < 0 or c >= board_size or r >= board_size:
        return 0
    try:
        team_there = check_space(r, c)
        if team_there is team:
            return 1
        elif team_there is opp_team:
            return -1
        return 0
    except:
        return 0

def advanced(board):
    # +1 for how advanced each of our pawns is, -1 for how advanced each enemy pawn is
    h = 0
    for x in range(5):
        for y in range(5):
            if board[y][x] == 1:
                h += y
            if board[y][x] == -1:
                h -= 4 - y
    return h

def chains(board):
    # +1 for each pawn in one of our chains, -1 for each pawn in enemy chain
    h = 0
    for x in range(4):
        for y in range(4):
            if board[y][x] == board[y+1][x+1] == 1:
                h += 1
            if board[y][x+1] == board[y+1][x] == 1:
                h += 1
            if board[y][x] == board[y+1][x+1] == -1:
                h -= 1
            if board[y][x+1] == board[y+1][x] == -1:
                h -= 1
    return h

def count(board):
    # +1 for each of our pawns, -1 for each enemy pawn
    # sum() is not defined
    h = 0
    for x in range(5):
        for y in range(5):
            h += board[y][x]
    return h

def horizontal(h, board):
    # +1 for each pair of adjacent pawns horizontally, -1 for enemy pawns in such a configuration
    h = 0
    for x in range(4):
        for y in range(5):
            if board[y][x] == board[y][x+1] == 1:
                h += 1
            if board[y][x] == board[y][x+1] == -1:
                h -= 1
    return h

def threats(board):
    # -1 for each of our pawns that can get captured
    # Note: double threats counted twice
    h = 0
    for x in range(4):
        for y in range(4):
            if board[y][x] == 1 and board[y+1][x+1] == -1:
                h -= 1
            if board[y][x+1] == 1 and board[y+1][x] == -1:
                h -= 1
    return h

def vertical(board):
    # -1 for each of our pawns adjacent vertically, +1 for enemy pawns in such a configuration
    h = 0
    for x in range(5):
        for y in range(4):
            if board[y][x] == board[y+1][x] == 1:
                h -= 1
            if board[y][x] == board[y+1][x] == -1:
                h += 1
    return h

def wedges(board):
    # +1 for each pawn in a wedge, -1 for each enemy pawn in a wedge
    h = 0
    for x in range(1, 4):
        for y in range(4):
            if board[y][x-1] == board[y+1][x] == board[y][x+1] == 1:
                h += 1
            if board[y+1][x-1] == board[y][x] == board[y+1][x+1] == -1:
                h -= 1
    return h

def heuristic(board):
    # Heuristic for how good a position is
    
    # +1 for each of our pieces, -1 for each of enemy pieces
    h = 0
    h += ADVANCED_MULTIPLIER * advanced(board)
    h += CHAINS_MULTIPLIER * chains(board)
    h += COUNT_MULTIPLIER * count(board)
    h += HORIZONTAL_MULTIPLIER * horizontal(board)
    h += THREATS_MULTIPLIER * threats(board)
    h += VERTICAL_MULTIPLIER * vertical(board)
    h += WEDGES_MULTIPLIER * wedges(board)
    return h

def copy(board):
    return [row.copy() for row in board]

def pawn_turn():
    board_size = get_board_size()
    team = get_team()
    opp_team = Team.WHITE if team == Team.BLACK else team.BLACK
    row, col = get_location()
    
    board = [[check_space_wrapper(row+y, col+x, board_size, team, opp_team) for x in range(-2, 3)] for y in range(-2, 3)]

    if team == Team.WHITE:
        forward = 1
    else:
        forward = -1
        board = board[::-1]
    
    states = {"sit": board}
    if board[3][2] == 0:
        new_state = copy(board)
        new_state[3][2] = 1
        new_state[2][2] = 0
        states["forward"] = new_state
    if board[3][1] == -1:
        new_state = copy(board)
        new_state[3][1] = 1
        new_state[2][2] = 0
        states["left"] = new_state
    if board[3][3] == -1:
        new_state = copy(board)
        new_state[3][1] = 1
        new_state[2][2] = 0
        states["right"] = new_state

    best_move = None
    best_h = -100000
    for move, board in states.items():
        h = heuristic(board)
        if best_move == None or h > best_h:
            best_move = move
            best_h = h

    if best_move == "sit":
        return
    elif best_move == "forward":
        move_forward()
        return
    elif best_move == "left":
        capture(row + forward, col - 1)
        return
    elif best_move == "right":
        capture(row + forward, col + 1)
        return

def overlord_turn():
    board_size = get_board_size()
    team = get_team()
    opp_team = Team.WHITE if team == Team.BLACK else team.BLACK
    
    if team == Team.WHITE:
        index = 0
    else:
        index = board_size - 1

    for _ in range(board_size):
        i = random.randint(0, board_size - 1)
        if not check_space(index, i):
            spawn(index, i)
            break

def turn():
    """
    MUST be defined for robot to run
    This function will be called at the beginning of every turn and should contain the bulk of your robot commands
    """
    
    robottype = get_type()
    if robottype == RobotType.PAWN:
        pawn_turn()
    else:
        overlord_turn()
    bytecode = get_bytecode()

