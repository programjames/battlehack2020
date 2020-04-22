import random
import math

WEIGHT_LIST = [0.5552563465897383, 4.90343181341726, -2.3195933004514906, -3.5445570059588705, -2.3217776374199968, -5.287660122650041, 2.871611641603295, 1.825985582534972, 0.8013053593732272, -1.1030675114263913, 2.6048049474961568, -0.012642289028018658, -0.9030327060356702, -0.7556627515887313, 0.2391482315137673, 4.93240706352681, 4.678907821855184, -2.9834475338065154, 2.8342586214892114, 1.825414749735411, -0.377994244345163, 4.35043623851168, 4.934247868227064, 5.412420873009871, -2.1129379112416458, 1.6095662298492688, -2.1866766456127418, -4.357990139057622, -4.908033441342065, 1.3785444670578824, 1.3614442878049167, -1.1173279345465545, -3.394793357027654, 5.259389037704193, 0.9934962527163422, -2.499673916929877, 4.150127136160164, -3.2842650387364904, -3.7458500942745996, -1.0329024941333238, 3.8318390360821537, -1.8623453799629792, 0.44048865195500636, 0.16358955001055156, -3.2615774709197924, 5.725090074507251, -7.880965834789534, -1.0375006298642306, -4.6135171048378485, 0.8787678802226505, -3.836642672319414, 0.6724032976951667, -3.5802828477910777, 1.888960327383898, -2.255515466798569, -1.5911782646933421, -0.41469800496550097, -1.9777202066337438, 4.890167932968793, 9.882537904942218, -2.195275411143964, -4.4925323378667, -4.3156736149277775, -3.5228461042540387, 0.72622283924458, 0.19924261206291047, 5.359910191182756, -2.193663170266677, 1.2324607255866251, -0.6893216712235997, 0.45120505912030956, -10.348204102156563, 0.48969267433377134, -3.6889800357420994, 0.045629262181142716, -0.965426548738368, 3.3942370306369845, -9.80234072512636, -0.07205406607057445, -0.567537954726347, -2.41418395068459, -1.107309050705243, -3.249844076011275, -1.2215097474627192, 1.016308484088834, 4.804821374831275, -1.8327286388723305, 3.9947699031823265, 1.3616665180583898, -0.6866649826457475, 1.0005278273276814, 3.780972544700781, -1.2454803235513807, -1.061217605449273, -1.580019199585271, 0.5347631206215367, -1.7484159254489635, -1.1332414037892449, -0.6263252079612798, -3.6899065424474755, 4.120205784475495, -4.828985689802749, -2.329239621611038, -3.6115132054174146, 4.935673342233405, 0.7500680070116331, 2.6953141204316484, 2.6880101202377515, 4.963365077169382, 1.8812735630346318, 4.383881784313146, 0.6052850791614355, -0.5353096949935197, -4.313452551806508, 4.457913978168301, -1.7107283354990555, 2.55765111391494, -2.772174921608909, 4.561816250597249, 0.5753317476579437, 0.6285769668027, -0.15858293692325082, 3.6004922400723016, 2.62025339326803, 7.012389447724829, 2.4374416461222306, -5.3573082427466705, -5.6354035045835085, 2.555929482790684, 0.05576628131912295, 3.62586604176479, 3.847483514830896, 6.496833901521004, -5.748514778748075, -5.194654584292324, -5.160482302592201, 5.247098931897873, 3.506073274845976, 3.5654848793185434, 4.549024918757171, 2.0709859151187704, 3.4844577287917153, -5.229162690917642, -1.0539605374750673, -3.6845596082561483, 2.5189908690615335, -3.948196405165419, 2.478491787057627, 0.4673087605877121, -2.477448176830881, -0.4264205104915267, -5.1210487687289294, -2.4225006260275648, -0.00590504460481312, -4.155167618151987, -8.68104038700831, -0.2160839055314889, -1.8161328772223453, 5.459089988941039, 3.7986574273106943, -0.9484483161105162, 3.8395904288104394, -4.556886677687515, 4.488046629069269, -1.1286138905925696, 0.36807154461609065, 2.104673832118925, -1.6873067344831478, 3.373547449038888, -2.6029623418777907, -3.4508194671619417, -2.423240331834589, 2.0618379006074465, -3.285708527649733, 1.8387793161541341, 0.19404615005969406, 7.303999646185152, 0.1367951867146557, -1.2372263259235783, -5.374798302049373, -3.224220578196765, -1.8823336189817992, 2.148812007401934, 3.655306660938783, 5.118861742849711, 1.1292683637459435, -2.6299884945492793, -6.111685054287558, -2.5120546495196403, -2.131958587852426, 0.09066467742298359, -4.282635051478073, 4.580321015731349, 3.2539746890989347, 1.9123170397907596, -0.43305247837848926, 0.7584398478459659, -0.521524453127236, 1.6990529347582275, 1.7660365985547588, 0.1283942544778335, 0.7042206339445304, 3.0333770797763004, 2.4166426587124863, 2.246276681977956, -1.349692641782432, 1.0355150592312579, 10.581234858435558, 0.5774055995914215, -1.1243913971226285, 0.6024273526761674, 0.7548829260683603, -2.937122928738197, 1.3024912910074284, -0.655554547747739, -1.7559163229976316, -1.6058818603800995, 0.3398523139331991, 1.2980226290678125, -0.7463467710655131, -3.9271782892122973, 4.079470998452047, -1.5695533316341297, -0.9517763289619265, 4.247733758545769, -3.5275256251956346, -5.027912265751969, -3.326999252145481, 0.16129422208007216, 1.7365315560162604, -5.340665931951838, -1.7059911682269637, -4.686984483022519, -1.6470639282489359, 5.2761792839184665, 2.402022180885073, 4.281148944831458, -1.1709927587515614, -3.6244696841279813, -5.933551758940212, -2.5669932542022487, -2.589282511205198, -3.59571810023101, 4.864808983348851, -2.604881020049079, 1.2125615938066405, 2.595060490127663, 0.22086884460676331, -0.08015643779266436, 7.1241648613141075, -1.5413164851046952, -2.1164381059409436, -2.295446808246536, -4.270954537902915, -4.851094324365832, 1.0211650557970278, -0.4228967402571615, -0.34905147527069974, -5.8067517342528605, -2.5115252331371303, -2.7315775929477066, -4.579767330733438, -1.826261161390328, -5.906803727585064, -3.0639144517865895, 2.6918048089953057, -2.3697542569621577, 0.594820327616203, -3.761948724950984, -0.5526801439596117, -1.6586739344403536, 0.16419857014921566, -2.9010783704754735, -5.621116956449444, 1.523766582888515, 2.0296009799530617, 0.2062508720491264, 0.9983407629619904, -0.7779731694879667, 0.3650393241665477, 3.9487527835840783, -1.029243030380146, -3.8944899823273187, 3.7503733340837604, 6.159941415486778, -0.07619020061942418, -3.3814644425978275, -1.8241052616589641, 2.6379310468420054, 1.7027683253087542, -2.9759557155137553, -2.6957832658874312, 2.548462987027124, -3.5736143469307784, -2.260583505640121, 2.355314508722025, 8.82990041715305, 5.943274269975164, 1.7992087649176924, 2.0457913955987808, 4.561549929996318, -1.8787311349502946, -5.845718589342271, -1.7712301918780071, -2.377422265068658, -6.869603315760177, -2.884457603108216, 2.296622209833007, 5.065601793140557, -1.4246102243976788, 0.6770441614470882, -3.920650440743922, -3.60109986124179, 3.2580857628479705, 1.8469793919380562, -1.7799535946469665, -5.645801556556922, -2.4022623869430766, 1.289508545917401, -5.594409779728976, -5.319878266111703, 1.2776985994253227, -6.803778034325755, 6.407228209743777, 3.433299618865391, 4.603705958187396, 1.9983284651752107, 0.27760528433822235, -1.269208250695654, -5.558254741609818, 3.963443967433925, -0.33532284374631005, -7.431014008255808, -0.09536141912757794, -5.032630076799139, -0.510354910360201, -1.6750350930147007, -3.452497582361248, 6.5130879746430645, -6.781593039404237, -3.2361129762817096, 2.6614728540309476, 1.4771350373470238, 4.181982307268758, -5.694688820333785, -4.635045112448878, 1.707339463642638, 4.798028376815008, -4.854448885542202, 4.647984112802742, 3.2538234951923, -4.022894322156574, -3.4004087337043387, 2.3135152932149925, 2.3304053528812565, -3.3912783721131516, 0.031676689862526364, -0.008535375342541503, 2.8129597526463037, 3.244470308271906, -2.243374891813016, -2.8281580457119984, 4.921840521802227, 6.048723183362772, 5.284807988301774, 0.11325232891864462, -5.839213112738209, 4.260581899777528, 2.607005903723315, 0.8503728238114315, -3.22667508409486, -4.712649417944712, -3.6677531675310737, -0.8940544679284681, 0.34006951731189916, 2.074984265433744, 3.920869424268785, 0.6826894584587799, -5.649257854196794, -5.260316959025734, 0.4240453962574401, 3.42423376517187, -0.8691020893022997, 3.170768818488699, 0.12267979647621115, -2.872063648079129, -7.234690897265211, -7.879285164181563, -4.59898286608484, 2.464895415607138, 5.6082325649856415, -1.7009131768873489, 4.70530778765715, 0.5099076572563466, 1.4409507488515618, -1.297876545633066, 0.34307161816958104, 1.1764569700575127, 2.2635374302974327, -1.498597368841214, 4.293606618580001, 5.551471352681845, 2.71115386717541, -3.454225950721982, -1.7097181542639948, 4.54279905552329, 0.7014139609020318, -2.1487422133534264, 3.8670209703457212, -5.551764920610315, -0.2995237727582549, 0.7873201824468948, 0.901210705056125, -3.2748473559965503, 0.9645610956077224, -5.6898231182605175, 4.129392679706908, -1.577772962135146, -0.7113106203884771, -0.9978123479242886, -7.395500703246151, -1.8334188835295213, 0.7517576951427254, 5.2248458631163155, -4.35216211475394, -1.1499936354338103, 4.089611337672337, -2.742834809854134, 0.9159473327179941, -1.9406941475557347, 4.3935273039516245, 2.7845061182550603, 2.9891916585856526, -5.909432741150841, 4.935339221609992, 6.186546789353798, -0.7350860861654498, 0.8081466246236271, 1.5841761668306993, -4.760142001349436, -1.6143859642949459, 0.656010820083332, 2.0184597771391823, -1.8305106518192642, -0.37682593193363184, -4.325772516697716, 0.711933945489717, 7.989120588190588, 1.8039707596565835, 2.9302353127173215, 2.4134940502816646, 4.523953851987925, 4.943223816065048, -4.361501281161119, 4.688519043539933, 0.001901349167731936, 3.6289988052027926, 2.553715177734053, -0.3773708620442624, 2.5177315299102876, -0.42301445616574895, -5.913920864333439, 7.693190544699909, 3.6807195504434826, -2.039349448872707, 2.06758940826206, 1.4950453205613599, 3.195344504581809, 1.3743928377817831, 3.0501707139773555, 5.181889566556973, 1.6573125261084365, -2.319559792010845, -0.10906049816899509, 2.498541727102656, 1.3498410538090444, 1.5777859618767662, 6.845657892880913, -4.275531611925342, -2.455110637229467, -1.194566333086118, -5.080644693858065, 0.5673191600401892, -4.342022452382132, 2.6965755980163797, 0.3999338783158273, -4.412018669987878, -0.812941143302781, 0.4792237726010169, 6.2665428759373, -3.2862954848807173, -2.8809664381452382, -0.6979087666890357, -0.2403742192058954, -4.864202483821114, 1.3656568720256046, 2.6064571362784683, 1.8393919093663182, -0.3706793188280051, 2.7273667043111707, -0.2898737211663028, 0.11087352405879616, 1.5465900699614044, -4.742574857382189, -1.6609243112370802, 3.6066038388940087, 2.866756137448164, 0.4920428129499721, 4.255057902824765, -3.0550885576834323, 1.8206297322544585, 1.0538528295139744, -3.7780088281971937, -1.7949088321895996, -4.913370124734251, -0.9755682259772153, -3.9872070892229443, -1.0059549151692881, -5.974629651260273, 0.2954373766386481, -0.04519486287143096, 7.00707788520285, -1.1827558045286233, 1.1077851524665923, -4.02098418553107, 6.96048647193782, -4.081432524521385, -4.130056081014578, 2.0471652803050464, 5.107550027675846, -5.502554700581706, -6.405059558740243, 0.9161349495597898, 4.223871369231204, -0.8999393029594743, 8.079507162008749, 2.523685229135037, -2.2999996285928677, -3.3300498963689478, -1.9880681082025915, 1.4646198639870323, 1.062886062590392, 1.438749730121715, 9.025657189981475, 3.803293205548908, 0.5694016132146761, -1.2689471149096636, 1.80910065908648, 1.5010465121148706, -0.5517608992382187, -0.28865009510809236, 5.977164157478591, -0.12506924539464614, -2.791430751386954, 5.4101755394181374, -7.766688847819005, 5.250567151967615, -3.88103664847454, 3.39895448556198, -1.009139847385709, 7.8052675153165065, 1.8964218403492932, -2.255837751500112, -2.1875312887525027, 0.02904512469377243, -0.11574923796606099, -2.461075726248647, -4.4207304529210845, 2.216500474923631, 3.959385463483786, 6.041431180505582, 4.874601200619471, 2.2476169087926787, -2.1533429508119997, 0.029686916596250303, 1.8500262669176781, 3.7026383790957915, 8.937936064892872, 0.3945577873020221, 0.22921571517109385, 9.609516307981375, -0.6105222060096829, 0.53573010212521, -3.1892593378826315, -2.555410075482917, 5.774540408628015, -2.352197853396089, -5.447777491267269, -0.23684568658152813, -7.364091431872863, 2.425095735743707, 3.0786418012503667, 6.111104020328696, 4.944775410415943, -0.9499783981887547, 3.806627934066962, 2.918484186320495, 4.107468827489608, 6.790736858340502, 1.3853922373741285, 2.303002494709557, -4.252477191233399, 2.013933295636522, -7.7158663153979, 2.159873705496756, 1.2664668559678778, 1.2182754528292083, -5.140241833193032, -4.542118792453892, 2.360126525547781, 3.036674323668946, 4.271394063570287, -9.137318343568529, -2.419121080535177, 7.444461311371337, -1.3560886509920058, 1.4423463900333087, 5.8290092354919505, -3.4731583985036063, 3.165335276637712, -2.0070642552903553, -9.991217402834083, -1.0501871036532697, 1.47376435193739, 2.901200548025127, -0.9072034735988491, -0.7008412554980572, -0.8067954673393011, 2.276401212778893, 2.4852961065178554, 3.2271226080424475, 0.28171385602645166, -1.4176901708191334, -4.2911694632385, -3.2279376419348593, -3.4221827448473965, -0.7067337155363733, 0.8595483502542318, 4.2241138407753525, 1.9516981875888284, 3.1780651693995003, 3.1080899068705476, -1.437071868596684, 0.16688078727720326, 0.9621780361454575, -3.0814240267423183, -1.6469597432704937, 3.474550073652224, -4.016511403368715, 3.36305096112137, 0.566058274670646, -3.691762787093735, 3.4475705367724117, 5.923986584917061, -0.4460388967604472, 3.2269342651277, 0.3772265061144927, 1.8509099847147878, -0.9160658940256606, -0.20122514419556015, -5.258689149276475, -3.35599686891032, -3.7151508317225543, 2.3414253539028955, -3.895270640944751, -1.5416948443917091, -1.133997644119111, -2.057260494590412, -4.905621037446614, -3.8691685668930536, 1.988574363117413, 5.6782342779322, -0.2071842808841124, -1.8284117894023755, -1.3587213148524586, -4.279298129954516, 2.3459695209247617, -1.5567080927105987, 6.690153948652612, -2.67310896365025, -4.74378976859322, 7.8852394462209725, -2.0447940046572697, -3.278979280251926, -5.161293980975835, 2.994210439981669, 1.517840421708349, -3.5556553717861297, -1.3621587536306936, -1.5927837699690868, -4.80921274305699, 3.3302160857987966, -1.3078288573723758, 4.379214249693308, 4.633041301019823, 4.290722354592674, -4.910053443166317, 3.6507233492044184, 0.2404961037213927, -3.3959975602093713, -0.36498008500494206, -4.744015117438944, -3.5419449436640584, -2.070701248265956, 2.5217655718464616, -3.4105632447945466, -4.679883925518828, 1.434116254718146, -2.755735686243185, 2.014110045934986, 0.4713590297611857, 1.6705378815781498, 3.9717595200453713, 2.93775119015685, 2.795236719205558, -5.86907459796889, 6.986261801842116, -1.3585811806216501, -3.46690772018134, -2.842913772128781, 0.15290794034077176, 1.4927250627553255, 3.0342583452877907, -3.5975687661219253, -1.0487255190510154, -2.764125217175078, 0.5864760808898083, 2.1882011489421953, 6.123741091763348, -2.7567955587277932, 0.0933824574186139, 1.4792306111277918, -1.2532898531691787, 0.7299035317750678, -5.734728708641769, -0.8391658775547465, -2.3812415304739343, 2.3550508943496133, 3.7753662126000793, 6.926700744333587, -0.8697835897959535, -2.2349703940331236, -7.985477305003767, -4.327537156627438, 2.992599139799923, 4.2169585474455, -4.418189813613118, -1.7747676076189483, 0.9783012288158257, 7.594493342586129, 3.7537502773015867, 4.879666529120703]
BIASES_LIST = [-1.3819735094014642, 3.7099313946405528, -3.6200819762262055, 4.794790990162171, 6.33659599463282, 2.7736359522018232, 1.1043688123373592, -0.08651104713034087, -1.1071462524632107, 2.653958567033648, 2.1213423039590635, -1.369675726164442, -0.0025470735146658112, -2.6241751235728383, -5.501566810872712, 5.266197148153673, 4.821608827908062, 1.4758324577140147, -6.567285037715885, 0.022063155054348287, -5.07860779968676, -2.799375952070372, -4.0604614544846855, -6.097684925039008, 3.921805528046141, 2.650763112838316, -4.027619222472057, 2.9219840063577194, -1.0791076124153136, 2.303162740974442, -0.3392771027002683, -2.2965985769289707, 7.11581513863048, 1.8553730180030106, -1.6826582047836334, 0.44285857692009944]
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
