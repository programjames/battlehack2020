import random
import math

WEIGHT_LIST = [-9.30756174440816,
 -3.4966433128206473,
 0.5787228665203268,
 -0.52312978692406,
 33.02842137185287,
 -23.38006097088359,
 2.2510381268882282,
 14.949699224717753,
 6.037345225822733,
 10.68707936383588,
 -12.483076074234281,
 13.595233483569023,
 8.862341415016907,
 -6.690784394309134,
 -13.614092020010911,
 -29.80966238910771,
 1.5903485739548653,
 -10.457643650418202,
 -13.79924148036942,
 -6.876548125843025,
 -6.208561017405299,
 -40.44823581986523,
 -3.8052534273492604,
 3.24388739631602,
 -10.807364390290594,
 3.037634091487214,
 2.0281759326648867,
 14.19501290290155,
 -5.386107103781036,
 5.242417295339228,
 -12.134133015917433,
 -4.136007361402357,
 22.282275088973893,
 10.82383495174105,
 0.8871986986393006,
 -3.8418150194830973,
 1.8234112085419059,
 -4.759948425878143,
 -9.926974385057962,
 -21.146565674187872,
 -30.953560316109158,
 16.20528776697711,
 -21.38780894239138,
 22.345700586198042,
 16.65351047689358,
 -8.149460106032084,
 -9.731582490385811,
 -1.8801069103319783,
 -9.49361942581289,
 -11.972857044110237,
 -25.336864210778838,
 4.729675869067691,
 5.51276331819387,
 -23.232889195856643,
 -17.866592299332762,
 -15.571210783359488,
 6.684839000571629,
 -14.479275214584733,
 -34.912513517701974,
 2.390782005587935,
 -8.2076581042993,
 24.694454954599802,
 13.9443695985077,
 6.3613225031128895,
 -19.973393123128304,
 4.553159926794613,
 -7.988871375056216,
 -24.122257050645644,
 1.4646026527490201,
 2.5917959384110736,
 16.348178310704444,
 23.961591762318452,
 -4.849891282351019,
 -26.646995741427716,
 -5.7919383645824105,
 9.884923026230977,
 18.33395090100799,
 13.10999606533653,
 -11.053290630841415,
 -9.117340318142608,
 -2.0943472199431747,
 13.233827317657758,
 -17.510011746158867,
 -1.645713440011699,
 24.1070558185614,
 -2.7422618822812854,
 -19.189483573136616,
 0.38249937778847065,
 -0.32723103037130863,
 -11.238962964596391,
 -28.889827529135115,
 -5.413500993415253,
 10.430931549091827,
 30.576397438228003,
 7.6914952438894195,
 36.3172706326977,
 17.476827675962603,
 0.6740923070251588,
 13.412164274259789,
 -11.843500466503851,
 -11.48710241291572,
 -23.763598390693243,
 -5.6596131058437145,
 4.522634848639298,
 5.005467848376919,
 -21.701611777049965,
 -12.010860580406849,
 12.635956236059513,
 -6.425860118711161,
 -16.510677226960638,
 -17.84255220272595,
 -12.530860513402194,
 9.489532656127706,
 6.193853070507104,
 -3.5347592783815696,
 -3.736741960851088,
 11.761367246844744,
 17.195401710102384,
 -11.50063783574682,
 1.432840022258697,
 2.108631041540246,
 7.151578037458097,
 8.147346618915662,
 15.264711939134328,
 10.3687259137954,
 9.381184479678108,
 7.586409856962471,
 10.935909338156959,
 0.7672520811175987,
 -11.117154100587008,
 15.67158770513983,
 0.7123965808149493,
 16.09123870720224,
 -3.2125148660122536,
 -15.80453617924129,
 18.887725547713917,
 -18.782088760422997,
 -9.339355093613445,
 -3.673485292561761,
 -4.2630827769362405,
 0.8217800628444334,
 0.6950804847855874,
 -5.3872151066178935,
 4.842804739205463,
 17.98171164299888,
 0.8683180842748841,
 -32.30411158352564,
 -5.639381134905562,
 3.5229149564212623,
 -0.39154662738074264,
 -30.285031608498375,
 1.3170387450090832,
 0.288806900032746,
 -12.557836387422125,
 -11.158908848468181,
 -22.817320902092067,
 -19.834199295124666,
 8.08643111805269,
 -21.83575615835951,
 -4.573526810317661,
 0.5683077485868437,
 1.7774001480868462,
 -13.559265997574084,
 -1.2404308239609516,
 24.24279115826525,
 -13.930130057078644,
 -13.403184388797328,
 -4.937478261278786,
 17.458184158113713,
 -0.8214840502083394,
 25.240005024551266,
 0.8853684097547696,
 1.7525484248247378,
 -0.6819837579540133,
 -2.6236132862087755,
 23.56973421807975,
 -12.605138645061361,
 18.428865374058578,
 -8.642784831496632,
 -4.6940863048500905,
 16.38047661145901,
 4.21652237378484,
 -14.036047202528495,
 21.334308860284978,
 11.427830134214679,
 19.666505139646763,
 0.8814335069593751,
 -11.458345140747346,
 -15.86400092865279,
 -2.5917608420997427,
 19.315467028356306,
 12.030934565615611,
 15.50297701799157,
 -2.1858935083981184,
 -13.234233282458767,
 3.4773588152282615,
 16.097170045697794,
 -1.7791927666411285,
 -13.860817490147708,
 25.862731928444,
 -1.4166568394981265,
 5.46871757364986,
 7.350084879509667,
 6.693282380878174,
 5.6928060554664865,
 12.77247087122013,
 17.090393209364883,
 -2.271720468811992,
 -4.153483585826175,
 -7.342838449948068,
 -26.665753103201446,
 25.73973773943318,
 -8.814289173422308,
 11.207705525133678,
 -13.658650870860223,
 -16.734656367554958,
 17.06686368460629,
 14.93890299896106,
 11.105959109738004,
 -15.416573983114079,
 3.7487145166207414,
 -6.703766709074159,
 -12.356287249229139,
 6.318192666635085,
 -36.456936541273315,
 -15.935619173058146,
 10.371796862517476,
 4.814634831892609,
 -4.8500172924759415,
 5.333774916644571,
 -12.911088585828507,
 15.017420176411557,
 23.482092081286833,
 8.208027056701376,
 -3.0477758192483737,
 -0.5971555300227693,
 5.65599920584555,
 -3.468165802206965,
 3.7282458372845824,
 -9.617025726772969,
 -0.8980246407415098,
 -4.672520018084966,
 13.474558416669353,
 -17.79291945059376,
 14.800745892994803,
 11.322461662757453,
 -22.964163558353714,
 19.54526347929445,
 1.69366747171049,
 -12.304239468951922,
 -10.472956252221056,
 3.9591890030671673,
 -18.128071963523166,
 5.741352407509659,
 2.37431093246479,
 -9.704822727026189,
 -19.78834115756234,
 -31.02848362615276,
 -5.807420321118213,
 -10.678399622439715,
 1.3749775366599015,
 -2.3836771721304153,
 23.997694854118805,
 -8.223024157120262,
 -6.455670663812796,
 1.322634532598798,
 28.525367422046646,
 21.729750269620716,
 -7.0139132255144325,
 -24.61283188322079,
 5.784747035074286,
 13.949579603943793,
 3.437281912154905,
 9.678649735862624,
 -13.608671039189902,
 9.604173255155075,
 -1.2270023350710304,
 13.524334232536201,
 -16.012965794654132,
 -6.457173519822271,
 31.43304734981594,
 3.2237728127469163,
 1.8328164810080347,
 25.755892240064266,
 23.730831809163522,
 -6.802124627922499,
 -1.881564793088318,
 20.370034700779126,
 11.121122452554895,
 4.8633543195715045,
 -16.149070744202945,
 12.94241851068695,
 -15.771242847529583,
 26.195753608492,
 10.862629433791001,
 -10.058458685362377,
 -16.6515597852744,
 -0.4666956582075904,
 -40.26200085113415,
 -9.341925828203587,
 -23.679082239462712,
 23.268645876263452,
 -0.552690366688292,
 -18.41209754587881,
 19.861643615323803,
 3.8257287057747487,
 -0.6523540847939003,
 5.472107998985212,
 7.910232908242775,
 -6.688409880282434,
 17.336990736825395,
 28.56924565771771]
BIASES_LIST = [-4.35980641127524,
 3.2113654554538806,
 -1.362171629006559,
 6.861551486306797,
 27.69298362171371,
 -14.194317437102725,
 -11.195552591167107,
 -0.6144657733317487,
 -2.013575754064509,
 13.817783503092148,
 -13.689564888170068,
 5.856714829307036,
 -11.827441439080056,
 12.638424236516105,
 15.778272482086072,
 4.032306536960628,
 -14.394354069808614,
 6.737802498857678,
 2.3228515475727844,
 15.445571737039417]
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


