import random
import math

WEIGHT_LIST = [2.808501134090097, -6.1565908631643, -3.981929188872561, -2.021072509340218, 2.493469434775747, -8.935337962246932, -6.73335052734833, 7.792139282443426, 4.052303982755445, 4.800528611365685, 9.554060646445308, 3.2262043499061033, -6.369981389310491, -0.342480152749836, 6.634653012056447, 2.0114261638385305, 3.5558433493580566, -5.0490602041043475, -2.318803504167537, -6.46638331642486, 7.274011254720843, -6.8170464467205445, 9.82335683566141, 9.773897435124294, -3.3159596815946397, -1.107926715997019, 0.6774661604193017, -9.197293215836401, 1.8714907843118382, -6.4384794145234325, 1.8790366857914584, -6.939281386507901, -8.355178440422645, 6.671659824189128, 6.650130624155544, -9.010432188673674, -5.141196643268455, -9.604527879004, -6.319724409209117, -1.0901655563853048, -5.8570105282398615, 3.32578092544556, 6.759577350783559, -7.95936506681219, 3.060268221235985, -0.5152143119487889, -9.669726101822604, 2.9037220789820655, -1.5829448265134882, -3.8326163761437755, -7.213610372050574, 0.33759796890437954, -9.306697528849533, 1.6878200045113818, 9.055729049203688, -9.30626617528036, -9.087898452272727, -9.740966835711163, 8.750352815265899, -1.120015712875528, 0.8077846574267351, 8.051848030803178, 6.588382100218862, -0.35479276593466835, -2.1820856762729886, 8.048169626155214, 1.8836833092994691, -3.6858330251264544, -8.67237472822356, -3.691488588006388, 7.580906135022506, 1.8728612134976341, -8.796551112461955, -8.690309099520197, 7.304874684367203, 7.518416766945272, 1.8907047317531926, 2.430837603571055, 8.098566233034305, 4.863776348313804, 5.392056221683845, -6.073548455443785, -1.299597386138112, 9.485969591697941, -9.875625323244302, -5.942262590949337, 3.145110878652755, -0.10325702415852511, 8.795534582944246, 4.75614629320474, 5.074210975601787, 6.5287336866744035, -6.749093409737359, 6.8166033616364174, 2.268929551936804, -3.739644965960771, 5.922652845042634, -2.9590009836242004, -4.92829515599996, -8.716968517929974, 3.25273643636228, -0.26804925149648007, 6.413076335852843, 6.435377121029493, -8.018685266655663, -0.3757654329801863, 0.94487453961227, -7.475421207745931, 0.2160445637962667, 4.850652246689503, -7.571838088765473, 1.3003068227405468, 6.803551464788409, 6.171940243854529, 0.04034633581193603, -0.22029069061878204, -9.538582776089122, -0.7289099424121463, -6.418738608580641, 2.6706786453917353, -1.809181056042764, 8.948284128682861, 0.5055955164278831, 8.347266749962063, 4.725120946486307, 3.8965646519864343, -6.605809261165105, -3.90437014443701, 2.562836595051687, 2.0406300647539393, 1.547450262102327, 6.857357511177661, 2.538979638611094, -1.145010500152111, 7.300244085191242, 4.881263372771883, -6.845314536205953, 1.3534029068573012, -4.693010837441669, 7.094187005011953, -2.459922914028027, 2.3364720979159763, 6.078356434985281, -5.781316659939309, 3.210228584723806, 7.809765870077239, -2.263020809206564, -7.474976917719605, 7.1041103700523145, 3.439070554772039, 2.6778767757033037, -0.20967268563064856, 5.868265469671597, -9.329090493219262, 1.2841999942852471, -6.871952410014586, 4.092465074977676, 0.8644703701952423, -4.67511122856749, -0.748968710916742, -4.521990908337818, -0.7547539543365183, 7.223885987579198, -0.9446214542747171, 3.780043831998814, 5.714226535261959, 5.24719656017454, -6.348830421680169, -5.082115752852996, -9.05811119789446, 1.3844660883834408, 9.394476335596764, -7.828617813585492, 1.4507419889814521, 5.503891320174901, 1.6415456221884366, 7.568222414075912, 6.385876566761237, -6.029892638933747, 2.8099776254230413, -5.7048782706470025, -4.641058840042125, 5.068714733526923, 2.2034360187472384, -6.192950772123802, 9.17255084234155, -9.216725925098562, -0.4816359695860086, 3.5037537676024595, -6.417965713705957, 5.513962616325854, -1.7307832409083836, 8.216702132256685, -8.645514497111781, -4.924937706527073, 2.836603388180148, -3.1587069822553593, -7.255660104591152, -2.733438592350133, -6.924192728483327, -2.0251050308327123, 7.485058418355933, -0.058366022716715094, -4.309335193204619, 8.926130715706918, -9.155969382532652, -2.248583099912997, -9.43781651323609, 8.87574140156132, 7.671272641820231, -5.145566581459313, -7.591080975778384, -5.690077117927932, -7.874789977094219, 4.547579731150595, -2.623041055213031, -0.785014454315661, 6.837106128078474, 3.619782752703067, -2.8052567379314546, 8.524820140367602, -3.9946899578054484, 4.87778544907928, 4.791367134396335, -4.68028051636729, -0.10593585294820507, 1.2581317686983944, -9.41848011004027, -4.884004073798403, 5.143977591831545, 8.671350648065609, -9.077101493811837, 4.439463170922904, 6.65253611200027, -8.57895848671038, 5.39790456012177, 0.10008018129532559, 5.23514673555815, -7.20534435993714, 6.100418046573537, 5.109078623898974, -2.120094318935786, 7.143364655035416, -1.358348575768014, -7.9618857725566965, 4.431452875604485, -3.36719356654795, 4.599221867347508, -6.905301725370501, -2.651372587458873, 2.2050175174512088, -7.835895817416585, -9.344838294031746, 1.6766059880998068, 4.079603423828413, 1.6478138020774438, 2.7374689512293937, -2.5775340828859754, 8.45271064325248, -6.484561616803612, 0.5585892613149213, 0.29461146377620295, 4.792663619856786, -3.8502990699287736, 0.2507509282267826, 0.2536861060061959, 3.3028766830693286, -6.026690678810073, -6.0842161049596255, 1.4280832218450712, 7.2471994472297325, -1.3029355042688344, 4.118336233963651, 1.6752013601562084, -3.9404892593728036, 9.882839014741108, 2.791572222855624, -7.389616608784162, -4.04754733307718, 9.771655955011997, 9.71604647799846, -7.3063146971993564, -4.392832870789379, 5.108875781208775, -3.984931498877944, -3.028124321616767, 1.2338748246021218, -6.625005641088125, 0.6661508627866404, 9.72106745633847, -3.1485947864375703, 4.327735387764038, 1.5717747380869582, 8.886793967857699, 5.42171190513243, -7.742504391787628, 8.13856276041578, 7.40876660466008, -4.210791797083553, -3.9999288956396706, 6.957076263000481, 7.687710007349459, -5.472680770556395, -0.09472082500543166, 4.110897695177105, 0.31726239052836647, 6.290886323744822, 0.933069723479532, 1.9874189342809974, 5.7442782171064515, 9.312241190490337, -5.3139468871727065, 6.158922405642322, 6.686567794804208, 5.137231775525514, -3.213643867138649, 7.121644512654488, 7.28518559929627, -6.7605460768915115, 6.561512336765343, 6.618200269160315, -4.076167853769714, -7.113268246764594, -2.1533808983372404, -1.7555031087437367, 2.780925439455091, -3.051828260293612, -6.861307407297388, -8.327926799421622, 3.8413616468655665, -6.311339344345523, -7.559660695859676, -9.81918998889224, -0.6852135988315098, -2.2294981374094007, 7.983258702701214, 4.761883715777673, -6.332583007599895, -8.122744378064688, 3.378558932858395, -9.601646416581636, -9.347980660435379, -6.731162274770142, -0.16840172419009924, 9.6234248057292, 5.236249308792409, 5.3389387961315435, -7.409738913608641, -2.416718720104929, -7.235324015236113, 2.638012315545172, 3.9921234236148724, 6.981451031639473, -2.568919501280032, -1.71276927204514, -5.372148940836345, 7.219500225305332, 5.773242047699664, -5.30555296793362, -9.656077259784542, 2.7356512281851373, 4.275506313499623, -9.736661297190697, 7.422702077584514, -9.310343375342033, 6.1150383380389, -4.138901338268923, -2.15150118224658, -9.97708593552699, 7.754889707981015, 1.7510691487520962, 1.186097131133712, -4.430910614363008, 2.139376948730458, -1.7439406165159355, 1.6856262296517954, -3.6132081194497108, -7.491520254153528, 5.29217272072146, 8.540905001872947, 2.902670980467219, -4.516941584169382, -4.192376338173576, -6.377904166226243, 3.0927518033961334, 0.11368626992051212, -7.362089587581737, 0.6552599984788721, 5.019576007255029, 0.9622988762003004, -1.9082095863624247, 0.928152154195125, -6.569725850238273, 5.77854147876543, 1.6392549487560508, 4.431333332022261, -8.0762456111456, -6.78006833351435, -2.56693529453657, -1.587170015639046, 8.595186733357988, 1.0744453697855825, 6.917909937432146, -8.892057010662226, -4.368481953378196, -7.616441236528737, -0.4835850825539101, 4.648268311976187, -4.618329669202355, 2.4285536174986184, -4.727755849150839, -7.475364430001825, -8.01155576431498, 6.71923094265156, -7.517775495330707, -7.91956147859686, 9.074447555500594, -2.7413776639102334, 5.749419110425077, 5.454413321837082, -8.986400203589914, -9.523539255008359, -4.591442742988219, 6.743080115122574, 9.343759259350431, -5.342674489663068, -9.446187253785919, 5.520431067788913, 8.23108440153004, 5.046372483428591, -4.775993146863231, 8.797995954550991, 6.211204136104239, 8.540178570851005, 0.8413688472769465, 4.632946622421379, -7.476119298363628, 7.983963083083275, 3.1505355009244536, 9.679806542836829, -8.81974382115525, 7.444026288298463, 9.71131716214348, 6.833629289454258, 9.701819650208503, -3.4913505855079308, -2.1500930659921806, 2.3476392715916, -1.830702389672771, 6.780158829815765, -3.6011768762642005, 1.9028839239231594, 3.1623870524334574, 0.09919156012273156, 3.6632756471458983, 8.590920947138027, 3.930439691102075, 5.542090346138339, 8.958010711455163, 7.884781680914866, -4.750923776740619, 2.5618605412431954, -2.958305704471808, -4.804976152791188, 8.83963161843041, -8.663696412278838, 5.58690816400431, 5.958496879918748, 0.39803144827154924, -9.9943215535285, -9.16859001800244, 7.204359599649852, 5.654249455883445, 9.263143747586543, 3.6094821310361382, 3.1473388069281256, -4.405373851681373, 7.865045375389315, -4.583233591763928, 2.4243927160529957, -3.3454622463366253, -9.872583634204751, -6.761942396500151, 3.128583476441129, 0.2810140540886046, -3.8646331916154626, -0.8649272499687015, 9.919289665240708, 4.479324337125037, -9.082941016774992, 9.3873339908709, 6.394059663985992, -8.11169126324279, 7.60393870476468, -5.4919177156138925, 5.305149516895874, 9.785302439596766, -3.3167374125594957, 7.270100973643267, 6.271101867649499, 0.10609911316646148, -9.344694084209614, -5.0308462820557125, 6.796827032736985, -6.550626623692022, -0.7842278281954549, 7.989591334592848, 7.008741175541569, 5.382892355263687, -1.2726920192692432, 2.9224785001860525, -6.069753324268015, -4.4744696644740785, -2.376929680187625, -1.5540955631519555, -0.4302464044156409, -2.319323273394323, -2.1609912528056103, -7.259892806311301, -3.2540887914436283, 2.3719115377360556, 3.650109405373623, -0.4748827961949722, -9.458443395461787, 9.362399353173899, 8.403811779557206, -2.8807405734186613, 2.548777261553594, 6.10664075384755, -4.881770295018142, -3.276468906947856, -8.920983225106436, 9.81711563108945, -7.434810752285235, 8.418152927168205, -7.178514830273892, 6.4009403956165265, 5.55654061462903, 6.002682584054082, 9.890913560767146, -0.5152958958980474, -1.8391604130513723, -0.5965346333471935, -5.6729299554714085, -1.1321085352935771, 2.8481337135298297, 1.742254482871747, 4.457296381302687, -2.6312242676709463, -9.411146921968726, -9.590176174024725, 3.6149360282106517, -9.897523435780549, -5.692881109029639, 8.427442820910429, 1.3327990429550454, 1.3865815305775282, 0.03350843722899022, -5.893557471067745, 8.707041680693766, 5.528944850108433, 7.008425400249656, 1.4095614734890187, -3.6499244337086667, 1.6463159975215635, 2.758144556240442, 2.2297454437522735, -9.188196949631742, 1.2739988689091248, -8.048696711861393, 3.2847203805291354, 6.1957181708815305, -7.267951402651014, -4.562206547098788, -1.1819319078135848, -4.988214950027244, -4.88739148998135, -7.987425400115999, 5.519041132287306, -2.44959858171158, 5.843789925646739, -8.433068041783024, 3.8519030910895964, 6.265089995268347, -5.310711833915431, 7.576501432316892, -2.976532458312777, -2.6305128410101997, -8.475962223701895, 2.6402221634220346, 4.850173599422353, 8.444062237333412, -4.367353409806338, -5.562249169902498, -3.5186409316579903, 9.627451462154998, -2.297544189759126, 3.3825781111057918, 3.6022206044907783, -0.5050149292309491, -7.005715471962565, 8.92056568631299, -5.7824493174222376, -0.9521081338201913, 4.335384878749345, -4.143290121711887, 7.797812801787881, -6.633075506461969, -1.4825745670497916, 5.786396369542723, -0.7519772585158329, -2.5657250007001604]
BIASES_LIST = [-6.833886836249629, -4.478880081962659, 7.313710543139386, -2.1937100106086493, 4.353060853981091, -9.600773541934739, 1.0324069667533244, 7.600209685929784, -0.10912212137980326, -4.310066160526585, -0.9052463430492903, 6.125751841693635, 3.9894706437731813, 7.62485026684972, 2.5714195046563315, 4.670718039934361, -3.67562505519639, 6.865241945400776, 8.948268079655087, -4.189313986267004, -4.927761312632299, 2.852214990533259, -6.784537082925597, -4.248038353499921, 9.757998166104482, 2.8297206000746122, -5.2437817439389, -7.464645575965996]
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

