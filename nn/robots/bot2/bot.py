import random
import math

WEIGHT_LIST = [0.5600679283515198, 4.904880174872782, -2.3145227129610357, -3.5473950688119684, -2.3233889932368013, -5.293617418017301, 2.875395838917532, 1.8317122216947743, 0.7973649794337685, -1.0989235452230803, 2.6025120316603245, -0.00912382132804764, -0.9123946606790011, -0.7642992013712885, 0.23625308206846415, 4.934186452621401, 4.678474617796178, -2.980879723214844, 2.8363394915714544, 1.8299736005396956, -0.37044504021460256, 4.346178927573729, 4.934316758835678, 5.416184246892423, -2.1140900923587007, 1.6104507307019902, -2.1870208923170704, -4.358143684008582, -4.910677202681471, 1.3842514770386498, 1.3652109898292506, -1.11720310172997, -3.3933845955686524, 5.262102542075518, 1.0003343512399199, -2.4907939183268115, 4.1553996362507855, -3.28921001262386, -3.7509737773793517, -1.0323364992595312, 3.823943837607942, -1.8580200487364817, 0.4304505268984636, 0.15990730874684336, -3.2701416859502364, 5.722608575338884, -7.881647827178152, -1.0369288663335703, -4.6166383229645, 0.8815909167822685, -3.8424012459132664, 0.6785862961956006, -3.5789155446073773, 1.8904625259942813, -2.254851141475662, -1.5837391878515905, -0.41498407550726085, -1.9752261543107723, 4.887254304906207, 9.875650612739017, -2.1947404105500143, -4.495610886834489, -4.321880279136485, -3.5254307494768495, 0.7291475373525405, 0.1982454331619661, 5.354411359173677, -2.2000151090559106, 1.2353597008230468, -0.6846256637051902, 0.4506441312174272, -10.346550209052866, 0.48682474007996557, -3.6887621224849547, 0.05045867579773928, -0.9620901789913363, 3.3936877127652325, -9.802165599041098, -0.07414104239799021, -0.5664729528348701, -2.418627409602507, -1.1131202205548252, -3.2541552070624395, -1.217787125620983, 1.0266855683506801, 4.812472165441957, -1.832030742487942, 3.9884456512913404, 1.3601805611696303, -0.6887018816188915, 1.0054001504011612, 3.7765109352215522, -1.2451147041268524, -1.0540551233882578, -1.5727793309908706, 0.5340931176054385, -1.7499608809099945, -1.1310687002115762, -0.6336617547722048, -3.6952441136391756, 4.117075934744457, -4.824485499919926, -2.330509874631734, -3.6069278799957254, 4.934604933506169, 0.7428035311905612, 2.700912058237698, 2.6807706515368297, 4.959548760057049, 1.889096806662472, 4.393698290611776, 0.6062604405112029, -0.5308567650498608, -4.312476234898435, 4.458463803928241, -1.7092479099356137, 2.553356255262271, -2.77210610025703, 4.566886807949714, 0.5699911549831157, 0.6326066050489672, -0.15775668736445075, 3.5961642670105847, 2.6159959974460794, 7.011726587584067, 2.4440335116810363, -5.36328180534036, -5.6271086881007655, 2.5512044287726154, 0.05873981338273414, 3.621975030556284, 3.8447872967616825, 6.502934090332151, -5.738719886143551, -5.189026832937692, -5.167381207493287, 5.248893745852036, 3.5082667083735033, 3.5717799345999106, 4.551174368247247, 2.073607832134592, 3.4816618715216707, -5.219572786286272, -1.0561971071451748, -3.6807439269342312, 2.5160073976071224, -3.9460845929717254, 2.4857953352354274, 0.4656918350630021, -2.477524544328808, -0.4227008638414975, -5.110818909050954, -2.4160938263851524, 0.00282677149646069, -4.152077623067662, -8.678259091541781, -0.21683089975022102, -1.8128459287806626, 5.46169299641655, 3.800111487453593, -0.9458798529247725, 3.847912851930911, -4.555631404481998, 4.471952696900894, -1.1252954061519578, 0.3605133743358831, 2.112429466837711, -1.6857109438678162, 3.3702005340734615, -2.611541045736015, -3.451193731139235, -2.4190414641795286, 2.0680429774261726, -3.2881336175527904, 1.8350652084123455, 0.20177229128087396, 7.3048432861520824, 0.13344798857489418, -1.2353226497078025, -5.379269960012704, -3.2197200159350436, -1.8823146453496, 2.1521508384449177, 3.6527619894229475, 5.116575495203224, 1.1353127535990761, -2.63486871244198, -6.107394101297901, -2.5136037968080154, -2.1323841877173715, 0.08079026523913774, -4.284109940465075, 4.5768650579480985, 3.2581281180381025, 1.9196570486633093, -0.42508180055600087, 0.7531093761551488, -0.525935104342557, 1.6913459012175727, 1.765303313356067, 0.12744816859830377, 0.7028364336075755, 3.0338153554702774, 2.422166290538399, 2.2516552379166868, -1.3476969619052268, 1.0320990189156025, 10.57277341760411, 0.573015385460382, -1.1258445676610431, 0.6069019740604614, 0.7508170139029036, -2.942332964070028, 1.3027376459080353, -0.6532168509436161, -1.7627604805579118, -1.6113570475930425, 0.33491562125531316, 1.2993919440105395, -0.7499239154573346, -3.9183895450216513, 4.083312989108451, -1.5738606682710883, -0.9543671203148797, 4.243650356800277, -3.521226749092886, -5.0301818040378246, -3.3247558137123105, 0.16503635931698996, 1.7377728014765683, -5.33885071911015, -1.6979021065681863, -4.683869666073589, -1.633521216988249, 5.275837064284404, 2.4060115976837024, 4.274850669408432, -1.168242494075426, -3.6222481137912568, -5.935771906055099, -2.571162446251462, -2.590162626721372, -3.5981240002106194, 4.859401878189594, -2.5981979257467698, 1.206825370479831, 2.591362646375214, 0.22076638840148718, -0.08668185928329435, 7.129756293875737, -1.5422851137337523, -2.1173895446088884, -2.2959070630133676, -4.27307861007357, -4.853127135203309, 1.0269951547369847, -0.4103151625028961, -0.3594797874086913, -5.814205078038048, -2.5138909803973832, -2.731969219896916, -4.581380437581878, -1.827105950156586, -5.900194656680192, -3.067455489455398, 2.6935808811332516, -2.3722523720505633, 0.5940714316935031, -3.758785884996109, -0.5536475787722037, -1.6504658171417135, 0.16348744413164137, -2.8983506900602554, -5.6181572140579075, 1.526313114768452, 2.0341143108866913, 0.19869175124919425, 1.002159929333493, -0.778821979762621, 0.36890686238749376, 3.9480044621980834, -1.0302555797710573, -3.899244522695969, 3.7573921782276862, 6.160194359816973, -0.07383437963172768, -3.386441054923775, -1.8271962858609099, 2.6389397464635653, 1.7010969957141586, -2.9681871790576544, -2.6873184183876706, 2.548222404065852, -3.5775305574329836, -2.2616197113067424, 2.357787644770055, 8.83241707947632, 5.948383742390786, 1.797869577520042, 2.0469858894148962, 4.559902443350834, -1.8831689991757312, -5.8529368644276705, -1.7737219872779593, -2.380268138617779, -6.865159407393981, -2.886090765565693, 2.295809317368278, 5.0645929468109285, -1.4260568422671231, 0.6844590851371165, -3.911539382854469, -3.5984480244700987, 3.266663229574775, 1.8414234700157233, -1.7785278670082083, -5.649392423703043, -2.407711890643486, 1.2943714659365864, -5.596834006838292, -5.3228206773800375, 1.2763720710537059, -6.801782602648118, 6.406045389082329, 3.4293943139379226, 4.598252890331027, 1.9907833273726605, 0.2761337619395197, -1.2649491156152046, -5.5546456599445095, 3.956836246508781, -0.3295799718809548, -7.4315213307065955, -0.10652581384301364, -5.029016407846422, -0.5087260744974849, -1.6732857981283977, -3.4558165531630314, 6.515322909757198, -6.781973583543258, -3.2352309086798896, 2.6644124871664077, 1.4733408195263378, 4.188012262944365, -5.6868391510116965, -4.6353897943165965, 1.7044389649657785, 4.800181269379949, -4.856131914900085, 4.652855832853464, 3.2451424799475643, -4.0309606612874065, -3.392342757010468, 2.3143364759387515, 2.3444615322719202, -3.38950858576983, 0.03503494554671569, -0.014806038155635474, 2.8118378496755962, 3.2375921498435387, -2.2525632672359186, -2.82360909166548, 4.918463577860218, 6.049387431591005, 5.285282961576072, 0.11512513773872289, -5.843487291405656, 4.257588276345645, 2.6115120647649905, 0.8601469786747907, -3.2224344242583607, -4.710181569406237, -3.6664781145249323, -0.8864695495977721, 0.3407970366277886, 2.0733673965549637, 3.9158976789722306, 0.6780131372434283, -5.654239435865171, -5.261303618761285, 0.41889366295872826, 3.4195649957279306, -0.8687435126364008, 3.1677164915142773, 0.11757356278885951, -2.8670376119590415, -7.233214788795336, -7.87525365523816, -4.595351564506921, 2.467029588223051, 5.612766382801254, -1.7005727839676845, 4.705933478560472, 0.5028382041665713, 1.4476096581348445, -1.291277140346254, 0.34270794233162927, 1.175517568702391, 2.263182847159801, -1.5029899836715026, 4.286251763591573, 5.551571713111181, 2.7186462799211784, -3.4488580431767533, -1.7137703379972473, 4.542777848117889, 0.7008883174931817, -2.1434881573485423, 3.8638675994260114, -5.555054932013133, -0.2991529467887449, 0.7937675508935569, 0.9102564107193654, -3.278580087070233, 0.9661196688621712, -5.686093536092019, 4.1344989431236865, -1.5765300278048866, -0.7127646981354513, -0.9962182046898779, -7.396374453820524, -1.8369391194801132, 0.7585705386356709, 5.227271487527362, -4.3495314278207236, -1.1496211854422091, 4.0840624776117656, -2.7445315262571945, 0.9066560187158901, -1.9376999791823788, 4.3853126131933875, 2.7838809885312763, 2.9961329959591736, -5.907546655912267, 4.931777011611442, 6.186981569607891, -0.7300349434787118, 0.8080950659969146, 1.5871841739587822, -4.763867431716475, -1.6132404144985621, 0.6545944430850404, 2.0229538011771364, -1.8334642541502386, -0.3739991931235471, -4.323393134751363, 0.7135078608993158, 7.989528425244663, 1.8070892114991193, 2.9375567118613013, 2.4122143854632654, 4.527729152664385, 4.945163392552476, -4.367547138946975, 4.685488057110428, 0.0023440089251163523, 3.62737444215965, 2.5601658585012887, -0.3783586395545931, 2.520848078505954, -0.421082345279713, -5.909355837651069, 7.696676430538044, 3.6830937307998663, -2.0459108775555275, 2.0679422598790405, 1.4970279563850948, 3.1883386841386234, 1.3655175889055313, 3.05105833198563, 5.174583606280184, 1.654056264755142, -2.3214336280706407, -0.11028895653425823, 2.4942284819880864, 1.34622335899695, 1.5693236129781674, 6.8507875046384035, -4.273290226672989, -2.455219626892647, -1.1952479880398281, -5.0812014277741415, 0.5617968578112573, -4.344434625922176, 2.7028168260916514, 0.3963062453591087, -4.41514422023446, -0.8155289006189684, 0.4776577076098971, 6.266482827749279, -3.281052253235261, -2.8817118231659937, -0.6869363450096154, -0.24002176934564293, -4.86639055706981, 1.3643868016441543, 2.6049834101742175, 1.8391130214556601, -0.363144980500011, 2.7318880803811165, -0.28680571826235934, 0.1107054485766309, 1.5355648798192116, -4.75088067420527, -1.661826207347236, 3.614637058698505, 2.8704248732189495, 0.4910828455302888, 4.255162351936412, -3.0544503752622125, 1.8255728571643064, 1.050720062594709, -3.7721243053281546, -1.7968011405909685, -4.908970903207332, -0.9709218745640112, -3.990986742786597, -1.0040430975051482, -5.974200377087206, 0.29909518434433285, -0.04623867901192209, 7.008545929395346, -1.1916846519190836, 1.1102709079322617, -4.025553192159395, 6.959379540529298, -4.076262965825171, -4.128537196651279, 2.0463543681115994, 5.102327262877327, -5.505604031109131, -6.406240682757881, 0.9166451986373677, 4.21913809377607, -0.910034405810896, 8.06807205621541, 2.5238625219977195, -2.302345676910287, -3.3345193484901765, -1.9921525514763505, 1.4608142836945013, 1.0622843907789872, 1.4404935849524767, 9.024477475222408, 3.8043781870686377, 0.5663106489501636, -1.263418220820202, 1.8104971508478285, 1.5088292580973401, -0.5446393855230834, -0.28731962255207333, 5.975639797690155, -0.12419748108121974, -2.789478881967726, 5.408727918365339, -7.767972984391352, 5.252608959146427, -3.8862865961965287, 3.406936850781278, -1.0009345539135217, 7.801844276791801, 1.8988745423383866, -2.2507487808960103, -2.179594141226175, 0.03673109343660645, -0.11639280460124408, -2.4628496896323173, -4.411830945765741, 2.2065604857825836, 3.9594522633040428, 6.045549736310671, 4.879058795280592, 2.255309795295614, -2.147799439905885, 0.029954098943418408, 1.8461121307293566, 3.7133316628668935, 8.944046341900142, 0.39456347044027223, 0.22854392826718686, 9.601281322082393, -0.6124367207084684, 0.5327407852898444, -3.1908252342249748, -2.548545573031695, 5.777262633055703, -2.3538041527464464, -5.445440999555621, -0.2434743917353002, -7.3593250367019385, 2.412531987626721, 3.0874517157410786, 6.111939286143928, 4.954597670692965, -0.9405829833321475, 3.808019556380174, 2.9141946533027747, 4.110298810674715, 6.792882438059519, 1.3861096987301977, 2.299594282921608, -4.259815490166557, 2.0134793964267304, -7.715902124668264, 2.1697700504607744, 1.2748357225419589, 1.2272297054324568, -5.135620746272816, -4.54704458043335, 2.364776151642502, 3.0382365109570966, 4.271087086285548, -9.139239735322384, -2.4194878807660123, 7.442080054501285, -1.354590835745015, 1.450528312839265, 5.817983251784224, -3.4682579545791916, 3.16500095145881, -2.0022906709667296, -9.986417485362981, -1.045896483575968, 1.4821118580156394, 2.9073151140803253, -0.9108213704099524, -0.700844033145559, -0.7977664652974795, 2.2778456649941465, 2.4870951561521957, 3.2307773881256345, 0.28336724502859634, -1.413883310855778, -4.289708781902959, -3.2202944309710557, -3.426140784032232, -0.7106237065030013, 0.8700695641035078, 4.2220765594778, 1.9529079813304615, 3.1848567660161193, 3.1079172041231273, -1.4358794713953666, 0.1620231167883958, 0.959389204567416, -3.0786580740617637, -1.6386892374516417, 3.4791068585261153, -4.023027294795132, 3.3583352116236496, 0.569290113168954, -3.6901959906176405, 3.443452802900627, 5.925253412282484, -0.4360180938334545, 3.230389660002496, 0.3798547592193098, 1.8502827145513723, -0.9162656897175325, -0.20358027067116846, -5.2574029106074915, -3.357864655183025, -3.7059036407765062, 2.341911496611932, -3.8993442794962734, -1.5407048497902436, -1.1354213852109327, -2.0613188915794223, -4.9106746172780324, -3.868831136609642, 1.9840156378195795, 5.685659987854986, -0.20412322904803054, -1.8229104999181347, -1.3556194371706032, -4.282299862990221, 2.3510256253937665, -1.5515293244745643, 6.6759100261925886, -2.6702826329611735, -4.742094623403812, 7.884422345788313, -2.041692563825751, -3.283673045816232, -5.158993212764969, 2.9944241307523485, 1.5184167684209056, -3.5597698694005673, -1.3615866282058509, -1.5921260935585984, -4.804069939545837, 3.3344987658225165, -1.3099365858551315, 4.389834453766495, 4.630720187161804, 4.288159654656529, -4.911559712619701, 3.654926423745348, 0.24056158563452917, -3.4014916525834478, -0.3532548512246918, -4.7513787562487515, -3.5422556381296015, -2.071815509422651, 2.5178370836865693, -3.4205755186014954, -4.681104810832675, 1.4295249093935951, -2.7559084506161384, 2.0151143185752756, 0.46922392151994397, 1.665468130668121, 3.966256158855484, 2.9393004759033903, 2.786156217533503, -5.866479205259499, 6.9957432817074885, -1.357220646031041, -3.471854541934923, -2.8537078159005196, 0.14218502853448564, 1.498736678555941, 3.0273798596951917, -3.595852862555604, -1.0492426441423117, -2.755091910401761, 0.5828652616081472, 2.1858426845894656, 6.123274973566053, -2.7581692905148536, 0.09442387787729772, 1.4799958988786388, -1.2540091792213233, 0.7319582888754326, -5.737971755778954, -0.840479314755438, -2.387838143706318, 2.3565935862854235, 3.763815966154767, 6.928951314465426, -0.8758986096931693, -2.2317034784868537, -7.97714159762387, -4.330590809354401, 2.9880279910026695, 4.225045464482644, -4.41761120000469, -1.7705579626795227, 0.9778195903416247, 7.5949341785839, 3.7562117327667206, 4.869742483615653]
BIASES_LIST = [-1.3850224744816015, 3.702999953774766, -3.616641868340701, 4.8005741421855825, 6.33487701795486, 2.762871854990366, 1.0959990092381755, -0.0797628176596257, -1.1095325428275529, 2.6552286800676685, 2.125026929492812, -1.3614824305260358, -0.004056110966057934, -2.6187107150581914, -5.504698247427149, 5.258476412407239, 4.812384601884482, 1.478946483874437, -6.574622119164996, 0.015609265420735988, -5.070145112749512, -2.8000978661396942, -4.067032321335133, -6.0935016722659565, 3.9285299570720844, 2.645311209739486, -4.023227865260365, 2.9197646577213923, -1.0837847851919347, 2.304109348034702, -0.3462990873275002, -2.29095968258156, 7.124095294751204, 1.8556121096594556, -1.6802204933396532, 0.44809848988757317]
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

