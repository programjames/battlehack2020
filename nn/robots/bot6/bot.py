import random
import math

WEIGHT_LIST = [0.564249995489778, 4.913478348379399, -2.3312586469054337, -3.5505224341593804, -2.316255840944718, -5.288351830416415, 2.8635175003962434, 1.8424820830129278, 0.8104425775610787, -1.1020825392492388, 2.599219161921178, -0.022326503830565357, -0.9121510227076526, -0.7533188591546713, 0.23923654243622006, 4.933538956410052, 4.6818612123284655, -2.976634619512316, 2.841226193737662, 1.8237399070284184, -0.3732492025932526, 4.359988273912006, 4.923069624114639, 5.41547124818074, -2.11052887225492, 1.598295301378924, -2.194947917897513, -4.36335361060684, -4.909150627875941, 1.388115181915017, 1.3560646008465937, -1.1249056565973676, -3.3917576418722395, 5.255288512861444, 0.9912634011940124, -2.4933258663466606, 4.14024481332106, -3.2870602612788873, -3.7662670600780834, -1.025566517702405, 3.829414666644846, -1.8576501391926599, 0.415538291118231, 0.17275954724833706, -3.273275779911635, 5.731898213803183, -7.87189834439808, -1.0390174199701692, -4.606231759006693, 0.8744794632443323, -3.8420303133621823, 0.6625788305960201, -3.5957086650842514, 1.8910057312031234, -2.2442401917650856, -1.5937258838012687, -0.4127277821227054, -1.9846596103549174, 4.897599951909752, 9.875607416115665, -2.188585511221271, -4.496466771446295, -4.308803971364897, -3.5189922516843666, 0.729507680360881, 0.18988242324897125, 5.346224185033126, -2.195079401148849, 1.2319353587582484, -0.6741855428275345, 0.44000593586630715, -10.347433887045145, 0.48224990683812163, -3.6861286373344893, 0.039428116339386324, -0.9708852274706494, 3.3897663939292384, -9.799740271670979, -0.07969145818729186, -0.568219278631974, -2.409218880804277, -1.1118176937060429, -3.2472888892845426, -1.2103566086710897, 1.028726104222258, 4.792247886982861, -1.8343713258244907, 3.982751361639221, 1.361744947638659, -0.6820932914426474, 1.0012504852790813, 3.775566983241582, -1.2533415209824346, -1.0729343786213223, -1.584163858158935, 0.5355838118236369, -1.7502364735546765, -1.1196345488378237, -0.629180890637083, -3.6931587168922912, 4.119965582178805, -4.823036803563696, -2.3422786043540693, -3.6064161650020203, 4.938087429785408, 0.7413641815356282, 2.6971188556705514, 2.6970625766011387, 4.947566286980206, 1.8810455447799839, 4.395263965318721, 0.6095853886049765, -0.526891535918961, -4.328722662619491, 4.460818435566276, -1.7143869997275738, 2.557330915808985, -2.7616321648360813, 4.551208619967352, 0.5646412217983321, 0.6263930054128216, -0.15717742435187493, 3.6027959652405706, 2.623260126625541, 7.006801096038885, 2.4368854983819244, -5.367077185447447, -5.635099396346216, 2.558495387636567, 0.06122480877394201, 3.6191374668756353, 3.845805455927913, 6.5195628250988005, -5.73019157364748, -5.199858750110602, -5.1490103495407995, 5.243087317799623, 3.5030979818814676, 3.568873877405531, 4.557290889926294, 2.0735189056008254, 3.4858445959229867, -5.227175571832312, -1.0469344768380948, -3.682504049832563, 2.5206311105192754, -3.937418434410899, 2.4943890618928073, 0.465074682131669, -2.478107713907427, -0.42816125773242736, -5.106607502151092, -2.424243177151532, 0.0015888826137960676, -4.143406588140699, -8.676038526267321, -0.2260876362135773, -1.808963424217422, 5.451544219054073, 3.8035875772432317, -0.9438216008451913, 3.842474034953186, -4.54752424235063, 4.482324375869666, -1.1222909599270732, 0.3742849088656907, 2.101083466958738, -1.6896454592132435, 3.3713005435145327, -2.6033686973737606, -3.456592926253689, -2.4208313218262254, 2.065552195875957, -3.2872443684954606, 1.8421688189597953, 0.20231426954814424, 7.299562996304616, 0.13651746734935535, -1.2464519313737665, -5.374047349446659, -3.214083020254649, -1.8772641410770716, 2.1520380283468064, 3.643255809744832, 5.116295736438144, 1.1247440471713679, -2.6194711879156256, -6.098767435149652, -2.5095134455830044, -2.1375087295057296, 0.08645797978380045, -4.290562049995588, 4.577974814082577, 3.242335859111978, 1.9148349174150325, -0.4305487761042979, 0.7583320450113633, -0.5261220625538958, 1.6898193299191255, 1.7613021681518695, 0.11441237060396249, 0.7117870474477893, 3.046380094205387, 2.42783718355876, 2.249782926859577, -1.3349033790704345, 1.030105858796432, 10.586393170792485, 0.5786067815269234, -1.1366470423361195, 0.6071396853806788, 0.7579101761868791, -2.947154512128072, 1.3030128050078662, -0.6564753770734977, -1.7637142767758218, -1.6089939713543, 0.3221389431451385, 1.3019853159072514, -0.7506594338324053, -3.926109578680998, 4.085268728898366, -1.5753481076236924, -0.9473064786501167, 4.248670835077501, -3.528585278706336, -5.032832025832854, -3.317060747489474, 0.15038638972555696, 1.7457005235056962, -5.336753734966902, -1.6971824305588545, -4.688360157814036, -1.643827868768204, 5.2806066776732274, 2.398618220197724, 4.263709748751716, -1.168298490207402, -3.6196471114041473, -5.941843415239819, -2.5730432197121935, -2.594169510914219, -3.6004640271664017, 4.848827016811367, -2.59602765245413, 1.2113558397024489, 2.5898685058385076, 0.20809743878842038, -0.09110236715917656, 7.121771789960042, -1.5448235713942275, -2.1169622881830192, -2.2981927086328726, -4.2675935084475505, -4.860758232036258, 1.0126458215786422, -0.4357834207457126, -0.353787249123377, -5.813711425144168, -2.5013946820336135, -2.7375993368705798, -4.562501600123808, -1.828899270480741, -5.901339330003819, -3.0702913577776, 2.695818587239329, -2.3701684253661255, 0.6023067588666658, -3.7646794683025924, -0.5467716185409577, -1.6610837665491904, 0.17491351384561077, -2.8919815934799216, -5.611338705772908, 1.511880353390022, 2.0398260846883076, 0.19359509259974367, 0.9946379236734877, -0.7736670351134743, 0.3767476891410684, 3.949225226095544, -1.0341042217715506, -3.8950397339044702, 3.731136672105588, 6.162369270042093, -0.09387317943205335, -3.378446427499253, -1.8284883197123232, 2.631866046598109, 1.7026835707670587, -2.975461701199943, -2.693533434865217, 2.5488136598638844, -3.571460558354548, -2.2704831999530724, 2.361610419777157, 8.828277116887522, 5.939887786738163, 1.7980340922175437, 2.055143156018679, 4.5611297996080635, -1.870487016858, -5.856177894180262, -1.777432100570083, -2.3765459830350033, -6.869330927456047, -2.886941639990569, 2.2963172861344234, 5.06107263382574, -1.4146036554571262, 0.6721026978900708, -3.9210500653753564, -3.6039113290465368, 3.2659287383472626, 1.854525210374458, -1.7837345002500173, -5.661181014988814, -2.414844862295104, 1.3026442428850857, -5.595205562173375, -5.314511710174054, 1.2697186771547313, -6.795566351948528, 6.4043237584445345, 3.435508403333386, 4.601286506376869, 1.9893022262387412, 0.2791768418642223, -1.279690705730393, -5.555646886155863, 3.9486727476203214, -0.3390488093216177, -7.438763266958406, -0.10876166184861102, -5.032143116473195, -0.49717880412188087, -1.6744658905683554, -3.4657378768349565, 6.499539508420311, -6.775720377079404, -3.2244297216421076, 2.66620109170644, 1.4826953879479456, 4.191741215498349, -5.705574014299801, -4.633028529121627, 1.7116727933196434, 4.793732720732632, -4.850190089111008, 4.662082088963677, 3.2504374789169184, -4.027609197418503, -3.396539565210362, 2.3148052768598912, 2.3395680685317055, -3.3941429010823554, 0.03236246141742153, -0.017024899666380516, 2.810920085990902, 3.254946542728178, -2.250788548987778, -2.820411449359297, 4.912926608455148, 6.057747809058012, 5.283387478686981, 0.11437730592502379, -5.843931151101084, 4.257990143543853, 2.605848225635794, 0.858364321324373, -3.214887701208965, -4.695269359258922, -3.6646296096738435, -0.8821951703400772, 0.33895095358673083, 2.07463656757472, 3.922669326111586, 0.6866842383929495, -5.647405963349131, -5.253417722486249, 0.4190043297365158, 3.422289166138477, -0.873390831601415, 3.1551666343279137, 0.13752234384203912, -2.8762950071091904, -7.238905967441203, -7.877936915388935, -4.6072902800315, 2.471327822603132, 5.603141912441865, -1.7022758972070142, 4.7150343334644615, 0.5018598729162433, 1.4340423090065253, -1.2878619367843944, 0.3394634240506464, 1.1937598626240735, 2.247895037319311, -1.505429220153669, 4.287535850563715, 5.540943481800138, 2.7191355609868597, -3.4638024171085537, -1.724639789597301, 4.551610953979921, 0.7174915019378811, -2.149368054581064, 3.860784465049711, -5.557300923648259, -0.29953415079230067, 0.7845794533284132, 0.8977871367493243, -3.281458705609103, 0.9624377118619186, -5.679972351913446, 4.136328558333324, -1.5791833073143628, -0.7113377926424865, -0.9968684794594914, -7.395038221582493, -1.8411445760702476, 0.7564045509582753, 5.214323935967698, -4.348763313196553, -1.1409708222620765, 4.08936516865495, -2.7479965459990363, 0.915861298717525, -1.9423740159685754, 4.388353869541369, 2.783067553122499, 2.9984764637125894, -5.903558569806401, 4.94096932885051, 6.1844748482292715, -0.7336836747283003, 0.8017317968495391, 1.5887578469728267, -4.772784256597734, -1.6102215197581906, 0.6672437688709272, 2.0166909595634346, -1.8224181452696682, -0.36917399693780484, -4.317145749980241, 0.7188916000181984, 7.987871518069528, 1.8038173944412281, 2.9341857728599208, 2.4112209735010914, 4.508281218801323, 4.941744792323852, -4.363572095021552, 4.683066538253745, -0.0072775074551273515, 3.6364766979079266, 2.5566080840684697, -0.383018143539037, 2.5187876635686326, -0.42505841568179165, -5.91772871251639, 7.6925778394161775, 3.6816395565145243, -2.0424443631786278, 2.0685220237287787, 1.4967893365587683, 3.189953854953741, 1.3709680010399337, 3.0414115149991785, 5.1886666983905965, 1.6525147369254942, -2.3181480664909935, -0.11303396059271688, 2.477724555653283, 1.3530890632300168, 1.5884486222166314, 6.859880692146429, -4.269654927485419, -2.467450101829997, -1.1961937475965339, -5.092433351300095, 0.5593330854046232, -4.355401110501409, 2.693290206360723, 0.41112832244740954, -4.409314996325902, -0.8151093488069613, 0.48018198738564727, 6.2647238135622, -3.274389313481575, -2.8744182169698576, -0.6845188922862958, -0.23452377068564206, -4.870689110259247, 1.3608960845750375, 2.606397871809527, 1.8358010149082455, -0.36248134321090575, 2.720755382514688, -0.29636126597874857, 0.11884170187579352, 1.5357334920242447, -4.754764520242577, -1.6481483982640797, 3.6169138170295927, 2.8638901463364963, 0.49280335356632066, 4.252277939333866, -3.0599818038017625, 1.8161943080088057, 1.0458168160148982, -3.7715720976176215, -1.7901247622619705, -4.919419861754973, -0.9653660978641907, -3.9942991644216663, -0.9953060877844923, -5.967046129389955, 0.29292948061960367, -0.05350037073240456, 7.019792273543332, -1.2012841188007368, 1.097032851125834, -4.024268585387502, 6.954161138534108, -4.074719909686767, -4.139615808607452, 2.037224942001578, 5.096829270032078, -5.508928659939844, -6.406839048636377, 0.9155035723214725, 4.223635275710981, -0.9124062063129904, 8.08000491977017, 2.522280147543808, -2.2953707124414495, -3.339962146269831, -1.9832387934316984, 1.4580531430202934, 1.0749116599780888, 1.441347390996198, 9.024488151154475, 3.806004506874828, 0.558457771750699, -1.26810909376797, 1.8100779836589387, 1.5079034906271704, -0.5388506768584245, -0.2936518946237268, 5.969610600129076, -0.1263131388750395, -2.7872347166076015, 5.410249131798637, -7.753710539960732, 5.258279265793194, -3.89543471705525, 3.40962494287598, -1.0030431459693885, 7.816380214540965, 1.8955296200401273, -2.2524251602138485, -2.1784987633909507, 0.0295181725563793, -0.12470929830819151, -2.4658308575373744, -4.412254599262478, 2.2103347324670226, 3.956794210899333, 6.039862350524436, 4.8760388215261, 2.2521180827228577, -2.162438085754087, 0.033229241693918395, 1.8433364310735223, 3.711231230843565, 8.940910813569088, 0.4119185265958352, 0.2453545285891673, 9.605537550148506, -0.6140462417994645, 0.540835587445122, -3.194625953103302, -2.553011127284254, 5.763209973607956, -2.3526618116785163, -5.446521416409659, -0.24105441024276533, -7.375382308505019, 2.425082143598782, 3.091955336937435, 6.109890039222341, 4.957256190591785, -0.9458275617030096, 3.7970464479770936, 2.92544633835522, 4.105381455320706, 6.785185008242076, 1.391014237162509, 2.3020423811478223, -4.2543144372471415, 2.0203903449971237, -7.736113289488277, 2.1490478435385345, 1.2689982464179865, 1.2346655508448923, -5.139451450279022, -4.538087697998381, 2.3634250204635934, 3.028310921833207, 4.273110661235069, -9.136488632292082, -2.415998384417949, 7.443674269320995, -1.3599887937082655, 1.4411869421575452, 5.824923099078969, -3.4582713860127567, 3.167138046926666, -2.009255663698555, -9.983222730166366, -1.0552791933629342, 1.4816483087834378, 2.9046359254252985, -0.9141377791198778, -0.7041357289756928, -0.8130500063481426, 2.2862727300592733, 2.4907443841375687, 3.2276661769860406, 0.2796819126433248, -1.4162133919988866, -4.297725578782175, -3.2286018987421694, -3.416450282490511, -0.7135738945604305, 0.8691889641104151, 4.225219423741094, 1.9457010923600537, 3.185652906406565, 3.1174905286848067, -1.4474450613797765, 0.15892872495392, 0.9563510839506558, -3.0840427126219745, -1.6277995655168527, 3.4855861231442615, -4.019865599129681, 3.355469973478856, 0.5754030645899815, -3.6915471094511574, 3.438742038799159, 5.922625405528605, -0.44838105308110254, 3.233208408376494, 0.3759282980484621, 1.8600047115424134, -0.9075172378858966, -0.21476509697343385, -5.2709276743216735, -3.358740991114153, -3.704545320545747, 2.350663314926989, -3.897417029181197, -1.5398210253123283, -1.1467885456048987, -2.069560972963573, -4.90398803287246, -3.868742620659786, 1.9768681318992398, 5.678305096987584, -0.1910818435978592, -1.8172207485399607, -1.3729744225067833, -4.269070325194486, 2.345240610930185, -1.5598436848893742, 6.689263435369492, -2.6730090729946774, -4.752948113046223, 7.887233945950194, -2.0324569085137174, -3.2824210340961377, -5.165662918768427, 2.9963052712347054, 1.5287912349550674, -3.561330433636036, -1.369772022266218, -1.5974220291107355, -4.7993482026849, 3.324936346419492, -1.3088750122269879, 4.384171623301926, 4.621637927964148, 4.294564836924175, -4.903574255874617, 3.6383437596503754, 0.2415833580724395, -3.394207424645229, -0.3667741621116894, -4.736095202774943, -3.534118446533637, -2.0664155559881143, 2.501374766690273, -3.4168673046003333, -4.681152465994331, 1.431178824016032, -2.750313871455154, 2.0194452328206838, 0.46503202510173614, 1.6643465553751307, 3.9568738364358538, 2.929040800672149, 2.7771103073911245, -5.861254410639854, 6.9885229545046705, -1.363103174723045, -3.4771084671607277, -2.8601073764203755, 0.15628375720670962, 1.4871787449594023, 3.040051208306442, -3.5938143761408776, -1.0578769438928357, -2.7570167626414257, 0.586649749635645, 2.1872745726680387, 6.113833318243006, -2.761306776733109, 0.0931903512766557, 1.467164885678712, -1.2544636455075098, 0.7290616663205239, -5.7301998102884095, -0.8411522676570375, -2.3850330309401415, 2.353042829902214, 3.7676853259326335, 6.916114974661747, -0.875275388268947, -2.2270000920021067, -7.993398444844968, -4.3181785895435185, 3.003496203123319, 4.224151417895188, -4.42390106776632, -1.770937633101311, 0.9640867298620696, 7.596238190808239, 3.747774765712284, 4.871614234714994]
BIASES_LIST = [-1.383138508458493, 3.7055392738657953, -3.605620400778294, 4.788327679649434, 6.341822400876495, 2.7692536280335283, 1.1007079926379884, -0.07174580884599426, -1.1142681968276675, 2.656171693454264, 2.129671304521367, -1.3719019113728046, -0.004200928310119109, -2.6243136911027323, -5.504227303463744, 5.267861590241924, 4.824265052937792, 1.4640451386912514, -6.575884953747923, 0.02064814350130636, -5.071870202150176, -2.8077091892387, -4.071680729478213, -6.09646498481062, 3.930819523632211, 2.6408787886921443, -4.029514567879269, 2.9117073909418005, -1.0716985059527033, 2.292654999668249, -0.3423006902861934, -2.288294060531757, 7.126185058447152, 1.8534749699520452, -1.678612584288157, 0.44903118956985755]
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

