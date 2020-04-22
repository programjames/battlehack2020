import random
import math

WEIGHT_LIST = [-1.1904805096544342, 2.9595782782477977, 0.07342595081183134, -4.761914037471051, -2.0587176217385728, -3.19311034545468, 2.7527053295821435, 3.2051893184949005, 3.4453959221669113, -0.6641865617912777, 5.598420615587024, -1.258280911785688, -1.6189774885905792, -0.7700758166793382, 0.8034488136504292, 2.8014427349854714, 5.304548557635292, -5.341720240727927, 2.533810705705667, 2.568556727999712, -1.194702107837973, 5.324707028226449, 4.235195605413543, 3.261543586617302, -0.7862009529466523, 1.1667863229204256, -3.671398979414516, -3.310119821932072, -1.338443014420837, -1.2614524914189804, -0.3400491178593845, -3.6306308639044813, -2.9140992922263083, 0.9449902267117214, 1.2606698034678008, -1.8874681865417133, 1.3615985872382192, -5.177931905377868, -3.1933539967428635, -1.7092771253410792, 3.8928707514502525, -3.4281119940635385, 0.9481058224021646, -1.4368689533172252, -4.81221592958667, 7.645912375633037, -5.094786023133658, 0.6909706466127215, -1.6729573906983766, -0.22225651412788228, -3.165451078245806, 2.446462312712737, -3.824872473681873, 1.0711209393292638, -3.2857329722172066, -1.032414728328923, 1.4333633660900835, -3.857314458730751, 5.3958214010329435, 7.7873788694309365, -1.8246686100275542, -3.233084126570997, -3.013699709651676, -2.9736365290418583, 0.7561372317068209, -0.2963357863940359, 3.9409449814656536, -2.3711534733087563, 3.883793896048056, -0.060014472777711436, -1.5048865923587202, -8.091852568377394, 1.4607576445737172, -4.818192513085193, -1.3659179916370694, -0.9546230340700077, 3.4095937212377896, -8.248607057346412, 0.33545374325992716, 1.2656320530240874, -2.169387633575055, -0.8231453920703571, -2.3516313646087625, -1.8492647755628469, 0.5854847322075685, 4.789351736006022, -1.774752447518521, 1.4749924006233526, 2.2240959309079615, -2.5023042482661495, 2.5342462983641756, 0.8411296044890484, -3.3333510199466394, -2.720863786127529, -0.20899735423171828, -1.9642056502127458, 0.513343997290568, 2.345805934025094, -1.6211190485326605, -2.4125255035944324, 6.403449059389146, -5.041816291361847, -0.9865863502348011, -3.4992532083008725, 4.443891117002556, 1.2421534760753383, -0.9055471249859011, 5.290765295756671, 2.6785776055216424, 0.738191452953274, 6.728880326006961, -3.311688033376785, 0.011152380933913575, -4.977863234196345, 4.588899747484573, -5.0426152348992135, 5.100011404339744, 0.49527131561485294, 2.4062186542410178, 0.16175780610044987, 1.441025967375583, -2.2929420525541024, 3.495529937473778, 0.8047552633417858, 7.136121430175928, 6.431415089150324, -3.881198826863623, -7.398088550746356, 1.6325668748537603, -1.7499320639635327, 4.365395975665778, 2.2638503623943276, 3.557641904787964, -1.660054274396685, -3.796288961298918, -5.482069069396236, 0.7972146162195788, 2.634053331256048, 1.0144405932083158, 3.789733728962444, 2.817603221234382, 3.4366497268754017, -7.478616759468165, -2.3556631709984686, -3.8317569400655023, 5.420717975055136, -4.2815057911236565, 3.543771482984276, -2.628801098585593, -6.289700906846281, -0.7811316271078923, -3.17083283438284, -2.057264717418544, -1.4381265884639578, -6.56370547029957, -6.727602203214877, 2.599085629661074, 0.3913996506789901, 5.084304947759008, 2.4725520205835436, -1.6437791141491092, 2.7887581390836247, -6.652646815341566, 4.357803083096314, -2.5027199826191433, -0.9782108805530327, 2.52018480904596, -4.195395250462332, 1.7254037013359498, -4.636003780335044, -2.367791326576979, -0.5357465937017254, 0.6740641281529178, -2.94806084331745, 2.4627084207122945, 2.317374233054096, 6.608123887366466, 3.170421030557204, 1.9119715476921768, -8.397276883066821, -4.191679793906118, -0.6855792201273541, 0.9983834967220877, 2.048762877551602, 1.652866283824971, -0.6798158983523228, -1.1709862370158872, -4.818370403311031, -4.200071918574828, -3.0679569802222555, 0.7219430088430494, -3.551775672213365, 4.990636986630105, 4.429842854075361, 0.5328770132388108, -0.4703459946189621, 3.637426404486936, 2.399261691391514, 1.3090473230743438, -0.9871806783770075, -1.3618403856177297, 0.4032220806202116, 2.8504163883867193, 0.8296604428978014, 0.1763002096139945, 1.7624044389572369, 1.780962669500104, 5.995683971063103, -0.18615810689539092, -2.6903133260808767, 1.622038688234697, -0.8371621839544865, -2.7784801763382188, -0.11437914563069151, 1.2869829139180204, -2.748297046644998, -1.218286329590908, -2.5597411470439257, 1.5628791374020183, -1.806110539246313, -4.245962898841769, 2.40919191551229, 0.28509085659004496, 1.678232375234221, 4.540433180974646, -1.8488601366606698, -2.902418017824628, -3.4706049353839017, 0.17065114957894068, 1.429134569348319, -6.3109886735635, -2.2027545957886567, -3.716232315572954, -1.431368681212312, 1.6546125323983318, 0.9380453339699071, 3.5090362621816507, 0.6295410530807395, -2.429969834818524, -5.652083918903372, -4.43293122103747, -6.615635708734753, -5.440297324101509, 4.1708946531411355, -0.7588024674496439, 1.1980192999378914, 0.07759160637496754, 0.8583494310045738, 2.0779276065661567, 8.084549349738133, 0.003294907398477598, -1.888144233319835, -3.594932113764945, -3.7569715582623737, -5.089045365043295, 2.3114277933941136, 1.2787601387805063, -0.9746196173265639, -2.4252646791954007, -2.3286348203280305, -2.7397971654455064, -0.9852348928410259, -2.2863034948952223, -4.4558303037158025, -3.1770680373461966, 1.9129884543714186, -1.6892001344303207, -2.060744037340993, -5.872057933932226, -0.7231756236674087, -1.9170731514095665, 1.6567143297050464, -2.8092537186782165, -3.565772924536348, 1.1019205526220546, 0.05405225662122515, -0.9918618076597998, 0.9285918835977303, -3.0619089317001564, 0.27586859528274443, 2.4233358919367687, -1.5480674480579752, -2.8432109167544812, 4.318186975948238, 5.488287994491685, 1.8107367382802337, -2.0039386455664774, 0.6919606095319477, 3.9034929119541877, 0.6528488960822678, -1.6439086129966192, -2.080044657329925, 2.825593388536496, -2.6437612624648947, -2.4466943190025727, -0.8622623448578417, 8.280161226868987, 8.114352039997645, -1.0290705432611809, 3.15114766666046, 2.4072275781049974, 2.0946861999649884, -3.133840716895395, -3.6742625954952, -4.016861992481085, -3.22378921690039, -4.149009242307891, 0.8157131052729776, 6.751831037016882, -1.6501626475689195, 0.04802399142201108, -3.92478663886845, -2.392372357538078, 2.84040608419535, -0.02586364112373718, -3.5256034381749286, -4.577040556450756, -1.280624853943106, 1.0966125728471128, -7.363104152882435, -5.067040238619058, 1.413555055890959, -5.436696022472397, 7.593260356467452, 4.578730542146863, 3.726647761628822, -2.269881613407019, 1.1038733025971013, -0.7600968706280709, -2.1536217926523378, 2.6974119753622885, 1.1750826405681019, -6.114814532426413, -0.8692956792495594, -2.3628102732153575, -0.3865447530311288, -3.3253579253874, 0.5505104032366135, 7.752922437735583, -5.629609297259806, -1.9149710097207469, 5.205113158777532, 1.5094138733734237, 5.113495550358567, -5.176856295155179, -4.319594193789547, 2.030900387908325, 2.4699367685511007, -2.859621213078822, 2.4308540743732907, 3.2125727651292237, -2.1870290763846283, -2.36106876341129, 0.5468622161977164, -0.2872526453452975, -2.6357856517434657, 0.2968578326464175, 1.170184068137678, 2.6003053442788246, 1.606885709522774, -2.3600849751140807, -1.3013333620692704, 3.252988246851868, 4.955406217392065, 8.066735344659953, 0.9275066657535149, -2.3869393601713416, 2.7057017476407257, 4.151813578631454, 0.7661886654013867, -5.888376902597475, -3.729003473278402, -5.3995816453107315, -1.8735567170110712, -2.1099255347115147, 4.667659895860574, 4.1477618133204555, 0.7991879772859398, -3.60192305407896, -5.83517445641322, 1.8300924990016587, 4.99796499340785, -0.7080696258882794, 4.170688155240684, 0.10699840568581842, 0.5765837581900275, -6.445058738921458, -5.40639922380228, -6.659425193778803, 1.9141480306385779, 1.458642589964545, -0.35426849728433707, 1.3960424398258198, -0.7356304171405378, 1.2882539162171964, -2.660265911257941, 2.7440755071565093, 3.302455490070204, 1.2484744386032238, -1.286151502825256, 1.594670545508189, 4.373319647733663, 3.2264386117142356, -0.4171720874104141, -2.11381179571314, 3.711715890483097, 1.1740257058037402, -3.368593491780982, 3.9582136120104776, -4.170768557405255, -0.17860754600884832, -0.6910984979234023, 3.5926253081252124, -3.855013364097985, 0.5197474747983071, -4.955912710888048, 1.9301588661098856, -0.6277012134848967, -0.3666367457810715, 0.3769680213543738, -6.930939718289389, -4.368339074432637, -1.6855548563024954, 5.075350177668497, -5.006539344303847, -2.471432801541198, 4.848013060302044, -1.91734779751354, -0.676580215433719, -2.1676754153977305, 5.12151648048861, 2.092084518354816, 5.471101696880817, -8.1357812497969, 4.539565190147154, 6.502303686674549, -0.20907059613179224, 2.405557076015481, 1.7322820371649588, -5.61361385965694, -0.522490471946335, -0.18391844594802897, 2.774796198823232, -0.778355665307501, -0.6751395420120683, -5.143168118774266, 0.7229114951899624, 6.1380502488581605, -0.07331421073976196, 1.4231135932262657, 2.3084545783680523, 5.234989310746336, 4.855754000606989, -4.3705827979107035, 5.991687833933792, -1.4103956911706421, 5.645861496754894, 2.175320798545746, -1.1260199903022807, 0.8705780768652798, -1.7155390602119824, -3.386089542829851, 9.192885817187381, 1.8290991604071545, -0.914308437818208, -2.5283348609143337, 2.9762417523142886, 2.8806533473375744, 1.182864428574737, 3.222062428941186, 5.04328456075352, 2.0483484640239147, -2.998918042803237, -0.32359968610054857, 0.8668120437087459, 0.4598549778813974, 3.8678654223878315, 3.668011019078415, -5.415006003571136, -3.3252490612916414, -2.508021991780256, -4.3088074200126005, -1.0755482492239334, -3.2092449375690677, 5.219523636884324, -0.5626956291159197, -6.550370533016089, 0.6853548092201831, 0.4561054853209161, 5.346918202857562, -0.4610148196222237, -2.321031518748592, 0.359549016677855, 0.1951782870710217, -2.9374792526898563, 3.0188203296601968, 5.344213426144611, 0.2522073016720172, 0.06183492964755666, 2.407129560652902, 0.584946946645206, 0.7118842854731664, -0.44501387535102177, -3.3103662961026687, -3.2384046206991757, 5.639435495893554, 2.812575355165988, 0.12702310867686295, 3.0657242019237563, -0.8741494543988337, 4.2743534338292815, 1.1265992103959577, -3.4512650394451336, -3.320469901581771, -6.220870688803414, -3.1070614088989954, -3.3408522393790343, -0.6099997759588791, -4.204210179096456, 1.0783673398956575, -2.5703641168279763, 5.643355958216679, -0.10664485584387196, 2.191605796683154, -1.2286947562896464, 4.772717872637041, -4.40358782084461, -1.6228829600020775, -0.893057408780064, 3.8895678959031903, -6.0825590259001725, -6.501690040659866, 1.3014335777545551, 1.2108974811171835, -0.48533421369927776, 5.932127908972827, 1.2747408167327134, -3.6516193851165157, -2.238216921042139, -4.513992945260845, 0.2633404961651966, 2.9731151596146423, 0.44512502845546553, 7.0273644256734755, 1.4436472416314468, -2.9456952945249157, -4.9916836392530435, 0.9851260589575768, 1.7931151338354256, -3.269423346777162, -1.7080630473505338, 3.1191628036522285, -0.03174317728258824, -0.13223165211608778, 5.243044947108622, -8.127299345423644, 4.760056202506602, -3.974388484252538, 2.1065088200011086, -1.2504580779577468, 6.568221091991307, 1.7285835103070726, -2.045430900817238, -4.98186068338142, -0.5579485740823888, 0.6841206895494554, -1.4117632165964558, -4.791766209018856, 4.492929474183123, -0.6219063110119765, 3.0323087052317463, 2.8535548497060725, 3.347956834211857, -2.645489555519476, 0.13373902943125526, 1.1349052618076971, 5.6402628613697114, 7.128402564452655, -1.7519840740254427, 1.0088044585569946, 8.354590536759373, 0.10618398396792217, 0.40064488314844615, -0.9116442401700067, -3.6350070435623403, 6.084227147161841, -3.9193510103899842, -5.405674213713319, -2.4399047583352846, -6.64216293709806, 3.036579748301417, 2.4325520592338794, 3.861621791307515, 7.814274725441146, -2.883593750368071, 2.1644599519294747, 1.330040144857108, 0.9262734121770151, 6.695359509083349, 3.9949942200571407, 0.06096697892468028, -6.308751474831894, 2.44375138337092, -5.681029875236952, 3.016465121380012, 1.943049406209958, 2.2409506449688728, -4.949365863246664, -5.456067686496248, -1.0875888904833042, 2.957958246444708, 3.5766202736408204, -6.742630717399651, -2.1195526813796652, 5.979002874541995, -0.6261564197796798, 1.6165944472270288, 4.382538402243717, -4.0148744597388575, 0.4208796831120576, 1.9201435864592993, -10.037117065684027, 0.3270952687537738, 1.7133062930134066, 2.337942012727696, -2.320349026963095, -1.0459010145010006, -0.9126027053818317, 2.257956138060628, 1.1550802822568436, 2.370630114668214, -0.5741008911640006, 0.8897203718011222, -1.7886310973905213, -2.862437090392844, -5.837747125435057, 1.0247213748205772, -0.09050170414382408, 7.697370330236888, 1.187727323413272, 2.3253550793741056, 4.24482138305858, -1.3045005390911135, 1.1070748931017702, -2.1255106829786357, -0.9169077220048516, -0.8572617025005983, 5.780847579316937, -3.9388731466353732, 2.367977971484929, 0.8026949389178224, -5.192246894352099, 2.4912926772614545, 2.26825394565321, -0.17405051981943265, 3.7644420513755037, 1.3155491970438606, 0.7556301986930738, 0.5307568965380489, 0.8109285914746212, -5.474073273743583, -2.8389613393105693, -5.387401536490964, 3.6790913381524195, -5.213778641518457, -2.1572990004041257, -2.5958251053222634, -0.10935606498431194, -3.7886185982335325, -3.6178860322737076, 3.1543202895011984, 5.362543272559699, -2.5177198544784587, -1.9204103938000057, -4.207685794338567, -6.399261004438267, 3.179544455967566, -2.49625229512616, 2.835552274115294, -0.47530151941701115, -3.4168089571693594, 6.447592129511713, -2.7540071743876386, -3.9450109319184774, -6.247209355749847, 2.6521497597234687, 4.277600319564826, -2.686761069994082, -2.4943857038046895, -2.2916710172315757, -2.943527375845604, 1.7099759346926646, 0.2556990652353921, 3.228391770604964, 1.9419417273532522, 2.1300171684175266, -5.42861776556729, 3.482159767836011, 0.05629175118613805, -2.6635178183910977, -1.694913389206554, -6.46132118765028, -3.155987971351607, -0.3815278147342871, 3.7145715772735937, 0.7872759846694062, -4.851709012870751, 3.689306570740448, -0.8326425948033191, 5.380323397478566, -1.0672099299356002, -0.7532498718965207, 1.6313822080173743, 3.9583621999036724, 4.5884432824820305, -3.6800713629891297, 6.673886565161019, -1.631433032570289, -1.376171203299668, 1.154868711299308, 1.5741044895096747, 1.8880500974959995, 3.159077027343182, -2.5814640294326354, -2.7027648541565252, -2.1042918814686224, 1.1947413170391377, -0.61713496265085, 4.3679942755792425, -1.947676586405208, -2.1307203211230488, 1.7967600644326946, -2.0274006703077023, 1.923102393209989, -3.1586303763089005, -0.5957673448775649, -1.706022584925332, 3.8972861343104217, 6.886232879782351, 8.196069984745156, 1.4208269067591992, -1.884813496320083, -4.100305628415188, -7.686474879130423, 2.78149748296474, 3.5330537775735475, -6.690531313497431, -0.8866634964559033, -1.2132721190360192, 4.878759063801455, 6.365546578358883, 3.3122411774087688]
BIASES_LIST = [-0.352223817457906, 3.863340995821959, -3.097284992071975, 2.7524853165800263, 5.386829522358735, -0.9473934897703573, 3.5587652963732186, -0.1294692433341842, -2.0869028327571097, 1.5922524236515319, 2.978003005254284, -3.4290628366773976, 1.2131206555682041, -3.5438186404697216, -5.857753900523511, 4.983941499487831, 6.195133964995688, 3.9775423007239272, -5.3728129544878485, -0.45436769095033, -2.204374229157591, -0.928783234409554, -3.396319205201351, -6.037349969385488, 4.79754686080191, 1.3451065465124188, -3.1932875694738474, 0.551525369346368, 2.5259477913559656, 3.500849364214215, -0.6257278023052308, 0.5628737104993646, 4.175023347052466, -0.9048952435640916, 1.4898798059489473, 2.5140027450219993]
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

