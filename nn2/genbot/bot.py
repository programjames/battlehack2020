import random

### PAWN WEIGHTS ###
ADVANCED_MULTIPLIER = 3.6986298089085548
BACK_MULTIPLIER = -3.273532649826768
CAPTURE_MULTIPLIER = 4.090752043341364
CHAINS_MULTIPLIER = -0.5176896785910658
COUNT_MULTIPLIER = -0.019510117348410128
ENEMY_PROMOTED_MULTIPLIER = 1.120979310344857
FILLED_MULTIPLIER = -2.013862327667272
HORIZONTAL_MULTIPLIER = -0.5920049326205388
PROMOTED_MULTIPLIER = -4.1601239348522565
STALEMATE_MULTIPLIER = 1.3853736575664106
THREATS_MULTIPLIER = -4.415240776791613
VERTICAL_MULTIPLIER = -0.2310979418295983
WEDGES_MULTIPLIER = 1.5126135043184092

### OVERLORD WEIGHTS ###
CENTER_MULTIPLIER = -0.5420474476271944
DISTANCE_ENEMY_MULTIPLIER = -0.3948127321761332
DISTANCE_FRIENDLY_MULTIPLIER = -2.805773268435026
FINISHED_MULTIPLIER = 5.4864383642184364
LEFT_MULTIPLIER = 0.7213735410340589
PAWNS_MULTIPLIER = 0.10606945028546355


GAME_END = 500


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
def advanced(row, team, board_size):
    # +1 for how far the pawn has travelled.
    if team == Team.WHITE:
        return row
    else:
        return board_size - row - 1

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

def enemy_promoted(e, row, team, board_size):
    # +1 for each row we are up, multiplied by e, the number of enemy pawns we have seen promoted.
    # +1 for how far the pawn has travelled.
    if team == Team.WHITE:
        return row * e
    else:
        return (board_size - row - 1) * e

def filled(board):
    # +1 if the back pawns are all ours
    h = 0
    for r in (1, 2):
        for c in (1, 2, 3):
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

def offense(row, team, board_size, turn):
    # +turn for how far the pawn has travelled.
    if team == Team.WHITE:
        return row * turn
    else:
        return (board_size - row - 1) * turn

def promoted(row, team, board_size):
    if team == Team.WHITE:
        return 1 if row == board_size - 1 else 0
    else:
        return 1 if row == 0 else 0

def stalemate(board):
    for r, c in ((3, 1), (3, 3), (2, 2)):
        if board[r][c] != 1:
            return 0
    for r, c in ((4, 1), (4, 3)):
        if board[r][c] != -1:
            return 0
    return 1

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

### PAWN GLOBALS ###
enemies_promoted = set()

### PAWN EXTRA FUNCTIONS ###
def update_enemies_promoted(board, row, col, team, board_size):
    if team == Team.BLACK:
        row = board_size - 1 - row
    if row > 2:
        return
    for i, r in enumerate(board[2-row]):
        c = col + 2 - i
        if r == -1 and c not in enemies_promoted:
            enemies_promoted.append(c)

### HEURISTICS ###
def pawn_heuristic(board, row, team, board_size, capture_):
    # Heuristic for how good a position is
    
    h = 0
    h += ADVANCED_MULTIPLIER * advanced(row, team, board_size)
    h += BACK_MULTIPLIER * back(row, team, board_size)
    h += CAPTURE_MULTIPLIER * capture_
    h += CHAINS_MULTIPLIER * chains(board)
    h += COUNT_MULTIPLIER * count(board)
    h += ENEMY_PROMOTED_MULTIPLIER * enemy_promoted(len(enemies_promoted), row, team, board_size)
    h += FILLED_MULTIPLIER * filled(board)
    h += HORIZONTAL_MULTIPLIER * horizontal(board)
    h += PROMOTED_MULTIPLIER * promoted(row, team, board_size)
    h += STALEMATE_MULTIPLIER * stalemate(board)
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
    return h
    

def copy(board):
    return [row.copy() for row in board]

def pawn_turn():
    log(f"MY STALEMATE MULTIPLIER = {STALEMATE_MULTIPLIER}")
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

    update_enemies_promoted(board, row, col, team, board_size)
    
    states = {"sit": (board, row, 0)}


    if stalemate(board):
        log("stalemate sit")

    if board[3][2] == 0:
        new_state = copy(board)
        new_state[3][2] = 1
        new_state[2][2] = 0
        if stalemate(new_state):
            log("stalemate forward")
        else:
            log("Not stalemate forward")
        states["forward"] = (new_state, row + forward, 0)
    
    if board[3][1] == -1:
        new_state = copy(board)
        new_state[3][1] = 1
        new_state[2][2] = 0
        states["left"] = (new_state, row + forward, 1)
    
    if board[3][3] == -1:
        new_state = copy(board)
        new_state[3][1] = 1
        new_state[2][2] = 0
        states["right"] = (new_state, row + forward, 1)

    if len(states) == 1:
        return
    
    best_move = None
    best_h = -100000
    for move in states:
        state_board, state_row, state_capture = states[move]
        h = pawn_heuristic(state_board, state_row, team, board_size, state_capture)
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
        if best_col is None or h < best_h:
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

