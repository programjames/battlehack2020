import random
import math

WEIGHT_LIST = [0.5614480636485598, 4.901882721575142, -2.3130874333114986, -3.549533081327181, -2.3253300116731475, -5.289968917533548, 2.871085903276271, 1.8303907330424367, 0.8114531270162737, -1.1038884675466052, 2.6011377568975145, -0.01365972798834266, -0.9020719979407967, -0.761201876678007, 0.23293481742364455, 4.9317250976348985, 4.68100558689998, -2.976456665005421, 2.8407360331345655, 1.8307871973363068, -0.37725619149811257, 4.355619019810805, 4.937962914766825, 5.420896006244611, -2.118584225896236, 1.6106922896214266, -2.1893772272918333, -4.358449374279379, -4.904049441317782, 1.3881849078393445, 1.3616444378755108, -1.1231881683345921, -3.3956768846202894, 5.261331542694306, 0.9931706101582706, -2.497740463277542, 4.153303138598642, -3.2905232653144276, -3.7496833746149867, -1.0280089529714416, 3.830058898708056, -1.8620109327495715, 0.43562778859218454, 0.16229970547495312, -3.265044403637915, 5.728877366696099, -7.87866104412135, -1.0424022519032476, -4.620959772998364, 0.8851643389977172, -3.8431786860987844, 0.6774009214969444, -3.5806763385383844, 1.8936136118701046, -2.251201910489727, -1.5939876117957301, -0.4168114737879083, -1.9809878805275705, 4.893724338402971, 9.883367246989176, -2.1939266568234217, -4.494736611107225, -4.315641916672298, -3.5222929209194804, 0.7289246947993429, 0.204062020014717, 5.364363857383774, -2.201843623281099, 1.2286079785671147, -0.6895926785988716, 0.4451592869167352, -10.348787025084297, 0.49217156799713363, -3.6929456007283608, 0.045285627026127206, -0.9699305343925954, 3.3904313682904808, -9.799328279808105, -0.06919698413468625, -0.5716978268564236, -2.4168240600999926, -1.1082405215242142, -3.24826796824495, -1.220499998721236, 1.0219657800218638, 4.8087534232839175, -1.8355557889394643, 3.9951926497862704, 1.3696334195372175, -0.688886078597758, 0.996654912871931, 3.7833420876607, -1.2439846688471412, -1.062159395179708, -1.5814212588541532, 0.5342824298970539, -1.7467723800176962, -1.133669785517914, -0.6275147138015962, -3.6847819379880615, 4.119824980948806, -4.825388982986523, -2.32857441717571, -3.609975689272891, 4.93192896766794, 0.744260479374997, 2.7030716931203442, 2.6846355489783056, 4.963111612183712, 1.885447122531518, 4.385332839631609, 0.6069443438767402, -0.5281416687647383, -4.311294178686191, 4.457210348701648, -1.707831929548726, 2.5563097245704123, -2.768427889028053, 4.560025312064976, 0.5754456099110433, 0.6285735285611521, -0.16047385781710607, 3.6006859989942317, 2.6176041983039746, 7.012735621767786, 2.437023526689954, -5.3565915971112155, -5.6305196314735415, 2.5509450235641276, 0.062381702437819944, 3.622229381720665, 3.847987094351231, 6.504870045640961, -5.749163420654708, -5.190211903648105, -5.160845873780915, 5.246845032281239, 3.5039342273246787, 3.56615237090795, 4.554851318593009, 2.073150695558501, 3.4835160976371236, -5.227953290567218, -1.0524796031909642, -3.6854519609054317, 2.5212823826479616, -3.9479270264808255, 2.4799045026309234, 0.46140507889361265, -2.481545665778167, -0.42241099174226043, -5.121316869381778, -2.4201862750337506, -0.003809578106078011, -4.158454170748623, -8.681315965195155, -0.2214035133587697, -1.8210436052206278, 5.459440970509371, 3.800985857635617, -0.9463154071725114, 3.841159825546037, -4.557227123052943, 4.481514764501825, -1.1284336863665025, 0.36760979180384157, 2.105859803406993, -1.687709497947156, 3.364916921406004, -2.6028396299869865, -3.452952810627206, -2.4253631351910263, 2.067324892746819, -3.2818098683362935, 1.8386482107491, 0.19673831960561194, 7.302009355386289, 0.14048438786952608, -1.2389525747896897, -5.377617983752091, -3.2192298852683816, -1.8758034768330205, 2.1481104952685666, 3.647408718987752, 5.11418412373139, 1.1338692375621435, -2.634317819424628, -6.107153189115611, -2.5104235372059422, -2.1285894006531594, 0.08789274939721681, -4.27922093037181, 4.576791257675228, 3.2519202621286443, 1.9160512497886548, -0.4299880557375243, 0.7525650324032416, -0.5180473363448539, 1.6954023715088633, 1.7687882783645779, 0.1255869748917152, 0.7059419523236119, 3.033608551002868, 2.4141038411632643, 2.250374316640467, -1.3545099366492794, 1.0343496169844546, 10.578453049719743, 0.5796247239520517, -1.1238105877396407, 0.602552781614433, 0.7509217323957571, -2.9419264523806343, 1.3076641575081949, -0.6539477188921853, -1.7588170515495063, -1.6106718195284646, 0.3383731350928094, 1.2994105602027106, -0.7531333026230242, -3.924988622651186, 4.081194086052275, -1.575017491158828, -0.9479867095461478, 4.255368945446298, -3.5317429049253106, -5.021300197490644, -3.3220539809234038, 0.15868028055111882, 1.732764424146969, -5.339696368739528, -1.7046297789550726, -4.686906913046652, -1.6483426106706844, 5.274938996286587, 2.402650170348025, 4.274093393178164, -1.1690866665412794, -3.621583663481403, -5.930335401436889, -2.572620373445496, -2.586002911650129, -3.598734363368966, 4.859193818560727, -2.6006078112347386, 1.2103120739482962, 2.5952303332917936, 0.21875847967786133, -0.07870315170473008, 7.1259333548592405, -1.5367356397721024, -2.115018446796798, -2.29367032284342, -4.264737973092591, -4.853376989055655, 1.022112904517933, -0.4159873984911758, -0.35066525715719243, -5.80714977293778, -2.5129866755635906, -2.7304431357020724, -4.576325452646757, -1.827771600932656, -5.9047435994512085, -3.0671071428030143, 2.69076595342199, -2.3731528669682054, 0.5899356800975528, -3.759584122515268, -0.5502019189133815, -1.66224330447981, 0.16850633157645514, -2.8917079976215643, -5.620652656249988, 1.5235806096731657, 2.0289267388004832, 0.20235214950471916, 0.9985794199507231, -0.7808973949585757, 0.3645455657323147, 3.944847044051415, -1.0285150960408858, -3.8933874240957453, 3.7510591830337825, 6.161124574514578, -0.0783410166085602, -3.3868866852611896, -1.8286488862454489, 2.6437524660498792, 1.7001557691572813, -2.97441070421212, -2.6913431190474486, 2.5505685947420154, -3.571731010479369, -2.262229826104419, 2.3652555538233213, 8.82784004526444, 5.9485066629860075, 1.8040078036419616, 2.046439073638477, 4.5591325680306625, -1.8797216779162111, -5.844956345736344, -1.7696242865790939, -2.371503427342513, -6.871450714678012, -2.881003980099073, 2.299123657183295, 5.07234717894192, -1.4293082884855097, 0.6698404124368352, -3.9169638562830755, -3.598461263028678, 3.2627168272615377, 1.844630211178862, -1.7795511084173532, -5.64628528402705, -2.406867711287772, 1.2879879867781154, -5.592426125985313, -5.319125705555804, 1.277655164495974, -6.804439471035656, 6.404972569903695, 3.430480134701001, 4.60386506158616, 1.9975156061083408, 0.2785488066081669, -1.270548852628957, -5.565212391103786, 3.9638604012927456, -0.33377801969479187, -7.423641519339895, -0.10054736677875932, -5.02246116734451, -0.5088198772021925, -1.673281056476786, -3.4578968583505674, 6.5111377734828855, -6.778246911337288, -3.2345232810628683, 2.665427973654059, 1.4809420850523822, 4.190714629922117, -5.692352024417717, -4.626830046128502, 1.7051163860622829, 4.803576443798216, -4.854920870104919, 4.647906246716879, 3.252777697943801, -4.023774947263878, -3.39930599216492, 2.3153998158597062, 2.3379780553654412, -3.388127006048205, 0.03692545597032862, -0.014300623755811436, 2.8156432559905835, 3.242950193416415, -2.241690995696778, -2.8249042034079666, 4.919389662899016, 6.055739394329017, 5.2844252247569665, 0.1181509678162733, -5.842916183475188, 4.261172020137428, 2.60702556329659, 0.8519666553407894, -3.2235152390342265, -4.7119610966931935, -3.6752634364955843, -0.8873688033374452, 0.34501810933937327, 2.0767888258860507, 3.920232019684184, 0.6777785342801947, -5.653411577754706, -5.2545070946017045, 0.42231767338361387, 3.4250581388307997, -0.8747192482897292, 3.1677338021409924, 0.12667024902835242, -2.8758758115952263, -7.229888466651695, -7.878911885531646, -4.5973900219124335, 2.461290390295389, 5.607877871582724, -1.7037469545187738, 4.710127120592842, 0.5162107252933913, 1.4484473940940739, -1.294712284678157, 0.3405649581088846, 1.178764924558492, 2.2589933374001854, -1.5000134864811665, 4.290122166243864, 5.553353059710428, 2.71508197649193, -3.4457804517201116, -1.7154121844620311, 4.540384419897636, 0.7033225864201481, -2.1531359698190244, 3.867496128131727, -5.552180398641779, -0.3057785669037548, 0.7810833875745113, 0.9073892579739216, -3.2710434656639547, 0.9658715707408729, -5.690387270042134, 4.13077819341541, -1.5799775183160292, -0.7134390866309083, -0.9916630152560554, -7.399258079564821, -1.8349754754491794, 0.7592184067982359, 5.225781620005219, -4.352558767953253, -1.1471696766591266, 4.089016488818886, -2.741884746368953, 0.914576729083257, -1.9446709980680053, 4.3937044732911925, 2.790449473009148, 2.997661456608677, -5.906968539317225, 4.933345041353749, 6.187985482210928, -0.7368808139268251, 0.8028824497851625, 1.5835677359021538, -4.7617061339189615, -1.6133601349887616, 0.6562015125883571, 2.0084933349024876, -1.8282686365293976, -0.37777451900161396, -4.323257818631883, 0.7144189088691042, 7.989722343343424, 1.7990893100209857, 2.926139895430804, 2.4142533241509008, 4.513766765914349, 4.937522160095329, -4.364451416884412, 4.691752344418288, 0.0027084844596245595, 3.6302176864106155, 2.5538962003205326, -0.37858074416868, 2.519474449663818, -0.415324224506452, -5.911694843454903, 7.7009942055361895, 3.6861451008061326, -2.039501479555818, 2.071270251164466, 1.4914089757166216, 3.1980631442390495, 1.3743512881213844, 3.0484016396634184, 5.181596070652069, 1.6569954454335232, -2.317296586668898, -0.10830333883329177, 2.502844442973628, 1.3412260537215241, 1.5761819522704053, 6.850220542185633, -4.281812957103655, -2.458823320086876, -1.19119714859037, -5.076320108510017, 0.5646406881357252, -4.346452366203635, 2.6924796797606447, 0.3928632871193348, -4.410740328665265, -0.8152100688277587, 0.47842312194396247, 6.265902408477353, -3.28469032539497, -2.881401083646169, -0.6921460143555452, -0.2370324216332202, -4.866344489575607, 1.3598258584119456, 2.607088009290214, 1.8366317051763636, -0.36924890292073054, 2.7316359629420055, -0.2908360664128896, 0.10701598196344886, 1.5386032578042994, -4.73851753415476, -1.6568666155425917, 3.604336353397357, 2.867660105216545, 0.49571171292084504, 4.255603185684452, -3.0551990074734325, 1.825970754499326, 1.0555802785925035, -3.775479788510009, -1.7883212722891149, -4.912105016075433, -0.9708768094402488, -3.9890729986958875, -1.006259718343231, -5.975612203771483, 0.29784919096472834, -0.04128101125153889, 7.009166716584486, -1.1853833063101946, 1.1058111626778064, -4.017528000856691, 6.958002367789278, -4.079511911424789, -4.129740558620884, 2.039670164583333, 5.106460166278579, -5.503062192315288, -6.405552291164069, 0.9142358058980887, 4.223682733500704, -0.9039876083567001, 8.071442109945623, 2.517073466728134, -2.3022560286459814, -3.3318735022932344, -1.9904286873090802, 1.4613955656297277, 1.062326008149529, 1.4304147292703817, 9.016542623764119, 3.7996070042742693, 0.564666305514147, -1.2635577635910107, 1.8070456397457535, 1.5019434516962034, -0.5478034966326644, -0.29083523108500786, 5.973690336348866, -0.1256638080236667, -2.7868466415600293, 5.405843105356925, -7.764132734040665, 5.249547459837351, -3.8832059025647143, 3.403964485929312, -1.0069427312157362, 7.8086529818202, 1.8909926779814517, -2.2551472343824814, -2.180867751189438, 0.0362444869220397, -0.1226089282670843, -2.460408552830646, -4.414430794446446, 2.216232442954068, 3.9635788010952613, 6.049787892392553, 4.8760736687445325, 2.2474362488344246, -2.1518609155384705, 0.03410714502645082, 1.8439503161440223, 3.7147906110826967, 8.940526691699008, 0.39628043984746963, 0.22740787924712033, 9.602955530453894, -0.6136875742088764, 0.5415026099779938, -3.190389161600355, -2.5529054450404494, 5.778540651083098, -2.3507318579488263, -5.447784226628016, -0.23573353428856814, -7.364680891681585, 2.42406283785989, 3.0821287584119106, 6.110151674027062, 4.951589192077971, -0.9477844130514946, 3.8116934462443908, 2.9172787015697255, 4.114219164774602, 6.783565021787868, 1.3790543978511014, 2.3072531318157323, -4.248879014531726, 2.018262078108938, -7.715141940008651, 2.1638419408890086, 1.2658801922589216, 1.2194452214213962, -5.136980386512219, -4.535832972006872, 2.365666806449268, 3.0314446062470672, 4.271397918010725, -9.138652901205473, -2.42127556399128, 7.440188387667111, -1.3610111272874688, 1.4427937997320024, 5.832276732295941, -3.469981151271031, 3.16054093584678, -2.005521459961104, -9.98737574032652, -1.0494734694932828, 1.4707474786236137, 2.8983660888214855, -0.9043379538041169, -0.6969929927236593, -0.8135433070766263, 2.278048085633362, 2.4898099838957886, 3.2204458619504415, 0.2848967588889853, -1.4180185349167054, -4.29429932884424, -3.22748597031987, -3.420930830702146, -0.7155637180245332, 0.8591076349135387, 4.219479825719973, 1.959236474291222, 3.181112167159644, 3.112795080163965, -1.4440551278965583, 0.16249217275975278, 0.9572609957004853, -3.0825480050770477, -1.644794244866767, 3.479758778714373, -4.023055014702361, 3.361171768375139, 0.5635939713135257, -3.689169264624778, 3.443422999687195, 5.921970023846523, -0.43897168453411356, 3.225840459898998, 0.37762811126593226, 1.8532460465889604, -0.914460677083348, -0.19967377783953014, -5.261455412984046, -3.3556698873319166, -3.709846215982162, 2.341276161376885, -3.8967870248494343, -1.537170303066283, -1.1353964156596847, -2.0597052090785115, -4.902000595964767, -3.863186200822595, 1.9852283375804614, 5.681004183050254, -0.1964165636991012, -1.8260165059997238, -1.3523898221397421, -4.278592677457288, 2.3438786607526727, -1.5543437058882545, 6.6880866248411674, -2.6813108448816227, -4.750402918377102, 7.889437023109498, -2.046171404290071, -3.278916994702961, -5.165959758910043, 2.999055879943669, 1.5211144137720867, -3.556001586567853, -1.367224967840109, -1.5908120977902889, -4.812325786906194, 3.331239250935374, -1.3058086616124576, 4.381687523220765, 4.629113462423437, 4.293127272735619, -4.913764695889619, 3.6454644867639336, 0.23810118634329924, -3.402794966670112, -0.3618041525542035, -4.745425876908049, -3.546115997300624, -2.0685545084091737, 2.5263413697717554, -3.406975261066654, -4.680316582044173, 1.426706439424176, -2.754089149682785, 2.011431179509675, 0.4739075154374939, 1.6691916313362274, 3.9658998082933947, 2.9338992118582756, 2.7903659467734023, -5.867012540405756, 6.9848501731709165, -1.3590687183247623, -3.465893224590412, -2.849371607208252, 0.14851525310361074, 1.4953497768440724, 3.0297672580060118, -3.597901208960883, -1.0536409280007264, -2.76047281310315, 0.5822274631813255, 2.181952874485684, 6.127374005370782, -2.758487853326484, 0.0911996312576336, 1.4718450123901587, -1.2507352266676381, 0.732371655216217, -5.73405661016928, -0.8324787671518807, -2.383921276968975, 2.3524357146740025, 3.774789043917039, 6.919781287039001, -0.8722668974458099, -2.2366900931287943, -7.984091395393145, -4.324060406832159, 2.992489345224317, 4.224400203846466, -4.422804707146386, -1.7781688261168622, 0.9728684763923078, 7.5924332152653395, 3.7535257989003266, 4.871596155473144]
BIASES_LIST = [-1.387806200928536, 3.7095352033873876, -3.6134088293553472, 4.793161975360508, 6.329592417574108, 2.7708266358520306, 1.1023827445146521, -0.0817573058287851, -1.1015968637428555, 2.658172077312955, 2.1289190813710666, -1.3610560886665015, -0.0030421811123283174, -2.6148628970909953, -5.506737037605809, 5.26462376373926, 4.817326132418562, 1.4789892747773352, -6.5627771487677435, 0.025776488347469626, -5.077498483944787, -2.795890629704382, -4.062721871260282, -6.097537312120572, 3.928331110456739, 2.6520529021871515, -4.028465099047187, 2.920899655644504, -1.0779141145619697, 2.306138763852582, -0.33825866264098703, -2.296962050975952, 7.124346326149264, 1.8515238964999103, -1.6799007434905309, 0.44578354006223075]
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

