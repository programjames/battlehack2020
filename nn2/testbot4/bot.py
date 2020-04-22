import random
import math

WEIGHT_LIST = [-8.799255803362566,
 -2.131725457799849,
 0.15519989265108847,
 0.3867900993257123,
 31.27651600924595,
 -20.44828007226514,
 6.167921635158548,
 15.611053308503534,
 6.046592037794038,
 10.844466030192555,
 -12.76453304963141,
 15.2428923715671,
 5.7072582358681405,
 -7.8752197102200485,
 -12.541232397675035,
 -32.70903459169926,
 1.130618713976452,
 -11.896020667658783,
 -14.267327395641452,
 -5.9918929146639215,
 -8.279205431436983,
 -39.99901307516588,
 -4.4905127992622385,
 1.004240744222978,
 -13.30563363684146,
 3.571904540291431,
 -0.05466423611126703,
 14.225278750146385,
 -5.360736336263292,
 2.301648944016537,
 -12.999440511643707,
 -6.026552773712811,
 21.41209279099545,
 9.752630188261556,
 0.7472300014662923,
 -6.757612626997926,
 1.5040376337938033,
 -4.598917247500534,
 -7.7790751312564765,
 -20.461921097864675,
 -28.165108066043157,
 12.542474722283828,
 -20.64816734957876,
 21.910454800168992,
 17.344943740203053,
 -9.14710465826907,
 -10.197942028723537,
 -1.759139863135996,
 -9.67170361360642,
 -10.338906548222353,
 -24.395007771854207,
 4.988457853800974,
 5.038846676716171,
 -27.486873627147087,
 -15.747209861025363,
 -15.909659332266136,
 6.290393306939736,
 -14.112951778482905,
 -33.51495433061703,
 5.450875979653185,
 -9.133581950001892,
 27.19171645659664,
 12.890985664171799,
 5.450013481676031,
 -22.044504145722158,
 1.4723946027165502,
 -5.138354133046744,
 -24.01938438275424,
 2.072590927200472,
 2.301770270093761,
 18.376782142273658,
 25.354890575601363,
 -4.859525616459662,
 -30.254288000951103,
 -8.178525263997857,
 7.691758933454034,
 20.961101528761457,
 14.647297966351454,
 -11.64775457779113,
 -12.455659801581419,
 -3.04346808081271,
 13.230991031276833,
 -15.328848481792098,
 -4.7014606828898,
 25.049332174294094,
 -2.9700204846617835,
 -20.94418126504983,
 3.5888260405464676,
 -0.7637433730515892,
 -11.744928310474842,
 -27.334851554592724,
 -1.899189528267712,
 10.296180649588047,
 33.97207567090615,
 9.018213046877408,
 34.60802085383571,
 15.851176237337748,
 0.707104075101167,
 10.747630699401675,
 -10.674121749024668,
 -13.174212305860278,
 -22.447657425514002,
 -4.971072506488695,
 1.951637565160009,
 3.285530394790019,
 -19.74761758588251,
 -11.028680594365552,
 14.242999547995488,
 -4.330080597900758,
 -16.908714310468962,
 -16.727982201531184,
 -13.459445487259838,
 11.756963966591595,
 4.404893903913461,
 -4.21678005239656,
 -2.1217108313975896,
 11.645826025646592,
 15.609185634476438,
 -11.917116000112717,
 2.98913656354328,
 -1.9842057552802015,
 8.575025540505193,
 8.11627558184419,
 17.705317849931667,
 10.217478079040216,
 8.551156058033833,
 12.424388056310114,
 7.987911063748852,
 3.1511516213667017,
 -10.047066612942515,
 19.00700118968743,
 3.2706862283918863,
 12.949274629989718,
 -4.638432879192568,
 -17.549356539062778,
 18.829618717485864,
 -18.792615304275383,
 -10.571330196386269,
 -2.9675778443292167,
 -5.545408495445704,
 -2.58761806242683,
 3.4622123318842837,
 -4.985877760986778,
 0.8725554452173991,
 18.722255350685444,
 0.8408571158187552,
 -30.614357833031892,
 -8.179047381161139,
 7.379300439427448,
 0.0168114102096536,
 -31.652579113612287,
 0.4381708305743739,
 -0.6843920044076,
 -13.080602663442843,
 -7.6948725764651495,
 -25.313661574847767,
 -18.393430027914516,
 9.352016447079773,
 -24.040203668734424,
 -2.389037411657989,
 0.8236223696371829,
 2.8312856017261394,
 -14.605926292572041,
 -3.3965003233246334,
 23.422848059048427,
 -12.642886932700012,
 -14.557459870015885,
 -5.349587893746046,
 20.714291899983635,
 -1.908479080790469,
 22.597285313613874,
 1.6042252997363537,
 -0.8003013348034431,
 -0.5530223201175446,
 -0.8137895854337334,
 24.097282563710124,
 -14.50751392906718,
 16.842838596467836,
 -10.861408508443684,
 -3.739185423253778,
 14.310080355730447,
 5.022683985873276,
 -16.504406370141762,
 19.505246316716814,
 13.394162013259924,
 21.161694529264743,
 -3.0757370598867437,
 -10.442223544550876,
 -14.727888168019176,
 -2.284098358187923,
 17.86329797047207,
 12.912797887029763,
 16.265950696429975,
 -1.4645818728979079,
 -11.756659886458857,
 2.664102559998782,
 17.808798639430837,
 -0.02490445375166417,
 -14.728117317731021,
 27.49679087542598,
 0.8408904484112336,
 3.266771484030219,
 8.268111784916456,
 7.103452689489041,
 4.540481554836725,
 14.701154384427728,
 14.102365289454223,
 -4.984405592495719,
 -2.3584501680418795,
 -8.481772787270842,
 -26.088718307828263,
 27.0275085086564,
 -6.9775865956538485,
 12.45677161023946,
 -14.22684138327997,
 -14.79234630771622,
 21.144226021097975,
 17.66878205273413,
 10.32754556412093,
 -16.530008954687496,
 3.412228209053894,
 -6.109208182225849,
 -10.66060032014092,
 5.274180812523816,
 -35.7233132236021,
 -15.067293662649472,
 10.908654732121528,
 3.680840121094051,
 -4.163887266796017,
 3.603507328341472,
 -12.929157209862144,
 15.654319050762373,
 17.96524211758441,
 9.561439046526786,
 -6.211287299594713,
 -5.168284883841972,
 8.156569858989238,
 -4.807684223645258,
 2.2532339128659844,
 -7.941601587229398,
 -0.45531979726308125,
 -4.338791772152321,
 11.464105641960675,
 -15.982669840317879,
 15.03836675895489,
 13.477865452259202,
 -25.270132095461804,
 19.740549207834384,
 2.631257603151166,
 -11.38003816608529,
 -12.854949277456269,
 3.382053928886412,
 -18.037107978906832,
 3.567336224405185,
 -1.5866638341483608,
 -7.716161451110585,
 -21.054125798847405,
 -31.231766752633476,
 -7.263546648149698,
 -10.036549134322458,
 -0.13628649123320657,
 -1.4722384055017848,
 23.35659693380024,
 -9.738382883287441,
 -4.030601167414452,
 0.6827083591128487,
 26.724811610715754,
 21.831194303632227,
 -6.306022413624078,
 -25.547758778969836,
 3.884051330636577,
 13.16200589513874,
 5.213484259752903,
 11.974205967666196,
 -13.4747904124325,
 7.194092414893815,
 0.7903253235544376,
 14.751778501380933,
 -16.20158779281148,
 -7.642776221893854,
 35.77654487113654,
 3.9171444150475576,
 0.8934737716197685,
 27.70088703974142,
 23.67717674202493,
 -9.342123962859715,
 -2.608681293901607,
 19.389376117277674,
 10.053136331995516,
 6.570587641272864,
 -16.089084698235308,
 13.55783483017314,
 -14.931700563724274,
 27.546207825176054,
 10.349471941210796,
 -11.30901651197626,
 -15.663548396010665,
 1.8622648370747348,
 -40.509958183632904,
 -8.667114098196736,
 -21.9787619477915,
 25.67340155372813,
 -0.5222241748709282,
 -19.086372096457453,
 17.96300897276961,
 1.5626222654507014,
 0.7065440723345369,
 3.4274579362576096,
 6.758712209297974,
 -9.617298686536769,
 16.637516185302648,
 27.904466004087446]
BIASES_LIST = [-5.318513163896683,
 2.8272544236612545,
 1.1419320973547913,
 5.715146653381254,
 22.93695273579147,
 -16.081714235984986,
 -10.89824794192791,
 1.0421809803383244,
 -4.413993029260934,
 10.978750019470192,
 -13.431269634510679,
 8.735882285226255,
 -10.639564828782962,
 14.90020752299107,
 16.166984031788562,
 4.113017795060619,
 -16.6805139455735,
 8.264750941011926,
 5.229702333746635,
 13.56200894012412]
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


