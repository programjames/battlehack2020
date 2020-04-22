import random
import math

WEIGHT_LIST = [-5.778707618323735, -7.558613288551923, 1.283303702724126, 9.492291929953392, 8.781221301838915, 0.6702855948707338, 9.092504080012954, -5.748167236905464, -7.043054989937607, -9.349322029403996, -2.6575346026072992, 4.8882391861482795, -1.2793564754127082, -6.76372981819553, -5.649843964825378, -7.600601600219623, 4.526709306705559, -4.254476207228414, -1.535950880020751, 7.813596214324047, -7.855179574403868, 0.3806511763174427, 4.347038686805103, 7.851058956593558, -4.557567000645544, 9.358239570744825, -3.493273355170519, 8.560463651191306, -1.1072831108337446, 1.5529267540650267, 9.782444726255662, 9.022102086380286, -1.4638370616011454, -5.608888754706838, -8.14042797233591, 5.506558187242206, -7.21713448963079, -8.884480314350832, 3.9636035230422557, -8.81991393319874, -3.6386491819315943, 4.266313521224745, -1.3101816136445859, -8.67178227083352, 2.3998819429595954, 3.9500748723169288, 6.389159109257626, -1.7186607051867693, -2.1432509646457536, 4.23497281499974, 2.21496161872434, 7.686482056460548, 8.530168594336903, 3.568302123710369, -7.393788544440394, -4.187088980683855, 8.459868287527009, -0.013234772256563332, 3.341600670786475, -6.366776790113957, -5.0239596763169665, 0.44218197944541515, 5.945921598337003, 6.860028938318614, -3.742210175764294, 7.796315618322531, -8.603795560262027, -6.9896383851621895, 3.015077013982923, -2.5061059858057515, -9.183480005705235, -2.8187790077565644, 6.860169521465821, -3.930026134345532, -4.151643142722881, 0.6175483219257671, -0.15552296782391117, 1.7897978295111727, -3.5181769354500787, -3.8909791437642527, -9.32414995511007, -2.6492186564830806, 7.139141692419031, -7.868675641660936, -7.407331016919853, 6.852541587111311, 0.4410014105146409, 1.8612235797759418, -3.630354183643001, -8.380483706404675, 3.0336970024059617, -5.709833404753876, -4.4097592697798405, -5.795038648849973, -4.061003561518072, 9.521740194926736, -7.38088415785819, -3.1188906090519115, 8.483126432886017, 0.48972176742444873, 6.974926027052039, 8.13587009495939, -9.661713564026167, 3.7168075385840957, 5.005411337390427, -9.447503567965764, -0.4332273575303667, -1.8724416045511205, 3.65709134523466, 1.4083428011385646, 3.668465343077976, 4.079983401688983, -0.2839141727338834, -2.791377930121442, -1.9746534743021513, -0.4925008082970521, -1.5785020114117199, -4.131447972500166, 1.4984503887920742, 8.80851758022547, -3.86339120878481, 9.80970831632688, -6.846604151061452, 7.226789043713232, -0.8653013184587834, -2.6538932274264475, -8.236493267152511, -3.91034482826627, -0.25054112471599765, 9.804916057330082, -1.907087258858283, -2.4136686260304474, 2.7881375627609764, -8.811215510419618, 1.526533915289253, -4.339591519976969, -2.7558047473299485, -8.932602048469153, -8.361069964393458, -2.8390385180166504, -9.564708293867488, -9.484565065626622, 1.6568723966071452, -5.8065742827267215, -7.697960897214571, 3.4048617524273155, 6.252337045915915, 7.907852242907815, 4.747745467879463, -3.420627555160438, 3.568943228995529, 7.676829129210773, -4.806456146005587, 1.79076951988071, -0.8533406862481598, -5.657047275010109, 9.244245642456693, -1.344781029518515, -5.377771253052888, -1.73413611348521, 0.2032531155793844, 0.06395086266735639, 6.158697357771249, -9.382757714986012, 5.268136105561718, 8.022825917637611, 4.368614892153374, 6.167897214557719, 7.928714607240757, -5.196127016830506, -1.6845472118256488, -3.626511840997477, -4.340667347461331, 4.044751328433895, -0.4164102294527936, 2.053567532096901, 3.5231377865325797, -2.529469369770423, -2.2325045232644953, 6.652531491305975, 1.9851364246827323, 3.036997252358411, -5.713238719708132, 4.546208778245548, -7.049994422173869, 6.3680894968381025, 0.6516353614560515, -1.3183386946254938, -7.770101183146345, -7.690649861378953, -2.787931802142099, -5.12011040769925, -2.10158839467669, 0.9489722070508044, -1.957070113387683, 3.044221335985478, -2.22514720808271, 9.538607717696877, -7.62664065167078, -3.6294857107582867, -0.0886025656002154, 5.68743756628918, -1.741646944794418, 0.19318053086160702, 0.338161592815835, 9.166450085496564, 2.4639049017079433, 0.2954002865976122, 2.5365055027823047, 7.892087194854646, 7.360543305373874, 1.0318132690137176, -3.688995795381958, -7.886592623240389, -8.971958444839858, 4.020589229059176, -0.9850281324287913, 2.199294437852773, 3.8741086714383925, 0.5254993910949928, 7.452249800836778, -4.259727503077921, 9.500772145147007, 1.6129258183849196, -9.298942446632598, 7.533508436049029, -6.6322012095060074, -4.864688398488656, 1.523107977882443, 4.642297654956485, -5.017366474418187, -1.8621190377273393, 8.658138057059876, -5.426089524852918, -6.868061090069699, -6.063578434330987, -5.951638864441811, 6.5145464539897375, 4.744022592582631, -1.2357233901927565, 0.2207592685421904, -2.5392251814933786, -0.7499578527732442, 9.417895408155918, 3.0274344286409, -3.6910974999515496, 3.5808881517930207, 8.44341467901656, 4.966577471632171, -4.606634739624937, 6.289283542536843, 9.455056954732065, -6.079617703951971, -0.05355910600176372, 7.540164052411733, -5.714112836352296, 7.596154692085552, -7.657236707473876, 2.282817013094995, 9.712117726531677, 5.4302586292965405, 4.45740939652406, 7.251842617004879, 4.667027821479513, -9.332514790948455, -8.570772474471868, -3.8683102755035943, 2.0778262056053816, 7.353134692846247, 0.8556020402516751, 8.743078586185803, -5.241402759994342, 5.5467937448732805, 3.7221324774114137, -3.666537168708615, -0.04395840327597256, -8.396396422084138, 3.493382893188137, -1.7416362305372743, -1.6645819648951754, 1.364087892813373, 1.714604889089685, -1.6674452092000571, 5.841951070141365, -7.241580734257596, 6.518198582720586, -0.8421931167712575, -0.6929908760852292, 8.009531457554306, -0.7206733309079603, -8.038633679703587, -4.117916002065554, -9.433313967413245, -7.935342915981874, -8.318106814103858, -0.6323763445047561, 6.112050086482938, 6.853103126471133, -7.221322984510952, -1.5317276504163164, 6.576420262874926, -7.120449575433461, 3.0987292560793716, -5.701871458598244, -5.009196037975261, -1.8232411957694872, 1.4178429192375255, -7.914417518204379, 6.539356197345537, 5.336652801678248, -6.981010377714356, -5.914977372927915, 4.0605714979464835, 5.180853863997793, 5.7146061330667575, 3.1250615287016164, 8.831692472242207, -0.6422592036004033, -7.364033039922841, 4.277173662119594, -2.692400418340668, 1.4751282472296374, 9.502922269349341, -0.6881812995234053, 7.559187782748467, -4.82888960800556, -2.760511505050731, -3.9116189796846212, -3.4821919594995476, -1.899499586063385, 6.555896781764282, -7.786856332679275, 8.628062266838146, 5.867442319479775, 4.705451894063318, 3.293238404068772, 7.07358475843407, -2.723493226005898, -7.660641071657615, 2.6992022173022505, -5.594316561724446, 7.789151467378577, 9.660602396705691, 4.409648501857236, 3.904831293921113, -0.3754005699922036, 8.624662820268355, -3.360559511648229, 8.576058679626655, -5.786413939934163, -5.692271152155694, -4.147038890035204, 0.7729464555129901, 9.841109310713463, -0.11806804039473384, -6.781934013354023, 4.083677619875461, -3.809629477847823, -0.8884068976745354, 5.113711912856484, 0.36406720787293345, 6.977543511177011, 6.87613130160927, 0.05865183367440174, -5.373797874718318, 8.983357484375265, 0.8459890688645206, -0.23419637274401772, -3.9311056312988546, 6.202274547495804, 7.236035319037512, 2.0654347949785183, 8.991140032001248, -1.6643599934089899, -1.4579358343881168, -4.596329725987303, 2.033540323702832, 4.587256980562042, 9.88294285764368, 0.4777433774313611, 2.88451473861503, 3.5612366290683095, -9.784432696432972, -3.1973441439090644, -0.9214493008151763, 9.117115857850958, 6.67411008226895, 3.4834961244557014, -2.7546235307534017, -5.32070113132495, -3.1639379308844795, 0.43866125782306575, 4.298930052904279, 4.884770138037657, -0.2404976235640568, -2.1231571165456042, -8.56656862445675, -3.4994267870478595, 7.340704030477113, -5.646577427008914, 2.369897946134154, -1.4749826642565012, 9.764091168751673, -4.984655564444633, 3.835746408194435, -0.8631390649218709, 1.5564170177205412, -1.7460355671067767, -4.383351352421718, -3.845602173356262, -5.85368536232683, -8.802330347567706, -6.517100093860448, -5.716184652630087, 3.970569677611355, 3.4428725486706035, -1.020167935025336, 9.774647275348855, -8.991268458961159, 8.7584348066516, -2.882732438390823, -4.828657918145591, 8.5997884534662, -1.4311916881031888, 2.82876799479261, 5.4622196810069354, -4.767602598552967, 5.703993236034785, -8.262114423173745, 6.7995563557903935, 1.2052984400212203, -1.7817053942845362, -0.22875427321805653, 9.286715514460873, 5.255915875811015, -1.2413881200406092, -0.4054621229234314, 7.272495293409065, -6.257562155674734, -0.23144554877404744, -6.5270249435596455, -2.817325428659368, 7.729139101161323, 7.502459800076025, 2.9389585800749085, 1.164334688421926, -8.227803240678364, 2.5622051256189806, 1.9463133467497364, -2.332426534579108, 5.408398424851262, 6.279763094183576, 8.388076135758066, -1.1465778256383867, -6.718065572507297, 5.192671730103882, 8.671427426944597, -1.2426494156436618, 0.06431842420200162, 2.6121743210659716, -3.9587356112145144, -5.405312996283136, -8.847316251988158, 7.448671375407951, -2.9074965785307594, 3.4807956267692415, 0.17713552153798418, -5.872115750221402, -4.304093067700297, 8.085739107670019, -4.428172897044595, 9.134880707013629, 8.067344404739472, 3.387997393519342, 7.3063347121705, 3.4377582629119434, -4.048709501430217, -7.718229666766905, -3.875811774179903, 4.767598976710257, -4.200975470145558, 4.653293240102872, -2.6827854235090793, 3.7162305635008224, 7.817423306136618, 4.8439472340088905, -6.329247981966768, -4.251923949793022, 2.100487590380249, -4.985848321987998, 2.9216639752967737, -3.2446709507519866, 1.6130901426784412, -6.432291412114686, 5.948875381115556, -3.387848708222778, 8.291778793075672, 2.2750906508657565, 0.5649240197707073, -5.086716741713293, 7.312870056933196, 7.3117236521990385, -8.204906791653809, -7.0836348171849295, 9.873217660814642, 3.8739911172768675, -7.497501461625998, -0.11634230514537869, 7.470593748403381, -8.748749085284844, -7.211822043366918, -0.9222250700042487, 2.3716319687056497, 6.0208963721043425, 3.529644075728717, -9.630503753486074, -8.296335865433942, 5.545119062912507, 4.138635079689511, -6.79956175161043, -5.2576658864758, -2.839239656834323, -5.321936182192076, -7.655774292010003, 8.895522314753272, -3.3433256964206226, -6.384938476505138, -9.952439370253835, 1.9582968575008586, 4.529901057380613, -0.631715621578028, 1.5636896307501296, -6.345842660412366, 3.8775572902665374, -1.1145698536815374, 0.10048430282939336, 3.0416435284846504, -0.9048410343656492, -8.695892654764721, -9.042789093235656, -6.06292471753386, -0.09413993024712397, 3.9312712074216485, 4.876107776437365, 7.825251265402766, 9.359413911194984, -9.049670180073937, -9.05515763140825, -4.377557676429802, -4.003621924854032, 3.1730946809554634, 2.380019045910327, 0.38623607643083524, -2.41638522086223, 8.551444786624021, 6.1503614033527185, -0.61674304665212, 8.35627548207226, 6.840199791338659, 7.456412168592372, -8.5984871693633, -3.656557111756637, 9.999881967411909, -1.88686579342491, -2.1271139826227303, 2.2999480854082073, -5.150290723178439, -0.018423298593866377, -0.49364938040851847, -1.9629645514517797, -0.7415287390564345, -6.874786249117761, 1.5411428755816594, 0.9654606899586469, 8.644841652674764, -8.517299536449979, 2.025693377460687, 3.447523744728345, 7.864683775550283, -9.746257931634412, -5.11335788921339, -0.5574866699928034, -5.586059469029423, -9.766888359724518, 4.485011809150688, 7.134207723664105, -8.394258583603055, 0.6010722785880525, -8.071516667710801, 2.4759925567489773, 4.552523114168515, 8.653835129137317, 2.8188271056907244, -3.996054885566833, 5.233853090046786, 5.7803213352732925, 9.39200855422197, -7.31103658336643, 3.45762983947262, -5.528241146233828, -6.65751328830188, 1.5093006140778797, -1.5223926666292158, -7.540800237772361, -7.671273869482668, -1.409845459156827, 0.23195152827142174, 7.086714159772086, 6.6230846993208345, 7.386828171005742, 4.222897890116975, 1.8369608582720787, -6.322979056977038, 6.1105672201353585, -7.573532284825726, 3.4155124876542615, 5.771724454622211, -8.921477546470529, -0.43399304559244634, 4.139789922922802, 9.726039163124597, -8.564082785111856, -6.726259774136523, -8.29939439740118, 2.781314927178432, 7.0577369064153075, -4.969083059311434, 8.685366256084375, 3.027624181011788, -3.1645608524836693, -9.975710374537067, -1.970639612882417, -9.719026579340738, 9.549680775694728, -7.68625144668002, -0.477649983692805, 1.9698161106463292, -8.358439624571263, -1.751471059626045, -3.7146569758926296, -6.826080760186697, 3.1712849443922497, 0.9995694356933633, -8.675840002411041, -5.216612989812058, -6.051336278043145, -6.700869988921367, 3.070017536825624, -7.962670924671178, -7.028980034038909, 3.3104184402411647, -4.151274078189038, 8.830237938545121, -7.107847727586494, -7.047615288018192, 0.8767163263446882, 2.1693276095758147, 3.7884083242275786, -2.775115575094227, -3.1848577927687494, 2.190362576022391, -7.729708849611079, 4.681089300445166, -3.6067698294553967, 9.564036899207306, -9.558551641264781, 9.9657908030468, -0.5777407897203695, -8.923715696162377, 3.6707113265265985, -4.58216979143409, -6.932378570151614, -9.11540149483363, -7.834444175491573, -1.94560875422704, 4.509913022888117, 4.150041392257233, -3.7453180548194043, -7.806143915554431, 1.3543954137271754, -7.363275642955953, 4.482339541126571, 3.9978370318543632, -4.6296957066619875, -8.703726536003092, -2.01267254402012, 3.897853430239662, -5.616314796120106, 7.570065310700137, -5.377879763186462, -2.071463236186302, -1.1702669247678408, -6.75733381294749, -0.014590613599679614, 7.9166376435264425, -4.23749311605561, -4.804792392671078, -0.5137963581442371, -3.631150811583222, 7.7512393686493155, -8.348531174169743, -7.96680199082364, 5.468526641497542, 8.666888043308475, -8.737828088070085, -4.275187596107324, -8.734987481069279, 6.501974777287344, 6.0172672236548586, -1.6556249548875641, -2.932569293524603, -5.008384034930236, 2.964266600593156, 5.008724162682494, -6.035886204340657, 7.436192330054784, 4.816393490161236, 4.519960613844503, -5.711762860246443, -6.667581046153681, -0.9225522634414336, 7.550193995624667, -8.40816601428548, -3.4022047990999438, 8.486602899880612, -6.049543726878886, -9.60471180355247, 1.302316342068714, -0.4436527911441033, 4.498694063237046, 7.115394809128855, 3.1796745231693144, 0.8639425945101387, 9.531757687733645, -5.460478485774294, 4.362879717988108, 5.024246531947831, 2.98087438173466, -1.8842941728089038, 9.361023464700125, 1.5733449448491132, -5.871626628199809, -5.112100169455855, 2.0283178888246596, -0.5399053591528329, 3.6192810389941084, 8.688317173790399, -8.333703472229486, 0.8408111608956546, 0.65439684621502, 0.2887830268722773, -3.3390890336463075]
BIASES_LIST = [-7.737071700560543, -4.508150221414922, -6.197235436632187, -5.327575165715064, 6.089497278642103, -9.930815328684588, -7.145445388244962, -9.974258323484545, 7.19318112190534, 5.056499133266142, -1.0903481302373486, -8.423162911782068, 8.819138829377817, 8.970089223094021, 0.34308053403552563, 6.341853005450439, 7.875946134818346, -6.795135502906882, 0.10063530572271517, 9.583088832694983, -9.368479992426487, -0.10018983709382745, -7.867650656298791, -3.6833092223448594, 2.247608401479342, -8.70336645435314, 2.39607161907751, -1.1895446455167598, -3.0997537522430036, -2.71164499257093, -0.6683324214197572, 1.8288876549718136, -7.680632194869819, -6.22050950209061, 5.924931037095176, 7.2769703505323875]
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
