import random

### PAWN WEIGHTS ###
ADVANCED_MULTIPLIER = 8.5
BACK_MULTIPLIER = -2
CHAINS_MULTIPLIER = -1.3
COUNT_MULTIPLIER = -1.7
FILLED_MULTIPLIER = 0
HORIZONTAL_MULTIPLIER = -2.5
PROMOTED_MULTIPLIER = 0
THREATS_MULTIPLIER = -11.5
VERTICAL_MULTIPLIER = -3
WEDGES_MULTIPLIER = -1

### OVERLORD WEIGHTS ###
CENTER_MULTIPLIER = -1
DISTANCE_ENEMY_MULTIPLIER = -2
DISTANCE_FRIENDLY_MULTIPLIER = 1.8
FINISHED_MULTIPLIER = -10
LEFT_MULTIPLIER = 0
PAWNS_MULTIPLIER = -0.2
RANDOM_MULTIPLIER = 0


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

### PAWN METHODS ###
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
	
def back(row, team, board_size):
    if team == Team.WHITE:
        return 1 if row == 0 else 0
    else:
        return 1 if row == board_size - 1 else 0

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

def filled(board):
    # +1 if the back pawns are all ours
    h = 0
    for r in (0, 1, 2):
        for c in (0, 1, 2, 3, 4):
            if board[r][c] != 1:
                return 0
    return 1

def horizontal(board):
    # +1 for each pair of adjacent pawns horizontally, -1 for enemy pawns in such a configuration
    h = 0
    for x in range(4):
        for y in range(5):
            if board[y][x] == board[y][x+1] == 1:
                h += 1
            if board[y][x] == board[y][x+1] == -1:
                h -= 1
    return h

def promoted(row, team, board_size):
    if team == Team.WHITE:
        return 1 if row == board_size - 1 else 0
    else:
        return 1 if row == 0 else 0

def threats(board):
    # +1 for each of our pawns that can get captured
    # Note: double threats counted twice
    h = 0
    for x in range(4):
        for y in range(4):
            if board[y][x] == 1 and board[y+1][x+1] == -1:
                h += 1
            if board[y][x+1] == 1 and board[y+1][x] == -1:
                h += 1
    return h

def vertical(board):
    # +1 for each of our pawns adjacent vertically, -1 for enemy pawns in such a configuration
    h = 0
    for x in range(5):
        for y in range(4):
            if board[y][x] == board[y+1][x] == 1:
                h += 1
            if board[y][x] == board[y+1][x] == -1:
                h -= 1
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

### OVERLORD METHODS ###
def center(col, board_size):
    return abs(col - (board_size-1)/2)

def distance_enemy(board, col, board_size):
    for i in range(board_size):
        if board[i][col] == -1:
            return i
    return board_size

def distance_friendly(board, col, board_size):
    for i in range(board_size):
        if board[i][col] == 1:
            return i
    return board_size

def finished(board, col, board_size):
    return 1 if board[board_size-1][col] == 1 else 0

def left(col, board_size):
    return 1 if col < board_size / 2 else 0

def pawns(board, col, board_size):
    if col == 0:
        s = 0
        for r in range(board_size):
            for c in (col, col+1):
                s += board[r][c]
        return s
    
    if col == board_size - 1:
        s = 0
        for r in range(board_size):
            for c in (col-1, col):
                s += board[r][c]
        return s

    s = 0
    for r in range(board_size):
        for c in (col-1, col, col+1):
            s += board[r][c]
    return s

### HEURISTICS ###
def pawn_heuristic(board, row, team, board_size):
    # Heuristic for how good a position is
    
    h = 0
    h += ADVANCED_MULTIPLIER * advanced(board)
    h += BACK_MULTIPLIER * back(row, team, board_size)
    h += CHAINS_MULTIPLIER * chains(board)
    h += COUNT_MULTIPLIER * count(board)
    h += FILLED_MULTIPLIER * filled(board)
    h += HORIZONTAL_MULTIPLIER * horizontal(board)
    h += PROMOTED_MULTIPLIER * promoted(row, team, board_size)
    h += THREATS_MULTIPLIER * threats(board)
    h += VERTICAL_MULTIPLIER * vertical(board)
    h += WEDGES_MULTIPLIER * wedges(board)
    return h

def overlord_heuristic(board, col, board_size):
    h = 0
    h += CENTER_MULTIPLIER * center(col, board_size)
    h += DISTANCE_ENEMY_MULTIPLIER * distance_enemy(board, col, board_size)
    h += DISTANCE_FRIENDLY_MULTIPLIER * distance_friendly(board, col, board_size)
    h += FINISHED_MULTIPLIER * finished(board, col, board_size)
    h += LEFT_MULTIPLIER * left(col, board_size)
    h += PAWNS_MULTIPLIER * pawns(board, col, board_size)
    h += RANDOM_MULTIPLIER * random.random()
    return h
    

def copy(board):
    return [row.copy() for row in board]

def pawn_turn():
    board_size = get_board_size()
    team = get_team()
    opp_team = Team.WHITE if team == Team.BLACK else team.BLACK
    row, col = get_location()
    
    if team == Team.WHITE and row == board_size - 1:
        return
    if team == Team.BLACK and row == 0:
        return
    
    board = [[check_space_wrapper(row+y, col+x, board_size, team, opp_team) for x in range(-2, 3)] for y in range(-2, 3)]

    if team == Team.WHITE:
        forward = 1
    else:
        forward = -1
        board = board[::-1]
    
    states = {"sit": (board, row)}
    if board[3][2] == 0:
        new_state = copy(board)
        new_state[3][2] = 1
        new_state[2][2] = 0
        states["forward"] = (new_state, row + forward)
    if board[3][1] == -1:
        new_state = copy(board)
        new_state[3][1] = 1
        new_state[2][2] = 0
        states["left"] = (new_state, row + forward)
    if board[3][3] == -1:
        new_state = copy(board)
        new_state[3][1] = 1
        new_state[2][2] = 0
        states["right"] = (new_state, row + forward)

    best_move = None
    best_h = -100000
    for move in states:
        state_board, state_row = states[move]
        h = pawn_heuristic(state_board, state_row, team, board_size)
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
    
    board = [[check_space_wrapper(r, c, board_size, team, opp_team) for c in range(board_size)] for r in range(board_size)]
        
    if team == Team.WHITE:
        index = 0
    else:
        index = board_size - 1
        board = board[::-1]

    best_h = -100000
    best_col = None
    for col in range(board_size):
        if board[0][col] != 0:
            continue
        
        h = overlord_heuristic(board, col, board_size)
        if best_col is None or h > best_h:
            best_col = col
            best_h = h

    if best_col is not None:
        spawn(index, best_col)

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

