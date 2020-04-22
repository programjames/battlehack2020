import random
import math

WEIGHT_LIST = [-8.169498841186089, -2.694507313150583, 7.373521675745437, -0.6754182754539704, 4.050768403880675, 1.9551109266469275, 0.3026855347581591, -7.075778034963386, -9.162355102832034, -1.2605758459337129, -0.2985149150770071, -1.909253535441102, -0.17849552859237153, 2.0208631455378527, 0.7235469789584295, 4.256144159055314, 5.315484428694559, -5.180989286819323, -1.0963316641203678, -0.24794307719578837, 4.17200520701456, -1.0810728874162874, -3.321567047915288, 5.833704272654723, 1.8683064054462477, 4.820591892580301, 0.7815214220615969, 1.1931381265103336, 1.2265272102601965, 4.186037240804873, 3.8591627172589678, 5.29798098182737, 1.3084185998185511, 5.5378910554812535, -2.031506229571585, -7.308217061834873, -4.252538638124948, -4.955092405695929, -4.088848696212744, -1.4855289812415577, 1.7290481227976804, 4.610073683901344, 4.128102345817835, -2.306181872877374, -0.4743348965011862, 8.83814135322379, -0.23685122236192407, 1.1431258619096687, 3.1314807211475575, -0.5954207573680184, -1.1045751037888432, -5.803892552047845, 1.0222591496003324, -5.0988104036807735, 0.4104493831781055, -5.825134878590428, 7.859189436117988, 0.5373736548358488, 3.8066468932742583, -0.29740466668933835, 4.622820681744781, 1.8105891979032465, -5.138547995509883, -3.420943144687753, 1.3504312719615887, 3.3705436676001495, -1.2587331600320228, -1.8381086598274887, -1.2569950025583396, 6.222734458525605, -3.1529863124163415, -2.2461640409943855, -2.32301856086666, 5.075777483541095, -1.5702106854111022, -2.6614434389044788, -1.4850196133602342, 0.07127449874522712, -5.636803224382601, 6.273248077724167, -3.0111540554665366, 5.149348379899198, 6.273298894033303, 3.655715286704361, -7.226567726504882, -1.717791755133628, -5.813060001415365, -1.8326529760291794, -1.0517180245996618, 8.034267977702607, 7.559725718594359, 3.4064157631002434, 1.0660298589129154, -2.409571380068042, 2.670247389838382, -2.151551588504029, 2.4652762318294514, 1.185102173488021, 6.02012092094105, 2.0009606956819286, -1.3064728738101001, -6.535658600626293, 5.907780500975916, 4.501823673309853, 4.7091661548307835, 1.9759114690661979, 2.5207154335337365, 5.217702496005188, -4.974729745746807, 3.871458626043521, -6.817651337141607, -3.1631264681387354, 3.445545755225717, -2.799556768722154, 5.733028932285325, -2.560493692075041, -9.863754883377169, -1.7222591811339507, -4.640128241956069, -2.5519263360090902, 3.2033110814694976, 0.4957811105709283, 7.768372790198099, 0.27871650461383174, 2.2856599037858834, 0.08898653848770549, -3.0720679880105455, -2.8857639983064964, 1.0125988370145023, 1.7883736826637366, -5.129024837615077, -9.266555847343923, 1.6637595373679728, 6.538656098704652, -4.565472933828768, -1.7486872615660851, 3.89747815500912, -1.1125960397235286, -3.590312123681168, -0.05533065836160467, 2.3395558848021927, -2.6118272168846266, -6.793917501259923, 6.849891040085273, 7.378307419926294, -1.7360810152446697, -2.4149035940492385, 8.152494492452837, -2.5951963038259636, 2.3378942010929564, 1.5066009231205608, -3.6789710721460547, -6.804685795416768, 0.8547306321712267, 1.354435628087061, 0.6181758395640888, -4.2998654710411826, -7.147094271356418, -5.638697929316682, -1.3756822247149376, -5.001863803842594, -4.204933144623513, -3.3645710550864067, -6.526133731093854, -5.562834166231167, 6.587386588299462, 2.1853866818722096, -0.07196183458762934, 0.052740013485337245, 1.2980536896389927, 2.9152449238605924, -0.32801672338561777, 1.7304840693487724, -3.0387776107975104, -3.34083318901546, 2.1152333948696778, 1.3518692592309376, -6.586039629960406, -4.574651251302302, 1.8038209794949074, -8.305692397093328, 8.921969390288128, 3.316613019205278, -5.664521521877117, -3.9320248046251085, -0.4366754560575871, 5.533542085586457, -5.270997633453883, -5.251350055390567, 6.928670344020944, -4.804464606019323, -4.973230887095073, 4.63175082669984, 2.5748863608221453, -5.408890120874488, -5.205179805033003, 7.016900605901564, 4.310299438724788, -0.1973059010569753, 7.008302880203513, -5.569051284541827, -4.55842286540989, 6.188437753985011, 1.1726384410030029, -0.3545179208435213, 2.7428675965574025, 3.2810131466385224, -0.4444024399359368, -7.055885875169766, 7.246753252658895, -7.291519330712376, -1.8830949601030422, 1.4087987564103346, 6.781494441909829, 6.110802849449521, 5.742782543636929, -0.7404312716262738, -1.5826784854626315, -2.6579535499347062, 0.49268190442616727, -2.474725753203193, -2.3324140531996003, 0.5332120497519803, -1.6423001265553818, -4.377931674409823, 6.427998333958467, -1.096179964697498, -1.5233948567634399, -3.950206165686496, 2.5768907297742634, 2.284177593082681, 0.7774898714725118, 5.873531172012066, 3.439004399032219, 4.069238896200483, 0.6701825449656242, 5.398702456724927, -5.783119972586046, -2.9518287391626035, -5.267512291690519, -6.187442385306667, 7.368242051543441, -7.014662677698114, 1.3276856843231093, 0.33373058143339923, -3.258854587202448, -0.2704235318399851, 4.226227721313816, -4.38906105233743, -7.579789175992704, 1.9231474613443367, 1.494652299377728, -4.835533492215523, 6.565093770728765, -1.3319142667018624, 1.816177773042336, -1.1018092798974353, -4.064266067181234, 6.409826234448129, -3.8447244480048606, 5.781015490814585, -4.064744390171798, 2.5780129172175825, -1.4310241388066038, -5.036447992199914, 4.645536889434648, -2.5777135582599295, 0.6642005939792703, -8.281128591798574, 6.811020982458512, 3.281805691989401, -9.691601358191141, 1.655643061705681, -6.343583714046308, -0.43791433116978773, -0.005267445512213087, 5.403300661855112, -4.350851099463972, -0.8967445683627879, 2.5675288324625414, -1.1259594097335288, 3.9971164979762057, -5.981916409596638, 2.548819094179469, 3.0742532485015874, 1.6736822794286934, 2.165135362526348, -6.422811367288696, 10.298989672325995, 9.121104759276303, 0.5732613979139942, -3.4063629811639218, 6.14804182453965, -0.8424678444533296, -0.7410216730788135, -5.9193380072234225, -1.2745951429858302, 0.3858425949425813, 4.902672662485926, 2.696878670939816, -1.4250531678533658, 0.20948918936562094, 4.909166111480983, 0.07316581032905872, -2.0279397546428584, -7.330743609052327, 2.127555747762448, -3.8138468629044486, 1.5034994980269702, 3.9030187504319103, -2.53446824169732, -2.1341205677899184, -8.217315921991785, -3.675827294912847, 7.666001858050642, 5.404063642560632, -3.36902962059088, 4.28469504895521, 0.9986385588303426, 3.4980372047570665, -3.32716508905015, 2.4401620049877644, -3.1941474176535034, 5.90324109311876, 1.8449018815662686, -0.27675897090883056, 0.8235908213517269, 3.4983660240186594, -7.920435506662515, -0.5162447506588299, -3.5528049773194534, -6.7470333223061045, -0.6853535084461522, -3.9842343452309117, 2.7353033389218555, 4.933495375973619, -1.4178098447056833, -6.975198269205871, 5.2582529958699435, 3.338758918951363, -2.2509833295241575, -5.505300304440439, -4.528569405297905, -3.626066185392736, -1.9081345602519164, 7.211635664981337, -3.7139191786257104, -6.985366487623982, 1.9865949565324228, 8.841568966341457, 8.970169330296953, -8.928264303472094, -6.994635569697296, 2.92749643290342, 8.166644104256997, -3.0313014153920683, 2.4617348785998856, 7.541050202935762, 6.287238455085013, -2.4304628861552287, 7.111980396655693, -4.11185605948843, -1.1593770184168095, 1.711505072444284, -1.0747846750574286, 2.752954478096035, -5.57237098103043, -5.774165083637974, -2.1564168658276452, 2.2742955649173493, 7.528039818576079, 4.273054826451435, -0.005416175008135626, 4.025076955791037, -0.18268577134972938, -2.4067750445100744, -4.985722137247339, -0.885242389427638, -1.8143394168051643, 5.420734236897303, 2.1359470864459773, 3.038913086959839, 4.141261385281093, 3.1781937303819467, -3.2269699450376184, 2.1144710262669864, 6.401538173661227, 3.3594443668682237, 0.574459029294901, 2.346585719971528, 0.4866808487655793, -3.3418067061309324, -1.2536464810655623, -3.495866094531367, 1.481495481099182, 1.7026324292455992, -0.23190985908562656, 1.3210790047403747, 3.025705156588204, -2.861125919377256, -6.170922975471438, 3.1937521734827317, -5.639105153461083, 6.558959346435706, -0.008523059539270461, 1.1480506745612784, -3.431538613245305, 0.5014970445294757, 2.489589916198163, 2.9956965033094773, 3.2197757441885875, 3.214295777651904, 3.543246654390961, 0.23317546618331253, -2.0926309465480983, -2.730512113548407, -2.782989242024402, 0.1350067405478989, 1.4106054815599247, -1.2474638639105862, 0.5609830111002656, 3.3400658262095972, 3.800938070415905, 2.060336081608963, 1.313816929698936, -4.645800662531883, 9.34254629964157, -3.430086659526855, 4.8703769062186, 3.919775468535723, -0.49330735430566025, 4.756707174614048, 0.46352493971983305, 2.996467047579056, 0.615582968821542, 3.6052308867144722, -1.367638377322017, -1.181213688515545, -6.365009753575922, -7.980872701255264, 0.9855636427606154, -3.6725270938097885, 1.7077564669219174, 1.643490576412729, 0.5699810660121387, 6.841098498137984, 7.52330805109757, 2.8779134996958353, -5.955171243627328, 1.4718780054293412, 5.373974630050908, -3.5928633492509374, 2.7381710887826336, 2.0073327178806886, 5.9403477493512264, -0.34648872333928527, -4.2152302640453, 6.776591197353261, 0.3581988077467601, 3.872325749216556, -2.7007735362645358, -3.491449043887116, 0.9393331991315053, 0.7301751322906305, 3.356537195932553, -4.350151797434483, 5.39765413845205, 5.825153569165111, -3.276779104328902, -7.990824704044195, 4.999417321948453, -1.3219958404345535, 6.750846850069381, -0.23162292314439598, 1.3261234624538438, -9.264192683945623, -4.3301423956368446, -0.8712636314915383, -1.4490928151328841, -0.5608204983598533, -6.876909676123279, -1.2410631497749247, 7.89080757129014, 8.185047759866087, 0.3883462436401312, -1.3378981721004186, -1.5307921009304006, 5.385687196733759, -4.086929673414236, -2.3761046697610175, 4.517843180665666, 0.9525598315568651, -2.993079601101311, 5.175524591270377, 1.8006172828688993, -1.0427614913795553, -1.2319297215707066, 1.9327071338540898, 3.247751939340362, 3.368778418414625, -3.072351077428213, -0.4338294738349179, -2.5171775661204734, 7.110930297034873, 3.0835926272755003, -3.0987394936710095, 5.063144592827744, -1.7484192222035941, -0.25866778712535754, -1.8229690205023685, 1.9663517292836592, 0.1568106767066278, 3.6505661253716335, -7.142466033589631, -1.2450504443993253, 0.4205207429033206, -3.949044033435924, -2.0415633421532267, 0.6170733158474933, 2.6922381794270627, 4.14278515557523, 6.168002410523766, 2.482831847386576, -4.7433872491276325, -2.7319372623359848, -7.5552673450499555, -0.0691475512086071, -4.250145732505587, -1.113414167190462, -2.9836841805238126, 4.362193890387473, -3.412219622042849, -6.865956362406587, -2.872175440512495, -3.843923763599238, -0.02809995726981737, 1.8242869935592307, -1.7351871027587984, 2.5978793788325762, 0.8382457854333687, 6.805747418819301, -0.8547387493836542, 4.496523771184852, -3.5659349617112204, 0.23897858413002143, 1.5579978433075272, -8.206864519168576, -8.122763967481804, -8.370422054482653, 5.937719971476188, 3.991284829693831, 2.119672296563046, -0.3960157754110259, 1.1914723429958787, -0.08118113487233, 0.9864262798599062, -2.5690154379592225, 3.6382133629210336, 3.7877519551648047, 2.7483630378062704, -4.795832225318669, 0.3132475932065499, -7.024257654414416, -0.6559989389833605, -0.6941931526592517, -3.1107337439893388, -8.048155923744055, -0.8214573116948716, -3.072905497525567, 1.9718936594087237, -5.422900538495514, -0.41140543312575145, 0.4574765268169086, 1.6614916778489386, -6.785595483507226, 3.0347199726022396, 3.7259675702379473, 6.446040419653163, -5.893950463530971, 2.461544328874844, -2.2112168902945606, -4.818983724084966, 0.615844050628445, 3.438628129193658, -1.8790398485117652, -0.17097463895663162, 3.6594593404347724, -0.36609525627179834, -0.9996651209742791, 3.934202722959189, -4.966834355445723, 1.6527705886635216, -1.1206317520982383, 1.2326591380859429, -5.089963823523555, -2.1707052773748075, 1.9415772252171641, -0.44709433761716894, 1.475313165918541, 8.974131682314454, -3.597582912060438, -10.177282526479104, 0.7541546346643502, -1.3122102996290856, -1.3245538864035855, 5.361852293050023, -4.64251580974001, -2.566010324152141, -1.555364709233471, 1.654076264218186, -4.186030391148435, -2.7728007300751907]
BIASES_LIST = [3.7638002536390993, 2.1754074721397023, 7.125409406053298, 2.030559840010906, 1.4113928449994335, -3.7775197946852734, -6.852794685707607, 2.305286832327456, 5.445700441353072, -1.0612978557955985, 6.0275857277279545, -6.769458813361116, -1.8491372523568472, -2.3773694975545148, -1.0851009207123237, -1.0435602920856977, -3.3822609657531326, -1.4485004673977933, 0.11600230657161437, -3.5336926734424146, 6.401267653056224, 3.257284945566052, -4.022629348829177, 0.8211133724290001, 5.457970186422728, -7.833082779728059, -1.8282179774981724, -5.956999776236118]
SHAPE = [27, 16, 10, 2]

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
        return sum(a*b for a,b in zip(x,y))

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

