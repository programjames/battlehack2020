import random
import math

WEIGHT_LIST = [1.279668345710948, 4.158432711882955, 2.1866553976065495, -2.842324105978819, -2.8637321370777915, -5.6239044670997025, 3.9190098579082013, 1.6676691691854426, 2.4142621947832046, 0.8808291738645646, 1.6643171083857573, 0.9188597729285546, 0.05644157175590592, -1.187218630671668, -0.09320171976668068, 2.697847768757022, 3.2041353765658176, -2.3655800401507596, 2.2581910789352495, -0.05665532315404875, 0.41758535567809285, 4.154979405102746, 6.455962756688487, 1.3509405881139163, -3.002006348478497, 1.649679947347657, -2.696393019451862, -4.6543412616761906, -4.168897645356471, -0.498051349299523, 1.744509001987363, -0.006587973657589119, -6.317664418492217, 1.8725046911549375, 1.746883545936896, -1.7288618914545613, 2.293460550937011, -2.4553319204718145, -1.860830699001275, -0.10014929382596571, 3.5272948457859954, -3.5859515558495687, -0.9886799890648277, 0.8203078061185334, -3.1902387939641867, 4.785258837824123, -7.352381624214797, 0.3876505451804122, -2.943625411264765, 1.4343624435247797, -4.0090758370009665, 0.5319409664876629, -3.221872345471561, -0.23450715628053853, -2.9631492310912764, 0.19442824060723618, 0.5564874591200695, -3.4134184258860563, 6.267011913072379, 7.701703345344342, -0.36663218734557246, -2.9360396826759336, -4.0752040776473955, -1.9750933605994272, 2.5481493352856743, 1.4057230190882057, 6.5260013346016335, -1.3133296373850338, 1.8466308341155298, 1.5671259840432041, -0.2393881720646842, -5.750049822451839, 1.6953323920971557, -5.203246196672039, -1.7918833991627463, -1.5476374882154809, 4.412743510193614, -7.273944505181831, 1.3820816538255682, 0.9020453182902586, -0.32333733323410885, -2.2124618766123163, -1.759569138310124, -2.77089278597425, 0.5824981826842079, 3.492521387747221, -2.374069265791616, 3.2996076329069677, 1.8820389696873812, -0.8547857245549643, 3.7867177827537084, 4.100182710783491, -3.1583875059063837, -4.410711445905511, -0.5564357170117099, -1.2476620302090304, -2.1184575536664463, 3.7490468723826336, -0.9875479593950174, -3.434787916691472, 7.207485442941529, -5.205429160336385, -2.025171130603904, -3.1290211003501174, 6.335742897414491, 0.49537002709343314, 0.5013078017462838, 4.27406789561363, 3.3125194058022434, -0.0639273210475505, 4.141851402545807, -2.4512076595251577, -0.2673085210184084, -3.733035137468176, 3.970464686196184, -5.249788352444927, 3.7377750509041654, 1.3724131612674282, 4.770250721142698, 1.247326750372105, 0.8515660982680808, -2.545708050365025, 3.1599001543555483, -0.947406561907415, 6.4072844733153085, 4.733017581724759, -5.884707568727751, -6.8407220949999195, 3.410482866996581, -2.592264211779945, 3.3306255240067744, 3.058427221251481, 3.532850731135298, -3.9803475175866296, -4.661873521422171, -4.986732009050156, 1.0698448667870353, 1.2391622664382318, 2.5233988856709457, 4.067584157957203, 1.5477219063865442, 2.8469822017736237, -6.504211408483417, -0.9241218035391245, -3.346332405816244, 2.665306973987595, -3.088492699370156, 3.6198931593002204, -0.17718847699507967, -3.8003943599022416, -0.36179700677188764, -3.402648493484189, -2.035169364023946, -0.3749484054919002, -5.2065885419585, -5.155527690051794, 2.7140093275768296, -0.1869074623536776, 2.199065347562792, 2.894743844651066, -2.526720278684589, 0.6305544685514324, -7.592196981808953, 4.891528566280951, -2.871567449895821, 0.5489360740115776, 1.3451108473298956, -2.6566160958201035, -0.5106138788244167, -2.4151304225942662, -0.6348754184298266, -2.6075451770628293, -2.35114809901165, -0.06944293954387848, 2.43630193215588, 2.182295894359445, 6.724635208367834, 1.7753245793589825, 0.1556298404879357, -7.408057458094863, -2.9365964064120753, -3.8542721138201883, 3.0983331190894363, 2.3988533972356842, 1.2592664462852432, 0.6905824020356217, -2.958336475003412, -4.005146584636796, -1.0399753362230912, 0.14361802146872638, 1.080539123478942, -4.127163456166521, 3.5921749947301986, 4.472678432823703, 1.9183010489735781, -0.5410813250900844, 1.5049415940313948, 1.5730824989107912, 4.124040515875114, -0.20769777035649917, -1.6190530753440384, 0.6827802188054701, 1.3587619615299982, -0.017888191516493124, 0.3206752970986977, 2.7460510727231884, 0.4495684219246696, 6.633774223693251, 1.8252803239713566, -1.3077213759654833, 1.6451755169821434, 0.09695203504166772, -3.5390713932406674, -2.1635606408133814, -1.2138876395513158, -1.5099442745928813, -1.2768342473103458, -2.2489295521608765, 2.3446962142665724, -0.9352982226554997, -3.6644038139839843, 0.6110078052412977, 0.23477890003531998, 0.43233178254047466, 4.966454668799133, -2.8894423334610457, -1.8657775347562753, -1.6370160015978934, 0.43535776027205175, 0.21142002680479544, -4.4401802405665585, -0.8765063851672539, -4.622837209657541, -2.211922259853707, 2.9524085437957823, 1.5389490534184551, 6.260125472537481, 0.3050684160861814, -2.2148014697436404, -5.874011530336391, -3.08712455080802, -6.179216730650385, -5.677139303731983, 4.468588705024498, -1.0955155448917036, 3.7757695673234366, 1.732868650497383, -0.41401800845391534, 4.38186991252341, 5.81788239130565, 0.2912895285434083, -3.6497593780688766, -2.289626801284394, -4.836645073670645, -4.205573642794282, 1.0409502071542658, -0.0484147635515495, -0.370604532221402, -4.182524586796489, -3.6170124450331356, -2.770696433861883, -1.7890480614330069, -3.7847145020360435, -3.449250126242496, -3.949372723499615, 1.5643962919122605, -0.1827466775019635, 0.5757189161295457, -5.303508650058007, 0.8757341735300457, -1.226405524614611, -0.6775280745207124, -2.8613343593971834, -1.215292499162518, 1.831081033089982, 1.4812131462012257, -3.8712220319579425, 2.1162930129210893, -1.695105375015219, 1.2625211194031518, 3.495358208263677, -0.3022577725307284, -2.470995402730781, 3.660627486603122, 4.4935930411421126, -0.3442595774720626, -1.2468554356901251, -1.0378588836758809, 3.769779738595008, 2.1183774746683754, -3.771321702313186, -2.221478997609224, 4.778914950736026, -2.8244951393600264, -0.3093419758546039, -1.1275421916041655, 7.698716663532256, 7.318312421752523, -2.6811594610724896, 3.4506646996983275, 3.835420765207502, -2.036527540422154, -2.0399110959403206, -0.292092435488555, -4.116387468324687, -4.86464656671262, -3.6278131325700254, 0.9636282857201526, 4.904457022746784, -0.9371386992279347, -0.191816600200287, -0.9381085678702863, -2.672472780125026, 3.093149627372605, -0.8242496178016994, -1.7288448856532121, -1.8136502624370576, -3.3781381773847956, 1.0921254899820676, -5.0911163090288305, -2.2256751301301883, 2.4243383913870042, -6.159285790898953, 4.209020788082497, 6.319811595574966, 2.3079125268188294, 0.4258147769781786, -1.3081321707379572, -1.8229629271169234, -1.6207230677021245, 3.7322237656258253, 0.6769520869846366, -6.631055148457652, 0.16928438834685533, -3.9318537227824515, -0.596827468532239, -1.1112949459314712, -1.678001999010568, 6.298437344338941, -4.394926502601843, -1.9777855950379017, 3.8885056551004444, 0.5530965655554501, 4.215597818633401, -4.165980170810266, -1.0973037147616413, 2.491323046450767, 2.8628554887233326, -2.471714691007108, 3.2976973664458393, 2.857190135329647, -5.135893715635931, -1.5658070529771793, 4.819436155193699, 0.45727387338089676, -3.1855416046103207, 0.20769849451396505, -0.6417467129154444, 4.906611773317396, 2.4271781117589164, 1.0656113203913007, -3.762740823176241, 2.8563120331521743, 3.068218150835362, 6.639691450517571, 1.1937323120647525, -6.0957632922257545, 3.456172211731211, 1.298475275476604, 1.3284462071174579, -3.7919028803729664, -2.873884601914189, -3.512464068291152, -1.3494415893473153, -2.355433681510516, 1.6123013784885019, 1.638257874423037, -0.1390751998569869, -0.3564387457455722, -5.253327557240413, 1.8296763962026081, 2.2737022180826916, -1.4608600181186766, 4.969282577056801, 2.1406361805232557, -1.1254779062031817, -4.3042659762630215, -4.476332207610946, -6.996068497180722, 1.8317871377794428, 1.933878995388647, -1.2086979710709018, 3.3236251216681225, 1.0566659990655993, 0.5344078609038123, -5.35123014714882, 1.6273461984756161, 6.6627983489718225, 2.1024973396669866, -1.51913329458844, 2.705845570284789, 2.19040959945661, 5.75946126103044, -3.06936189008298, -0.15114366862125017, 4.364348260473134, 2.053116056914067, -4.413363805265298, 3.8696701447659674, -2.0378051090288087, -0.474766356256744, -2.186400383940602, 3.2174894110443857, -2.3671573046842713, 0.8900995765509161, -3.973432074396067, 0.200226216391596, -3.2757860961575087, -3.6054150527406996, -1.64261418686272, -7.658221891405908, -4.1852239620633895, -0.13312213920378013, 5.0281360355519205, 0.05643515936995103, -0.35566936388583337, 2.697231946608034, -4.162456009801947, -0.5955448084066113, -1.729941974397933, 5.416143820626048, 0.5806992397540891, 7.555965504771914, -3.4415685432320005, 5.8336748947337345, 5.923007065088845, -0.7771554844156422, -0.04460606596136607, 1.4122156893237294, -4.550539246706129, -0.19643436213541887, 0.008311857795000988, 1.8188606743107494, 0.02545745367453711, -0.19669213385129092, -3.378300441570462, 0.2740576252640903, 6.229500465307092, 2.3827513522018116, 3.7624199213748035, 1.9818958280095966, 3.4555546740501626, 5.20837939129184, -3.7718494881998277, 4.121241907645198, -0.29648985759193336, 3.1747434720515013, 3.1266447036588314, -3.889887987986229, 1.0987136896666438, -0.8190085649851564, -3.7311218296313386, 10.703012342785199, 2.9501799806759994, -0.31976074645243613, -1.7811782912858563, 1.2809222322147313, 5.93940241376294, 2.8990333137753597, 1.4039949925866058, 4.513575575582543, 2.398942012710772, -0.043688158639441754, -0.9777947000672418, 1.7206146105979157, 0.01724836096829696, 4.021232923454115, 3.5230961966383614, -5.719378658125731, -2.6667882760495027, -2.379727098801216, -5.078023428512966, 0.7130412145297238, -2.5879899998573794, 2.3851384907995645, -1.1633702969126218, -6.451698491163425, -0.8688692544178462, -0.6109229610506244, 4.512912605793309, 0.8396382820827137, -3.5241028572415356, -0.9519675025804761, 1.2916844535529917, -3.321945512028272, 0.46951345762700925, 3.1474863294059503, -0.8437521695301013, 2.493880768458774, 1.2839798599097705, -0.2942082580054044, -2.005749813933912, -0.3526137767568832, -2.6495348194713872, -2.6576218360121686, 4.525170887935717, 1.9017730619476998, -2.634792117524601, 3.7021079727168384, -1.8193965450732543, 3.3828536773715587, 2.4350326920396377, -3.9141284933160163, -2.93305292395105, -4.90052230650953, -0.5378601656344151, -3.6986982525601872, -1.1657864754551888, -3.6101655196258164, 1.2679938921715874, -5.4780238601934315, 5.042066484794877, 1.3779115613164796, 0.11699427546577645, -4.07694022676734, 5.674667159227918, -3.121921426161755, -2.4587395316844254, 1.6371392665309217, 4.922194545412628, -5.821262721134059, -6.507991960410973, 1.2863039332843416, 5.240328810443379, -4.361642723502697, 6.114210721472906, 1.4789883981246907, -4.665867834739879, -1.2392387682063768, -4.11870574214749, 1.85137411360187, 1.9767227502719646, 2.4539605116499414, 4.852150681651671, 2.182178501486903, -0.48379392492150397, -4.87036226649321, 1.493183617868795, 2.0208101023242557, 1.5249150848266297, 0.5337032085139848, 3.5471847680952413, 0.31410880840680333, -3.072570002442303, 7.087818682771115, -4.5450876790672226, 4.5165106267228134, -5.7824552633716495, 2.5994160843313217, -0.24443010021793699, 7.047441283101927, -0.021579525805744404, -1.9291919369790524, -4.263234210961786, 0.5499678857521206, 0.5045585354245237, -0.8611722921908318, -2.89678392451073, 3.2355443537010267, 0.48403485675002056, 1.8534714261079062, 4.114148292378323, 2.2089593165636145, -0.5121780436446258, 0.5564626663041459, -0.22625955709758894, 4.26847323180589, 5.906275506095332, -1.4479764414858896, -0.29819058687326017, 10.275834571756235, -0.9458483745953291, 1.2347380102167524, -2.102216334022725, -2.4206279551137833, 6.084845549229637, -3.280035963058285, -5.791018872331721, -1.5159162457372277, -5.872380222984852, 2.905553521686288, 2.0659459678247187, 3.653559617791437, 3.686366713425506, -2.279558063278736, -0.0525866530510104, -1.1878047905284725, 2.0499888725857423, 8.276562711145091, 2.5700822009962527, 2.3282579123087537, -7.02344214371691, 0.9127155641004128, -5.531803093762484, 1.5147441887560822, 1.9010574850728674, 0.02883645888875641, -4.838254248663841, -4.969927251251094, -0.383439006530087, 1.4414116360070865, 1.5048254181573864, -5.882976886325448, -1.1164977098614155, 3.461233510830599, -0.18612949522777733, 0.7403472761613856, 3.9380770942606045, -2.8999409887064598, 1.024381019690666, 0.0729890521464942, -10.503608173648894, 0.4177151229837328, 0.40445604995343176, 2.4934194664976976, -0.5488435048518641, -0.6621809181774816, -0.7097822211403241, 0.8230871324107147, 3.2592433486499877, 3.790751346477773, -0.23890115916803445, 1.4465376740109352, -0.9188379726848939, -2.974729776756514, -5.835675725823379, 0.24504684245457575, 2.8486923586321353, 3.715757874520433, 3.178245296950479, 1.7818586679507664, 1.200545711436778, -2.563512942900055, 1.1242555924388569, -1.3254832568978867, -2.8085732123082296, -1.8108111108691407, 5.1852761346407075, -4.167216192673751, 4.402258527433713, -1.3264784274021126, -4.517770865231905, 0.5892322157053398, 4.712582988614912, -0.8278757320373651, 2.6353269410932425, 0.7366204351187777, 0.5501211650862705, -1.6219473176290218, -1.344717874017602, -3.5303181766890717, -2.2815333524472496, -3.052321687367238, 3.6748422623415333, -3.7016253557278, -3.1546563989882985, 0.9829478750042111, -1.7378035273380403, -4.664357412053312, -3.283837433194334, 4.398434278499311, 4.538379747929719, -1.5116070322460284, -1.925893619649442, -2.315950214018416, -5.2662666056247485, 2.5959049635971603, -5.8520769351225095, 3.299140100359974, -2.659533796234979, -5.53717414964444, 6.672420927561175, -2.7509727909405397, -0.9741574570816831, -5.752135043604852, 1.576103616468497, 3.0532141114996074, -3.068820864889757, -1.0836314888645742, -2.50529640123861, -4.779302866714628, 1.9422001690329376, -1.6329235918052403, 2.7936453496336098, 1.702456994174058, 3.5428636616070897, -2.7614798398271025, 5.569117183165364, -0.3258860874724111, -2.31397204187921, -3.448701738515273, -5.411922652858562, -3.8182024349264583, 0.38822215068844, 1.5600287810284157, 0.4633640719234524, -3.4473310884780126, 1.0570400079110742, -0.8382085206046344, 4.487219471735963, 0.7958443025871864, 0.0010610120609331197, 3.6164459673018268, 1.7916977856610767, 2.059754508111111, -4.150395619426844, 9.677992116451032, -1.6027050095733915, -2.638666178397072, 0.3237346885786381, 0.009140108238334665, 2.2171239506807803, 1.3520275336295944, -3.0537550874955106, -1.1763650538785768, -0.9742672764016767, -0.36666977939268, -0.380631774095995, 2.8217022923909183, -1.3749226995224455, -1.174442087478676, 0.9862620198310459, -2.432738674886514, 1.9828033478129186, -3.646827752581119, 3.519241952714232, -1.506386873766785, 1.8031582131004162, 4.619049092315645, 8.002221337000703, 0.9635990383974513, -3.0327221851480473, -6.796396669235287, -2.851601312299188, 4.257407908950517, 5.195492197137583, -5.529288774590217, -1.6290051678881055, 1.4360343502177444, 4.257060301263226, 3.848892673659976, 4.951817224011377]
BIASES_LIST = [-2.1225988802945643, 3.273239510123206, -5.235935048975153, 5.658172061378652, 8.209201835623873, 1.7361605364256727, 1.17677418522414, 0.5893605077244666, -3.513485956243206, 2.7669929896994767, 2.458238583914858, 0.6613814214644584, -0.6931532379329239, -3.6558629723318123, -3.70382033681003, 5.5433279141042675, 3.345681491449545, 1.867869583908551, -6.62686068631736, 0.07597932850994438, -4.778813270229582, -1.4019796778063078, -2.7480306719751955, -3.5916970862010196, 2.689881583928962, 2.3489112738850983, -1.172584579570852, 0.40582641212961823, 2.2811676084304904, 0.7081585326983892, -0.6461049860147361, 0.980237629582527, 3.3842340610053068, 0.43648494213081745, -0.6371808569816362, 2.774061413207094]
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

