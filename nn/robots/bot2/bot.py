import random
import math

WEIGHT_LIST = [-0.9686241531329165, 3.168342785261707, -0.6375288193554636, -3.6238175194998017, -2.829379713388239, -4.218037605182454, 3.6742301214169952, 2.7964907424041217, 2.9932122310212854, 0.5784483169588737, 3.7582637593834356, -0.8106249748017412, -0.29084555779268884, -0.47062119218319587, 0.6447231998409229, 3.612723793383471, 4.587002540597492, -4.268888257750231, 3.932460945776742, 1.217382272611892, -1.257131225696858, 5.530615199705434, 5.182182109507647, 3.6043473243506954, -1.1620369944390303, 1.332385329039588, -3.961793490413043, -4.127553921691824, -2.4261968010542976, -0.6139927175941569, 0.2668143400128149, -2.5372701065713796, -3.2041795466928047, 1.0175333092109566, 0.730873436092818, -2.654033239057181, 2.283237851041055, -3.5224757933821818, -3.442522404545337, -1.4104306765260852, 4.559622894139485, -1.6724112248669574, -0.6959454429784527, -0.09358937702791226, -6.136547046633673, 6.9904451187150105, -6.209117913879972, 0.666265715615618, -1.1191835641688908, 0.0945170930159609, -3.3241701730544317, 1.5409367125308364, -2.7803161770264233, 0.4731952371415531, -2.57061343429031, -1.0396451649862046, 0.02378214305669668, -3.3698501343626956, 6.612693844426578, 7.594394831530277, -1.6419445465643452, -3.196709252151795, -3.799118249062681, -3.4577048679854823, 0.9923599896461632, -0.29579211523496207, 5.127544134045971, -1.8256223417339559, 2.7935370907924115, 0.35146822873768446, -1.9936575746908725, -7.09354035146773, 0.4495577138141478, -4.332092450285948, -1.0865253537641815, -1.9327214223111364, 4.351258605235438, -6.891922092689966, 0.42598478722442623, 1.174281031998333, -2.1983176244022364, -0.988230140732776, -2.2521097380845205, -1.2919208238491837, 0.6950727410808517, 3.3522206759061763, -1.4507710192684748, 3.179083786324309, 1.8617068805945483, -1.5209887095844692, 2.814407976919437, 1.7090914315981118, -4.521771503665331, -2.138566168856727, -1.5761320056789931, -0.8568649068226759, -0.9559270990369177, 2.3342153398428946, -0.9588669205931081, -3.513102699613598, 6.94334875284645, -3.9599024200230746, -1.4171422953917394, -3.4921509891608333, 5.583877790587028, 0.4148447379377902, 0.06525091682825446, 4.032693084644903, 3.4458583372048777, 0.5628481664255394, 6.213834169133786, -2.2383446293683926, 0.05376617079802681, -4.85010245199879, 3.7175448564912044, -4.1430717541952955, 4.709553551345102, 0.029095135790135895, 3.2720022817852703, -0.5333535577209869, 1.43944983101991, -2.328785800399067, 3.552383018092778, 1.4446221633436558, 6.987663078967111, 6.06380501322215, -5.542506680560869, -7.379899235853168, 3.1952502805266283, -1.1719621251038137, 2.762427345536623, 2.9606266754575845, 3.3531528258471424, -2.9324104040203567, -4.693452873648008, -5.016319121084381, 2.3435100383277723, 2.8301932059232815, 1.75494412036704, 3.088458879530622, 1.9092175810124137, 3.622523042552471, -5.904606783170424, -0.6420778624915019, -2.575020843240635, 4.978100961420646, -2.8019296350745018, 3.742593869361876, -2.1833198430308407, -5.296038451740275, -0.6637760633871137, -3.7417256148175504, -2.976460709386717, -0.8753404116170767, -5.481366158030535, -7.0092070242570195, 3.5343487533497147, 0.35608503220129517, 3.7938071840583802, 2.8291573026951733, -1.3231504383207753, 2.5164795872656605, -6.956126562880397, 4.094952029514513, -2.5576784256061353, -0.5524563893425551, 2.2065190282863956, -3.6521380468041564, 1.551660152898691, -3.9144867468510984, -2.0123422615368973, 0.16422158457305835, 0.43404151284814296, -2.8794083206747345, 1.0545439523724927, 2.8240324233272855, 6.5405203449612745, 1.8372505218168858, 1.3528163238771476, -8.142384475824931, -4.634807192192169, -2.133248283215332, 1.7031026214639327, 3.358568652885978, 1.876164874052344, -0.3805334442290649, -1.6045500460954751, -5.812188031971905, -2.65711101546312, -2.247410577055506, 1.4386069411252054, -3.4932095584347116, 4.2197025707942135, 4.120710621481149, 1.3130372560796841, 0.018155432392160886, 2.7534048271772966, 3.136544563747952, 2.5472892639893514, -0.13955247850208818, -1.9806475699694472, 0.19290589061568886, 4.501872158095355, 1.0059555962290898, -0.12378259172883865, 0.5923497464424898, 1.6921521164176414, 6.921839252393804, -0.047486759084438446, -3.0854456352784583, 0.11633163957263437, -0.5977483042854723, -1.6708076197132042, 0.30775191433888893, 1.1071963565308263, -1.9920862644175361, -1.498818154913494, -3.5682635852094786, 0.6565857044380699, -1.4484383613715393, -3.1479872233979087, 1.9167721361245134, -0.48642224014813185, 2.2784541996823857, 4.917515004379321, -2.8093911663271975, -2.820046751898142, -3.169475853829651, -0.07155400049549043, 0.9877452497538375, -6.295474194561059, -1.3968783655810155, -4.324098366026647, -2.0560502963910157, 3.3829454662877243, 0.6750964345311758, 5.282023117375346, 1.836441154671383, -1.652257692200997, -5.285528879164423, -3.1422225867580584, -5.071720705017243, -5.746372362541397, 4.419147715016962, -1.541928850254302, 1.547639933656145, 0.3033179799194492, -0.9740447936026377, 1.4718639196696808, 8.07596645803245, -0.11057225440524487, -1.1737590203806965, -3.4673261978678065, -4.144555133113384, -4.274303282417419, 2.3673676549734766, 1.1763491874760375, -0.394157876869751, -2.4475353469563332, -3.1069449448616604, -4.553580174258775, -1.8356807835443096, -3.211079479626228, -5.542794992504276, -3.2609162191788217, 1.284799994599147, -1.5675073387870797, -1.610250501689518, -5.537899451278539, 0.06215407720878208, -1.9994146467253122, 1.546706195508699, -3.1837790580931946, -3.3893936802948303, 1.1021779382301284, -0.17034557344116708, -1.8850661557029615, 1.5826305103695537, -2.2403066842494557, -0.039762242626323885, 1.6526227255120487, -2.3766996353018355, -3.0907757227106925, 4.204112446498264, 5.905344155169628, 0.6421668560999465, -3.5120020278149253, -0.8478727896907203, 3.6036137864418505, 1.3223037435529834, -3.148263448085739, -1.4844617870634043, 2.5902950409721024, -1.6440406168425847, -1.459367344636508, -0.5118603292789742, 9.523834876712778, 7.657239972111512, -1.858942387098853, 3.0056896402427595, 2.8073691522870416, 1.1083543009297916, -4.330738595339948, -2.5537798622165266, -3.4646926762849644, -4.542322075985901, -4.281659253572875, 0.8248257950106095, 5.689360282075957, -0.6211416507656817, 0.30466412411942523, -3.679849614366442, -2.323163911859676, 3.1089098188341993, 0.7228762388429413, -2.1408387094800507, -3.4666447884180505, -2.6018768284864606, 1.7850014696005294, -6.153065959113316, -4.254798056914236, 1.5832581310632419, -6.894384392458672, 6.325849484068095, 3.8054342903077014, 3.8900528684070235, -1.2165214425578041, 1.5460042847620317, -1.3214416114794978, -3.255976946532016, 2.2318242326407143, 0.6165699768206703, -6.678473502838045, 0.12673364026712153, -3.046301905085058, -0.2719930165302169, -2.9300994459927585, 0.7834063746737516, 6.937843745594488, -5.831681120352469, -1.0051242601659645, 3.7709142698552993, 2.4119056086957174, 3.2092185353828437, -6.4839485726844, -3.2702911623796815, 3.696662035845449, 2.3858529985500976, -1.9963029549768119, 2.073572895613683, 2.6717663092264665, -3.617455740105937, -1.9892793710603112, 2.2789666019838446, 0.26757176468374233, -3.005363986649103, -0.40128124673133825, 0.9455798968678288, 2.253592530374396, 2.489585712551574, -1.7077926603421196, -2.4542097817886557, 4.492570240776754, 3.9243493218741508, 8.10295051808295, 0.8166776354660612, -3.7861714858493607, 4.013291185867879, 3.787280436814533, 0.7540281601302488, -5.615834467191488, -2.6759982235307107, -4.859241196191812, -1.0994683353270769, -1.58745647560611, 3.569369474278723, 2.8578688429105377, 0.614270062089413, -1.871234391025788, -5.585995592292511, 1.9410096902260268, 4.822600538615328, -0.783356966663823, 3.3559034692022625, -0.22282539708732507, -1.0069254757155426, -6.49790996905699, -5.8652586970957366, -6.684800517560285, 1.97404947536754, 1.280236798948378, 0.2148193626204331, 3.0005401929592566, -0.27849387439491025, 0.6121354913461534, -2.9620204981860043, 1.6297597111421056, 3.6131856586624878, 0.4556275700561063, -0.9117617215091944, 1.7219454309284385, 5.41831047127611, 4.023194827708467, -0.6509066111791713, -0.7548770790759618, 3.8852660726693706, 1.450188756483353, -1.9863441787804719, 3.552604437989089, -4.897442390564555, -0.047900526058868964, -1.0274537418465475, 3.5098853105380243, -3.3969829991078937, 0.26173261527823155, -3.7500423647463537, 1.5895281148210465, -2.3285184969879067, -1.3112612376041708, -0.5868886388803431, -6.820745779542004, -3.3573167561902246, -1.1476591472567308, 5.39699077190999, -3.403557019091955, -2.3328897898713814, 4.358648352650178, -3.207068948153266, 0.1553600905408461, -1.7973444017631572, 4.371219732037308, 0.8045081279116866, 5.4778528359140655, -6.169795766773461, 4.722007785246288, 5.844700129786395, -0.10917971907699764, 0.989121808762701, 2.108064225227376, -6.852415149079169, 0.9045603604331205, 0.10999097315866457, 2.636639893849816, -1.5932929079072204, -0.36664034240935217, -4.410357949663726, 1.1147040693074084, 6.066203837653465, 0.3903536806614134, 1.9841206326072394, 1.2619113354594536, 4.20342099011769, 5.160741735788536, -4.192055442933898, 4.337282370881844, -1.0030194318558057, 4.726795791594068, 3.8737150784063967, -1.4075183605626047, 1.2716360553062023, -0.1837143841980271, -3.1722172658049406, 9.926852024153309, 3.009066494670872, -0.9558122235388677, -2.2097117364380443, 2.7864470411433544, 4.307776824034638, 2.147745567995524, 1.6388854439998495, 4.731667597587659, 2.8537020272938225, -1.5287360094956681, -0.4560522712061723, -0.11414406003384858, -0.0944104409737182, 2.9033737111052345, 4.198462218753292, -4.7888988784779425, -2.70636081673916, -2.714494192466555, -3.1951175475103666, 0.07760130551001332, -4.394461131799327, 4.937745524437334, -0.8406312494975983, -6.742778294780002, 0.9157992176734937, 1.0948429887686402, 6.118185136123245, -0.6815645892114908, -1.815905271653702, 0.8334946290158218, -1.1548973986983322, -2.6334423209185913, 1.6560343728676425, 3.8163177319717505, 1.0269556857211022, -1.2469827199695185, 2.4038490371715406, -0.449249053792519, -0.36900788448886757, -0.7236558698546178, -4.607734704537015, -2.8081901470324864, 4.7107107249833975, 2.5813687651220016, 0.045998706533745715, 3.9002765972398805, -2.530469628470725, 3.445634045924466, 1.2506074013388293, -3.6590208680330836, -2.076848357252035, -5.432148251986825, -2.3932365160866858, -4.2302036371769365, -0.792077125718567, -5.115218022235197, 1.0054745958121503, -1.6870280258690449, 5.929554415989861, 0.20436047094945975, 1.7923042515660246, -2.2580567381767267, 5.2960696563293554, -3.163387234457973, -1.2912837035144542, -0.21140304538191468, 4.0724606511712995, -6.361528078183716, -7.0811525345934925, 2.2921454744575365, 2.1125967403437604, -1.1133369647896212, 7.313882772790613, 1.1770530999171989, -3.3376441967991104, -2.893314884718148, -4.8026971697102425, 1.6523878237693888, 1.5569391576367195, 1.302633579725513, 6.846293371897985, 0.8223135515140712, -2.031203108699646, -4.180867101515424, 2.4871440665786615, 3.241327188543817, -1.8395291586823723, 0.1827433495223969, 3.6005541812137123, 0.22298680663888248, -0.9989798149109477, 6.421091054910116, -6.594638488243428, 5.164402052162079, -3.635647704235041, 3.152639993506746, -0.8059820418497352, 6.389636680457942, 1.3734353429224022, -2.7601266611618795, -4.879397708399592, 0.39127146337703045, 0.04615763661375638, -1.8949878050255227, -4.398879774136861, 3.857533065264458, -0.0907705875103808, 3.781617254556495, 2.6881929710551358, 2.5875140987376684, -1.976139972178841, 0.8866859637834819, 1.148152475266551, 4.177177787304214, 6.884826447163469, -1.2078222757827364, 0.7295412194996089, 7.95709804662185, 0.29705083374185604, 0.3811108998193453, -1.8111777145827865, -3.1462475397195933, 6.1471543480901385, -3.9706790740400093, -4.143265031207694, -1.273598889445656, -6.3249259038841155, 3.035950164068116, 2.1577369973383487, 5.170591383159626, 7.126101422292598, -2.7902728376743773, 2.194564844235583, 1.8765023766174562, 1.9853398245607892, 6.607029146385854, 2.0720533681709377, 1.5598970552700364, -6.807916301593591, 1.0604804506515872, -5.127419922647209, 3.6015849465545404, 1.4242941393479933, 2.0818322422934505, -5.071028500547547, -5.0359768034068475, -0.5098144397227441, 2.95011551207834, 3.010166133061823, -5.710878683242495, -1.0467649895251727, 6.849599567286605, 1.1808879833673265, 0.8731356652058118, 2.518831108476151, -4.094248428737387, 0.43030198930335883, 2.094801219888105, -8.99753621897443, -0.4497950409260143, 3.1726320632424034, 2.1835166138898625, -1.9100602417978354, -1.3048330091896012, -0.2945948905574255, 1.7223775708221112, 2.2710440889214993, 3.5490388365753205, -0.3499085185366324, 1.3329386772810876, -2.4568749813410147, -3.821732486260647, -5.673774521893122, 1.3825763299985203, -0.450763075076521, 6.079906743474356, 2.511337025224949, 2.996814413852465, 3.6030778794955225, -0.6178784682423399, 0.47901729193180387, -1.613765319049392, -2.144777991480336, -0.15073690041729437, 5.110528454137739, -3.3478968421508353, 2.4385975561770667, -0.3191354992710914, -3.8616273467929694, 2.220861935627258, 3.506367571681678, -0.5057491922538755, 3.2318424656169853, 1.9413365673258811, 0.8097550123154087, -0.22111361678555175, -0.12488875167987479, -5.36999723825719, -2.851975328306017, -4.057983845703577, 4.631453733753896, -5.775898991603594, -1.7992535370252203, -1.0169598550562717, 0.16912945810560043, -4.362384909102667, -4.357399898775638, 4.142536271998099, 4.484614878912854, -1.6382726509221075, -1.7591336361338035, -2.998578348567814, -6.0391728260176425, 3.288040081644178, -4.143614782352032, 4.391497091279309, -1.3020767800300082, -4.971886659817003, 5.836184727070538, -2.685953800813352, -3.014124699463326, -6.23553766561664, 2.5468360846817255, 2.8705229273184916, -2.7739947329615697, -2.5893822287908774, -2.1767508918467224, -3.3251574185732062, 1.3351950100708958, 0.37146353812923505, 2.8384711561135254, 2.416660681859821, 2.2719203548323827, -5.454838777570963, 4.98839221238447, 0.6293690295117536, -2.2281791887247664, -2.1353586900761696, -5.546168083200204, -3.981147642772848, 0.061138873300401686, 2.488559728385992, -0.35175863166375687, -4.571641680350995, 1.8230503233095359, -1.1173505224400702, 4.853645076841534, 0.03421523303998364, -0.8555209000152627, 3.1932142599542557, 4.255215039367098, 3.2181464541284743, -3.837276850017283, 6.709818615351153, -0.11116016035111465, -1.8774661688018464, 0.26200914605757397, 2.126847782187697, 1.7108044958733366, 3.4264768114768094, -2.222960096595674, -1.794413998736465, -1.419148176651312, 1.1667909147659583, 0.4791573372783735, 5.296590944216773, -1.3717809138686787, -1.9809066486496774, 1.4381240038367835, -2.2313180886458728, 1.3704278149131763, -3.688929896624095, 0.7500628750121898, -1.5310596593594774, 3.033831435584476, 6.418531516357719, 7.965229260195311, 1.157328511337698, -1.6496992649821571, -5.418898776549724, -6.1606868370817, 2.0635130715128858, 3.7835296483468204, -6.754921518564929, -1.1406561953269696, -1.2361976038381703, 6.782268268204225, 5.230070432146816, 3.2181382646602117]
BIASES_LIST = [-1.0599206608457759, 2.672153417574073, -2.5103383738897938, 3.537646836980473, 6.151124978085373, 0.5978243709619175, 4.423977431840018, 0.42988971646286056, -3.427342788566187, 1.867976296302916, 2.220168854185015, -2.312015155234822, 0.06649516280780032, -2.2999294480952166, -5.726687833094713, 4.807109553228607, 4.906408240074818, 2.9497374048505405, -5.874143390063579, -0.3528880203763409, -2.6139932149841094, -0.47328360021796667, -3.6682770144365864, -5.553627187612762, 3.22958169278317, 2.1311617429298044, -3.59883195334643, 0.271472271895425, 2.6374474499666842, 2.542660365869462, -0.0989950771056245, 0.13560693383920563, 4.062902057892536, -0.8587009538002839, -0.06229143450075125, 2.050280913079379]
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

