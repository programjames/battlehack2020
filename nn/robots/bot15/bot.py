import random
import math

WEIGHT_LIST = [0.5606987867778973, 4.9018883726405615, -2.3153133905122236, -3.5556960682069563, -2.321573238090494, -5.29114894221139, 2.869387303758276, 1.8280588831333389, 0.8053937582564971, -1.1072050337365176, 2.5984601293005722, -0.008486969296010812, -0.9031955243423578, -0.7615485094173415, 0.2309636910066534, 4.934387405260171, 4.676950123053382, -2.972896758815997, 2.835399423812867, 1.829786795757772, -0.3797550853812071, 4.352151599340021, 4.932135102378167, 5.41689712905572, -2.1138654559726175, 1.6157701614378777, -2.193225183762298, -4.361275967071362, -4.8998738622338545, 1.3863262698472818, 1.3593541473922488, -1.121498504551307, -3.3936532376052253, 5.260514137058307, 0.9944286419664664, -2.4908457267062296, 4.150908274171307, -3.2875970218586215, -3.7532887919151747, -1.0273033707071793, 3.8312649603176783, -1.863442861999389, 0.4353993189116484, 0.15843286201951784, -3.2630520468478874, 5.732261631385489, -7.881546318135936, -1.0389117341021716, -4.617506977519509, 0.8868061436845159, -3.8367752688517682, 0.6783930087269064, -3.5742084139979258, 1.8896526547762877, -2.2550549971207507, -1.590083535527339, -0.4085305973742294, -1.9777043280027624, 4.88999037548365, 9.880523444612676, -2.1989337991850237, -4.496981914743326, -4.309868938354684, -3.5305272872479336, 0.7309281513485353, 0.1984532428877213, 5.360610316447725, -2.197705753450275, 1.2323074963494267, -0.6876890412641018, 0.44544899929188514, -10.341463386864596, 0.491908751465745, -3.6867465566377806, 0.04417367457610284, -0.9683486415173984, 3.3892494857165585, -9.795234598896316, -0.07133421009237163, -0.5720518205089759, -2.4176867821989396, -1.1125389483917452, -3.255879564038872, -1.2228228823347125, 1.0162400342102633, 4.808439201968073, -1.8325518699327472, 3.989605801210621, 1.3705341400330633, -0.6878181574255571, 0.994447104783072, 3.780256424957154, -1.248271007742574, -1.0577963386791314, -1.5797972397433693, 0.5393250024821846, -1.7556303017316737, -1.1336552841417202, -0.6290175788875996, -3.693666976919576, 4.1228189313377035, -4.828155532630386, -2.3276887038469285, -3.6118359610476114, 4.941228297942159, 0.7527098711302553, 2.698024850372394, 2.683425946991055, 4.964480142646849, 1.8837298439340118, 4.390495543510754, 0.6080036079646952, -0.5341440500465, -4.3209574548171625, 4.461669024755212, -1.7128234934061741, 2.559754486048785, -2.7735387345009714, 4.560983255045879, 0.5731912281798957, 0.633444171660906, -0.15966262073562898, 3.602791142320686, 2.61720659773692, 7.012840369549254, 2.4398400480330364, -5.35654656582692, -5.631003419595917, 2.551327212116824, 0.05760290878307203, 3.6238003678710666, 3.8436954060328783, 6.498407424292817, -5.748767200466822, -5.189647323255188, -5.164712622975768, 5.24200441839492, 3.505538113213866, 3.568350694957482, 4.555703048730868, 2.07298235861513, 3.4779731291863496, -5.225142477793067, -1.0505860521201373, -3.682970303705954, 2.5181258890755625, -3.946945787775516, 2.4808056379226198, 0.46021610101480454, -2.476732075506119, -0.429658957549172, -5.113698873855058, -2.4178662787683396, -0.003523753778896289, -4.157895640406545, -8.681695669649033, -0.22379026409665406, -1.8198346151011386, 5.4633597682744846, 3.8031181140496875, -0.9448193975425752, 3.843059350159043, -4.5602756677212835, 4.480529216551322, -1.1246949855467472, 0.3663456604242858, 2.1009255512945098, -1.6905047242669555, 3.3715191050270046, -2.6014038206014236, -3.4550932331549706, -2.426681172790488, 2.0609385510075984, -3.286005334160261, 1.8345297202972293, 0.19490690114836348, 7.298195012498923, 0.14072102564158223, -1.2334256537114927, -5.3793263843059425, -3.2168508498410135, -1.882641692642251, 2.146304596162166, 3.6486850984699672, 5.114336111311763, 1.1277702696878114, -2.634921468010335, -6.110587217608202, -2.5153623080700664, -2.133144909676612, 0.08188718121297751, -4.284295686453315, 4.58483778008052, 3.257655187351513, 1.9134339129947402, -0.43252957578477386, 0.7548120269348799, -0.5213653541843056, 1.7010866271071519, 1.7661608979637546, 0.12479034944383434, 0.7067614546404316, 3.030565736358143, 2.42182452266569, 2.249826849681471, -1.350474705775096, 1.0340943252486707, 10.578766570206954, 0.5784714816057757, -1.1256500311356377, 0.6014766422614218, 0.7561528540790804, -2.940523007872527, 1.3064230499056588, -0.6497964845824943, -1.7604271457467533, -1.6035263585203812, 0.3286309563539178, 1.2981256615250052, -0.7510687422543342, -3.9265775694622835, 4.083046050372662, -1.5737307094374549, -0.951966052341485, 4.250700865594539, -3.5308624203470096, -5.023975967229292, -3.323159703757348, 0.153627734808993, 1.7355210194909987, -5.336594288464853, -1.6971060150743467, -4.687557214031266, -1.642764623384828, 5.271930863637505, 2.402837155070638, 4.271803229696728, -1.1707249221304756, -3.6241665351641155, -5.937103956224626, -2.567941412945783, -2.5883373731891495, -3.593138105807269, 4.862276531092646, -2.599795641088331, 1.2061038721414759, 2.5981115711158993, 0.21891064494888682, -0.08417996382633954, 7.122932936115844, -1.5363726446173906, -2.112957265338462, -2.291946602123258, -4.269517871184397, -4.857311246682198, 1.0182807226693904, -0.4181342912633808, -0.35502844127239486, -5.80792900733206, -2.513357765632936, -2.7258935287724033, -4.577080032901549, -1.8355088886911484, -5.901954511304703, -3.0648283757023744, 2.6879824782451878, -2.375012797685112, 0.5927543056038321, -3.765832872532028, -0.5483951709660494, -1.6582168890142135, 0.1726324080279684, -2.89139865611714, -5.617727592036945, 1.5213882349568932, 2.031207635462219, 0.20050447164812152, 0.991727655824069, -0.7808793934331507, 0.36165346739220905, 3.9457806632131907, -1.0314505520627677, -3.894285405754526, 3.7542483837847476, 6.155835342120492, -0.07610661399574067, -3.383407767845811, -1.8292029272011538, 2.6390511535084165, 1.7014419421784102, -2.9744072886710895, -2.694068067580628, 2.5467416708720214, -3.571483777668634, -2.2656532781257965, 2.3583426388483906, 8.83141973266857, 5.949639097185583, 1.8026568996318393, 2.04586742614932, 4.561878937238802, -1.8775503935351687, -5.842239387817194, -1.7676941790871468, -2.371439875819322, -6.865118420183664, -2.883126257604947, 2.2995400269152286, 5.0641028937209285, -1.4279609857049425, 0.6783203445195094, -3.9223813944884043, -3.5982631950809334, 3.2646099257913885, 1.846904957430886, -1.7800887243367287, -5.6466804415743965, -2.4008523464070377, 1.2839413162250066, -5.593150687750524, -5.314349249821632, 1.2822128469387235, -6.798840012784174, 6.4022194851966985, 3.4366756690061218, 4.600692525614859, 1.9988773261195907, 0.28114701315824203, -1.272284645937132, -5.561374142815121, 3.967906875501261, -0.33124978379430675, -7.43095745093852, -0.10276749232123057, -5.028141790973861, -0.5123047334562595, -1.6733754164081605, -3.4579879759492917, 6.509992145788269, -6.786245105188807, -3.2404035657175507, 2.6674822410875856, 1.4733338922299877, 4.186633804748177, -5.6906536139892365, -4.632041300191972, 1.7027881613221751, 4.79884267145156, -4.850329535094576, 4.650495367588428, 3.2505670230995776, -4.031119208486108, -3.3988164508536354, 2.312226997930052, 2.3403803261404486, -3.3890860569739973, 0.030945143097573322, -0.011670655609105848, 2.81227677540415, 3.2467535877877816, -2.2478336436959605, -2.828365578198026, 4.918613745062271, 6.055283929759221, 5.283436668860389, 0.11329541733016549, -5.840202350934034, 4.260727208655334, 2.609396304357621, 0.856842647462041, -3.224246570067969, -4.710038891722806, -3.6732748824579726, -0.8867692376247259, 0.34157394531736296, 2.0761744216888953, 3.9166873100328723, 0.6775790054929166, -5.649500596952491, -5.255284952105006, 0.42194494017457995, 3.424446514625542, -0.8725430838319289, 3.1728434522339497, 0.13022222267121938, -2.868073422974801, -7.230903987589825, -7.8754943621979345, -4.597143430188066, 2.4620529640411104, 5.607056815337687, -1.7070205352897836, 4.703195772858317, 0.5131155330871838, 1.4440025350648407, -1.2944227326716065, 0.34181111265714675, 1.179493422170435, 2.2612752368744222, -1.4982038840032985, 4.286848901785969, 5.552009466875587, 2.7129297716948995, -3.451756802663113, -1.7145243126347025, 4.538445708544123, 0.7020099231557273, -2.1527753349940344, 3.869727497113195, -5.556246774529206, -0.3051530023492987, 0.7849509125137227, 0.9030915079201222, -3.2739992188536355, 0.9632176005374519, -5.683489988472888, 4.132160271257535, -1.5787148673657379, -0.7119208955044766, -0.994202199827577, -7.393619613981859, -1.8392411793888002, 0.7527196313883854, 5.219966174151049, -4.349986324000097, -1.146672392619268, 4.08585557631104, -2.744326318420358, 0.9175250373359468, -1.945114904279478, 4.39089768834288, 2.7874706270007383, 2.9942714506758987, -5.90585044102465, 4.939605077607434, 6.181551169646318, -0.7360721703745668, 0.8092259954401577, 1.5872143741248184, -4.761476267255335, -1.6174049913606086, 0.6535016784184053, 2.0145665757588365, -1.8306136033214173, -0.37479664486022535, -4.321915303285824, 0.7154331873492327, 7.989644723311271, 1.80454321822579, 2.9311713831505815, 2.413915141991418, 4.518895110233979, 4.938538374699107, -4.361980478648685, 4.685812756024839, 0.0029843447831676157, 3.62983131845835, 2.559072364392967, -0.3737381542258395, 2.514547950804752, -0.4198447251236089, -5.906645049591219, 7.692082617445454, 3.6916051977703144, -2.0417341718883155, 2.073063022951147, 1.4949898354930873, 3.1985777794948618, 1.3725302500525594, 3.050156001249276, 5.180380986149279, 1.6576579189442302, -2.3182027279988477, -0.10770512724658056, 2.496415436958704, 1.3416866031580736, 1.5792370107608926, 6.853959320878609, -4.278717242349333, -2.4592842019676286, -1.190315261127913, -5.081132885117476, 0.5642496489155563, -4.341680058895202, 2.6911428854549118, 0.3930907286480556, -4.412784785007157, -0.8114004468588878, 0.4779483153437412, 6.265866207514843, -3.2863952890193064, -2.877705749769391, -0.6958327125524605, -0.2398015559780163, -4.868613869132559, 1.3668167256269257, 2.6065455028412985, 1.8448790039869738, -0.3641769827281964, 2.7244624681735257, -0.2844211113535807, 0.10552790743534471, 1.5437063894362875, -4.736420380857048, -1.6611868030050383, 3.6015971535400726, 2.869085327771791, 0.49299660899429404, 4.259258672874121, -3.051626487534459, 1.8189278720499242, 1.0493821782324095, -3.7710017622598317, -1.7928462589563356, -4.912674513927202, -0.9736821546457556, -3.9964947111296065, -1.0070696868353857, -5.974420049206463, 0.3074908339027658, -0.04878540254481227, 7.016072846132084, -1.1861617660324058, 1.1057656686612432, -4.01596205062145, 6.955773995959526, -4.07650345637969, -4.130148530638829, 2.0399142610810177, 5.104507956664954, -5.505531727211117, -6.411929225971458, 0.9133648102645302, 4.219360524589094, -0.902334599870177, 8.078428563793755, 2.52178451841464, -2.308732961498059, -3.3299615805786904, -1.994394459466774, 1.4603255915807203, 1.0633265488707728, 1.4352350989547038, 9.024811624159437, 3.8096019482810335, 0.5690270558193401, -1.267553855018608, 1.8054551924690467, 1.5010625571494112, -0.546976611108583, -0.28541573324723585, 5.97407534523141, -0.12878909691932733, -2.787386678757431, 5.408347246303864, -7.766839866675643, 5.250703829930242, -3.8785984799955595, 3.3990308595075693, -1.0142508592679502, 7.80621516897973, 1.8936865714316162, -2.2545372998220423, -2.1780649639212664, 0.034594145770493315, -0.11725146566826052, -2.4637470668323203, -4.412216664041091, 2.2132842080410695, 3.9595906825551057, 6.042416320633827, 4.873156721341475, 2.246539272910573, -2.1488325632151835, 0.03018298878953796, 1.846708832514351, 3.714268937581979, 8.945787465107932, 0.40000138716701417, 0.22787102809533535, 9.60259226169033, -0.6124538895721581, 0.5369978765226784, -3.19140772227185, -2.5502593071819204, 5.773100406537733, -2.347076627351426, -5.446805275707272, -0.2407247118545141, -7.355656000070956, 2.4203354318277106, 3.075744501378664, 6.11275608555955, 4.947892148793261, -0.9521527569294513, 3.810742254861849, 2.9139913913310194, 4.110735489931986, 6.787432396024368, 1.3904306140020923, 2.305553482563261, -4.256229558483768, 2.017893071393457, -7.717286586723355, 2.1608580536171624, 1.2620477319217234, 1.2206976922577635, -5.139430162085894, -4.54157372054816, 2.365375819336144, 3.0357650329920363, 4.273800516363781, -9.139101915803957, -2.421548399099705, 7.444241082325055, -1.3607089478875012, 1.441771608019282, 5.827508955279213, -3.4642411931278927, 3.1626988401707132, -2.0120955152232574, -9.980281212432553, -1.0500090241860816, 1.4790069987452639, 2.905246489346849, -0.9122825519095826, -0.7011529983496545, -0.8057495066596945, 2.271364960585543, 2.4914711894999577, 3.223662477171426, 0.2789692060411743, -1.4192832152064796, -4.286416904747954, -3.2249732899140873, -3.4223166623693864, -0.7112939306075907, 0.8638357370776457, 4.225498458741105, 1.9535941968582795, 3.1849304892704273, 3.114058252118337, -1.444722311850224, 0.15976060821248284, 0.9657682001706851, -3.0850653047866192, -1.6511171785635805, 3.4803247719743244, -4.020187894654134, 3.3607062433455783, 0.5667650915439683, -3.6907787044089053, 3.447090305462147, 5.921651600555006, -0.44357628095704277, 3.2309431872521315, 0.37833393125410464, 1.8472591334677724, -0.9176366649353486, -0.1997086736082631, -5.2610915483060285, -3.3618284650996717, -3.713618204937125, 2.340287336038113, -3.902729253949366, -1.5420501744285808, -1.134900036653805, -2.0580476807677197, -4.900414197468641, -3.8667446965453722, 1.9815610879541736, 5.679003270755636, -0.2050458772635618, -1.82148110345654, -1.3592865409695765, -4.278541305783962, 2.3423240697517334, -1.5545438172145942, 6.68381645501462, -2.675414620594231, -4.751108959013726, 7.883080392240303, -2.04242838804498, -3.2756323047247307, -5.159581719024128, 2.994594533882951, 1.5182441214272062, -3.55205001074452, -1.3617697513148446, -1.5987389384663968, -4.808566102274235, 3.334848460764023, -1.3019164940723464, 4.381456740596495, 4.628831111578263, 4.298342331295554, -4.909706637953739, 3.651032346818026, 0.2410865151188443, -3.401368507002101, -0.3634025731647681, -4.738795108736341, -3.544558177295798, -2.0663623667400084, 2.525598074006624, -3.4131121317632385, -4.6800966990380575, 1.427473088741331, -2.753764959737665, 2.0143453878415776, 0.4711282964529521, 1.6664304527864133, 3.962444724389885, 2.9306313140667997, 2.787207254645689, -5.8633029423119005, 6.987401641283504, -1.3558985956024796, -3.4636359126645715, -2.8530332369006284, 0.15054612742294293, 1.4894592407812888, 3.0301375997467224, -3.5959197479543725, -1.049595050349128, -2.7624157513775667, 0.5787342277799147, 2.1879497505326753, 6.128763873746584, -2.7648065317348958, 0.09298926067425942, 1.4736832134387405, -1.2523009755001573, 0.7320536719125662, -5.735941780417946, -0.8410608731333508, -2.388801488051354, 2.3548027837965533, 3.773812510813299, 6.921851797250577, -0.8723520007910202, -2.2307222617110063, -7.9848236559439485, -4.332177838717731, 2.9982679563979935, 4.21741682581407, -4.413845548064417, -1.778634204699109, 0.9777913222361637, 7.599714623600357, 3.756306027169879, 4.870702176084936]
BIASES_LIST = [-1.3817393523581112, 3.7119755286391607, -3.615884838744677, 4.79145605824734, 6.334370618639926, 2.7690778622312657, 1.1021545495712284, -0.07853395609463772, -1.103327795726112, 2.6568975500575327, 2.1296259477531776, -1.3670778591906236, -0.007201847781285702, -2.6171328010408614, -5.499158384779249, 5.26136539522929, 4.817961004385089, 1.4805296770701923, -6.563033899207606, 0.020820610733407765, -5.0739130094994875, -2.7941666354933363, -4.063263517642431, -6.100390283149659, 3.929642149313798, 2.646487935165116, -4.024676526717459, 2.921774835396834, -1.0805753440910055, 2.3056406981108304, -0.33830069072003005, -2.301701528403347, 7.121523372029396, 1.8546253012081961, -1.6838490051201602, 0.444784381753457]
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

