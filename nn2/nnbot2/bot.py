import random
import math

WEIGHT_LIST = [9.007749464530114,
 -8.768363971659344,
 8.890735137906773,
 9.087060340637482,
 -8.520658761189209,
 6.226411675984668,
 9.827719799466323,
 -7.516331715153932,
 9.473674250849196,
 -8.581048198395735,
 8.05917875540517,
 -6.657415753758807,
 9.708600296427576,
 6.612719196890922,
 -5.57565697787571,
 -1.4923760346720378,
 -3.4340581781858877,
 2.6855629749146193,
 -9.264956251432118,
 -0.5611652966338365,
 8.602211156403428,
 1.0366713444003643,
 8.748866199479039,
 9.946134986274352,
 -2.4222673668913846,
 5.265596241793988,
 2.873219815364598,
 -7.825358368894464,
 7.0532596996322425,
 -7.451162186296849,
 5.977849979452603,
 9.111226930874569,
 8.692519107337596,
 1.7737786963878328,
 3.8917847375048,
 5.684290320525152,
 -8.456875293370237,
 -2.669116048075595,
 -7.847896588774441,
 8.90072656691877,
 0.16379435107207563,
 7.381648979884904,
 4.62035161975529,
 -0.7333874017461,
 5.856665010190575,
 2.866499723350559,
 -4.488754415551563,
 4.306076025045687,
 -6.686764663531209,
 2.5199519657168885,
 -1.0069666201031797,
 4.486103942802824,
 -9.889312654651178,
 4.209427711355726,
 0.5504753430944813,
 -6.018680739928208,
 4.649549663045413,
 7.599588710146577,
 -0.5911474477585781,
 8.163482809758417,
 9.698340747754784,
 1.7811855240071104,
 8.721483891186097,
 1.7167395964962644,
 6.2323714983917675,
 1.5382675053651518,
 -9.816346190098965,
 -8.892665558576603,
 -6.43786746186493,
 -8.962786503825013,
 2.226890558211167,
 -3.495006384366672,
 6.742569648002789,
 0.5857377545685409,
 2.489905717012819,
 -2.95461018849082,
 8.875127366101843,
 -6.024633042460765,
 5.505298714539322,
 7.896340806800357,
 1.1658536745882042,
 -3.3123746726036636,
 7.351066497792839,
 -0.26837694485523933,
 8.772337876554882,
 9.365686951432668,
 -9.063643754067686,
 8.999051142490238,
 2.977936148430553,
 -1.531189862263906,
 -0.7947578567905182,
 0.10523974084293641,
 3.35949175676663,
 1.156684084310971,
 2.2547027803327744,
 -8.087064323126473,
 7.442972479665315,
 4.488347167133984,
 -1.4637065697229819,
 4.701218755714386,
 6.115844841687853,
 -2.946510692339814,
 -8.256593216444138,
 1.0698307958733828,
 -3.963762085967222,
 -7.253462707535066,
 -9.037596218167682,
 -2.8247351069547193,
 7.4873628796830225,
 -8.373120401192985,
 8.971879785735702,
 1.0887038426514106,
 5.63944763393873,
 -5.125123649052941,
 4.060500460910465,
 9.702746744968735,
 -5.711449795564134,
 9.86754847689506,
 4.251036678179577,
 6.753589689883398,
 -6.987266278139108,
 1.6619932390640368,
 0.18671572790416846,
 -5.169731509513009,
 8.12041937867172,
 -0.6990503757492288,
 1.5538170535808824,
 5.178942880529629,
 0.4974187440209512,
 -9.535475299255989,
 -3.1835854068038056,
 2.885694556046545,
 -5.6456954294378825,
 2.5913873015465168,
 6.583105895073867,
 8.833562360176384,
 -6.279643063925098,
 4.43829672844152,
 -8.369808279480553,
 4.862246491148195,
 -4.141176301070535,
 4.697665676371516,
 5.575800351611875,
 7.195836040499309,
 8.85800715819883,
 -6.03792329854522,
 -7.785242226299243,
 8.342852836422459,
 4.53828079354474,
 -0.18974667326351735,
 5.799595354652274,
 2.4658378410890194,
 0.5221135392857938,
 -4.3482911799822865,
 -3.7344118663062975,
 5.344068769131214,
 -5.954393114709767,
 -2.391078562035407,
 -8.664911145720664,
 4.989421302397666,
 -4.783082779966112,
 2.7870595308749575,
 -7.898343319269339,
 -8.415141927343202,
 -8.454992406684916,
 -4.149795691779213,
 -5.660888111462419,
 4.946354971396794,
 -6.873693004898625,
 7.966913407371113,
 -2.0245680461194615,
 -7.336306095526068,
 6.766992731805992,
 4.644179444976205,
 -2.230189367865729,
 8.48016458069726,
 9.588452071501312,
 9.44733093174312,
 -1.6437228872825127,
 1.8177669425830345,
 -0.43455990346337714,
 3.833913396351729,
 -1.3055172720954005,
 -5.594218576170038,
 -6.675173740409253,
 -5.148969907588659,
 1.1799477538387322,
 9.292928916163998,
 8.283833456938197,
 -4.387120230507218,
 -3.427675579254183,
 0.5265345858760728,
 -6.576619483162567,
 6.397509389757516,
 6.687653294605251,
 -0.9165847133848395,
 -7.615614076396304,
 -2.3439528323780534,
 -0.8064592847161229,
 -6.349546098371722,
 6.993523487035468,
 7.120190567357557,
 9.919575505228021,
 2.6918428611760987,
 -6.1072684141796625,
 0.6479384454951465,
 8.443312624583847,
 -9.472978321923653,
 2.176420824051455,
 4.5831537113438365,
 -3.397373498855723,
 -9.307020620455646,
 6.05950389500552,
 0.39733393400883443,
 2.7724502505929305,
 1.190671840691028,
 -0.7479837541733385,
 1.5228765195814393,
 -2.8766477936133095,
 1.2357039884685008,
 2.4347790525288797,
 5.361166076654616,
 -3.667470045615568,
 -8.112711388755049,
 -0.12649724989688416,
 8.867129176619159,
 7.4102001103911235,
 -3.858844888889255,
 -1.8334080699617843,
 -2.647032249944152,
 4.495688972572427,
 1.6032585590161759,
 -4.245704677651386,
 9.85831428580029,
 6.5826250785911675,
 7.679733528142187,
 6.513748671312854,
 4.685576767771607,
 -4.674665108677461,
 -5.16338510994861,
 -4.20880427682553,
 -7.891800970051599,
 2.087016659487082,
 -6.227325204361438,
 0.01828530884250945,
 -8.08807121858601,
 1.8011274293459643,
 5.368578283721561,
 -6.897970966624454,
 -9.034034891308522,
 6.077638390531664,
 -0.388127367195068,
 -7.747027114240172,
 2.399459794153877,
 -7.7493805427217595,
 -6.73585955207312,
 2.3192499518974845,
 8.564555715132666,
 4.227221828971061,
 -3.6607896982829535,
 4.025864719464456,
 3.626630210833506,
 -3.401810191774439,
 -4.08844946053148,
 -4.658647505569018,
 -4.49926004612861,
 -8.238397461287,
 2.5915990377189164,
 7.451972266417339,
 -4.383941574727723,
 9.129853256820638,
 -8.930853900605873,
 -8.800066947780662,
 3.1810752967691904,
 7.374246750070938,
 -6.41507918803728,
 6.992459362461837,
 9.893454691579791,
 -4.183367068778323,
 -7.108383200587067,
 5.877164683952589,
 -4.925109914256716,
 -5.557708028983717,
 2.6048876056808865,
 -2.274268825192209,
 -8.101216307027219,
 6.664173164248005,
 5.742622536886712,
 9.329580601435378,
 -7.32111974517621,
 5.147663634869025,
 -9.490504496814347,
 -8.369981830855476,
 -5.019408179029665,
 5.988951986014657,
 -5.993787379967532,
 -1.5850058361851573,
 0.41626274275818176,
 5.767510176787384,
 2.5712236051967317,
 -6.393970639376545,
 -0.9797537158584149,
 -9.423628147791694,
 -4.775652824787702,
 -7.359256665265221,
 -8.886228800903398,
 3.666220614424061,
 7.265057291330358,
 -7.085217993186415,
 2.2393380960695435,
 1.5804696151213982,
 -0.014194851288797494]
BIASES_LIST = [-2.5820808544330998,
 7.610902802686429,
 3.1001612438666637,
 9.52838050237235,
 9.279106308548528,
 -7.712057720856764,
 0.4757155057448408,
 -1.0570785873053357,
 -8.664987234816014,
 6.363578525884574,
 -0.3667423625680222,
 -9.488021040377907,
 6.207444938972586,
 -3.9908399995680703,
 8.982395539074648,
 0.702934991819637,
 1.1273463281777136,
 -0.903258430962147,
 7.733120172221387,
 -7.0936971786366065]
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

    r = row
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

CENTER_MULTIPLIER = 1.8046815
DISTANCE_ENEMY_MULTIPLIER = 3.401718669
DISTANCE_FRIENDLY_MULTIPLIER = -3.52584115
FINISHED_MULTIPLIER = -2
PAWNS_MULTIPLIER = 1.1707371322
ODD_MULTIPLIER = -20

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
    

def copy(board):
    return [row.copy() for row in board]

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


