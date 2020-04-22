import random
import math

WEIGHT_LIST = {weight_list}
BIASES_LIST = {biases_list}
SHAPE = [27, 8, 8, 4]

IN_TRAINING = True

## NEURAL NET FUNCTIONS ##
if IN_TRAINING:
    import numpy as np
    def sigmoid_list(x):
        return 1/(1+np.exp(-x))
    def dot(x, y):
        return np.dot(x,y)
    def vector_sum(x, y):
        return x+y
    class NeuralNet():
        def __init__(self, weights, biases):
            self.weights = weights
            self.biases = biases
        def compute(self, inputs):
            v = inputs[:]
            for weight, b in zip(weights, biases):
                v = dot(weight, v)
                v = vector_sum(v, b)
                v = sigmoid_list(v)
            return v
else:
    def sigmoid(x):
        return 1/(1+math.exp(-x))
    def sigmoid_list(x):
        return [1/(1+math.exp(-v)) for v in x]

    def dot(x, y):
        v = 0
        for a,b in zip(x,y):
            v += a*b
        return v

    def vector_sum(x, y):
        return [a+b for a,b in zip(x,y)]

    class NeuralNet():
        def __init__(self, weights, biases):
            self.weights = weights
            self.biases = biases
        def compute(self, inputs):
            v = inputs[:]
            for weight, b in zip(weights, biases):
                v = [dot(v, w) for w in weight]
                v = vector_sum(v, b)
                v = sigmoid_list(v)
            return v

def list_to_weights(lis, shape=[27, 16, 16, 4]):
    weights = []
    index = 0
    for i in range(len(shape) - 1):
        row = []
        dx = shape[i]
        for j in range(shape[i+1]):
            row.append(lis[index:index + dx])
            index += dx
        weights.append(row)
    return weights

def list_to_biases(lis, shape=[27, 16, 16, 4]):
    biases = []
    index = 0
    for i in shape[1:]:
        biases.append(lis[index: index + i])
        index += i
    return biases

weights = list_to_weights(WEIGHT_LIST, SHAPE)
biases = list_to_biases(BIASES_LIST, SHAPE)
if IN_TRAINING:
    weights = np.array(weights)
    biases = np.array(biases)

nn = NeuralNet(weights, biases)

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

def flatten(board):
    lis = []
    for row in board:
        lis += row
    return lis

def copy(board):
    return [row.copy() for row in board]

sprinting = True
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

    global sprinting
    if sprinting:
        for r in board:
            if -1 in r:
                sprinting = False
                break
        else:
            if board[3][2] == 0:
                move_forward()
                return

    if row < 4 and team == Team.WHITE:
        r = row
    elif team == Team.BLACK and board_size - 1 - row < 4:
        r = board_size - 1 - row
    else:
        r = 0.5
    c = col
    if board_size - 1 - col < col:
        c = board_size - 1 - col
    inputs = flatten(board) + [r/board_size, c/board_size]
    results = nn.compute(inputs)
    if board[3][1] == -1 and board[3][3] == -1:
        if results[2] > results[3]:
            capture(row + forward, col-1)
        else:
            capture(row + forward, col+1)
        return
    elif board[3][1] == -1:
        capture(row + forward, col-1)
        return
    elif board[3][3] == -1:
        capture(row + forward, col+1)
        return
    elif results[1] > results[0] and board[3][2] == 0:
        move_forward()
        return

################################
##       OVERLORD STUFF       ##
################################

def max(a, b):
    return a if a > b else b

def min(a, b):
    return a if a < b else b

def check_space_wrapper(r, c, board_size, team=Team.WHITE, opp_team=Team.BLACK):
    # check space, except doesn't hit you with game errors
    if r < 0 or c < 0 or c >= board_size or r >= board_size:
        return 0
    try:
        team_there = check_space(r, c)
        if team_there == False:
            return 0
        if team_there is team:
            return 1
        else:
            return -1
    except:
        return 0

CENTER_MULTIPLIER = -0.7907822902051973
DISTANCE_ENEMY_MULTIPLIER = 3.0911788574398384
DISTANCE_FRIENDLY_MULTIPLIER = -5.282679434855145
FINISHED_MULTIPLIER = 3.414835990920963
PAWNS_MULTIPLIER = 3.853422030726663
ODD_MULTIPLIER = -0.7069367969710008 * 5

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

def odd(col):
    return col % 2

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

def overlord_heuristic(board, col, board_size):
    h = 0
    h += CENTER_MULTIPLIER * center(col, board_size)
    h += DISTANCE_ENEMY_MULTIPLIER * distance_enemy(board, col, board_size)
    h += DISTANCE_FRIENDLY_MULTIPLIER * distance_friendly(board, col, board_size)
    h += FINISHED_MULTIPLIER * finished(board, col, board_size)
    h += ODD_MULTIPLIER * odd(col)
    h += PAWNS_MULTIPLIER * pawns(board, col, board_size)
    return h

def overlord_turn():
    board_size = get_board_size()
    team = get_team()
    opp_team = Team.WHITE if team == Team.BLACK else team.BLACK

    board = get_board()
    board = [[0 if not x else (1 if x == team else -1) for x in row] for row in board]
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

