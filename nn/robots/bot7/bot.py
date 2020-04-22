import random
import math

WEIGHT_LIST = [0.7674631792424922, 4.011972760470056, 0.30667871674931346, -4.426899398062488, -1.8023984471483718, -6.3086922652189905, 4.297571127539122, 2.0374783255662967, 3.9853829045516003, 1.6413331102998887, 1.8287601430205322, 0.1473471880660231, -0.23459063446073802, -0.5518128416379671, 0.8763599427614075, 3.672712821299127, 4.08437190022329, -2.7835456146835647, 4.246411325176636, 1.6470667454013492, -0.9122388355017181, 6.034910450953214, 5.19008413433962, 3.8916553470074806, -1.4215654176360233, 1.986087839446224, -2.536673002023177, -4.142137250332283, -3.6554562414753033, -0.2921452366056443, 0.7695802086878589, -0.06884798806239556, -4.4049130183090615, 1.5509476384066412, -0.49817951112831693, -1.2668847920319255, 3.438292888324475, -2.7626474830058303, -4.057833351631252, -2.0168394534088376, 3.7944144789244767, -2.7728528698924566, -0.48298621996742597, -0.17731263803080122, -4.756466630638931, 5.200136766783822, -7.367335576566093, 0.6403550010776069, -2.268905686115782, 1.4551838856861705, -4.470391640470159, 1.6323176151969174, -3.852892315873527, 0.8012090862315508, -2.564091816723028, -0.8706012227203561, -0.8203168747428382, -3.024263036895654, 6.933227910661261, 6.883242139278289, -1.3157533708913671, -5.124448784108829, -3.783807513829088, -3.1127953946080447, 1.5858257195779615, 1.1856537440053652, 7.146113310630593, -0.690515864054057, 4.0956555347186026, 0.7603984783176054, -1.7075618752356874, -6.645224176191752, 1.4863234333008046, -3.7464406672890833, -0.6743406458153667, -1.8004852443861, 2.290229273089401, -7.366971788099591, 1.0376984196454728, -1.2322915884539867, -0.38096011956210696, -1.6046139438120353, -1.5065826040672265, -1.5108806802596526, 1.0582047614341081, 2.7420621023090437, 0.3699178306672297, 3.8926696253533617, 2.7710897107544885, -1.06171826570788, 4.33184952967589, 3.2601884740730345, -2.652100918772067, -1.6039378542083882, -0.4095198099824777, -0.6796229082847154, -0.5743022755674351, 1.557869183349105, -0.6004917706889986, -4.967943580710895, 5.845378025489156, -3.878163887402751, -2.2051644144117097, -3.2909931866620603, 4.6063326222413705, 0.37251018870353025, 0.13269581038753575, 3.2467506049681614, 3.2313533204703813, 0.3305117264903257, 5.379504173059883, -0.6304673946719805, -0.2184051732485306, -4.798673733261925, 2.0178512807931046, -5.578437734167779, 4.135262295238776, -0.7018017485073825, 4.342080213465109, -0.2936152544936157, 0.8428781279667437, -3.0107129087374744, 2.400875191426156, 0.21577716612495745, 5.761591315646415, 4.506553383423851, -5.557851836551945, -6.5930375841509425, 3.6605402261329507, -0.9498444141981943, 2.8668360677576605, 2.5576773961995216, 4.994129190003713, -4.550827935406227, -5.880653624517322, -5.417314323740946, 1.124853168911466, 1.8950225406289185, 2.8303039280276194, 3.574834302557237, 0.4019073998739875, 4.246105793970305, -5.172175865916316, -0.45367873677942583, -3.9009155547350765, 3.655207204142714, -1.2903264084897237, 2.9584883332696106, -0.612984357201054, -4.840975166106665, -0.5282479958916003, -3.5454123614427235, -3.5750686102842875, -0.33864903766888643, -5.385793334707371, -5.860527680385333, 2.8987458902016465, 1.112480193013952, 2.817841740338853, 3.9407307858286016, -1.818912524607675, 1.3840181544804135, -5.695440188266368, 3.0459928544761468, -3.6244688931033044, -0.3529029850890454, -0.17754933378408067, -2.1314980425458594, 1.8910588545640783, -3.4111946658285586, -1.6394608229719008, -0.525082546379322, -0.3008596224050142, -1.964165337454135, 2.3566598218027863, 3.3242384023503577, 7.221459492629709, 1.3535769239155728, 0.6086754238210577, -7.505174326266625, -3.5889924545898864, -1.373625006427858, 0.9334891132192247, 1.842007285497492, 2.744119072006313, 0.36565669685972724, -3.74694919340986, -6.015979112544209, -0.35049633902720645, -0.7340690095484725, 2.5505514549233013, -5.22403273879117, 4.296912827531655, 3.2646896068080205, 0.8496902262588253, -0.5060036804472842, 1.8417095703374868, 2.674676410529201, 3.2939827116203757, 0.6037150840546892, -2.1006490212277327, -1.3035004732491946, 3.6131461540605683, 0.6709019377719838, -0.1641126333957451, 1.0228100893818297, 1.111897685297782, 6.754399497931441, 1.1924228465850257, -2.705248708075279, 0.49547074337950203, -1.7249353880373135, -1.3176404521205294, -1.7639222364225116, 1.1132934634723397, -1.18771773188593, -0.8548752122019789, -1.5036974561728278, 1.4377499668441, 0.18114392582449046, -4.1439337533297484, -0.5387272464118156, -1.8270241125937847, 1.9638791879106843, 4.364393130395925, -3.768661472332064, -1.6354606022640543, -1.9590065140497648, 0.00845929264771339, 0.7987798527293348, -7.221859326980817, -1.2950053277055344, -3.7540337472096157, -1.5989998417038784, 3.469910740547415, 0.6349333467024338, 5.177744791282163, 0.7721341174101994, -3.0983588589810536, -7.1447252149432146, -3.3107044030447748, -5.6078257978090305, -3.9557851382767053, 4.320042587237298, -1.0108992633228533, 2.2360337980047618, 2.246763846735, -1.5329651995030542, 2.4016345517111812, 9.270954374592609, 0.4055851878361767, -1.9420974372057545, -4.226241299033258, -4.846397293589364, -3.3474923196109643, 2.2819238815663407, 1.3647745392743134, 0.019726498545270754, -4.519688923384723, -3.5504071092928315, -2.286369083779883, -2.635570874155565, -4.351312840172147, -3.9391221674133527, -2.65206103570629, -0.20834745118128395, -0.7146724175569532, 0.18989226092240452, -5.020386785685183, 0.6636650478459476, -2.358218312178761, 1.430076584678253, -3.260177604315806, -2.815821260284343, 2.3203284179796992, 0.34835203039454554, -1.5388883792487882, 2.6078790177519346, -1.4234845244983754, -0.15233937282330667, 1.8742978912745407, -2.0074020036168907, -3.1950993313927585, 3.316021447461546, 5.459989567450529, 0.822727962109802, -3.331121016751858, -1.5377863900825512, 3.433944652196633, 2.073819029604704, -5.6188649053290165, -2.7190444909837765, 4.233350910699473, -1.9621180228967259, -1.9163967605406416, -0.3632588234377474, 9.553048320817576, 6.879763943719858, -1.8578952338684103, 3.5712516658960034, 1.241658664768317, 1.1048264122645075, -4.533077922460073, 0.13588110816784882, -4.859872870479695, -4.389678462602902, -3.966094133316383, 0.04997907995405759, 4.1377694869427035, -2.3428093872227964, 0.8931012630563229, -2.087235747696343, -3.0379866118637042, 2.252224300470005, 0.870637469891351, 1.022091203661088, -4.086986581303462, -3.5369227672381496, 2.089727515469936, -5.01329573418716, -4.462948424459953, 2.3429461463627295, -6.044043276444463, 5.999686915869682, 4.550609068702766, 3.9348288319354134, -0.34404610313357287, 0.2451266477520757, -1.0914153309609254, -3.103720795655744, 3.7143241069270756, 0.5397443950115723, -6.681694304745578, 0.7657886008212651, -3.533107851646597, -0.41436008973281924, -3.0360930334188607, -1.722398809856445, 6.647536536009344, -5.364899526651365, -0.09127697412389102, 3.0122415902463295, 0.18012515861071066, 3.702829120948052, -6.102340422664964, -3.671791370464409, 2.5193471456585668, 3.1701799653661134, -3.6979334121663907, 1.8512903513855523, 1.8972426297613936, -5.108599501919002, -2.3801992452567706, 1.9998234152630658, 0.45753183843522915, -2.4559876966944554, -0.04679761973575325, -0.32662275263143714, 3.3437508498085178, 2.8427289469780943, -0.33252101369966014, -3.4799237321447043, 2.838025817607355, 4.4163980646309735, 7.8329811014518835, -0.05415041964865419, -4.4174257206615, 3.2557380448036906, 2.572737253083457, 0.9174398034426989, -5.110736053161594, -2.6101000362516826, -4.040876300357502, -0.7876088491708894, -1.541628536043511, 2.8199200879537223, 2.0612932514282294, 2.182277202696687, -1.8010203693014097, -4.284010925764804, 1.6340637920796546, 4.171057342424542, 0.04237890782364406, 3.593467059673456, 1.0466758990595295, -0.26223768794342495, -4.062704999943825, -6.659893541312851, -5.742832145662975, 0.27124776230266123, 1.1923244359240095, -1.59292975549896, 3.248382122178546, -0.07748682185994848, 2.7088369771597693, -4.749809530729332, 0.8153745804731523, 5.501389529272284, 2.5689246090779707, -2.090969613697195, 2.099278123240471, 3.984716272260629, 4.718164426829919, -1.596269610219109, -0.10779650000270458, 4.357032402513263, 0.7649247009435103, -2.0873345607467337, 2.8482236170825104, -4.112377393756543, 0.14389128380530591, -1.8663073040093225, 3.089407035025749, -4.745590168707875, 1.2709496701617762, -5.828900262722034, 1.9419027206794723, -3.591034130355582, -1.7181269422935925, -0.651293549856004, -7.585316617712181, -2.4671333532127346, 0.6880413571242774, 4.05399687615196, -1.921441654878382, -2.1991203988661083, 4.658448526920943, -3.000741661549213, 0.3666351957052345, -2.3057032565275, 5.106687988187875, 0.5948649016727237, 5.768352149838776, -5.385763305082899, 5.235875123171317, 5.582216039452477, -0.4583550569635443, -1.0242664181849928, 0.7910220790729061, -5.579816301123257, -1.1732308183281546, 0.07333263584216576, 2.7755269711055233, -2.1592299744505086, 0.399081164531514, -4.077037434903836, 0.5837337045374205, 5.820010081147451, 2.6866025954553843, 2.9627168705450604, 1.2235689164655605, 3.1130559917179923, 4.124943181964412, -4.233377123166117, 2.5792513541191937, 0.24728513091445503, 3.130792658534033, 5.2216666443437205, -1.5663558826395751, 1.632074872790069, 0.3100056058634868, -3.3088474733507676, 9.775754288736163, 2.9416693439075896, 0.38258796340189516, -1.065199879100312, 2.1968592486992247, 3.164388693724982, 2.213631727385048, 2.463491998122503, 4.713453893317432, 1.5956974474747052, -1.1871975586800299, -1.4667302779907598, 0.12566142727041907, -0.4923671798666567, 3.8471173129549223, 4.187312072333697, -5.880222403012307, -1.9149683040407368, -1.9703432023867429, -3.633232356699492, -0.03059343447285634, -4.688545672254585, 3.5511370415420362, -1.8439246116015608, -6.549080016475298, 1.5333552940474, -0.45459653021833113, 5.962611804475593, 0.11541282062020963, -4.421895866089831, 0.04936906103585237, 0.44213437980400294, -3.8196094812566352, -0.32813911281600106, 5.203993960160258, 0.2542232314395978, -0.10796619897805315, 0.9218317537366163, 0.5938482671788248, -1.7306732316942115, 1.0824872509553907, -2.6579913172566263, -1.1882575571822582, 5.640880083480889, 2.6460309439839573, -1.0512063045288507, 3.2345979980718402, -1.986540968810228, 2.7346335890358238, 0.33714226227582733, -3.144514295083347, -3.6944961414668205, -4.831805946346068, -2.764953473400783, -4.468821353006005, -1.1446018938313354, -4.465990093439515, 0.7455012508226693, -3.014807384345416, 5.77319616988508, 1.3431224225738125, 1.7804519433754122, -2.1369875462724144, 4.819355571391714, -2.7872435520827628, -2.418103889923647, 0.6171485060462893, 4.292479512244387, -5.16125653711664, -6.848120210440639, 3.4726741898895037, 3.558069270703621, -2.0580202349334673, 7.751445438792425, -0.2640245692284392, -2.9849562965059206, -2.86991257521367, -3.972164720201222, 1.468412013767355, 1.5867731079719984, 0.5086753132206661, 7.039684581619079, 1.4995334761419707, -1.0867424298823511, -2.577441826596666, 1.2879502511829548, 2.580525334292728, -1.4707781208408446, 1.196332019827154, 3.1380177725424785, 1.8509913708077734, -3.2338224392691255, 4.544987137525251, -5.333909074768391, 5.131003868874492, -3.716197154677186, 2.7259910539942176, -0.9961765818932077, 6.458527964730822, 0.15388423110027172, -2.3097793026045945, -2.822937957781181, 1.4493675340046432, 1.6620177988284115, -2.7112905101921734, -4.000773748163532, 2.8409885308070133, -0.7596785330143567, 4.19680023490831, 3.6157646401822348, 1.4631987305769805, -0.779308033129305, 2.4495479753560203, 2.556153789060389, 3.4105438475512955, 7.673171810429389, -0.48872627418311065, 0.20192082326253535, 8.767642579540174, -0.8627683022267479, 0.005507958750583075, -2.2748796311640547, -2.6006756745817547, 5.542197852021543, -3.703326104279337, -5.715544959401865, -1.0470507356394763, -5.834411563459331, 3.2199816997576223, 1.3061038712237059, 6.798499134272802, 6.258613038423682, -2.433181933303998, -0.7511850349359881, 1.6439360593245982, 1.935968976293311, 6.908343471865438, 1.2000375899792104, 1.341016167272607, -5.410309537366781, 1.1726732456280362, -4.871822483558041, 3.7960418360697927, 1.4764106320406514, 1.2435053980106137, -3.7303068008637834, -4.980536149489216, 0.1993834583555012, 2.528246284894025, 1.0523664872168697, -5.082504293397722, -2.0088126372875745, 5.593868474108691, 0.4159498649238651, -0.9751485463751464, 2.825329500542878, -1.5860274400795096, 0.5123560200029531, 1.868169378509355, -10.791623260555433, 0.9766120802518861, 1.9508609540505506, 1.8490643866156313, -1.8583211593189608, -1.1860600861337363, 0.08115184346180992, 0.3569310343864034, 4.557001763997379, 2.358677563285939, -0.35622420163643, 2.133103110902762, -1.8425782367336068, -2.752827774126545, -6.712215735822003, 1.5427693613487956, 1.699841118166384, 4.337722036070826, 2.0686910564586007, 3.8517151141464314, 3.3709676181560466, -1.5410088677362483, -0.41965438234548325, -0.30403967262712095, -2.2072603616282676, -2.060834343041635, 4.565270795153049, -3.5512558133168555, 4.053934468134131, -1.2830699276286168, -4.090050414342309, 0.6234782653721735, 3.7480637689611758, -1.125597742714172, 3.835694276273884, 0.9323737284854019, 1.2731329560705849, -0.1645968021957176, 0.05182921243268135, -4.961018667160215, -2.2640658010525403, -4.890572680014361, 4.601258997402924, -5.0331234146071555, -1.1943953927664555, -0.21029964766161324, -2.177991189094694, -3.5411869367345763, -3.5881516259611885, 2.654159032895362, 6.668594161033996, -1.1898062353929553, -1.7583836538845625, -2.4226987796775994, -6.808539233907851, 2.7497231692832047, -4.642679484060878, 3.5659459698391487, -2.667710880444453, -5.6989537810158675, 5.560908915268051, -1.4257526226471278, -3.557755955509514, -5.11397636234199, 2.74461703693693, 3.2121088048110122, -1.1913585676701628, -1.4918768621819019, -3.5887111419827624, -2.8112080811092475, 4.1036184839401475, -0.5489814222515397, 2.9840737433146804, 1.8788415052271663, 2.7417814456419545, -5.0714423138222875, 5.452900297349067, 0.8548566622819205, -1.3831874752838578, -2.4381575708078476, -5.227508275583359, -2.765865539509127, -1.8255265065712518, 2.3887361509376763, 0.8579188695158653, -3.6791765107217342, 2.8669611376984907, -2.2609429254805815, 2.387615876214644, 0.6940024696773197, 1.590094355155836, 4.935907414644285, 4.644320806242175, 1.645547716551543, -4.494976937973973, 7.4592302342658865, -1.6881394602325461, -1.749518935041073, -0.48921114343091743, 0.40560624552503866, 0.5451679503613054, 3.7051535112377714, -2.9861423560907214, -2.577690257253768, 0.4356358527450013, 1.004985511253797, -2.3497773200898795, 4.486942278598703, -1.9053300432920484, -1.2956065933413121, 0.45619601413099153, -1.0896831591249707, 2.4421264195657892, -1.8280776622991628, 3.245167288287565, -2.062430699761965, 2.437320251219588, 4.652150754427, 6.901089518642324, 0.005180065006156864, -3.277936090125458, -6.522573799491666, -3.90528890235868, 2.3496107841586973, 4.008268962845202, -6.979948279632608, -2.2882650822124546, 0.6041655515765281, 6.918989116538442, 4.032682224911676, 4.6623924068867115]
BIASES_LIST = [-2.338566499288121, 2.702506474613936, -2.9759312955168573, 3.4391513112373158, 5.659207965901427, 2.3732130374265354, 3.917825221635592, -0.01282564714794876, -1.4350420925939515, 1.5445810107566142, 3.3361426225831874, -0.31627907404574607, 0.8417242433118435, -2.9882312692109494, -4.559691210068494, 3.652413595438766, 3.2541600856132096, 3.3124579863107453, -5.773574293053924, -0.12752422045875944, -3.4732981424187903, -1.9112732439891664, -3.136921244212396, -5.184246130973874, 4.886169772764261, 2.9467177977089465, -2.825412637776842, 0.03848178874453856, 2.7186440684866886, 2.2239198347753177, -2.2818391636128967, -1.0172409393206518, 4.238215476531746, -1.518249456813758, 0.42958448416138806, 2.364588800420019]
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

