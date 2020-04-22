import random
import math

WEIGHT_LIST = [0.5585131834090087, 4.908332673486685, -2.3170387698158232, -3.5504261779476805, -2.321789438357972, -5.296617167030068, 2.869785128121382, 1.830042126930077, 0.8076837621300617, -1.107334903821395, 2.6042207881101405, -0.013393587662079431, -0.9038942136496331, -0.7627901680856991, 0.2331953889436711, 4.931923544472909, 4.677493370701185, -2.9812882614394156, 2.837167097999272, 1.8240601776399534, -0.38275852571054525, 4.356166511295591, 4.932294496275423, 5.414585976608053, -2.116784299314041, 1.6123178990267997, -2.186678214676776, -4.354586921735908, -4.90654399092838, 1.3824781873721215, 1.3653890491530771, -1.1193333587369316, -3.397870168800372, 5.260894071264799, 0.9968196104182706, -2.5019231034201925, 4.1518049755714035, -3.283805570160704, -3.7536411144550534, -1.028376427199605, 3.8327460777062416, -1.8642400934789445, 0.43526792239484297, 0.16126012754842609, -3.2602035692221865, 5.729582217244062, -7.881672264303882, -1.0428207091157897, -4.622467938749945, 0.8812421384570531, -3.8447898438181927, 0.6742971278642947, -3.577128516717578, 1.8901195509672821, -2.2541030488293514, -1.5920814385812576, -0.41117890746697955, -1.9823660868182813, 4.890057848341181, 9.883269603258883, -2.197112351776083, -4.491315561597175, -4.318408541703593, -3.521830114096463, 0.7274521639699438, 0.2048017365378922, 5.362323593660784, -2.1966690896353946, 1.2333770170347653, -0.6869169030569112, 0.4482908828293257, -10.348836620473945, 0.48466924819233026, -3.693691885094491, 0.040219725002741374, -0.9687804973515923, 3.3913023955930597, -9.80073524651454, -0.0695623658513778, -0.5718277944497054, -2.4142979688162067, -1.1108905181682867, -3.2552301181346666, -1.2214444549585064, 1.0182980056578304, 4.806579082742492, -1.8356633548440824, 3.995167130811985, 1.364231437099813, -0.6918259325591369, 0.9957039477481968, 3.783522401154224, -1.2426622305733108, -1.065258188422501, -1.5819035185228458, 0.5392905512436459, -1.7464296606914853, -1.1366318497529022, -0.6258009889116726, -3.6916521041384183, 4.1145138896780304, -4.821788643904825, -2.3263848090870507, -3.612141629548623, 4.934070154339415, 0.741864719527709, 2.6998000445997246, 2.6875232771467212, 4.96288151376973, 1.8784400457033408, 4.386637024710865, 0.607146949815652, -0.5292504554922712, -4.315419828569875, 4.4617726656942835, -1.7076406029870241, 2.560927301435876, -2.7675984317399354, 4.558731593882063, 0.5723338877308769, 0.6266385885834541, -0.160242683506628, 3.5981015793948163, 2.6171331971612446, 7.012832981674095, 2.4388631923549284, -5.358428215769699, -5.62830418626569, 2.551232493389732, 0.06531630428315079, 3.6270981631899426, 3.8478847740319444, 6.506297061767741, -5.742616416517214, -5.191223563053269, -5.161518765223008, 5.246951272415167, 3.508537136970272, 3.572830346217949, 4.547942984028459, 2.0757908319065703, 3.4812198128816303, -5.2312705600329945, -1.0536415778843884, -3.6810408423155474, 2.520517306284483, -3.950222802193306, 2.480613037367232, 0.4681351910668201, -2.4773720775500605, -0.42657970547553037, -5.121672320350941, -2.4166855152646813, -0.0037479779367113456, -4.159195054742178, -8.683402465785825, -0.22054750536196652, -1.8165790360533862, 5.4639634589775055, 3.8042484363149534, -0.9445665991669403, 3.8400112058874813, -4.561671686452859, 4.482236559102479, -1.1238708450939128, 0.36577216823800296, 2.1060062324861772, -1.6868499414486162, 3.3680805598998096, -2.6071663868164547, -3.4535228634066883, -2.4258641170414883, 2.0625196654895115, -3.2817263457171735, 1.8361248652373883, 0.1965703859223239, 7.302769555871163, 0.13621356192974615, -1.2330645549747383, -5.376648001855906, -3.224323551611072, -1.8793735898451045, 2.146501738777141, 3.649619096281092, 5.114903080303832, 1.1321571133288288, -2.629516485107542, -6.110612031815416, -2.5148971295553157, -2.1304979941000886, 0.08627087650934959, -4.280665640968681, 4.5773984570909825, 3.253719558937158, 1.9146960825743977, -0.4319879075219919, 0.757130705942048, -0.5217700091026932, 1.7004155562619097, 1.7621379562178634, 0.12672229309152927, 0.7080882462521686, 3.030976641044043, 2.417568512045252, 2.250260795835977, -1.3515704477471475, 1.0372273355911195, 10.582192147267929, 0.5749789946217082, -1.1259113868972792, 0.6082874099654653, 0.7528101355745218, -2.9447576298746925, 1.3071399645517476, -0.6523643875582522, -1.761412299224248, -1.6066912460799443, 0.33871472376054507, 1.304081443197667, -0.7470055269267568, -3.9243210068178924, 4.079125347483081, -1.5764632835016754, -0.9533134243038831, 4.252180464160068, -3.5313724109169953, -5.02570311232515, -3.3236633232729242, 0.15811507873443165, 1.740158933256697, -5.333814015291914, -1.703146941125537, -4.688290091099083, -1.6484454176187195, 5.274993513009762, 2.4062498387107403, 4.275674306965168, -1.1728183312217129, -3.628346430248628, -5.934405027427307, -2.567903641405479, -2.5852254923744327, -3.5939449834303843, 4.862748387050838, -2.5978847394382125, 1.2076193907489121, 2.5970025468139672, 0.2198012935816947, -0.07711763254532743, 7.129704981808133, -1.5366663497743958, -2.117086394365138, -2.2953244981696934, -4.268093703013155, -4.855519638858733, 1.0200632751536005, -0.4191536581263627, -0.35514103361119653, -5.807969025722624, -2.5159892959801393, -2.7230492810243354, -4.576984953832753, -1.8338152307757172, -5.90300841301943, -3.067648364105739, 2.6914574760136776, -2.373333677075742, 0.5902667041961202, -3.7664441178909462, -0.5509407685121523, -1.6637550575433049, 0.16753538997088666, -2.890947595762674, -5.6184338287956725, 1.5237141664875633, 2.0323858550107907, 0.19986186707148623, 0.9936792881457929, -0.7745322012349686, 0.36090236544329446, 3.948313993986065, -1.0295246635195632, -3.897618639258778, 3.7558136807450504, 6.161622605959352, -0.08111312986095745, -3.38606910728456, -1.829506121894924, 2.638755807406602, 1.7024465809267901, -2.97825768158779, -2.689421226218022, 2.5440117071376878, -3.57417714318383, -2.259856576494188, 2.363309288683553, 8.832766263763745, 5.947569003634409, 1.7996349339123625, 2.0503391349679743, 4.5619052944401215, -1.882098535072885, -5.842541360404251, -1.7729675397592193, -2.3760958831124945, -6.867039372037792, -2.881317217782732, 2.2935312794693212, 5.064822457679987, -1.4258680393527348, 0.6709031803278922, -3.921054555033472, -3.5952154107986996, 3.263259314774467, 1.84203264969369, -1.7792744378047258, -5.646098805909814, -2.400880532227443, 1.2873675582690933, -5.5910020419575055, -5.312745238233124, 1.279610960252468, -6.805792555579908, 6.404021449606591, 3.4298193493974245, 4.5973624294715165, 1.9958250760191274, 0.2815000511317252, -1.2669714962009533, -5.564180026180714, 3.963370141923516, -0.33513289167917326, -7.424833659925673, -0.10293972457108473, -5.026756699743028, -0.512874546785477, -1.6752186950866965, -3.4580875564864675, 6.515104982336182, -6.785440927323548, -3.2361186124393835, 2.6647500145070406, 1.47659021759343, 4.186730900949763, -5.691760072537879, -4.633279290745479, 1.70933929168503, 4.804996150853655, -4.853981951331618, 4.650355232368051, 3.2555367257898635, -4.02567076696981, -3.404318422981401, 2.3127903213331775, 2.334084184603034, -3.3851063348415624, 0.03150013785481452, -0.010136030135942036, 2.8159125760253976, 3.2438197464466567, -2.246390891338577, -2.8250669787690987, 4.920353212193865, 6.053290962436028, 5.28075905930559, 0.11746302047082906, -5.845772999089703, 4.262779479113521, 2.6066658099690896, 0.8498766263012777, -3.2234536493385613, -4.706675189728772, -3.669106297607816, -0.8914601664202224, 0.3448857781690411, 2.0707863147559484, 3.9203622162402327, 0.6846229321019043, -5.649637125603935, -5.259549997196551, 0.4256458401818337, 3.424908886695515, -0.8725400716980555, 3.1711758946519026, 0.12622707061684219, -2.8743386422525585, -7.232523017680567, -7.8845388244340375, -4.598841352812256, 2.4598564756207506, 5.609797509305816, -1.701124199534398, 4.707082962491973, 0.5142125955994632, 1.4446571198791982, -1.2956908761641013, 0.3424717437712321, 1.1823475807125046, 2.266583548546415, -1.4990278983762864, 4.288010325193677, 5.551736057444446, 2.715413265632956, -3.452548977749605, -1.7140175747430797, 4.538646250490633, 0.7053250822127514, -2.1489753369924225, 3.8702276109544225, -5.553224185472315, -0.3041866749778875, 0.7843680917473981, 0.9057174142202312, -3.2711978435569073, 0.9670935934463643, -5.686107932144532, 4.126503597105139, -1.5834119352481384, -0.7144674895280745, -0.9945709188522867, -7.398618163693426, -1.8412307762924887, 0.755800202153075, 5.221743137633701, -4.345083142423862, -1.1536788015127284, 4.084737519222549, -2.7387477605902353, 0.9159201436100474, -1.9419644813068748, 4.391056417784568, 2.787888232273269, 2.995015976362441, -5.903706174432984, 4.938707619849985, 6.184273307935036, -0.7302941321766216, 0.8051695474822508, 1.5815477860061824, -4.762330139804953, -1.6124794195670489, 0.6569159337130206, 2.012768801392016, -1.8269552200425185, -0.3720453566160935, -4.325352537917275, 0.713961620856337, 7.984737903548086, 1.8043149576820656, 2.930810504053683, 2.414150078309117, 4.519985500437154, 4.94053068800351, -4.360826970869625, 4.692694924835033, 0.0023945896162128697, 3.632544488502103, 2.550782850537521, -0.3799721532225476, 2.5170140927873526, -0.41868316304379255, -5.911015964428186, 7.699501087279146, 3.684460965899384, -2.0454395855851213, 2.0727685009654917, 1.497885532549397, 3.191812862072248, 1.371309063768948, 3.0521714445408903, 5.187167609569416, 1.6576638500664338, -2.315886197731163, -0.10645561349151433, 2.495580649241821, 1.3427135744431533, 1.5820287605127679, 6.851263760308742, -4.281869498250159, -2.459160753619295, -1.1957262559928254, -5.076251011167579, 0.5679914290965886, -4.3454270902064325, 2.6928797616929065, 0.3968420915577036, -4.412090215546959, -0.8149499498038578, 0.4760505708595249, 6.261171257628995, -3.2817003683099606, -2.8829337920097036, -0.6972068351904788, -0.24141299652827164, -4.862574030226118, 1.3637737059951593, 2.6069116176185907, 1.8338681795479224, -0.366903444495111, 2.7293476813635706, -0.2858046684215017, 0.10799384843000104, 1.5416909411188344, -4.740038886784151, -1.6576658059080807, 3.605099206449705, 2.8667059999167757, 0.49346047521398245, 4.253506715377052, -3.0578114106935588, 1.8248568505899294, 1.051691094241069, -3.7745547616815642, -1.7930985854587667, -4.908235461457777, -0.9699990994897203, -3.9873259324806756, -1.0041768773684738, -5.973088171090601, 0.297650495914131, -0.0388431288485024, 7.010007437745079, -1.1826291467970682, 1.1094896299046253, -4.018153027030549, 6.960794827290424, -4.0777639792729214, -4.132274066618672, 2.0460027214506638, 5.101242425529599, -5.504872545759371, -6.408196950847881, 0.9161280689620814, 4.218292925841086, -0.9032834338584322, 8.07846414540433, 2.5234194141719755, -2.304925423295923, -3.336537159171568, -1.9914503956551133, 1.4643983367878939, 1.0679890828294543, 1.4335721590967438, 9.019680646356763, 3.802487702100461, 0.5636248979385158, -1.2661442148902058, 1.8088403697357245, 1.5034300496565023, -0.5521776166562944, -0.2857044024775181, 5.973246323647044, -0.12327405524121103, -2.79095035542804, 5.407383840837508, -7.761670609230425, 5.251996470567522, -3.887558897733178, 3.4032250936222717, -1.011307290786251, 7.8068100657907085, 1.891147295833247, -2.261405167175292, -2.1787256892671985, 0.03178035922207646, -0.12282356160083524, -2.4643107246122518, -4.410464883605691, 2.2092615886317066, 3.9634675864898643, 6.046984107779995, 4.874165872908204, 2.248376365376456, -2.1525669658143896, 0.02869999357629018, 1.8473296512318942, 3.712097937864191, 8.936087501069014, 0.39617809596431713, 0.22639405208271587, 9.604742070667868, -0.6148568657402006, 0.5360368391138374, -3.1860752722188193, -2.551160103713397, 5.772493086186153, -2.3508101699050292, -5.450299600307424, -0.23835484272939692, -7.360985526856732, 2.4239573345534056, 3.080062590381163, 6.107056675210474, 4.953710095055704, -0.9546879016855943, 3.8062696997778747, 2.916511450593879, 4.110536847713658, 6.782408101926133, 1.3860862884657588, 2.3078948829857935, -4.249334478097754, 2.014861698555585, -7.715878875682729, 2.1650160316057847, 1.2597273144348933, 1.2181609291906164, -5.141744465313916, -4.541355440889932, 2.3626116296037982, 3.0289067662221676, 4.272217501766973, -9.137823576959237, -2.421484040306864, 7.442782175715708, -1.3577587374085405, 1.4428535345226778, 5.827740745857211, -3.4698802527133377, 3.1622051311041397, -2.007722575355332, -9.98389245081445, -1.0512530180876316, 1.472315923718955, 2.902847536922982, -0.9090775066344079, -0.7024274269792968, -0.8136959377960227, 2.273863744881337, 2.488881329509782, 3.2251502828437175, 0.28234237421410013, -1.4164782246556322, -4.287077367063332, -3.224376002865262, -3.4191480152561606, -0.7150667602030595, 0.8628811927284661, 4.222115455306735, 1.9544556218976354, 3.181927224108158, 3.1120705653683793, -1.4447477271373914, 0.15472299645077386, 0.9601637925037301, -3.08243837687094, -1.6411827380559594, 3.479460202657722, -4.022765204103554, 3.360980754771084, 0.567739469615615, -3.686466319441895, 3.4467645259703237, 5.9222891623805625, -0.44406158000649465, 3.228963465123275, 0.37727062443259146, 1.8538547010542348, -0.9189975488607434, -0.19890638041487196, -5.263817487375234, -3.3550058399091762, -3.7085489594419707, 2.3394845333872807, -3.901466995921028, -1.5426474745281324, -1.1387088625547106, -2.05651665370137, -4.905947605751762, -3.861637288451371, 1.9828377198752036, 5.6776815002651615, -0.19892559968965653, -1.8238895776540682, -1.3575977958313932, -4.280336697281362, 2.3487643514330196, -1.552566667728003, 6.689607194472, -2.6806797664392943, -4.747039288232821, 7.886166351077466, -2.044533961127968, -3.2802496904501326, -5.166950128181244, 3.0002076900604226, 1.5198936725840144, -3.5530608027547537, -1.3618324668154558, -1.5910080150902512, -4.8106552297976215, 3.329426409874214, -1.3053906198044447, 4.380083263244943, 4.631670608200863, 4.29523231871858, -4.907105820158862, 3.6478520895836293, 0.23738822649656746, -3.404256608728675, -0.36054545330372656, -4.741235952295191, -3.545880499090946, -2.0717904235706768, 2.5240948880481198, -3.4101586381705524, -4.682596271677131, 1.431671249967436, -2.7548642682386464, 2.0182926188473242, 0.4707146250825016, 1.6721343020637196, 3.965715260973578, 2.937904259438812, 2.785523011835812, -5.862538821196403, 6.98529290883121, -1.3650991444921519, -3.4689084091102447, -2.846787584737346, 0.1503767875491119, 1.4922697064921506, 3.033578842672423, -3.5970547963213435, -1.0521353445510446, -2.7632958995677233, 0.5859488817267009, 2.185746647790158, 6.124196865840438, -2.756810958258004, 0.08756378052763125, 1.4737375434750237, -1.2516512162532663, 0.7366067001703003, -5.735654606473735, -0.8343521567030224, -2.384424834551774, 2.3508523066053986, 3.7749903661850697, 6.925469031711141, -0.8746456390377093, -2.23608058208509, -7.983763071633964, -4.328223074236865, 2.989043615316799, 4.218149514106159, -4.417104352281865, -1.7780978778466519, 0.9727375711783277, 7.594508861797065, 3.756323752838562, 4.875699483710277]
BIASES_LIST = [-1.3857412076541578, 3.7107764657499085, -3.612054717727392, 4.795018012415598, 6.337155539050993, 2.7705562751926625, 1.1010706251181765, -0.07733546792409707, -1.1039381510840085, 2.6504134562888413, 2.1241531572659627, -1.3649182676601885, 0.0035299166752827404, -2.6209547665343957, -5.507340589358269, 5.264073479855851, 4.819471297508022, 1.480977840489082, -6.5625029758426345, 0.02159281918428179, -5.071055512468609, -2.7973526908475037, -4.065020458981936, -6.098499791971304, 3.932080321168866, 2.646100301566115, -4.026886047909289, 2.9136969860818245, -1.0808440327424897, 2.305279726305245, -0.3406993102400239, -2.2962461392055595, 7.119895170151163, 1.8503464719466043, -1.683663464383163, 0.44912111812731]
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
