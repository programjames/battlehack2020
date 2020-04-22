import random
import math

WEIGHT_LIST = [-8.462087776695194, -2.6043532046297564, 7.436888240261103, -0.55190178895212, 4.201602847157385, 1.9462991059831443, 0.315795739398049, -6.87784814655777, -9.256388917479558, -1.1712504410364477, -0.24977612677424066, -1.9385654318453338, -0.06182000636510582, 1.742619396820628, 0.8111342783610196, 4.292892279097871, 5.0639566800455205, -4.776266651755577, -0.7934957321312079, -0.016776808463945914, 4.14011306097436, -1.3035331979139393, -3.2623410949313887, 5.405732593570052, 2.1165250838952336, 4.421148782307453, 0.4612213374168958, 1.3652274460236065, 1.295590124543011, 4.127804927159461, 4.574935715362592, 5.185279360001805, 1.3628122263991924, 5.493234193863904, -2.047612945534964, -6.992075547672545, -4.105977081809423, -4.824427666353378, -3.9457918756086148, -1.8035653584686442, 1.7308282588920758, 4.662843588505388, 4.066061504809088, -2.3072211884733136, -1.1576739213229978, 9.18223356030242, -0.2533465194401769, 0.9265196843409071, 3.1621446402531705, -0.2894932885394749, -0.8956679670471575, -6.0914741420540786, 1.2790091434586992, -4.6513910081862315, 0.0979594324341978, -5.955543763561795, 7.696589556685625, 0.6819198559841582, 4.136583891570095, -0.6070919978998524, 4.757130611715215, 1.8285443018001994, -5.052590585893498, -3.056377588534399, 0.8251162718363583, 3.3798092474614263, -1.0007334193456443, -1.9471890838591948, -1.2744866714067735, 5.9942838536231875, -2.906491913046458, -2.3505167736183363, -2.497736374510315, 4.808891095595708, -1.4773724463042728, -2.165854352530473, -1.668674020093572, 0.10774914590752022, -5.485662322729873, 5.795141339869493, -2.646598999609418, 5.065949563968531, 6.223897344498332, 4.076037580963499, -7.571893419725142, -1.8853080657446382, -5.566478702792607, -1.8869614987592362, -0.6699267942411145, 7.825588498412034, 7.564190506110173, 3.5838043679155995, 0.7468117215715879, -2.460620363267116, 2.8390015506001425, -2.112512638140858, 2.736254392750153, 1.3538038852303012, 5.979304833919008, 2.296240441330707, -1.5636052231603972, -6.855152152314055, 6.0720175840357715, 4.628809824356425, 4.646888782580095, 2.223244569394959, 2.6230802317645945, 5.566589100190565, -4.828361887960657, 3.584921080504389, -6.4611619320647256, -2.963795448676054, 3.55510515678142, -2.6853701033806483, 5.734801303664075, -2.6002248940443753, -9.90218263422822, -1.5555723045528467, -4.814193391535856, -2.4341310451619615, 3.669265869214271, 0.3554439762285451, 7.34749667615933, -0.13286680091499659, 2.347002317304859, -0.13092377004167727, -2.667227448891253, -2.7599317141845123, 1.1578518617249396, 1.7319905142298422, -5.194893119940629, -9.70487369398871, 1.86264360328027, 5.960634475227957, -4.783521855089824, -1.7796718901841102, 3.80234413590432, -1.180700084119586, -3.7975208654059656, -0.05132176021491136, 1.9568238293008524, -3.001872434389531, -6.869303172936046, 7.157411806722129, 7.265751621959723, -1.2519706036319096, -2.553002179988264, 7.9405950494243145, -2.395209574688823, 2.4280709312272157, 1.9024381151483114, -3.8842730546629984, -7.023277800354945, 1.1131728488229848, 1.2154863993153509, 0.8667980122701582, -4.165258334125924, -7.213451493597965, -5.5333922463012515, -1.871465450851239, -4.749882939158443, -4.218153862753813, -3.4526124406308174, -6.669276375210943, -5.168281524626225, 7.072216260181567, 2.4362496511990424, -0.5294184637926123, 0.4116850204727773, 0.7277798850013397, 3.088882644663004, -0.45902763001611563, 2.2540518784454178, -2.970254203404094, -3.8612580114261847, 2.2147069546465823, 0.9764003075294012, -6.217504822030848, -5.001788931107608, 2.104622923129956, -8.316507023496234, 8.78606074315844, 3.5998744833040615, -5.520276274243938, -4.244084255871666, -0.7097042570126948, 5.348229728163112, -5.251981901438727, -5.210244512152663, 6.628369964216791, -5.418363342865523, -5.105979988368936, 4.711182242202187, 2.5300066398965404, -5.512888446237667, -5.436768229302215, 7.116534058553404, 4.2626966464401415, -0.13859555925145886, 7.305392305793721, -5.537541193458123, -4.366519912796124, 6.435533886828611, 0.8951659588377596, -0.8778919243355419, 2.5276665572515142, 3.174801811539529, -0.4515019832051161, -7.161286146088723, 7.510540178755092, -7.2517156763648005, -1.8346568045738516, 1.6267995305522385, 7.218679997817286, 6.231459245662099, 5.647200958644247, -0.5676485470878769, -1.7544741248988796, -2.6339271613077377, 0.6313841245356393, -2.2783442756127825, -2.2709165086525966, 0.2765441852607264, -1.7379200921825235, -3.994712539120887, 6.402518337268569, -1.1406500884513273, -1.5184589473494776, -4.099018850438326, 2.671501793512067, 2.3411785523836595, 0.7236346796953272, 5.816022266372245, 3.6433960178324276, 4.346457003357387, 0.8063843412687615, 5.366142119335485, -5.862461427511973, -2.773365098163042, -5.402069609249265, -6.428969964812234, 7.260832788097124, -7.0989501621571005, 1.4183176801504958, -0.12301376604846515, -3.222869595190229, -0.06145898774980921, 4.292313583567346, -4.354100932271844, -7.3025579510029015, 2.1083295618242044, 2.0828649523688627, -4.529352458500569, 6.160433360032389, -1.432085212883706, 2.148906114877102, -0.7171058935710568, -4.123762584979927, 6.294512917204244, -3.7386893978848215, 5.836011579237623, -4.365818105461425, 2.827743182478235, -1.5153996741323525, -5.349379199480924, 4.279003197574679, -2.8106994273882653, 0.41822011865561065, -8.202971440729147, 6.651561147229823, 3.373518469166703, -9.679447155609209, 1.9709120193522107, -6.548780754599668, -0.44325287343338, 0.19848077527370372, 5.2995673609019835, -4.505200786431941, -1.070146063678589, 2.8294660623223025, -1.1509085521169762, 3.942612870973749, -5.663066836457422, 2.9955361277340207, 3.0565185124003857, 1.8402812354626068, 2.1750390586889816, -6.0773976007336366, 10.228896356041709, 8.841935197333875, 0.7260477167037096, -3.758365477582059, 6.1076955928086525, -0.7886813602604636, -0.9300778099333005, -6.304845256176715, -1.3860181644402747, 0.45880570679494287, 5.057642866887846, 2.5333865428145086, -1.4030111411143826, -0.18230460865034417, 4.951382459886946, 0.2799201347267101, -1.9924066659205013, -7.1400383316279665, 2.1516346068112115, -4.10267296013016, 1.3455419511517879, 3.7999481193752795, -2.301249472531904, -2.360567162139592, -7.8188746333612125, -3.5756540368327405, 7.757909610889306, 5.825556215980713, -3.3761666505222987, 4.27387666176337, 0.9562334893324889, 3.5593814972592845, -3.312376787070446, 2.6349313119835216, -3.2557006337088814, 5.65450512278076, 1.23280379328616, -0.11192069127486443, 0.8135129482864303, 3.5898148452395984, -7.895541540094835, -0.8193965484366028, -3.463419674355261, -6.923674578474483, -0.5836075920839547, -3.7877348822248567, 2.79857551194135, 4.885120465592728, -1.5981999632999295, -6.777084583400086, 5.438449341832749, 3.2740781498357467, -2.3597124063038764, -5.869774756165709, -4.67262961450712, -3.47950533127181, -1.7100136954363752, 7.010036568173245, -3.6898198164174674, -7.755633951392895, 1.9226282262998677, 8.739502040696674, 8.887499710635206, -8.98476194990385, -6.6399253152706015, 2.6276816045277496, 8.388453994846426, -2.712542599719307, 2.3422985553500144, 7.162201450286067, 6.0074261433529506, -1.9635560747383016, 7.256017217435313, -4.231368557247628, -1.2448556334552672, 1.4972913443434133, -1.090188275953487, 2.8495419006779006, -5.4769078764889905, -5.7043434224511635, -1.7651480466816742, 2.1798932551200374, 7.670275947434672, 4.140435530939198, 0.31302650908499635, 3.646010724956416, -0.12611485286568164, -2.318025595417175, -5.027952826707822, -0.897957113797877, -1.8872270545674907, 5.333476789845104, 1.7869067279345354, 2.7922188508733004, 4.249273979977902, 3.8377805534335674, -3.135544853084478, 2.0856998316869633, 6.26792871412512, 3.3717060517087982, 0.7767611821172249, 2.0983341908656596, 0.4036414002465782, -3.5409842032766727, -1.0804766429593153, -3.6034772380197797, 1.2623276372142302, 1.5295180525241499, -0.08498738805701969, 1.882996256546134, 2.8982665511460772, -2.684890069733644, -6.1341609256384, 3.2091583649955733, -5.648921471237999, 6.387720168515801, 0.13764166728199684, 1.4450054017533638, -3.6214232858940156, 0.5377826910553964, 2.395616026214316, 2.5593358616877326, 3.2860698816558025, 2.7043618647087797, 3.5416615744323203, 0.018711943518727292, -2.106018884645474, -2.6226438711065425, -3.027598883060253, -0.1423612050708425, 1.6695057763507033, -0.9270763591628177, 0.6053189156727665, 3.31289944690385, 4.029782335794119, 1.7324649332594078, 1.1381714298089811, -4.760202761731617, 8.84859830317262, -3.7194073514809944, 4.910780429324058, 4.063732040461302, -0.49390711252073316, 4.882212069570633, 0.5118745642081597, 3.30663080019842, 0.3760187656454837, 3.0298134657398594, -1.4880441020331792, -1.1594803219408483, -6.373947482856615, -8.041386592627875, 1.1046650277223764, -3.900664651816793, 1.5400137211708214, 1.269168284095772, 0.5032370917950333, 6.48321321595104, 7.40191044875981, 2.9802083106516797, -5.625487107828866, 1.5675157959176422, 5.31396765725254, -3.6639108548503696, 2.9298511791078243, 2.1291189192148767, 5.787658807973536, -0.4371389676806142, -4.055229974445376, 6.243731856029449, 0.023868579291471292, 3.7308272449946287, -2.793470497874742, -3.6543120092049843, 0.8195180332952399, 0.9458432578250766, 2.8765343052477905, -4.035539861472261, 5.4101997961188175, 5.361695893260032, -3.7730488868237697, -7.9966893565635, 5.146133389254624, -1.9194803235722535, 6.990095053110089, 0.03492018416997472, 1.4447523640245397, -9.203140269020707, -4.276495778065783, -1.0867830942257097, -1.542443413035031, -0.7135633664754106, -6.999336613568782, -0.9704935032009976, 7.747546267620293, 7.962335245198145, 0.3222055988469839, -0.9081722444482012, -2.102618610234071, 5.668343621854576, -4.04738546823079, -2.2011588724417743, 4.590543021858404, 0.5925164096427753, -3.4697579281336672, 5.001540815904744, 1.8920225336268839, -1.0054276862152274, -1.2420020779076686, 2.2570329405585485, 2.796636552431198, 3.7947387056431343, -3.2902278487569987, -0.6148686711125217, -2.318682117925308, 7.515167801117992, 2.904914146286466, -2.9298404758102787, 5.267509839609997, -1.4696812808842525, -0.5456114589191302, -1.631936885203247, 2.2818442619418855, -0.0581120595603663, 3.745089509011173, -7.411809406876174, -1.6054529197301006, 0.08948254143240275, -3.7321622984599405, -1.7840749476348703, 0.5276226694633463, 2.2750617739800454, 3.8370571316854067, 6.164221448940572, 2.0588208335951115, -4.986623168094661, -2.7225892864387213, -7.743001886222887, -0.08997107585767986, -4.236153807176733, -1.5640664774630988, -2.6719783275684743, 3.7921803176407907, -3.5112731904246353, -6.622901137199684, -3.2577291324226114, -3.799191443675637, -0.31458167943647186, 1.6540287782006937, -1.672606133709865, 2.547697520251281, 0.7632410494727833, 6.955998502846227, -0.9907218327844556, 4.121965631138202, -3.5184900006078395, -0.02658567229350256, 1.604601060029429, -7.999958860224492, -8.402116360417118, -8.455733282036462, 5.786304926564434, 4.1830089411316695, 1.967901913832248, -0.4328690400423763, 1.1992984202606072, -0.29077026981937676, 0.6852790538113722, -2.821149209041592, 3.6723126880333155, 3.905516840353114, 2.819664152356317, -5.234964335782284, -0.12048351636867201, -6.979000935786802, -0.30038585797418665, -0.2817044558626632, -3.205009261830209, -8.025764030253287, -0.8794597677279339, -3.1431892089860076, 2.2697249688535543, -5.49995620557886, -0.5266114962904267, 0.5568520825328205, 1.5785495964762593, -7.202603410178282, 3.3260503027229307, 3.75402831157941, 6.307391404160248, -5.82206097278199, 2.373653328020091, -1.9305487126965661, -4.833808625865444, 0.7817367053471771, 3.294890747872522, -1.740458042487717, 0.010708239686563786, 3.8223150039272897, -0.47727951822276765, -1.337266193990302, 3.7887463659317855, -4.7270356111078415, 1.5159385629245077, -1.092669177038796, 1.1337051940379217, -5.192426329421387, -2.708071195557934, 1.9572711638995974, -0.5629341182847732, 1.1181425637016449, 9.35925284984824, -3.713308916964899, -10.237399034886193, 0.3198979746685769, -1.2426891555249042, -1.2233423438594515, 5.474374219449583, -4.383064485736918, -3.005630903583058, -1.6339319650725241, 1.8094187705395504, -4.067523988228181, -2.7024890788984655]
BIASES_LIST = [3.845842491555388, 2.1989178245042846, 7.396413189203201, 2.18371490325149, 1.0628674923506007, -4.046828031528299, -6.653382056274731, 2.745895876437906, 5.282553361301702, -1.3831457031510603, 5.919165679974425, -6.963117621812992, -1.541779908667221, -2.4040149053788498, -1.2503029054229655, -1.0344858859879267, -3.3977154815297292, -1.336732144885213, -0.04453833564904619, -3.864445547919452, 6.109262693583422, 3.228818494774205, -3.510733874449404, 0.685237645272684, 5.061763209752069, -7.833795261270299, -1.6024926199750285, -6.116876755684224]
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

