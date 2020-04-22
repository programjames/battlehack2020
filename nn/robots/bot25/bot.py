import random
import math

WEIGHT_LIST = [-6.002694540336114, 0.8920894041254392, -5.673651703549753, 3.5424648790535933, 1.5410574715433878, 0.4941690747393661, 0.4904758761040391, -4.894785518019926, -5.871792053417984, -2.464230681642759, -5.680983624097613, -8.909043902377258, 0.9353048523230321, -0.21331682749899628, -2.131943617455807, -0.35935103193486206, 4.1537543522151115, 4.015410101801486, 6.698924053292281, -5.130573126796061, -9.718453442190384, 1.565570308136925, -8.061967394059677, 8.290290019812645, 5.702775267973134, 4.711892141827514, -7.616066046092403, 6.4797835589520965, 1.2503570590730817, -6.101423609470579, -7.980942740228563, 3.958180562435654, 3.7179594754483407, -2.429783672907475, 6.1873925141533945, -1.9096736554499731, 1.658574959791487, -0.8645145864973003, 5.012091970518032, 8.818411739546299, -6.087154793838236, -8.927202547640302, 5.151215426382535, 4.033946107999354, -8.690057175772573, 1.605564042672686, 6.027628880655989, 0.47392552748663874, 5.070200491400183, -4.500866739199967, 3.6850193563905, 9.626842938898857, -5.733762121690482, 4.358596931692418, -0.3903305626325082, 5.661171742865346, 9.852537906494106, -0.2321708511186582, 8.53352221270892, -4.439302159357743, 2.4436520152089614, -3.5959109867091232, -8.60766814934951, 8.854352116614447, 1.1598487056267075, -0.16442353697050827, 8.515478195005837, 4.911748378527292, -4.543806922663636, 3.864283595377877, 0.7397457079754126, -7.326165259684703, 5.936336251235566, -7.131218066840887, -7.010791273786319, 0.15514241771985127, -6.837430147837051, -9.381420310174729, 0.5270328340722781, 1.3637657730364978, 4.412655325938298, 1.3702379477007014, -8.23268393491407, -8.575918035506414, 2.7298001745164395, -5.554780114032402, -7.985209274690508, 6.130688846524098, -5.07893894093508, -3.4300071908740275, -6.02604789514203, -9.504878827811186, 0.24879688195923677, -3.611972208022822, -7.77258505717545, -4.368707013922224, -6.84618394641247, -7.051729362825601, -9.707558766570383, 1.7702630448505623, 9.418399697356609, -2.3142778109289264, -4.900627961805579, -2.9332110024459856, -9.681181679437184, -1.4299407146265644, -3.629767492376976, 1.0170012362775953, -5.119993232996649, 6.3883036392660095, -7.010086990922185, 8.722353844929884, -6.451097318871928, -6.612198961479201, -9.51522240009277, 6.760234140273347, -4.069506190946591, -3.2389177134892178, 4.857277232787293, 1.4455684240757236, -7.063715293130306, 0.09353367460531992, -5.202166431726001, 7.3254592454004595, 1.8800102683617546, -7.981803979378929, -6.8867348913022175, -4.807956264701443, 6.744528684201757, 1.093350000332677, 0.8802846598954535, -3.5632462729541174, 3.4071276596624482, -7.201403682507319, 6.395664004887827, -4.9441364174221665, -9.180232200549874, -8.343334543118974, 5.172912766497106, -9.583477648943193, -0.4546331061322455, -9.263070558698338, -1.7821153399133767, -9.643387735924343, -8.028796234201913, 7.664308321282132, -9.172135821265188, 3.861324465818388, 2.0936249938526608, 9.450071372816556, -1.7120861839608459, 8.87499363089935, 2.960009620465687, -9.630571274397767, 1.5981567698290267, -0.08308551418438448, 7.96468325605445, -0.10980111918921054, -1.1560387680681394, 1.5995185103872984, 4.797467640150138, 6.38805071708936, -3.296249496566337, -8.45917654839342, -1.2033847869583987, 3.854421683166967, 2.0428876660971955, -5.493013679083525, -5.430107937205468, -7.97265708849475, 5.408066680344222, -9.676505621561457, -8.842168250747111, 9.53162016405092, 9.914205407384301, -5.135227869188174, 3.688534199790716, -5.551910476977291, 5.4134618875309926, -4.687877166656788, -2.9464802961557908, -9.812494975337554, -7.43617302950341, -4.674301726522108, -6.441242783200838, 1.8363228483715481, -1.3639516909337974, 7.0268928165393945, -7.292037677515648, 7.61855485998797, -4.031024936357637, 1.3921957784160615, -6.143785460435389, -8.25926787138713, -6.80458455995089, 6.678365237558449, -0.24665600057008952, -1.9136415107374294, 9.676708410796344, 1.6896844186248021, 3.6055655971880807, 7.078201183484168, 5.144918935094939, -8.239389076212118, 0.6501992951702213, -8.447101276306725, 1.7891114239772143, 0.6340336887772491, 0.9211242739302996, 5.131023944958244, -6.924587128660422, 2.9785322112916184, 8.830461885392808, -0.4228867631019746, -1.1546305649073432, 7.55413500391526, -0.010071692050900083, 8.655168083619959, -6.677474411725561, 0.6617732323680592, -9.437061035181348, -4.221303415194802, 1.7246522873810868, -5.280912667699265, -8.415916432235695, 1.7180336427545395, 5.080818352506071, -5.915665848209257, 5.451959656657667, -3.504642341629804, 4.974489654860122, 9.070849589729757, -1.5828784673995155, 3.1291735962373757, -0.48879599252997785, -3.488503018844935, -7.537230010830673, 7.164084942036798, 8.781131608636205, 3.1188101347023345, 6.760935659477319, 6.026862318212917, -0.9596264726985311, 3.636226580801921, 1.6599736802681235, -2.382681273414806, -1.3653420197020552, -7.1206190102920885, 4.452704915182444, -5.794527923723656, -2.2583635114559986, 5.573436524089537, -4.593035275555937, -2.539052349186255, 8.441781070663176, -8.66176796506937, -7.4734461266763486, -6.921537836480285, 7.479970760008737, 2.3003729752537296, -4.6661024537724005, 7.613897432712424, 0.2311640916263098, 9.331033257317024, -6.93404296667609, -8.194906009930607, -5.112285520730058, -7.906136847480729, 3.6233199580599162, -5.884735367142408, 1.8942842863683396, 5.022423217932278, -5.492023485903799, -1.5483734031766065, 0.31714120550677904, -8.814404363758827, -4.318322800587248, -9.77462044240414, -2.2108032837800318, -3.848570267235802, 7.695075063594782, 8.323286140625846, -1.1880540154738188, 9.714458738562378, -9.681948016975152, 0.7118286519776689, 9.565653454140833, -7.538556947568424, -5.766347816519161, 3.6124492170617106, 9.296651796005712, -5.7626195523124, -9.846962963527481, 3.060681631405288, -0.11218263698307318, -4.558948938511554, -3.9739574393144146, 4.129355103995474, -3.50498919116297, 7.614772593502185, 2.2086396801057173, 4.955364016492478, -6.196773892122575, 9.983481869071955, -4.133593851120163, 0.16497473019007458, -3.0725426842466312, 7.297900270067014, -0.5962744946236942, 5.14074474516873, 2.99143848075056, -0.776106684596165, -5.2347370632771995, -1.0378398544322245, 5.688257737729893, 1.637581023967238, -1.1192666811338103, -9.749520489486773, -1.0241326975346539, -2.7894240001390607, 1.9786552646171032, 6.154405316669447, 8.705401553100906, 1.6304839988125543, 8.000806461300293, 5.370908289100473, -4.77353662518089, 1.550514246980688, -9.120956317914493, 1.2500434096499724, -7.998441265066029, -3.6015456957029386, -3.8795506774944926, -4.407925593333484, -5.866675347524948, 9.705098856909878, 7.153163956118952, 3.2790566903627365, -2.6894150509562076, 9.791677557481695, -0.04954244710875422, -1.30429072916629, -2.9870553375982016, -1.3553349416945633, -8.417393991969302, -2.5126609137024003, -5.022640944481629, -9.947506180920207, 9.812523352225288, -6.627614148056297, -1.6533347890184977, -6.216872327117673, 6.176885228510024, -2.2242740114549413, 1.1604109703433085, 2.956002769003911, 9.692474359169225, 1.2668445246908604, 3.520757974619876, -3.840405663215341, 6.327684416996561, -8.096820389431027, 6.787182456541142, 7.187431080935827, 0.5455025186626887, -6.563932395592644, -7.297209426610571, 3.8665200740492622, -1.7509512846119293, 4.042928243858615, 2.9111789201079734, 7.723750561015024, -4.578675413810673, 5.7572805339029, 4.629686479897616, 2.6586907171776417, 1.384853900218907, -5.743485979605807, -7.969547868916136, -9.550979507612464, -1.8679515356829057, -4.8457382491131185, -5.330049829371033, 3.386679994295152, 2.2990988206033656, 1.709226847535012, -3.5472034709904072, 0.14797985135344582, 1.2870404818954135, 9.13081307744719, -4.595962050633656, -2.929217114734646, 0.4230047721559451, 0.004672173016036396, -5.402256403397844, -4.878585431385005, -3.4246404645830486, -7.989903161637308, -6.307619163320783, -3.6637450306652797, -6.967499592158317, -4.188559641495688, -8.164329738350457, 1.5357931033884835, -7.271486210083338, -5.021824591190285, 4.841128385593711, 9.426126412337663, 2.190347939167932, 1.4224154634746924, 2.738790975875391, -4.513393023537513, -2.9849995586554083, 2.738940110444119, 7.242662611069118, 0.720819660210184, 8.717025159372433, -1.7650300672041137, -0.7650393340768815, -8.705685142145247, -1.830500461075836, 3.944566137349989, 7.34848971799725, 2.9550564802120682, -6.37499198995144, 7.508472860968563, 6.075301032521889, -8.216655734008231, -5.797792843461449, 0.14769696636829366, -7.983585471373429, -9.544756444496032, 8.76297991227592, 7.4836800154006085, 1.5239119553566738, 4.377744356618344, 3.3400826866687527, -2.5047788620084095, -6.308414071321349, 6.56428544860692, -7.183567009450447, 7.92555116407846, -5.768782731645786, 0.4579352581863496, -3.6152172422669393, -1.7624909258785486, -3.109344967681351, 2.921315226347474, 7.730000998415608, 0.2744628974401273, 1.3805080661720321, -1.6094466815882775, 2.7224765210135686, 0.6763868764956111, -3.8492625639177476, 6.903912144725954, 4.389851183321449, -0.572036368720763, -6.602660014676262, 3.891071326252792, 5.586643971755908, -0.089846894044177, 4.040912896795682, -0.6977716256180617, -9.932449123443538, 0.8231368582364667, 7.564244854324759, -2.5162479537736875, 7.599442915194636, 3.5842628954188562, -8.64638277991995, -9.610059654020906, -0.36540769685131735, -8.209836766445244, 1.1425823874360006, -4.513184786991995, -6.999276808033878, -8.694751512365045, 3.082734626046504, -2.2020579766838004, -4.849507791323717, 0.5611601055902042, -3.348669380640443, -5.226220535485854, -9.84704425921663, 1.5085605245885425, 0.2914143355966594, -4.343648063287267, 2.088461621960409, -0.12605783335146548, 1.1770894351519061, -6.0603941180978165, -9.715404590477837, -0.7516507240548531, -5.089542901348252, 1.0040277374652273, 3.3104255534344063, 5.409193161569096, -8.122109211504021, 8.117217961345279, -7.551232583526939, 7.4430950247159835, -4.9344547454872645, -1.4239739406237035, 7.928793497381545, 8.871351806043663, 5.121770581574216, 3.312785941743819, -7.0386211263069365, -7.670194027421529, -0.9321022594751422, -6.5994030266701875, 2.3964010552941133, 3.004309330096266, -9.896756919876069, -9.839650931950183, 4.836647202315387, 1.5665427732581882, -5.424949048464159, -7.343283773108822, 7.7143750967270535, -3.139512198436827, -6.391110530590192, 1.957645989272514, 9.25098797272376, -1.057321004161988, 7.984484278268106, 7.2079173511008285, -4.5939151781804615, 8.678064688560308, 0.6715823166472177, 0.06089965809097464, -7.08768939375889, 4.211586950649886, 9.008283159719873, -2.138275191582741, -4.051296481731798, -8.074233242761206, 7.910075903880159, -8.699752073820834, -4.328696745412146, 5.713875100292272, 7.230153980313258, -7.831955676251113, 3.2774540333527433, -9.65773607301639, -1.9835347079167693, 8.258102386129057, 6.579869512018494, -4.856334710810555, 1.9026495614584444, -1.7659090893870317, 0.7791312542550379, -3.0871409544342505, -6.061941498919994, 5.691652878763268, 6.524522804416929, 8.013669935796386, 7.710324112402315, -5.707864378867436, 9.323202471665862, 4.094207354899416, 8.067680011156689, 9.148709293474674, -2.2872658694005255, 8.670344034936008, 4.585197676151969, -9.612717654195688, -7.020961905562508, 3.0653911783926695, -1.7482422696664113, -7.510512850423026, 4.442637134002021, 9.165585808814576, -1.8185645722150454, 7.089284662058379, -0.7196423837801724, -9.16612206758648, -2.3614254974344995, 7.154616805050939, -7.974877725653043, 0.11392478554084917, -5.7010258817399295, -3.422238031454752, -5.364886560745397, 8.147895401683002, 5.3198162830443, -8.854038927074475, 9.269786398694247, -9.498772507939243, -1.5521383919865492, 2.90461544681202, 6.768014310124478, 5.637128977926762, -2.0321495455902667, 2.5474085418115884, 2.0133063402210034, -3.987495670025451, -2.368025270650797, 6.104104353439485, 4.247584276958287, 8.601045793369057, -5.0761671200754455, -5.858974297397022, 6.327248610147954, 7.4514690619370505, -0.7862249053865575, 7.134713321213695, -9.26562071939262, 1.2178034254626464, 9.909096973151613, -7.740687452526764, 4.073604344683208, -3.1219008612281147, 9.018677638968033, -3.3996236696006354, 3.833518300763153, 0.950595272222607, -7.905239940376312, -9.818930370379224, -0.851954216281003, -2.994045425942879, 2.9627554221370183, -5.162296663125674, 4.053908596430782, 7.467165219474843, 7.233724334482204, -4.672313994637611, -1.0769753348528717, 0.7823613115210506, 9.830336419217684, -5.624990926149957, -2.2758678078092416, -1.737395358188154, -7.546275135057248, -3.654901632183771, 2.2914568355217284, -7.218386745443759, 1.6038415627473093, 2.806360855156875, 5.322119839120392, -0.5680367968502775, -2.393092429596768, -0.04054273622424098, 0.1344811735841489, -2.0413552667045964, -2.487152509568668, -0.21524838330206642, -9.291358544328824, -6.7471874844433195, 6.039283917654245, -9.060921757554413, -6.518137674392412, 6.423647249122713, 6.3692752221524565, 6.606636229997552, -2.742443985217962, -6.579815774479103, 8.56216797675847, 9.181433496974918, 5.499438957469058, -5.518538913920263, 7.543846298038119, 6.942415416901909, 7.311073828729441, 2.5149807823845887, 8.777696439163588, 0.3163349009072558, 6.491135995021949, 5.670928326466809, 3.9990766043462322, -2.2015556911959555, -4.3079321250858555, 6.704383966140554, 4.994662995356496, 8.589112292105643, 8.875442327143432, 4.96126111984057, 0.7649741644832169, 1.3582594814976297, 1.2802062700026156, 3.0930241690178164, 0.03158440610037161, -3.9589344182409185, 1.0367598736616142, -2.9688322479998863, 7.557661824397506, 6.199613170880639, 8.827329568156411, 7.456261227972707, -2.3530116650523976, 3.702650328576409, -4.337313880832214, -9.64277955418349, 5.569483662224542, -0.5277594564854997, 6.159269723128876, -6.467173920928038, -3.4892930736108063, 7.685091418161942, 8.099672196208285, 7.840249067475796, -2.0741719264440084, 4.630635768459149, 2.7396738774491514, -0.9417107409074248, -9.8747148686968, 2.355000260092501, 9.396695342292201, -5.2081686450886355, 6.605162974733879, -5.2839795109097025, 9.065169951302884, -5.150377910386221, 5.204573389660387, -8.792639176541746, 6.037142285886631, 3.1317770856122564, -2.960228819623076, -1.637930066819866, 7.376397363654274, 8.671488926687068, -3.725909269337267, -7.149663529293657, 7.24362307425627, 2.358158996732591, -1.5259314818997574, 4.450716192843757, -6.329806667178273, 1.648190646308949, -1.2313575963936412, -8.917128644034381, 7.418891985780903, 6.71625038533335, 1.6704816233084134, 2.8082689776546914, 0.3494174211787815, 3.2446912482742967, -4.0007289571134885, 6.136656337585229, -8.114140863646167, 9.429362247647283, 0.2872281509364676, 9.461166974027254, -1.1018298632582084, 8.305669988945638, 6.1200377149847505, 6.097476535508232, 1.463106704112871, -1.6191880470008115, 1.036861462703115, -1.977582260346864]
BIASES_LIST = [-1.242993807965231, 9.159279642677856, -2.74017416792052, 6.494994939282293, 6.983064145895245, -0.45065947507507786, -5.032580885081064, -1.2373113555714816, -3.319604357477914, 4.604789995009742, -6.401164369931651, 2.9431309498200324, 3.49030888567529, 8.13390260151559, -9.46865770677263, -8.750484763878427, 4.528960631521439, -2.7129169243999645, -9.36009676225267, -9.723762831840212, 3.302710049616005, 0.23629661116104117, 6.549409899288346, 1.1686513001549947, 7.724476465034197, 8.117868524929108, 4.163112893068126, -7.664384155241224, 3.4570733034322814, -6.927156606327419, -4.4892762024224435, 2.7501711549100314, 5.390528150599334, -4.030486864776515, 2.801653626172504, 3.8132467516835646]
SHAPE = [27, 16, 16, 4]

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

    if best_move == 0:
        return
    elif best_move == 1:
        if board[3][2] == 0:
            move_forward()
        return
    elif best_move == 2:
        if board[3][1] == -1:
            capture(row + forward, col - 1)
        return
    elif best_move == 3:
        if board[3][3] == -1:
            capture(row + forward, col + 1)
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
