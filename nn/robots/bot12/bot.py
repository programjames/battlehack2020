import random
import math

WEIGHT_LIST = [0.5627329694714599, 4.905711721832402, -2.317000145389442, -3.5556991930629445, -2.3186332898027144, -5.291995534635032, 2.871383484930457, 1.8270404904224609, 0.8099140484590097, -1.102422458473607, 2.601236368448298, -0.015281983205306464, -0.9059115255178593, -0.7596096128128118, 0.2370058773473709, 4.9349253128089385, 4.6822276417944835, -2.9806163507665575, 2.8379589453775003, 1.8266600430174669, -0.37578244724632104, 4.349127316038412, 4.933968724055935, 5.412500201960663, -2.1182738765856586, 1.6133950176796437, -2.189300362470206, -4.352722198347833, -4.904979276200719, 1.384567514596273, 1.360825729346569, -1.1169790640133725, -3.3943660284191073, 5.261305433131199, 0.9962732981703432, -2.4999402926852774, 4.150425575902427, -3.2866133886023254, -3.7522411732573255, -1.0354385300152098, 3.825187544148736, -1.8614905253601777, 0.433380614142416, 0.15959520924977016, -3.2617528946995047, 5.733104872089697, -7.884879676798488, -1.0382719143176775, -4.615091116085602, 0.88107189648388, -3.8471842026222256, 0.6757254261259177, -3.578108670455009, 1.8899576112302283, -2.2498751357695075, -1.5897400109710074, -0.4147148530185511, -1.9765631120857392, 4.895361024549894, 9.880966530975991, -2.1930226810402575, -4.498316936372825, -4.317445433364628, -3.518913197955722, 0.7307533676350764, 0.20086766765113864, 5.360381260903233, -2.1944014730674772, 1.2288397240358724, -0.6908747282038978, 0.44605768888096003, -10.340006017893003, 0.4877060800231539, -3.689769734697467, 0.0425708160705794, -0.9742987153892247, 3.3941830205246277, -9.79989248397425, -0.06897490849748422, -0.5698166559368248, -2.4177551815621245, -1.1089528921688656, -3.258731981853415, -1.2116085523852314, 1.016422553052284, 4.815132510829971, -1.8338690535019988, 3.992026763330628, 1.3684097675896862, -0.6931064860963344, 0.9974539014064857, 3.7812351011196297, -1.2478810082406566, -1.064619366260182, -1.5776821050143457, 0.5348886594275774, -1.7513368663039406, -1.1328766020241214, -0.6235574020524043, -3.693135285722848, 4.117932993593475, -4.8199344891253695, -2.3298641859811378, -3.613786300511642, 4.937797323527318, 0.7484146215614316, 2.6992370120084286, 2.690172908206631, 4.966640816338823, 1.8807744256839685, 4.388741711690968, 0.6006550159222809, -0.531900567996568, -4.313160409196664, 4.451456119603691, -1.706860191432981, 2.5535066292655992, -2.7680469913295234, 4.5678750601806755, 0.5697540366049458, 0.6272646758342546, -0.15770615165121052, 3.59348907115452, 2.614542066921277, 7.00333272461575, 2.4375914453928336, -5.358730756476464, -5.637312184845676, 2.550262196694508, 0.061433291232329476, 3.626169376205864, 3.8466998261007106, 6.508712460617962, -5.742651197793779, -5.1921809815684545, -5.156984542317908, 5.246154201815505, 3.5126585966801263, 3.5720668422658197, 4.5496422077172465, 2.0751933225533246, 3.475918478998678, -5.225550801667523, -1.0539009842289582, -3.688777493677971, 2.519829397396573, -3.9468521845652553, 2.4831839192094627, 0.45719917810234983, -2.486871084900971, -0.42144932581311173, -5.118148347265684, -2.422811499118489, -0.0038123387718271727, -4.153507221983253, -8.685961313095845, -0.22245943082841368, -1.8205491455982648, 5.461982109450957, 3.80605073202594, -0.950681245781368, 3.8450044989269903, -4.554718895056875, 4.483502559981323, -1.1257036641666456, 0.36601919955008183, 2.1051199347914693, -1.6876638943950717, 3.3700618333608667, -2.6018958047781693, -3.4552001632477816, -2.4202131374592892, 2.067187876928401, -3.2872319903593796, 1.834076265792886, 0.18899824484307717, 7.302602200776895, 0.1358044951211745, -1.2356997988607241, -5.375432743264587, -3.2232665589542284, -1.8759174586124392, 2.151987760257542, 3.6484307170767827, 5.117959669215568, 1.1308566817547614, -2.6284896687657113, -6.11054931235251, -2.505020071829835, -2.13389420160038, 0.08280735431992339, -4.281859135824887, 4.578523291556648, 3.2572186237700884, 1.9167845426117205, -0.42846409641287714, 0.7580649809147357, -0.5141434133036171, 1.6939045976517606, 1.7611259153334775, 0.13225876712631005, 0.7015666787842827, 3.03139537092482, 2.418959340130418, 2.2500391838816807, -1.357174565747883, 1.0363192264498051, 10.58267404934456, 0.5785823645450668, -1.1202325741179904, 0.6075401131047837, 0.7453015707829285, -2.938389677706125, 1.3011207650264613, -0.652885810140034, -1.7624990776721727, -1.6094824191660775, 0.3358389341677825, 1.2988059101945975, -0.753620296469291, -3.925246521692184, 4.079210905122974, -1.5768905796927384, -0.9550524376418111, 4.253481196964729, -3.5321785537228143, -5.028637085420958, -3.3205741440635137, 0.1587817872890734, 1.7435777009948648, -5.335328264255257, -1.7011152887433243, -4.6893443578145275, -1.644619097085775, 5.271019537555756, 2.405043681473454, 4.268841628988563, -1.1687952629333993, -3.6255265637348786, -5.9348701147740135, -2.5717582784442623, -2.5886634485632136, -3.5978302423100907, 4.860033356654347, -2.6007746075186584, 1.2053706359613767, 2.594241837873264, 0.21462795444127167, -0.07991590295935992, 7.12309065089232, -1.5374530290504382, -2.114394568262881, -2.299259615117672, -4.26701887379365, -4.851602240427787, 1.0123812640907155, -0.41761898976916656, -0.3543183958117378, -5.809037524736546, -2.5111941652857275, -2.729454626730679, -4.575254385117377, -1.8266853740563391, -5.908255474019833, -3.0652749464585582, 2.6869699320727514, -2.3683534929094074, 0.5947435259468041, -3.755898777727704, -0.5511948163238022, -1.6626121022231495, 0.17205269739823661, -2.8936413586900445, -5.61991990750318, 1.5249868264244126, 2.031056190881621, 0.20695682717522146, 0.9925723423787052, -0.7809656264799925, 0.3638270372671839, 3.9419855684542235, -1.0320211677333593, -3.892983015489381, 3.7526122777175663, 6.159096425641497, -0.07938569858179073, -3.3811583067919755, -1.823854447662267, 2.637604954764059, 1.7015903559316072, -2.9764654367707917, -2.693588347234449, 2.5498573065154893, -3.573885582944908, -2.265869275389918, 2.363930082691792, 8.833396707112332, 5.9442520122527025, 1.801499694275882, 2.0516323359874695, 4.563351309375116, -1.8783335132777261, -5.847992210595102, -1.7680755882418862, -2.3776126130167987, -6.863616611656984, -2.8822920861826895, 2.2985900629475298, 5.069548363613312, -1.4307107704904127, 0.6742303376568723, -3.9211451207292995, -3.595695377679867, 3.258941310941012, 1.8434622415110702, -1.7828650550852911, -5.645464354744794, -2.4029114771590816, 1.293050595254532, -5.592919278889795, -5.314907123624746, 1.2776830448129386, -6.804247939711723, 6.40353783272459, 3.4353838250644837, 4.602913687990468, 1.9974242665245878, 0.2820877235381157, -1.2747420337276936, -5.5670000324170905, 3.9662024616284226, -0.3303940825978129, -7.422578997691215, -0.09921479315707583, -5.0312563632891125, -0.5129963682213462, -1.6721007114929647, -3.4484988694270906, 6.515412040727081, -6.775483493695107, -3.2376405042541316, 2.667372900119255, 1.4718992161655442, 4.1898630827634245, -5.690889760981454, -4.631285709472192, 1.7025387903700904, 4.800669611808539, -4.853231487064113, 4.652954648352008, 3.2474610568767805, -4.022701678676199, -3.4029437929622586, 2.3175151310907514, 2.33845668203225, -3.3934749289598445, 0.03629756842151466, -0.011404440914666192, 2.814761813048692, 3.240986866748117, -2.248432298296182, -2.826448003704355, 4.9205130372406645, 6.053953105160859, 5.289833652105166, 0.12016106088703782, -5.842081654392231, 4.264544621167994, 2.6110014894635944, 0.8495092476090573, -3.2202073402988445, -4.713256286873461, -3.6697278667227957, -0.8924104433237204, 0.3436865254343969, 2.0689062961131683, 3.920250334817257, 0.683659977521265, -5.64981573752149, -5.258828464204905, 0.4247219725309091, 3.4259995866834223, -0.8707665475016971, 3.1690106396108226, 0.1251019695119142, -2.8712580602305997, -7.232349807353379, -7.881487350909653, -4.603889688418251, 2.465304351922767, 5.605306880856082, -1.6973580311641734, 4.703053660818973, 0.5176841684015138, 1.4436836638538888, -1.292284918135661, 0.3412661076056657, 1.18456161437236, 2.265893462864984, -1.5028744602827613, 4.291696421531245, 5.556741533132984, 2.710202821345, -3.4515578325463556, -1.7147698461717156, 4.542255664644836, 0.6991060962674509, -2.151381022916682, 3.8679267340523538, -5.552432782183231, -0.2988381309551102, 0.783400293199328, 0.9025766810005252, -3.273753931946932, 0.9691835187990254, -5.682485809418831, 4.126290432532916, -1.5823085674640298, -0.7118356078496727, -0.9916878506008413, -7.3965682287621775, -1.8395176984805273, 0.7578231246795124, 5.225258852673577, -4.349456234629777, -1.1467587702362725, 4.086132922081681, -2.748583623747368, 0.9184959610095081, -1.9444967941086644, 4.392272526099269, 2.78589197639745, 2.994320703059215, -5.904954661780445, 4.938121422856896, 6.183340394958398, -0.7277742471753422, 0.8055816123451263, 1.5817807063089764, -4.764012971591409, -1.6155370546495937, 0.6497202528720288, 2.0161476084424894, -1.8281411105671133, -0.3712236238319516, -4.319429003966149, 0.7136224775458243, 7.989026510054156, 1.8012341575697866, 2.9244206296887265, 2.4115478817157054, 4.511921036459491, 4.93561057065416, -4.362942816142159, 4.689945839342487, 0.0006230541251945288, 3.630575724478314, 2.5495663995509696, -0.384489181612673, 2.5151637301880974, -0.419693119527457, -5.913634422756852, 7.694326521365141, 3.68348008573836, -2.0484109515846884, 2.0709440445261356, 1.5004297540687463, 3.2003546092364186, 1.3733084341477686, 3.0496164839256252, 5.184287560747777, 1.6543927475691904, -2.3231066657907258, -0.10532243291423928, 2.49755053326458, 1.3471387265149877, 1.5705468718791824, 6.849696662338258, -4.280642226926016, -2.4566331078664954, -1.1893582600288608, -5.082314757766241, 0.5630726498147853, -4.351143608329149, 2.690780456977567, 0.3905481088797227, -4.410828309488026, -0.8202146812259975, 0.4775087341296905, 6.270000213433695, -3.2815843121850947, -2.8837782922224156, -0.6990367668056361, -0.24274804526578447, -4.864447904037783, 1.3606903023655503, 2.604227532948847, 1.8351505867816746, -0.3669530037693271, 2.729431507604698, -0.2895537105806563, 0.11766101831338997, 1.543255590160298, -4.736774313863132, -1.6585717377485316, 3.6060609235302805, 2.867666880946788, 0.49184637641114787, 4.251045894987481, -3.056365983743459, 1.8274468408246163, 1.0488519142729442, -3.775776159523599, -1.7930523271784307, -4.904834429116219, -0.9685277466909314, -3.9934251705394046, -1.0074606239593573, -5.972392819792371, 0.29959306342893244, -0.04445870573863156, 7.011032287833612, -1.188195331335814, 1.1031231734512885, -4.019936228500779, 6.959868238452046, -4.0774461726864155, -4.132880928828046, 2.0425109459778015, 5.101419542658475, -5.505325385273306, -6.406535059181079, 0.9129365635029045, 4.221834974755321, -0.8981971148271675, 8.074397972747612, 2.5230419682664498, -2.305933220181949, -3.337894288169739, -1.9905993376627025, 1.4679228317345758, 1.061846580785289, 1.4316193655628648, 9.02714329489969, 3.803793525498233, 0.5640133028315893, -1.2619059258326601, 1.8132909453316328, 1.5002163588745305, -0.5485222831544153, -0.2837995011766419, 5.9769154885833125, -0.11819640182654575, -2.7911115868081176, 5.406484082297774, -7.762806622135613, 5.254022231947053, -3.888554457366682, 3.4005087397166487, -1.0087985187436117, 7.805558056807339, 1.894425883203026, -2.256719975550994, -2.1804899418813015, 0.02998969915648036, -0.12292630464259807, -2.4647838217527425, -4.41760622112236, 2.214267543528456, 3.960131213771149, 6.043366216174397, 4.880919503362102, 2.2469983049141904, -2.1493706459299644, 0.03307687875793884, 1.8444598040076694, 3.7069637899587953, 8.938828650471766, 0.4058696838260296, 0.22345919199738282, 9.600630485549907, -0.6132143409866908, 0.5349815902198616, -3.188631254511546, -2.551645310926937, 5.775903098524202, -2.3433944796166526, -5.452778197860289, -0.2367279062900882, -7.359250963877262, 2.419847573359443, 3.083687845920485, 6.107912577731241, 4.951878026776434, -0.9573741121405115, 3.8076600224923816, 2.912214815331171, 4.110905576075057, 6.787363145603852, 1.3797223527128841, 2.301510533145302, -4.255067276727298, 2.022334699408479, -7.717252421992133, 2.1592917711563606, 1.2609755786617465, 1.222315034174768, -5.134721658380389, -4.5389875223758835, 2.360230193958245, 3.0330241587035354, 4.27394834040104, -9.132204848605012, -2.417224913687619, 7.442166253768075, -1.3564943395750653, 1.4410800489992055, 5.832617642753485, -3.4650934601138923, 3.1561903349276514, -2.013126288188752, -9.99118273303323, -1.050987870688863, 1.4757302309862874, 2.907262572230735, -0.9119752764531136, -0.6969682284199774, -0.8074407895619363, 2.2732038882011985, 2.4884870097294343, 3.225257144577344, 0.2839675957548336, -1.4204383724204863, -4.296701854643649, -3.2283945587350833, -3.4230645451359596, -0.7108324806417436, 0.8676669833957961, 4.224442192519189, 1.9531687230575532, 3.1790066566435713, 3.111126196108611, -1.4461155011799458, 0.1566542392978272, 0.9649869019438073, -3.0850957253820623, -1.6384176432434572, 3.4762946138180935, -4.0213966186275405, 3.3642811836718405, 0.5706628872820183, -3.6913636052872416, 3.44819921538806, 5.926647087733928, -0.44007575653356473, 3.2272439485175477, 0.3797254805110505, 1.8482358987536442, -0.9156454898812204, -0.2025094544575573, -5.262057227614736, -3.3592879278993797, -3.705278187897241, 2.338395595521248, -3.9040963672451032, -1.542988745016817, -1.1383118971458406, -2.0598227382298924, -4.901089793255243, -3.859101696613758, 1.9855981465131627, 5.679931447625922, -0.20235503079989592, -1.8318252883430446, -1.3558483794926826, -4.275070924934472, 2.3461817130056644, -1.5589967883818607, 6.690538268621241, -2.6731177592680897, -4.745556481114426, 7.889871022171526, -2.0464297391069532, -3.2784865953652913, -5.163873813872799, 3.0023938535353083, 1.5251336729068228, -3.5577724949203393, -1.3613750464160304, -1.5927625912665462, -4.81180674385112, 3.3322328261265612, -1.3085108419682248, 4.383533830026248, 4.630672614265793, 4.293574308336288, -4.909362423950985, 3.644020715325209, 0.2357284100571229, -3.400655103822495, -0.35646700006248394, -4.743016028446451, -3.541120912870737, -2.07608459396865, 2.5278507480573356, -3.40774050532649, -4.680071358293137, 1.4289152603311202, -2.754023391152419, 2.0111120672660854, 0.47155599146229726, 1.6703177101812687, 3.963908740470934, 2.932021434800818, 2.7920366715833453, -5.867468880833749, 6.982437512786819, -1.3629441735570846, -3.470635478854639, -2.848518087831513, 0.1438660452918213, 1.4941963959154276, 3.0363969862431164, -3.593377174847207, -1.0551353405415884, -2.7580987389197724, 0.5769846651105904, 2.1818512861562747, 6.125355731744911, -2.754492968260717, 0.09044787859233748, 1.4794581320125337, -1.2527635555151007, 0.7373278590087375, -5.739478963072536, -0.8396300473932697, -2.3838745933311576, 2.3592241178654474, 3.7742428555634318, 6.92536617126593, -0.8749795584395929, -2.2307784501999572, -7.979878736743986, -4.319468929682376, 2.9902672369029135, 4.224202160293032, -4.421024825559046, -1.774665115318057, 0.9764739065860115, 7.592826778449921, 3.759112113702991, 4.8755331338152255]
BIASES_LIST = [-1.3837034182627184, 3.710893506045527, -3.61432892462988, 4.793282653779513, 6.33428998660208, 2.7763622510851174, 1.0944747571948334, -0.08366152718986374, -1.1076090733804884, 2.652451242913091, 2.1221928597202453, -1.3611302178461684, -0.006504619961135966, -2.6178463715875444, -5.503097930495408, 5.268342276750482, 4.818196288696041, 1.4799327618420623, -6.560125441126469, 0.02549306608269275, -5.075130753066909, -2.8023965216785256, -4.062602720083333, -6.100325549928662, 3.929639943955927, 2.6539982204878916, -4.028295948691141, 2.9194165184098977, -1.0819887856691244, 2.2995870445453743, -0.3444243782252153, -2.2975280233668385, 7.123983091630456, 1.8511453395308892, -1.6824106123729434, 0.44116633525507465]
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

