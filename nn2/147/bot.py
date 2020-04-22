import random
import math

WEIGHT_LIST = [-7.076625670536103,
 -3.0669552811568863,
 -1.7934669838350168,
 -1.3200692179786189,
 31.79044783228823,
 -23.332421195141706,
 3.889546483321263,
 15.041948792392342,
 7.056222447266972,
 11.54090287025854,
 -13.280452754661189,
 15.037264000367292,
 8.518842703005621,
 -6.378339546041034,
 -12.29390605469626,
 -29.672235530970013,
 -0.7143767754421053,
 -8.76302250351923,
 -14.353754377750251,
 -5.995062326331787,
 -6.903686650542973,
 -40.81576291166466,
 -5.130284443670819,
 3.0947070341278575,
 -12.050006146830174,
 1.4200819392077833,
 0.8030786570326471,
 13.492915258059965,
 -4.519629875064246,
 5.115073919753129,
 -12.133770591659795,
 -5.07672766758288,
 22.412718747368658,
 9.47846926759309,
 0.939536593973413,
 -5.869500842239405,
 0.5040740072225542,
 -4.919904824974651,
 -8.423528188362859,
 -20.115226784704568,
 -30.581375908157632,
 15.833731013768032,
 -22.609989670831375,
 20.546801128566344,
 18.186284019901336,
 -7.508103685012383,
 -12.160368509323563,
 -1.0392997523963339,
 -7.43634158670157,
 -12.62807090223178,
 -25.271673600258744,
 5.829639984768679,
 4.629871289165715,
 -25.405871109460584,
 -18.057940560543088,
 -15.312216329707455,
 5.072518422574254,
 -14.53908672216413,
 -35.94791676196859,
 3.3614873112654307,
 -7.842620092333562,
 26.852324577210958,
 14.316498516743927,
 5.953172144445217,
 -19.71827670029893,
 4.04164451723913,
 -6.4470654502763605,
 -21.921897281303046,
 1.993899184050881,
 3.1986819196959626,
 16.765244880468607,
 24.760774492151093,
 -5.213744591378851,
 -25.069636059374034,
 -6.640205117520372,
 9.89447360160312,
 21.629994181184166,
 14.497726762853665,
 -10.548701327272044,
 -7.892983162379981,
 -1.9258002454521728,
 11.588847755554896,
 -15.758295053428425,
 -5.137454566741258,
 25.423670399401225,
 -3.473951838511046,
 -18.614093616693303,
 1.5436799414502191,
 1.869060678746191,
 -10.156297586862811,
 -27.812315799265896,
 -4.490854315231816,
 11.336671643206623,
 30.04388547751048,
 9.565617016359525,
 35.75861162526007,
 17.60048482966385,
 1.1184808402182052,
 9.87696464093766,
 -12.768956252943482,
 -11.573009403767559,
 -24.370984904984226,
 -4.83780106098957,
 2.3349783864320486,
 5.110397634208877,
 -21.096983881760615,
 -11.530003524018616,
 12.421008390734972,
 -6.973854141078948,
 -17.139094269971505,
 -15.848676345504067,
 -14.569149893247392,
 10.443562184868973,
 5.860941661906137,
 -2.3004130161573464,
 -4.747461729810837,
 13.101452580263446,
 15.819952123126084,
 -11.556485706637313,
 1.5156183399173964,
 -2.164038916762547,
 7.594291766191988,
 5.406793200524606,
 17.246989120721537,
 9.719520644563284,
 9.106627482227458,
 8.480139109889436,
 9.606521787349395,
 1.5232377185480503,
 -7.832665012628768,
 15.729604435955357,
 2.600974393633667,
 14.063009138754847,
 -5.46612412742361,
 -15.05003550044756,
 19.35728577650189,
 -19.634357689764528,
 -8.695789055330948,
 -4.269289395466221,
 -3.410702414986177,
 0.4191793877529748,
 2.0495450681965233,
 -4.857399998382576,
 4.2152239112863334,
 18.7774968579929,
 1.1541710097383788,
 -31.258633070925114,
 -8.176244651508462,
 5.516683646164945,
 -1.0377415020657776,
 -32.39791626552872,
 0.7377958719333524,
 0.7635184697715651,
 -14.900291756887928,
 -8.9091880613164,
 -21.952907816444693,
 -20.26970970971805,
 8.30859042741744,
 -23.058717499808118,
 -3.4824619205990532,
 -1.0993019080680309,
 1.708180824361781,
 -14.285429523906094,
 -4.960543264447855,
 23.223551277942697,
 -15.250223411125768,
 -12.997343948374587,
 -7.945633219213484,
 18.042495381920695,
 -2.1082640285678966,
 25.68338442881702,
 2.1019453541239,
 1.9501937423675977,
 -0.7136910481883962,
 -2.5187661351504267,
 24.696600625021212,
 -12.375012613277926,
 18.336833706169145,
 -9.887043524578896,
 -2.438742001238042,
 15.952442514438596,
 3.73662044525644,
 -15.882737153746884,
 21.948113200635795,
 12.173330770378167,
 21.443827606963495,
 -0.6435637612605811,
 -10.484013132363271,
 -13.265195823879091,
 0.23390327891765272,
 21.141391525746563,
 13.636542432149646,
 17.98309795752212,
 -2.1511921199611166,
 -12.040254980163878,
 3.0272111638614136,
 16.586081396332297,
 -1.7102025738559143,
 -13.645539756532445,
 26.130213009647903,
 0.6393789061220065,
 4.661494821615722,
 5.874655614745718,
 7.611460102507504,
 6.893160795025983,
 13.638609359384155,
 14.795046416411624,
 -3.235036258041111,
 -4.154186205046509,
 -5.767853652783861,
 -24.995662487056364,
 27.56557470956838,
 -7.632966629005695,
 9.633766706124263,
 -14.344770238127516,
 -17.02426623745107,
 16.450927833661872,
 16.706532214609858,
 9.719348374819546,
 -16.309298512839398,
 2.7303069680019636,
 -7.75652675026901,
 -11.439549982062912,
 8.304779843596501,
 -36.31954091142836,
 -14.594953584657873,
 11.622194641703171,
 6.066472663914743,
 -4.380617065861518,
 5.627014052622734,
 -15.035117828387925,
 14.143034115462012,
 23.392730062004574,
 8.084845460376128,
 -2.8447936329772885,
 -0.9210789132637105,
 7.073101218931015,
 -3.6474962136144606,
 1.2747062783310987,
 -8.767689952078594,
 0.7968375897096074,
 -2.872371051222319,
 12.604360046789873,
 -18.41311760216451,
 15.223889744123804,
 11.85672010541378,
 -24.397591174565363,
 19.747890699951192,
 1.790435469745499,
 -11.410050980219017,
 -12.176659939845177,
 4.209041856975592,
 -18.132927136377198,
 3.717346697527966,
 1.3205731146069004,
 -9.616418251855851,
 -20.795134932906777,
 -33.162113308192595,
 -7.050878632512235,
 -10.426691900072765,
 0.4080655999862577,
 -3.451297243003732,
 24.75912659706188,
 -6.882547502412457,
 -5.200406640787945,
 0.12966555666913582,
 28.514086558275622,
 21.411971323991253,
 -6.521671123855412,
 -24.84808966878966,
 2.8066310363826315,
 12.80610337184113,
 3.154238975973354,
 10.340329576865079,
 -13.700767850825406,
 10.0447478402457,
 0.4668605333700384,
 14.360283936899222,
 -16.235577660168524,
 -5.371361348935281,
 33.55318997708521,
 3.6734296153732986,
 2.528256081042393,
 25.66070608156791,
 23.426046763318475,
 -9.512310973389562,
 -3.461154567789305,
 16.087197184317496,
 8.286315872615104,
 3.9299478793734233,
 -16.166146224702445,
 12.168373140597865,
 -13.170401384727622,
 25.496312382692565,
 8.41183630604531,
 -11.919805165212543,
 -16.456157764850353,
 0.299404739426538,
 -40.36843860760033,
 -7.5456009789587455,
 -23.24595233669276,
 25.69905351164028,
 1.914151072148488,
 -18.190442207470852,
 18.31059478272227,
 2.8800231832823675,
 -1.1183474728823568,
 6.178060622882989,
 4.9914765270452,
 -7.24057359006993,
 15.635514584229123,
 28.246103720405422]
BIASES_LIST = [-2.732542498661529,
 3.203216580515573,
 1.3477956352916074,
 8.25814331890466,
 27.304104129456142,
 -14.90919413061217,
 -10.0300806998533,
 -0.6000119384233539,
 -1.8483738048597316,
 13.150903208286497,
 -15.388909210191775,
 5.5061973601296454,
 -12.976287304702048,
 14.353457812288314,
 15.938789007464925,
 3.435646571617977,
 -15.958761527027436,
 8.44382030682639,
 4.568504573969578,
 14.09598591610735]
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


