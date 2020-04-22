import random
import math

WEIGHT_LIST = [0.5618565963708777, 4.905625092708299, -2.314245823697726, -3.5508586549664813, -2.320371472814589, -5.295634081938653, 2.8743645050272613, 1.8306707630521808, 0.8043404271321849, -1.108680201601007, 2.605032546627927, -0.011357505744623474, -0.9019279991950591, -0.7617097992852256, 0.23423866934081752, 4.932076243274806, 4.6782793688580036, -2.976189642684079, 2.8399073598294264, 1.825768264724811, -0.37873938466628054, 4.349938344778892, 4.9348222393727985, 5.417545176233303, -2.120356776714092, 1.6126249452396035, -2.187496700462448, -4.36001714181481, -4.9018513479834604, 1.3841922934775495, 1.3625825852893163, -1.1167151341840462, -3.393499053148605, 5.256858500060781, 0.9929936417212345, -2.4994096654808327, 4.151244954929962, -3.2889104284166844, -3.7477539899876744, -1.0299831591780226, 3.8322087412495764, -1.8627592166827727, 0.43718144697263933, 0.15976456125206703, -3.262343005846681, 5.732880402749321, -7.88402093881475, -1.0406472119854833, -4.617008814684798, 0.88373038667918, -3.837568426607523, 0.676314236699314, -3.5768957799966135, 1.8938199115330183, -2.252191787325719, -1.5903160649824948, -0.4156957588631598, -1.9802996767810266, 4.889896995505684, 9.880514827846586, -2.1973497857173334, -4.4928444444332225, -4.313917478826944, -3.5267670425761484, 0.7277534616646042, 0.19981364896734402, 5.3607121042080665, -2.1974444686946013, 1.2326386350223775, -0.6862477458401499, 0.4478746138885405, -10.346002317767109, 0.48891143920842745, -3.6921347284881234, 0.04256367061236939, -0.9654923378155068, 3.3946702359546483, -9.80211328970727, -0.07589442583532267, -0.5713944906312559, -2.415150808315645, -1.109088767347686, -3.2509950473605156, -1.2243252694655407, 1.0164884744811042, 4.804418998452669, -1.8347500732384379, 3.9935775871477786, 1.364059194020843, -0.6912383676529354, 0.9995953650033337, 3.7780703420791872, -1.2431228457701315, -1.0573469794760777, -1.5795867790872749, 0.5389677929336065, -1.7508148805922994, -1.1348805561464834, -0.6297407663121366, -3.6885679681424937, 4.118743101592848, -4.827840210175099, -2.329322778037447, -3.6086892359286558, 4.937612012317983, 0.7476257895840216, 2.6966811494244958, 2.6870988329791072, 4.962546327172462, 1.880673415444017, 4.384785159204991, 0.6073378247173871, -0.5347525944983628, -4.317064690308235, 4.45936652407444, -1.7115103249560402, 2.561918860042681, -2.7691833938549073, 4.562243285622876, 0.5741225230246025, 0.6282355935775633, -0.16057280856661435, 3.6010535131476082, 2.619931635386528, 7.01172096732028, 2.439500238785878, -5.358912978336445, -5.6326204658063785, 2.553798708416762, 0.06007233544633582, 3.627622846589634, 3.845045337788453, 6.500053531305895, -5.745659702153352, -5.192703147638113, -5.16392592063145, 5.243566692045138, 3.505497078543135, 3.569678952960095, 4.550255180243987, 2.0735604863696575, 3.4821077486030623, -5.225934173806827, -1.0527045924577356, -3.685275870926407, 2.519320511883823, -3.9498110191794695, 2.4798144860377898, 0.46763239174595195, -2.4761281144485343, -0.4263095632919832, -5.1188034351426115, -2.4196586960404827, -0.0018565434121128148, -4.157521602933548, -8.68105769093138, -0.22065484321837642, -1.8168587289470057, 5.465795836557808, 3.804312984463166, -0.9472566242795251, 3.838591155929811, -4.563439357652305, 4.4802138344303435, -1.125373492113129, 0.3674479285975168, 2.103117445222153, -1.6883825015200449, 3.3684714374554474, -2.605247110010212, -3.4518288145065816, -2.42449900370254, 2.064426564454701, -3.279298005583391, 1.8343729449829347, 0.1959483880744147, 7.299778126381313, 0.14181455728456677, -1.2355870088116379, -5.378386185473801, -3.2197414097106325, -1.876807060419107, 2.1504350019844085, 3.655661894962043, 5.112560081213503, 1.130956072218354, -2.635380831602714, -6.110332026023907, -2.5148141595962508, -2.1320449287360077, 0.09041224257796522, -4.279582113228497, 4.583394061650476, 3.2549843934112523, 1.912674727079508, -0.4339200043490629, 0.7543319377392732, -0.5203460193019126, 1.6988495927359797, 1.767062528866699, 0.127763721728475, 0.7061710403476688, 3.033575598086441, 2.4170317470012215, 2.250911032822818, -1.3488165473258982, 1.0351965352604842, 10.578716363033354, 0.5779480996379939, -1.1299735536687712, 0.6043274354016329, 0.7556588946335935, -2.9414751618814057, 1.3061190943244894, -0.6492168175117213, -1.7584714978036542, -1.606105187000718, 0.3332540656897555, 1.3038789602914158, -0.7459432078134105, -3.926991124849844, 4.08127394756346, -1.573829533736983, -0.9519284730884243, 4.252478103319427, -3.528835927156254, -5.02205435075174, -3.323667428071671, 0.15553600460391356, 1.7335758429028023, -5.336975920127041, -1.7021409823041915, -4.6902476739171375, -1.6439401460744922, 5.271802980842708, 2.4025204364774106, 4.278329049703308, -1.1723210673140974, -3.628249078327328, -5.931684684489142, -2.5724076382127237, -2.5882510781536734, -3.5937273165743377, 4.865206037728937, -2.602704274444568, 1.207409686904169, 2.5960184616742152, 0.21955066841376353, -0.08458109083056027, 7.126657242821501, -1.5423657859036495, -2.1134067260020566, -2.2932182819979143, -4.266419786669187, -4.854804113888582, 1.0192466915218679, -0.42047987893133193, -0.354896472512838, -5.810181698005316, -2.5133718947202035, -2.7296202383363704, -4.5774700531304795, -1.8306895044885976, -5.903382692036998, -3.060610375425752, 2.690788639416939, -2.3699722406786052, 0.5895961311026565, -3.768452561904186, -0.5514938844994236, -1.6615069494266193, 0.1713210087643251, -2.894694361000734, -5.6164031370420995, 1.5190308667302288, 2.0342934075956727, 0.2030897788930639, 0.9928783016251879, -0.7803291932565041, 0.3657068592985372, 3.946000619465112, -1.0283040178829133, -3.894658333914627, 3.7543248176835733, 6.1592124741247325, -0.07994094664817063, -3.3830962294189835, -1.8266617324299668, 2.6409209939827205, 1.6988264640889466, -2.9762463568446575, -2.689822231824839, 2.5466084550668966, -3.5755807742467485, -2.2599754369460587, 2.3602563195133457, 8.826998850834372, 5.952010910719249, 1.803010459843256, 2.048076777358192, 4.563167728269968, -1.8821621673752569, -5.844341209358097, -1.772971624808033, -2.3737004768896153, -6.867908001994619, -2.882077308436605, 2.298737925233294, 5.067302774488827, -1.4234191550506097, 0.6757389313603703, -3.9187570783056387, -3.59594223456334, 3.263232028940241, 1.8453098557004413, -1.7788077685766188, -5.645665358105015, -2.403146692084197, 1.2884103461597542, -5.589726903353751, -5.316404378960915, 1.2790684280782594, -6.803238746531628, 6.406222215596043, 3.4309436219044747, 4.600410889406352, 2.0022669949533305, 0.27856635868371116, -1.2693184485299456, -5.562264882705847, 3.9666962782647195, -0.3353175631755504, -7.429490661828519, -0.10234094124727347, -5.025546699010694, -0.5107360947963988, -1.6765822173617424, -3.454723225745977, 6.512161535694069, -6.785966797653686, -3.23994925424658, 2.664376589902836, 1.47729300114329, 4.1906253079761955, -5.688428662764196, -4.6314629976604005, 1.7043679086754542, 4.800066467306117, -4.851260791678992, 4.648051600706833, 3.2561805311512133, -4.026958826260581, -3.3983873928772117, 2.3156136807056398, 2.33513916279411, -3.3868228637489497, 0.03427858028927009, -0.012497861209104164, 2.812707727006783, 3.239529627170553, -2.2438854056384963, -2.8256802613636336, 4.918861883579123, 6.0532846360501935, 5.280049486583284, 0.11547383394005296, -5.839826091305446, 4.259927945449364, 2.608164557405839, 0.8538714285811622, -3.2240634912408237, -4.7081564291358715, -3.672393250552054, -0.8881439289952171, 0.3428993339814753, 2.0754959331110814, 3.9186854242685873, 0.6754325799198682, -5.6523119196209555, -5.258739286241338, 0.42150715474641515, 3.423645288592028, -0.8688770044074859, 3.166499190443774, 0.12624171601561293, -2.8701868101278, -7.231562921161691, -7.878610041219628, -4.595291477173117, 2.4618357775648665, 5.607281842180512, -1.705902527057682, 4.707278561903783, 0.5115786700619869, 1.4451920665603413, -1.301636460833344, 0.33769136276326367, 1.1800648138144207, 2.2632375925399693, -1.497353599190304, 4.288778953927431, 5.55133170850503, 2.7106894902633445, -3.4505729003887837, -1.7103949865336598, 4.539166710982546, 0.701280866371227, -2.149205524179548, 3.8719074514291116, -5.55258039272836, -0.30425058101075303, 0.7837263813031426, 0.9051373757192283, -3.270129097990168, 0.9616873143736177, -5.68808781676749, 4.128219888891332, -1.5782231774471798, -0.7129185466654997, -0.9949767608597458, -7.397873983129289, -1.8356541502061607, 0.7543109301946288, 5.22089402722829, -4.348141916170176, -1.148465245486997, 4.088435360299109, -2.741210524750201, 0.9184852558035269, -1.9451044929089978, 4.395252496553517, 2.784006545408903, 2.994576266601822, -5.905461576793554, 4.937156168970508, 6.186588163096299, -0.7384885983637732, 0.80722093784208, 1.586224885651165, -4.762114853332966, -1.6141587748977524, 0.6575124689044134, 2.0143417296850896, -1.8269192149124216, -0.37792617898247766, -4.322520135631503, 0.7139109479308532, 7.986873027295227, 1.7996126292106684, 2.9277307015568894, 2.4104528453524923, 4.519525831851151, 4.939690676345079, -4.363167718206185, 4.690608750162465, -0.0006521520405903744, 3.6285426232865143, 2.5567154854100016, -0.3759544966414223, 2.5176121717251365, -0.4216777833177502, -5.915261411680897, 7.696520362363961, 3.686168805881268, -2.04037041141589, 2.0692554893987083, 1.4926675597185293, 3.1934158478612806, 1.3733397991985703, 3.0518330059140624, 5.181842017557958, 1.6534933053539556, -2.3194642819946143, -0.10988004001032192, 2.4996475042829687, 1.3440148204124245, 1.5800355626068199, 6.8520834362821255, -4.278166314843071, -2.4590531781024776, -1.1927514339179452, -5.079682414251549, 0.565134832762023, -4.3413764320720185, 2.694951494670548, 0.3988305993198827, -4.409929154952834, -0.8151658790214247, 0.4786049493666017, 6.265097154006476, -3.2840682173031848, -2.8792317776419343, -0.6953500957389407, -0.2377880068244667, -4.866040144767806, 1.3652876118087631, 2.6111080447281214, 1.8371136195636755, -0.36734401238019093, 2.7328079163032104, -0.28761492617904216, 0.10877547392781108, 1.5415547468380564, -4.740153782347517, -1.6596981957346317, 3.6026995942324263, 2.871798625310525, 0.49212935928901347, 4.260736082264149, -3.0572202178363383, 1.8248894633911192, 1.0528242721327525, -3.77322393795196, -1.7913549642771098, -4.914032576405188, -0.9747023756131589, -3.988711762723299, -1.005157237842597, -5.974937546908968, 0.30084438481309056, -0.04470108656935265, 7.013665526885749, -1.1824792482373458, 1.1088424889918762, -4.017886355261067, 6.9591850890114175, -4.077629256214979, -4.132820688010012, 2.0450408866518974, 5.107116774831168, -5.509594960788081, -6.40737181328366, 0.9143433849777934, 4.221265629331807, -0.9003600070204008, 8.078607931557407, 2.5216601617257695, -2.305361299460268, -3.3314112299772645, -1.9885717979908049, 1.460582702248951, 1.064564530936798, 1.4363493557584062, 9.021097125883083, 3.803075367674862, 0.5697976974354113, -1.2663127150553253, 1.8071811230254011, 1.503544791066538, -0.5487488130365116, -0.2875821609757031, 5.973021665010023, -0.127545234420235, -2.7926673032460436, 5.4081711630322555, -7.765148060708134, 5.249595770480076, -3.8846008602700843, 3.3995140634229557, -1.0104490809207567, 7.80802781103694, 1.8928729846502217, -2.2578290973793793, -2.18494860013302, 0.030720629346294093, -0.11585262995406115, -2.4582547071281495, -4.412059821227564, 2.215703160061507, 3.9593791307799733, 6.049633233223609, 4.873292959519715, 2.248739464016701, -2.148928663410995, 0.03131825308850409, 1.8505134624655943, 3.709191187879342, 8.940294323220707, 0.3995370738648285, 0.22489074472872667, 9.602814312661105, -0.6140658503198274, 0.5382986913623194, -3.1848724310389867, -2.554950735267348, 5.775561136256363, -2.349487802381763, -5.44880715002223, -0.23963196103774934, -7.359917338544795, 2.423572079943266, 3.0775038217161512, 6.1089546121589064, 4.95132613444714, -0.948992713892402, 3.8094729600242703, 2.9161654188235953, 4.110408110063488, 6.784821715042766, 1.3860793053296225, 2.3062009747827816, -4.2513693028489845, 2.0141295467864824, -7.717642888093503, 2.160684792993993, 1.2659072000603242, 1.219706470299527, -5.1403414856878, -4.537546005841554, 2.3639234921452967, 3.032786075910906, 4.271533425428687, -9.13856844684015, -2.4232776947453796, 7.445927898626422, -1.361226605966999, 1.445776462519582, 5.82888541074035, -3.470446230750697, 3.1646047599020974, -2.009412200062472, -9.9825090115741, -1.0519955772436733, 1.4772963176943712, 2.899987782348047, -0.9073460563890271, -0.7013397206590986, -0.8083158446801118, 2.2753144770052454, 2.485885533035514, 3.22587205942315, 0.2824827071314919, -1.418309939987551, -4.2888676460816795, -3.2281362135832925, -3.420628432374426, -0.7117436113736524, 0.8605222804449683, 4.221915901708669, 1.9557163961259518, 3.178129725454979, 3.1088284311340297, -1.4400936734765684, 0.16156773927901122, 0.961938689056602, -3.0885693147880198, -1.6493202492368506, 3.478658284495479, -4.023323772423476, 3.364548015385935, 0.5646295294791251, -3.6882980800309944, 3.4447857070436703, 5.925623583769665, -0.44555589714013627, 3.2252271638867507, 0.37633933974423356, 1.8540629573973593, -0.9164853586052624, -0.19921231945594156, -5.263377484765392, -3.352942463793205, -3.7132492786656255, 2.3391722607666923, -3.900828985696662, -1.542650368243974, -1.1352648768995022, -2.0569872814668235, -4.90358045971702, -3.8662343713226717, 1.984290751314484, 5.681499895566153, -0.20017795560635132, -1.8282528069315018, -1.3546804611115744, -4.2847973696358626, 2.3433483504379002, -1.5560950737362491, 6.685369911680624, -2.6782697507978077, -4.749510526673632, 7.885114893341416, -2.045094758821495, -3.278723410920777, -5.1636425777373836, 2.9957877724100004, 1.5184806205453376, -3.5563995444413594, -1.3642690839704912, -1.5936507482950344, -4.810831333987223, 3.331812378622292, -1.3057514422548142, 4.37870866603965, 4.630688502279324, 4.293127492922587, -4.91126538357873, 3.6478437266216215, 0.24105168684369963, -3.4014822191989196, -0.3638299335659373, -4.738839097283102, -3.5438332273186317, -2.070634530003928, 2.5225618685299556, -3.4067142903741097, -4.6763042760418845, 1.428209079203586, -2.7544487206121744, 2.0170763130424474, 0.4704063176513965, 1.6722286457394009, 3.9669212496138577, 2.9365378717903763, 2.7916895489328586, -5.864213230505254, 6.990168757952745, -1.3607436983255798, -3.4664468882096253, -2.849419253128166, 0.15004421322213485, 1.4940822756366463, 3.0333281990063634, -3.5970955865735665, -1.0496684471597977, -2.7607434357156, 0.5844794383200429, 2.185167753887867, 6.126675347358308, -2.75929077879658, 0.09488472671318327, 1.4752836438816859, -1.2531085102911999, 0.7316725920678414, -5.736983425906255, -0.8365156299359686, -2.38492664948185, 2.349966695458157, 3.7733065490048965, 6.921841132649809, -0.8742790231826832, -2.2362675880346563, -7.983384408915503, -4.329315873927331, 2.9912750577439002, 4.21805802862017, -4.4206114227319215, -1.774661138567352, 0.9759962680054539, 7.592213581141731, 3.753418814510554, 4.875531753964047]
BIASES_LIST = [-1.3831479281445742, 3.7109789502459782, -3.61504432000563, 4.793175795284738, 6.332298226571589, 2.768379452017689, 1.1028700323481118, -0.08029393241029581, -1.104497480208347, 2.654500605446971, 2.1258472443157164, -1.3676294184348092, -0.0003697128130588532, -2.617932547738751, -5.505154747405521, 5.2652094905040006, 4.821147340837239, 1.478102886288984, -6.566780298001569, 0.022974244250089586, -5.074141763804479, -2.798975509842937, -4.064119009728334, -6.099034786154179, 3.9261725308593225, 2.647440598381591, -4.024365019539371, 2.9204981675698387, -1.0810051853950897, 2.3042550552864696, -0.335909220298389, -2.299289872117044, 7.1166353899879375, 1.8536136938650063, -1.6842340047470972, 0.4488740071752906]
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

