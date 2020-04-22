import random
import math

WEIGHT_LIST = [-7.6798732718964935,
 -11.72981993840543,
 -7.981563090734939,
 8.546644122828486,
 41.659505286158,
 -17.911436383684496,
 1.4172653412382576,
 -2.580470920028141,
 11.433095787989043,
 8.189042625550222,
 -9.19942819115689,
 22.02248125979733,
 17.387834137379723,
 5.046702334399683,
 -13.750389931057754,
 -29.964281287732444,
 8.420930596874264,
 -3.348652511615521,
 -1.2996416612843724,
 -20.50536142750687,
 4.5688821599574965,
 -39.306400795191344,
 -7.588371795603614,
 22.75982023864119,
 -7.6785316892561895,
 15.623119183573735,
 -3.002677672334654,
 5.00004490329302,
 -11.022847141783659,
 17.80686764512275,
 -16.06962731156269,
 -2.468097264081438,
 13.857037102166135,
 -5.564458082091268,
 -8.669474024229736,
 -5.6552613086146595,
 -5.165756857309822,
 7.1230145290281754,
 -19.318751962416567,
 -28.768350279496644,
 -26.980177820110903,
 24.67908103939488,
 -26.718754716589828,
 18.485461579922095,
 14.56320599390597,
 -12.234535550236368,
 -25.82963581521053,
 -10.26562674235996,
 -10.65331201748231,
 -2.9880576731552484,
 -15.188467394726324,
 18.173552960236247,
 -7.280919788254991,
 -41.752167389036224,
 -5.012717229429647,
 -27.858970748736816,
 -1.413431924825442,
 -6.188078397515112,
 -42.09009186508442,
 -8.101651458731258,
 -6.60684259623019,
 14.632181697509598,
 16.84305513678648,
 10.2359759384474,
 -36.756981444864834,
 12.611693878444225,
 10.701061735052548,
 -23.724099627396022,
 -3.9967541131884285,
 -6.4478423307007695,
 13.683788795822153,
 18.938264656733256,
 4.914053945877811,
 -16.016185895462723,
 -23.106360567341458,
 -3.747605299880224,
 15.81867914734599,
 21.314096628093147,
 -16.94163234516796,
 -27.123628090914067,
 -24.035437432256256,
 -3.3308947110845306,
 -14.755817216878903,
 -16.83971663037981,
 38.03920045902048,
 -1.5981171296693297,
 -16.9960112790262,
 8.875180187792644,
 5.8205443861982396,
 -11.53901053017384,
 -24.74273296762199,
 12.357540225788743,
 4.902871091586306,
 28.4891030231868,
 12.280223427475217,
 50.036294538157385,
 3.7308560442941925,
 26.939854461858495,
 5.182988877843954,
 -2.4876314320175954,
 -8.019703851873498,
 -22.899914525616012,
 9.023105979540066,
 -20.39731868942772,
 8.962705807017446,
 -30.15128309657057,
 -16.19542930939386,
 13.46631880158504,
 -11.444242177142025,
 -4.753660911831355,
 -28.82107648344119,
 -1.047707859679491,
 -0.46198014909813523,
 -9.673219937723601,
 6.839267096837766,
 5.985626311402445,
 18.250402288770864,
 27.136450585490103,
 -23.372896941175206,
 8.830115845591266,
 -10.844277037090103,
 4.378628130056519,
 15.246619752378692,
 12.735625610681627,
 7.879209062503644,
 16.79663270599692,
 9.66263327384846,
 15.439069170483457,
 6.708854772713426,
 -23.81628997411085,
 16.908206176744326,
 -1.0793553698635527,
 12.039060747810083,
 7.743242013199797,
 -20.810834890754744,
 25.865791264880087,
 -21.36283395513312,
 -12.050680277749644,
 -4.567712709742491,
 -20.920851401974723,
 5.114696782536182,
 -17.843880644775666,
 -0.799958935307373,
 23.307518062202845,
 20.441414549284296,
 16.12715274870152,
 -20.996176423570745,
 0.1793217275171095,
 7.633715527880945,
 0.7068999269607232,
 -36.401469423689115,
 -5.912970606430549,
 5.792604714951626,
 -0.16922382014577053,
 -2.5384279378266275,
 -13.25281249281744,
 -9.228432561158042,
 24.50216168125295,
 -16.884372747585196,
 -5.36115950370724,
 -5.131439203709424,
 -3.946878559190875,
 -15.18514644429459,
 8.446672684817507,
 22.414265145664444,
 -12.0368785627114,
 -14.535899280157068,
 -12.161348515876652,
 14.862867095375535,
 -0.869673470109813,
 17.412350887685708,
 12.659154122866585,
 21.197609999079212,
 3.4701529607526282,
 10.51760145788992,
 33.55840529230471,
 -0.901559672395118,
 -2.8061078600910765,
 1.856044325462392,
 -10.588783918550552,
 10.075868032831337,
 9.368592563071815,
 -25.68975344619618,
 28.13422453380761,
 15.982755735433827,
 40.59324624360814,
 1.9136665416160419,
 4.043338366377409,
 -10.445647252677329,
 8.407956000574469,
 9.23711555137513,
 5.11122278622328,
 5.227390888078414,
 -4.194215169363494,
 -5.6465375727394065,
 -8.070570403121227,
 29.147265676986805,
 17.594120896020673,
 -32.1789208289085,
 19.90264940438935,
 12.700947509457258,
 -3.7552507729524613,
 -0.027978517874519326,
 15.149656805900825,
 13.485857361624475,
 12.752318752514832,
 33.19486996551039,
 -8.474350370427578,
 4.232415415914794,
 -10.70487925349595,
 -17.28121144861534,
 21.34028012794913,
 9.386495373470524,
 1.9743343738270855,
 -12.811627834740172,
 -22.85828142358828,
 43.710814764517764,
 6.101756336600815,
 12.353409020098233,
 0.4419437072569963,
 -11.88985918425231,
 -8.982867980723965,
 -20.845860698467106,
 14.50661545651403,
 -28.706873938167934,
 -26.71430728455436,
 -2.2773796628753082,
 -1.8783027322350385,
 0.6882458524624955,
 10.647622077092166,
 -18.836621852105527,
 7.015849513304872,
 14.290868448947318,
 -2.4391889783108276,
 -7.842549217334591,
 8.94349014271613,
 16.528077373132625,
 -5.955897573933296,
 8.18372578547229,
 -8.262618628437682,
 12.884704842951834,
 -17.375264045378177,
 23.17564987186057,
 -22.64641298988484,
 9.522646126148334,
 12.170803991688096,
 -36.25656922110973,
 27.29342385422411,
 15.816012975506105,
 -7.676138507849345,
 -16.954005320742212,
 8.581064775635685,
 -4.18601377496552,
 13.467982033492824,
 -1.687058512597499,
 -5.140675537624849,
 -21.43964007195825,
 -18.310535934600537,
 4.693467137461866,
 -20.177981969412276,
 -11.23881962169294,
 -7.646285339007013,
 30.358793546903755,
 -26.305658788704836,
 0.7940154635894103,
 2.7812453111891973,
 30.05842446273182,
 14.381382498570652,
 4.681819562108256,
 -24.901599675470756,
 -11.457529357891108,
 11.940178742829495,
 -2.9564381606318726,
 2.852152543332789,
 -21.738851996449476,
 12.339164930969115,
 13.212507477647527,
 11.610947765209826,
 -21.198883932699857,
 -11.9013973014805,
 30.112131979523205,
 15.433457444105976,
 -0.658536481689751,
 36.6275576537041,
 22.15432863812253,
 -6.7173672235715705,
 2.863956906624516,
 16.805318712450394,
 5.832455225221327,
 -8.789000442115375,
 -37.78321865740341,
 4.754613316211,
 -18.692848596555766,
 31.215190953587687,
 10.160117062027776,
 -8.1119486697534,
 -24.151188367608164,
 14.241379907372952,
 -26.916183412286518,
 -11.656928376406544,
 -26.704235807062886,
 28.85687780842283,
 1.1115077727028968,
 -18.22380584953883,
 17.45129261344238,
 -0.9984179392106931,
 7.504894642003272,
 8.655566174220784,
 11.044814739639762,
 -21.429494486298804,
 2.329240514284688,
 37.465166305002455]
BIASES_LIST = [-14.738808338412893,
 12.825568252343665,
 -2.1998848856944093,
 10.40661429700285,
 18.19884768030738,
 -22.229192990961735,
 -7.963042180602555,
 13.672778680406772,
 -6.789112012501045,
 3.957208052151188,
 -26.102068005496083,
 6.121800206916333,
 -13.882853954486938,
 0.9358115012435011,
 18.149361977692156,
 2.3874207477990126,
 -15.538741543647285,
 11.404783275459813,
 8.016368851754876,
 -0.2071029889402105]
SHAPE = [27, 8, 8, 4]

IN_TRAINING = False

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