def list_to_weights(lis, shape=[27, 16, 10, 2]):
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

def list_to_biases(lis, shape=[27, 16, 10, 2]):
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

    inputs = flatten(board) + [row/board_size, col/board_size]
    results = nn.compute(inputs)
    best_move = 0
    val = 0
    for i, v in enumerate(results):
        if v >= val:
            val = v
            best_move = i

    if best_move == 1:
        if board[3][2] == 0:
            move_forward()
        return
    if board[3][1] == -1:
        capture(row + forward, col - 1)
        return
    if board[3][3] == -1:
        capture(row + forward, col + 1)
        return
    return

def overlord_turn():
    board_size = get_board_size()
    team = get_team()
    board = get_board()
    board = [[0 if not x else 1 if x == team else -1 for x in row] for row in board]
    cols = [0 for i in range(board_size)]
    for row in board:
        for i,x in enumerate(row):
            cols[i] = cols[i] + x
            if i > 0:
                cols[i-1] = cols[i-1] + x/2
            if i < board_size - 1:
                cols[i+1] = cols[i+1] + x/2
    m = 10000
    index = [0]
    spawn_row = 0 if team == Team.WHITE else board_size - 1
    found = False
    for i in range(board_size):
        if not check_space(spawn_row, i):
            if cols[i] < m:
                found = True
                m = cols[i]
                index = [i]
            elif cols[i] == m:
                index.append(i)
    if found:
        spawn(spawn_row, random.choice(index))

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

