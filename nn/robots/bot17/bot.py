import random
import math

WEIGHT_LIST = [-8.359200711948482, -2.5048658384842084, 7.304396971949143, -0.7838999783982947, 3.7050531614723483, 2.0684425745559847, 0.22292045234955843, -6.831113969274823, -9.068162386301907, -1.41607901558968, -0.2774711669651638, -2.0868342221416123, 0.06247252166167033, 1.9598000493586287, 1.0890670504300675, 4.123717570527184, 5.299681139510159, -5.188069888922108, -1.4020419634286125, 0.012040178163405357, 4.410808932078619, -0.9815165024044095, -3.3311084823784984, 5.854767395970981, 1.7215083342451063, 4.418027442354964, 0.9295681727897447, 1.2947700250178693, 0.963777381611262, 4.449387686567456, 4.190745746182597, 5.104133378932634, 1.1657514953671635, 5.362777915453623, -1.9307357017426128, -7.261651130995357, -4.4406023411988365, -4.984071609339966, -4.091006797536456, -1.4383433199350124, 1.9636386949941738, 4.449491775980853, 3.897854652912699, -2.117234866200182, -0.7210169090707568, 8.897905359247325, 0.12736755129149213, 1.2165577236757996, 2.9324257304044883, -0.5713592083666994, -0.9246940334538385, -5.72618267130161, 1.1107385892963129, -4.985014057368533, 0.43400717124057825, -6.024518856939866, 8.186179082547168, 0.44427780870208927, 3.9984827687610136, -0.48618185200681147, 4.516504463858742, 1.5427400564407197, -4.868303775689218, -3.115599329709632, 1.3568295128418844, 3.5416309720895987, -0.977159435541989, -1.8739611507162808, -1.348254940830762, 6.017668992353206, -3.2586675437700023, -2.562282733337846, -2.3555041738460516, 5.0381282001350245, -1.7434813625240084, -2.425384702519774, -1.3757056761140907, 0.013090821289823168, -5.541260568226801, 5.996200480350714, -3.157609075232653, 4.911505252698015, 6.452591254718006, 3.6347563581553266, -7.299123053851687, -2.010592346225595, -5.905066758511013, -1.683117358889002, -0.8522236163170165, 8.06538546535136, 7.6199772039479665, 3.654876159102863, 0.850822627994646, -2.4072764371253754, 2.789833929005583, -2.123184227791704, 2.3459265688617252, 1.200366640927842, 6.172091284253197, 1.9131763682844087, -1.2157064750604278, -6.629835771663236, 5.945329753673823, 4.651573835300974, 4.726800339032723, 1.6847444154638358, 2.3259725676060907, 5.642155482192976, -4.58316062650712, 3.7788738261470427, -6.590253338313243, -2.961929817072815, 3.6096309089231835, -2.742301402161397, 5.4563295180430025, -2.5017076413219868, -10.087380135738456, -1.8040019292297131, -4.48429707196176, -2.358215426496771, 3.512122056302593, 0.4442749685182255, 7.565295049606199, 0.46079831141307753, 2.3261171126588747, -0.19515693973704598, -3.2917367278530962, -2.6558749016144048, 0.9567287339035171, 1.6259993262908838, -5.042689239999867, -9.515850349663255, 1.5970123352453842, 6.275359821166776, -4.621360020436182, -1.7803347022333205, 3.8473875688225756, -1.1433006861600168, -3.3625412392353673, -0.21215200463489742, 2.3817147343915783, -2.549727427082968, -7.093366401615078, 6.8699055281830805, 7.553977589253478, -1.72989063237547, -2.4702610289041864, 8.23426098815943, -2.6491218730734447, 2.5447181766255706, 1.7285582986167098, -3.9794492762046634, -6.808479182368907, 1.0135985343198086, 1.0081025734178801, 0.8517934743229214, -4.145445569614663, -7.263688009759817, -5.7575692481749625, -1.7562839655483542, -4.77334612563724, -4.103081799065553, -3.3310076381878084, -6.380512380805014, -5.5054108097022665, 6.7104784983533365, 2.573807225696348, -0.02905246272305051, 0.32959030259397076, 1.2476037101227162, 2.935771089692845, -0.47759214307710335, 2.0589028927970663, -3.2839408840264275, -3.4372691357428247, 1.8069999313563678, 1.314349728652252, -6.610524961902802, -4.843004619782351, 2.1112058571629233, -8.289375889169616, 8.897776099050411, 3.684994897678104, -5.615981031987629, -3.9935360204960846, -0.6796518928907294, 5.39368022484919, -5.217685038168549, -4.9078438584207, 6.894084553819615, -5.00943529751622, -4.7526601781218245, 4.438355820425664, 2.5152881976984527, -5.757454360696236, -5.158399881134611, 7.211946171125252, 4.291777584657465, -0.3985559309683424, 7.45459631432784, -5.405852708359483, -4.724060385974199, 6.204709440015806, 1.1815148980620978, -0.2967514503175958, 2.7812425833352172, 3.2670820126583875, -0.6227220594195889, -7.323918998843958, 7.357728410385342, -7.451717268391256, -2.1617073825529296, 1.467321149770424, 6.706881087969734, 5.82880872447416, 5.6301804680264445, -0.6986005659144701, -1.8397773761902871, -2.77875054227359, 0.5863192120356961, -2.2032357251028043, -2.66263210225324, 0.41615715617197674, -1.647688759008028, -4.322466536912199, 6.019190221439903, -1.1009482585637063, -1.6917230427325287, -4.051243938528149, 2.5353953759309173, 2.683892507184825, 0.7005591645231584, 6.085849393760529, 3.325485552132213, 4.271516087547548, 0.3302748114430563, 5.547867150512533, -6.061792083916508, -3.3081437753541647, -5.516959378981133, -6.3439313455522806, 7.508169616529403, -6.841052107716721, 1.734789319119575, 0.3378651109935706, -3.38582970107163, -0.22581520515346004, 3.9746335303683202, -4.483785789463777, -7.473496040867881, 1.7235828104719606, 1.9249247255250945, -4.6768022421612105, 6.385732552611186, -1.4309640370094232, 2.1196883365157504, -0.7894251965736385, -4.471695767530058, 6.6270655570005115, -4.172117782728556, 6.041417368852543, -4.109132227387584, 2.6888829373317655, -1.1885435158469588, -5.076243090740203, 4.599475827300088, -2.420010060228092, 0.5638224437866621, -8.34713117312327, 6.515801892754964, 3.6011906596044976, -9.56029027610696, 1.6623217627888358, -6.633898858744055, -0.4338540557137703, 0.1348230050973092, 5.3987284206531125, -4.285217729193165, -0.7242605309591528, 2.7825979313321185, -1.0329929193999396, 3.924601829499823, -5.567220895798052, 2.201255946053947, 3.2500561988002192, 1.624473963262506, 2.5155375130875344, -6.116887981319912, 10.411873521720436, 9.04622638592209, 0.8467365724600655, -3.7665092516016827, 6.185010155455414, -0.6597465225697032, -0.735658506237959, -5.9546857064302445, -1.445094667836595, 0.3946529046895329, 4.497591269672512, 2.3423121457214022, -1.5234927095852657, 0.06706943620706479, 4.995285450798268, -0.01177900727962089, -1.743350732951444, -7.488314231491818, 1.6840958091634664, -3.978731444853708, 1.3846517521873836, 4.0380423592539865, -2.126966435754917, -2.282272507446625, -8.221889817544948, -3.647002930611038, 7.715008513201078, 5.497529904116436, -3.5457887937833665, 4.430764845403607, 0.9737067765687117, 3.373658350344559, -3.3092982678622596, 2.7029397406016455, -3.0770424939585763, 5.722624770627317, 1.7711231680746429, -0.4544303956317311, 0.6475825227371073, 3.685441638521739, -8.261755135639753, -0.3485507450369674, -3.5956826034536493, -6.9540862749802335, -0.6658508010368083, -3.564521018961201, 2.4536630264468537, 5.368934324736551, -1.5226888771886333, -6.984027612905998, 5.091245814664658, 3.0524588719533314, -2.2545362374755915, -5.429626821921789, -4.413089357936051, -3.723090161254653, -1.8649244959587288, 7.133018233479853, -3.6519225665544366, -7.100793678684767, 1.8346754487116712, 9.068462508966215, 9.064404294556, -8.752667848064101, -6.931618096133905, 2.6989215576027252, 7.96164787550916, -2.760066284717668, 2.5065399860601034, 7.3692187855190205, 6.328479205747032, -2.004176698228454, 7.18941860664511, -4.023985197481066, -0.856565075979385, 1.6402048900321824, -0.7292008192385245, 2.8005600136663373, -5.361003198484849, -5.623171860592372, -1.9367014168455488, 2.2012467242911145, 7.677391261766288, 4.561219488864117, -0.07460900661517816, 3.7773419826374393, -0.30842890566642567, -2.2811338714938243, -5.214144732182725, -0.7420886672114464, -1.669548309782005, 5.507685340094256, 1.90367289832309, 2.992895215352726, 4.08388783959088, 3.537696174082233, -3.3322632184291354, 2.1429608790900025, 6.389456867802694, 3.249347899234503, 0.3699705384328839, 2.219474608013658, 0.27269664649162245, -3.389666120860121, -1.393844844583695, -3.492870754843152, 1.5279559601650365, 1.660524267951986, -0.09282397113414603, 1.4715053537246106, 3.137033889116062, -2.5067927444995224, -5.914833099399928, 2.9470512005638554, -5.90648465513916, 6.532493210033276, 0.1268157250520191, 1.5387640332860304, -3.646272869324242, 0.4531592745083766, 2.591314086788978, 2.995366406615547, 3.252336596226533, 3.3061086330627023, 3.7038713947140347, 0.14755057827018075, -2.0176671852612538, -2.441022848931071, -2.8887497210859285, -0.030582011948220272, 1.4139602027705562, -0.9128797782974141, 0.7230928786556892, 3.138786769602442, 3.662969801931601, 2.0789676703153592, 1.532356542247418, -4.286335966853599, 9.170186628917028, -3.363235748629354, 4.623338000294587, 3.8518679363489183, -0.22939886462765385, 4.93929070614245, 0.5109063733450889, 3.050920389805863, 0.7995445470479883, 3.5835839439603108, -1.3961479550900933, -1.4843362746214313, -6.160402065061115, -7.76885842807257, 0.9876273175401677, -3.978963974090246, 1.4233418022934656, 1.7085743747289097, 0.6868490885770206, 6.939014651315018, 7.72407756763637, 2.746681795576988, -6.160984394703165, 1.4342449172790699, 5.0622575056003845, -3.6163676727479843, 2.864012725114661, 1.6973409771766157, 6.044150332651537, -0.14898440861935897, -4.147049132620733, 6.931243128276399, 0.2572953443586269, 3.760781920261158, -2.2731369850158676, -3.5468761678420875, 1.0345247854223598, 1.025857036675884, 3.300511857320028, -4.294920692381032, 5.629083920509831, 5.627083926640116, -3.4239292686480924, -8.05052279164258, 5.12962273234925, -1.3840798209843104, 6.961877958139217, -0.3190936599181855, 1.3501787844932271, -9.061450134274999, -4.550661985009137, -0.889401663551727, -1.5392419391644157, -0.803734727343669, -6.945809162937822, -1.1341913739908946, 7.750792892318447, 7.9955767707819385, 0.6337824635539491, -1.375717204288017, -1.670040545796187, 5.474024342664078, -4.376469831672763, -2.282165324336234, 4.322346745941467, 0.8585836339462485, -3.3307869810711375, 5.308236091258629, 1.5533763434728762, -1.3611779029750481, -1.2642636853978109, 2.1373917940377036, 3.1373191119074617, 3.659330664258322, -2.9106176673041695, -0.5480118630202355, -2.5621340987876295, 7.365122418212805, 3.0774623087043396, -3.154592430417814, 5.351250711383028, -2.0079255084472076, -0.20888749128861095, -1.654822512602972, 2.3001145837409998, 0.2795445932164004, 3.6190736826919423, -7.214281347120656, -1.2917684539788936, 0.21000632498183092, -4.008708635211008, -2.27651613133779, 0.3546000992203849, 2.4404607033229766, 4.100104914968961, 5.945410011087934, 2.3887455630641057, -4.450388055007734, -2.9563386251581365, -7.562415734161809, 0.07250630096568472, -4.201811190757726, -1.3308542651321162, -2.8108619123805902, 4.3635701895635615, -3.4904117562332067, -6.923569326522509, -3.1484537210566623, -3.568061930993352, 0.09860046457786725, 1.441411414159172, -1.936212255560359, 2.200837625064958, 1.0608526779415302, 6.670048523073354, -1.2314750054387213, 4.432655306662107, -3.850469852853717, 0.18758353054139587, 1.6653841440230015, -7.751941072855588, -8.41855532380791, -8.357700061934693, 5.738562772221073, 4.3432162439054665, 2.2092119984795513, -0.35168193572772605, 1.432208106831208, -0.030929466939872224, 1.1978086739335114, -2.8737101801664364, 3.5931882587328006, 3.821535739648978, 2.7232855867041157, -4.765854723410237, 0.11244242122375098, -7.1661618629906805, -0.4762932573767732, -0.5038777968870649, -2.87914317267834, -8.015441062474437, -0.9835179087779315, -3.258009942534255, 2.2322416212148197, -5.214085945608786, -0.3721333246549149, 0.45579058560367663, 1.6026264741286316, -7.22237022566572, 3.0911690374332434, 3.6272583258718347, 6.133888925893879, -5.9701794375692, 2.4598317653910637, -1.797558519153307, -4.9864945915688565, 0.7994569978805228, 3.1864509666763507, -1.6172919571786646, -0.15970142952715882, 3.5910020689104867, -0.04345325355529556, -1.1813258852816535, 3.866431199481625, -4.530665689788531, 1.7076757158752338, -1.1923209334206786, 1.1199622704297347, -4.863433292422214, -2.0891033819593585, 1.9322983465138344, -0.5826504198158475, 1.3712116249994213, 9.156060037394656, -3.6985594779711106, -10.157384737942815, 0.6540528894121762, -1.2609558525760958, -1.212992738257104, 5.502188430703327, -4.273958503755933, -2.832157437126607, -1.8210735015867021, 1.984966692545881, -4.304699739769917, -2.945843486598688]
BIASES_LIST = [3.7320912638253785, 2.0950778234860032, 7.132991434090613, 2.0179683900022565, 1.8381294589384622, -3.7863752312785484, -6.913546365068933, 2.4271899979643616, 5.251247007320196, -0.9861252778158454, 5.97399621072395, -6.8249467762325935, -1.545402018645167, -2.1996429995812092, -1.117313137870331, -0.7651398257390256, -3.8456214948408447, -1.1701784327989373, 0.025889920745164163, -3.712569314768044, 6.266017425290316, 3.225368668726614, -3.831171952205238, 0.928688974888698, 5.367490108403739, -7.7594389610292085, -1.4973326556644562, -5.835313173326055]
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

