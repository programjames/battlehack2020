import random
import math

WEIGHT_LIST = [0.5566144916059655, 4.907026728824875, -2.3168177649273374, -3.554570017015106, -2.3247044906243786, -5.288477995222074, 2.87417004936192, 1.8261344047120436, 0.8083661746123317, -1.1088882371709612, 2.6036592670380267, -0.010598995344568481, -0.9002641399722745, -0.7569286554116487, 0.2279211390697268, 4.931455241901989, 4.67905579035669, -2.9780896012011744, 2.834544690075269, 1.828337501503186, -0.3735357317912487, 4.351035157457404, 4.930624090474515, 5.416724919588694, -2.116302288275863, 1.6114479907900536, -2.187948821354264, -4.356184089126381, -4.908640482531177, 1.3817932716492796, 1.3613186165141307, -1.1193468107385331, -3.396883082269693, 5.2571218462259, 1.0048481880236915, -2.4952785266279203, 4.154663038838941, -3.283767781502696, -3.7498617126614517, -1.0366485410237627, 3.8259013116496114, -1.8637147980126123, 0.4349209837704467, 0.15749723843209207, -3.2612955671337387, 5.726709615522728, -7.88662302125596, -1.0388890346857054, -4.611925293995811, 0.8816632530628659, -3.8386064857423925, 0.6805578119362873, -3.5797415842130778, 1.8965105252946488, -2.2488993491605274, -1.5877784612260963, -0.407423359768295, -1.979862314916402, 4.8951995958628585, 9.87394497176296, -2.191654327475111, -4.494534156386221, -4.319355775083664, -3.525086510530639, 0.72992454935226, 0.20164047671197502, 5.358693182827933, -2.1969346253087174, 1.2293303739489052, -0.6907160522899548, 0.44438246384993607, -10.344267196218, 0.4890970189934675, -3.694109775178296, 0.04907041503793258, -0.9660884496824216, 3.3909845057856076, -9.79850025529786, -0.06913147533668826, -0.5755173804913923, -2.417378459248704, -1.109282115345753, -3.252117110565223, -1.218768531062382, 1.015986356630942, 4.810769812788434, -1.8419044749318656, 3.9908960399567435, 1.3687572385690354, -0.6908311309925296, 0.9992413192535524, 3.787546739240121, -1.2440362679306625, -1.0625009465729827, -1.5804383745717487, 0.5309089661252461, -1.747800799451387, -1.134899298487278, -0.6262369632270294, -3.688135753448596, 4.123103883449938, -4.82256022427034, -2.326974223028474, -3.6144904698177704, 4.9384832515352395, 0.7484179235735642, 2.699337697937404, 2.681969474945197, 4.962760871966789, 1.8862751632530113, 4.389216744092688, 0.6037929674650944, -0.5293377452113461, -4.314047400424654, 4.454681858919384, -1.7056046495176675, 2.551645495485124, -2.7650075761819983, 4.5685069764111255, 0.5752847014775825, 0.6289617543349175, -0.16186403179829, 3.5930286987661217, 2.6144400737727924, 7.008780630820136, 2.443881709071287, -5.3576178433223145, -5.633569516568088, 2.5560216055930423, 0.06317144403631736, 3.62194233654327, 3.847015783560716, 6.501702613264673, -5.744586145653383, -5.192959197396283, -5.161678323038198, 5.249123647399815, 3.5115117330281254, 3.564866300398452, 4.551409365486174, 2.0726165939623615, 3.481572746493028, -5.221667726634562, -1.0524771796144863, -3.6830995900395544, 2.5157725002355766, -3.9486959399011563, 2.482571748917492, 0.46617291626783397, -2.483972675970576, -0.4266887939561866, -5.120097734158935, -2.416855119189497, -0.0010526078511832386, -4.159376718053055, -8.689259245245117, -0.22071861811764934, -1.8228643094920114, 5.460601062474805, 3.801718918014783, -0.950936328609611, 3.8405888029963764, -4.5570922139159595, 4.481243483886193, -1.1300646011164714, 0.3631931314654348, 2.1094766269040877, -1.6906693991251398, 3.366589304924513, -2.6046668780305944, -3.4536902823676927, -2.4221006865183496, 2.0594670072618735, -3.2905806199992336, 1.8303277692108557, 0.1931807297303584, 7.306095130921631, 0.13507551591503963, -1.232837754707717, -5.373612886305412, -3.223195528309469, -1.8771959579681474, 2.1525298651808864, 3.6494576176493374, 5.115627743293174, 1.132855646724929, -2.6365669124035698, -6.1142919040962, -2.509245420948886, -2.13267918791992, 0.08692084624175439, -4.282474783726104, 4.586112201143175, 3.253762462720821, 1.9112745059788965, -0.4271239628623208, 0.7556798999925579, -0.5198212714463922, 1.69494577455025, 1.768497793892081, 0.12381013712251125, 0.7047995022361463, 3.029132265815728, 2.4190246700260745, 2.2486923424104757, -1.3557691838159558, 1.0402607035255997, 10.576384470607298, 0.5821967317238831, -1.120342925990166, 0.6052023704819733, 0.7486620559173156, -2.936285604027184, 1.305444675704852, -0.6543971213852389, -1.763969382140344, -1.6028829301937568, 0.3287106379196834, 1.3024883479359184, -0.7550153201865867, -3.9306485208094415, 4.078170426649699, -1.5739182065487265, -0.9563684282953012, 4.250057906778193, -3.5242638753378266, -5.032836819609759, -3.3226603975756985, 0.15813816029775585, 1.7373438093055864, -5.335075650220881, -1.7006197787220019, -4.685299508346831, -1.64642438668444, 5.273165718200097, 2.408577990932533, 4.274992329064271, -1.1644228265717482, -3.631169008813907, -5.93569819435317, -2.57183275369789, -2.5906168958405305, -3.5976924636357825, 4.867710802791011, -2.6040677404178894, 1.2096559192010956, 2.5943740560675908, 0.2142032954205276, -0.07764631083811864, 7.120711422766159, -1.5406744725226553, -2.116377144875661, -2.3001568525688616, -4.26816949633112, -4.8559466636795525, 1.0178744638446093, -0.42031914300979284, -0.3559635231311905, -5.812609065947662, -2.5094227493839822, -2.7275467193559275, -4.581760651515233, -1.8229952276239922, -5.906303110706905, -3.0618979159242277, 2.690863258772031, -2.369232563876701, 0.5927883688518618, -3.7590705042140313, -0.5490673901188917, -1.659736982451472, 0.16530662469095087, -2.8976699523404257, -5.618246703280715, 1.525436597131491, 2.0322196816581535, 0.20921696257780167, 0.9937319858115513, -0.7815845625467461, 0.3681322120759583, 3.9454760793775763, -1.0302513862185039, -3.894476774888954, 3.75432444301503, 6.16186704315554, -0.08016292075873367, -3.3818469249973786, -1.82262292634969, 2.6351208361096408, 1.6976191749276608, -2.9753526184043606, -2.6950543371457276, 2.5508419621328557, -3.5701535382785687, -2.261528565185218, 2.3622600963631926, 8.828634937780686, 5.947504866347355, 1.795785608429899, 2.0512606803771196, 4.566038790562589, -1.8761642854054439, -5.842531622918812, -1.7697547768137094, -2.3783742682848397, -6.862272196027594, -2.8808108964286507, 2.291384329941666, 5.06238253942323, -1.4257917624682297, 0.6774457923210301, -3.921385310490863, -3.5988353466184853, 3.261064237993852, 1.849506807774769, -1.7814110424507066, -5.651678985537195, -2.4028666311126385, 1.2855914840848164, -5.595852897284354, -5.321245273813296, 1.2723360337439045, -6.799497707984943, 6.4048982949962125, 3.4376685777396827, 4.604338442973159, 1.9997763196807203, 0.2785299262347859, -1.2738733739371897, -5.5640835204917956, 3.969841745393568, -0.3381945441513538, -7.424806758224818, -0.10070438451081662, -5.028669498800728, -0.5100606761016699, -1.6698174949072682, -3.451770028807897, 6.516797161208791, -6.781945403606816, -3.2333271104304355, 2.662652734080858, 1.4783983605402438, 4.189754769314291, -5.692308011303968, -4.632618095829896, 1.7003087796494503, 4.798386347052814, -4.852135433850282, 4.649116075065267, 3.2500710267281416, -4.029504798513941, -3.4057699610134984, 2.318870046611383, 2.337024349250503, -3.3873507833561987, 0.03984164727707276, -0.014795686739564134, 2.8212085994788363, 3.243563097528426, -2.2487730223596634, -2.81872108113604, 4.918039290748712, 6.053498362821049, 5.286490341700629, 0.11587959229254999, -5.840554548645142, 4.265642440531672, 2.611377264016111, 0.8507329903724692, -3.2229108944779523, -4.71742734860549, -3.6737133013739447, -0.8955443080917813, 0.34141856731282555, 2.073471733347237, 3.915915406107789, 0.6818889345984013, -5.649937219769918, -5.2589660826576266, 0.42371406878061135, 3.423076207048873, -0.8729685346096149, 3.1717568606942668, 0.12719945395566293, -2.869881963497511, -7.234884203269364, -7.889870510313811, -4.60162007566859, 2.462116097141542, 5.608588027289285, -1.7026213023297143, 4.703627932380071, 0.514508024956567, 1.4395275694230356, -1.2952252582487007, 0.3406440133858809, 1.1852328676138728, 2.2633515283063055, -1.5017215231997567, 4.289787368261744, 5.552688492270502, 2.7172731556844902, -3.454411893039844, -1.7157372616576423, 4.537050314435429, 0.7032011888197487, -2.150871614581359, 3.869150710410114, -5.552600774958043, -0.30618739898525504, 0.7804007122364004, 0.9036957875285263, -3.282976490450752, 0.965884072199674, -5.682206061884495, 4.129985655194646, -1.5794869638101223, -0.7083256882340684, -0.9960821817777618, -7.39659236924814, -1.8334957955959987, 0.7605548926715507, 5.22732088813792, -4.3448198749252835, -1.148504924880343, 4.086171657813358, -2.7487991941790817, 0.9149867501096886, -1.941370373981161, 4.396381170581388, 2.7824566443859737, 3.000609693279206, -5.906185725522541, 4.931194777195255, 6.1862519580387865, -0.733472408974775, 0.8048922265324523, 1.584069612852214, -4.761723298917476, -1.618761588299019, 0.6483174353305065, 2.0124871376665445, -1.8370122101517883, -0.374264539611391, -4.320479705017858, 0.7103487620178085, 7.9866791843913045, 1.8100035511467727, 2.9330103455089938, 2.411739847354377, 4.5178745484806155, 4.9336653299629765, -4.36664089034354, 4.684626051549506, 0.005819201212682323, 3.6231886568708584, 2.549699994045582, -0.3814845522722499, 2.518990504748075, -0.41756237230079074, -5.913979832871262, 7.7018837430767935, 3.684480127339019, -2.042697146458936, 2.0666158234859813, 1.4923628868008125, 3.1981954470967606, 1.372965070922274, 3.0517502912479837, 5.1819160909485955, 1.6528753936240494, -2.3179586767312905, -0.10948941862503414, 2.4955258722003917, 1.3529189631246588, 1.5753487829968142, 6.846059902853642, -4.273609522399134, -2.4568466443579866, -1.1933081965259942, -5.085162555422849, 0.5652341207049905, -4.3478255943451325, 2.6938982402293443, 0.39721149373735204, -4.411194761465651, -0.8188293578383903, 0.4720812689344566, 6.266802383731611, -3.281591696186232, -2.8799048940684084, -0.6909072630287646, -0.24057861403006245, -4.859648210435593, 1.364037703396903, 2.608490928003576, 1.8353135324291447, -0.37374870872323074, 2.726858397788133, -0.2899270230740347, 0.10958286526214586, 1.5454077733896403, -4.736413867759764, -1.6536488923910777, 3.609956740743089, 2.8705291467312577, 0.491572831805306, 4.257201801886185, -3.0527402417916614, 1.8244988455322257, 1.0535600872930293, -3.7772165805905935, -1.7969799623951166, -4.90889605532326, -0.9780074384169898, -3.989071351267336, -1.0068726122184843, -5.965961426971181, 0.30232516245965924, -0.04767236399268436, 7.005820581433994, -1.1831798297092526, 1.105756602822971, -4.017747519623103, 6.954688208036823, -4.083080968315482, -4.134574302323674, 2.046187320928012, 5.105081331975866, -5.506986309746596, -6.404964724770482, 0.9152049632083048, 4.222607658615197, -0.8996352108494017, 8.075952522581499, 2.5302132664683845, -2.3003803839133674, -3.3359718242418075, -1.9998279054135875, 1.4641342008154477, 1.0574535255580082, 1.4349814610531586, 9.022082790849332, 3.802940251494499, 0.5678348069264337, -1.2656820842698386, 1.8090452355847448, 1.5036390864723965, -0.5474231146063933, -0.28392861605912995, 5.979810995889561, -0.12205510818895782, -2.7921983956322536, 5.402423606911518, -7.759322388482474, 5.2578135241753685, -3.887237293015278, 3.4008331530217135, -1.0105620051432325, 7.802217220105909, 1.89151328727752, -2.2571319288816034, -2.185974412609156, 0.02860754637037437, -0.12189733305673342, -2.4560119083155594, -4.41550127318132, 2.2068785265350113, 3.961940232098099, 6.046930291557516, 4.873798251269726, 2.2549823813495555, -2.1545785196543217, 0.027273333728475953, 1.8501254667521965, 3.710220630893414, 8.934809891854496, 0.403684390321774, 0.22025096867841604, 9.609094876412819, -0.6129728051798226, 0.5338762082337366, -3.1898478117015845, -2.550542086166136, 5.776323396315328, -2.3504369470183253, -5.451486033647156, -0.23561898497643505, -7.365422723477988, 2.4161120863101258, 3.079800716977543, 6.105979231991342, 4.945755600996225, -0.9556435241385481, 3.8036081367280516, 2.9153861000746515, 4.115873437560967, 6.782703981364421, 1.3795051839135006, 2.301410649481027, -4.258712648690907, 2.0201923165217726, -7.719531349390224, 2.163087229109102, 1.2659311679869791, 1.2139713791900133, -5.138513026897638, -4.540933244481466, 2.3614577919707536, 3.0331914327548364, 4.275385111628236, -9.13935883536728, -2.418488809684875, 7.438989969611949, -1.3574294632720496, 1.437319445651845, 5.831555042410615, -3.4677285287866693, 3.1579506217415063, -2.0118020260821377, -9.986824988927257, -1.0539931893840502, 1.4749804960743362, 2.9039736651532584, -0.9070733584900715, -0.6996697380487872, -0.8139660575030129, 2.2731590152886567, 2.4924035362450185, 3.227158546519771, 0.28499200906981215, -1.4177654247160911, -4.290991466465129, -3.230405626925504, -3.422840765001193, -0.7148770285545959, 0.8603243100135017, 4.223526595789593, 1.956221705834026, 3.1842701666932136, 3.1137112264846984, -1.4463489966965317, 0.1566511633874416, 0.9598185111364383, -3.082167684989382, -1.6495372113490483, 3.4798921650647996, -4.020608093570377, 3.35692621567632, 0.5714159827523908, -3.691590195531395, 3.4441755641398553, 5.931217763369095, -0.44208705734148435, 3.22706168328408, 0.3802869068184563, 1.851566494463164, -0.9142996122191309, -0.20000021465345058, -5.262493523277284, -3.3626784548776616, -3.7126803458982094, 2.337176269097397, -3.904527288229668, -1.539541471407813, -1.14537102324124, -2.064279503616696, -4.9036000744741886, -3.86460369067737, 1.9847124744260982, 5.680123884335135, -0.20365014788330374, -1.828777311236866, -1.3500544905163037, -4.283434426976441, 2.352833557605122, -1.5543727935815956, 6.685883126471778, -2.6755740934343444, -4.749849114782182, 7.886634636621581, -2.0416433373850102, -3.2755733756135053, -5.159421045825881, 2.9977257466646234, 1.5135538280975773, -3.5545529827701983, -1.3596912505977317, -1.592803818149013, -4.812783761680736, 3.3278251378734445, -1.3071029248417418, 4.384531424857995, 4.632068624837453, 4.2934041179316855, -4.910499881064763, 3.648622162025639, 0.23947115737310662, -3.3982215652246506, -0.3570582258955417, -4.746573547254594, -3.5377029660434935, -2.0708710298005584, 2.5245379757379363, -3.407682456357054, -4.675348054049317, 1.4319884901786124, -2.7559543825479245, 2.013473717942581, 0.4708723096031627, 1.6648504252408147, 3.968326907759253, 2.934630650901752, 2.7928534926608815, -5.870289367959288, 6.986940711271111, -1.3630651287488886, -3.467338564937463, -2.8442926929519294, 0.14465538700069983, 1.4882126444261734, 3.034681483595392, -3.5916958296728705, -1.0557195445039569, -2.76135381177281, 0.5821805306177115, 2.1870882822902487, 6.127345906037945, -2.754073307250386, 0.09610837985046548, 1.479803650340693, -1.2532202697550876, 0.7321732878218046, -5.741193954822905, -0.8367231396368094, -2.3847403939207323, 2.3591868499138062, 3.775557913357592, 6.926250031034283, -0.8686404188464442, -2.2305889191737918, -7.982425386741636, -4.32600593132811, 2.9966334461038215, 4.224425969515049, -4.415857712943008, -1.782812118715993, 0.9694642767360404, 7.594750694522501, 3.7632771511324545, 4.881056459260273]
BIASES_LIST = [-1.3811661585017598, 3.708258257588348, -3.6133776571498757, 4.793945859360753, 6.334715462997316, 2.772020206410219, 1.0964239644923008, -0.0780752863859949, -1.1023731652288602, 2.6555772336213965, 2.1265409513023816, -1.368106647716588, -0.007504253426539208, -2.620988600574944, -5.502143095907636, 5.266628298626189, 4.821100542120695, 1.4762229608895758, -6.560669899413403, 0.024648916639859814, -5.071674122623397, -2.8000623528857513, -4.061046072006732, -6.0979992488694945, 3.9305768218564463, 2.6547694782879314, -4.027908332081722, 2.9217794079656163, -1.0834339645113569, 2.301555001033315, -0.3410530066864647, -2.2956372108189513, 7.128714808031984, 1.8532774557001206, -1.681676521645761, 0.4464902095792009]
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

