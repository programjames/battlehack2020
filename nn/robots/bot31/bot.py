import random
import math

WEIGHT_LIST = [-0.4818293711912496, -9.25705547533919, -8.942727939274667, -2.4084727465638434, 4.600662314151563, -0.3355241670853779, -6.54103147590634, 8.555523739551909, -6.714852186623068, -7.466452817080194, -5.516102142247461, -4.925817274847208, -9.370846630759997, 1.0567850090463988, -0.9330394497913126, 6.567421278833773, 8.848214578716021, 4.108761472724092, -0.7030012393806295, -8.823062482082884, 5.405405698278297, -7.971589019690908, 0.9360666293766187, -4.216352995003582, 7.1612070153731295, -5.156984395437137, 9.111758957721296, -3.3104437088950274, 3.11250909164324, -5.8026366643948695, 2.776700593789041, 7.441940813288909, -9.85772261648022, -9.243410180405506, 7.747990990881036, -8.105546384035305, -9.12407593063014, 0.1749444418189583, 0.38382646577721324, 2.1739435854492015, 2.2874097080843576, 7.212222000244633, -0.05488346625486784, 6.148386782099294, -0.5563764029660874, 4.108197285682941, 6.519044771428206, 5.390913022981575, -8.820363176596393, -7.993770009963452, -4.294047223412849, -7.664785674432563, -7.90976938879695, -8.146742913255531, 2.743305596144216, 5.179302912083951, 4.009501831474207, 9.46910239505874, -8.291140263048595, 9.365490517175516, -2.915969315048188, 9.527844520029038, 4.810519198231734, 0.9332546260572823, 2.8939001692457715, 7.871533947461913, 8.388045520710612, -7.349442940879327, 8.534483994508456, 0.07628567967863198, -0.006787538782013769, 7.524955604258693, -6.224363256184655, -0.5354972657870682, 4.358978602948735, 5.511608884014086, 6.739393699072025, 7.10147741886405, -4.426135695132601, -7.689675269956455, -6.41802205296675, 7.56634133522023, -5.518413287339343, 2.072130676674739, -6.162026767328779, 9.635097128310544, 6.512074609951661, 8.25797668488017, -3.5980809865812553, -3.4550459992356153, 8.097976128150044, 7.324710080865994, -1.8515810614796262, -3.715364657916547, 1.0858324950418385, 5.476463982143224, -0.0023000078832140503, -3.914900602088305, 1.2994500499451291, 1.8779311508306016, -6.05545982256007, -0.8776069879055015, -0.3190695475861851, 1.524877174326214, -8.633414322409902, 5.04037043374392, 1.8462749367098912, -9.900728693844975, 7.482839086974206, -0.6680778042600366, 7.8876047860628695, 0.305645484438271, 3.580942281057764, 0.7813325439363439, 0.18823456387972826, -5.495636681817945, -5.627894126370814, 0.009372255608342428, 4.000050448702888, 9.031443620899434, -7.196359967425008, 2.5879332482546324, -5.085926637224163, 1.849199459576523, 5.852041904420101, -2.5914984747919645, -5.450086406042891, -4.67837486653877, -7.807244935454351, 9.43008269698488, 9.1001221014332, 1.7397913836284769, 3.906147221056722, 0.3382134834514279, 7.589357354473847, -2.68704196879119, -0.5012244565641861, 4.557860780410476, -6.518461463651779, 9.12246007476229, -3.9427352678212273, -4.919788802333221, 9.640927672209042, -2.663619212732355, 0.6410539529134311, -1.3374982193817821, -6.678650812810645, 8.293188740251672, 8.841823523363104, 1.0557079594343897, -2.5376611786237575, 8.203275499783405, -1.4752236199649378, -1.4082374326279101, 2.993483128404627, -1.12141178112374, 5.427806034551965, -8.781146633474215, -1.8210533905056252, -4.420758630928789, -3.0960793907364836, -2.8216441236467222, 4.777355624145121, -0.2254748998058016, -5.649470005350858, 6.921888451255498, 6.7074731863442025, 6.302971771891276, 6.751133881182106, 4.840474027305069, 4.582185981209658, -8.876973969552356, -8.705933855010954, 4.1306705112638795, 2.008265214177662, 9.676683232724585, -8.39248006965075, -8.175811311996542, 1.7193751283718441, 5.976061360786794, 6.191159082034435, 1.5156038820307138, -1.9147749652676147, 3.7793115413991245, 7.972005787719965, 4.12941903107683, 5.780056751039586, 5.642982900993568, -7.97777378708306, -1.2827737156245398, 7.418793200474639, 8.270532664652634, -7.040750172798271, 2.8988486149487223, -3.876971265504203, -8.168171550753181, -1.4179819453495348, -9.778002470780908, -0.32812324635303547, 5.047442000855147, -2.5709224144844285, 0.8525873113993612, -0.21871463318704976, 3.5265936129796653, -8.869175873475502, 0.8646385019855192, 6.824443637306821, -8.26425486081675, 2.5651639571245077, 1.076232975706164, 5.551250664552974, 6.761325940200592, -8.253705921753031, 6.399019593430083, 2.8626278568684036, 7.982881998301075, 1.0520004614604268, 8.861172406072505, 2.640726535658084, 3.3059226531237194, -9.039281244766899, 0.39867539425600995, -9.373566814987257, 1.855375256574824, 1.3483581970959442, 9.972294314099614, 3.885015491043678, -3.2976503281714775, -9.248030176477815, 1.846765568844873, -8.092750024356459, 6.826384915812021, -7.510193310037245, -8.438694179052586, 6.125752998976221, 0.5113161988620654, -1.0914911335508055, -2.5511933264155484, -3.362625835504767, 2.2374410038500248, -3.56613679259919, -2.108787295739811, -8.356707185730102, 6.2205140206497695, -8.29440029879368, 8.855742433315847, 7.74810016368161, -1.3605160502240121, 2.6723609212437296, 8.406684502994807, 1.4670870256454975, 7.254295926296997, -4.7406986478458935, 9.437646275030442, 0.11791961718222055, 0.5532656579148174, 1.6802350236348413, -6.602116875377688, 2.0144595216066907, -9.723479126811911, 8.952333220105892, -3.672341139365889, 7.26563234738996, 3.1964380423152416, 9.823141512372032, -6.6679410152386565, -1.500462118983938, -4.936519955122705, 5.172697828423679, -8.411008408929085, 1.6972261865305232, 8.915063909156679, -1.4411341348136695, -4.9621120758890385, 6.136628737917611, 6.594874636255167, 2.528163650745398, -7.752549136960376, -0.7696656422558377, -7.094575379755743, -7.5426527809732296, -0.659409263345685, 6.450600937301672, 7.160556780758338, 9.80258549883132, 0.6705077532719379, 4.547611294540438, 4.664622452087821, 2.8135431830776536, 1.9943167841202722, -6.539411733452994, 4.029257265665615, 0.9769803604020701, 3.6643982201104013, -3.964022649677288, -2.359806034201048, -6.4618191014772774, 9.346475621834692, -6.29862143388777, -2.4684768610531442, 0.5611022283913947, 1.4026946730671934, 2.044998744292281, -9.046614663225544, -7.013014748901972, 3.3582605120111637, -5.168148333966567, -0.3630236708850809, -3.7576954965489033, 2.9007346585853444, 2.7136638599493086, 5.51275810905895, 4.132144666255302, -7.670941972714762, 3.4515212452452655, 9.367734440162149, 7.641992151388589, 6.265912186547052, -3.6380242534720715, 8.758492143071372, 1.4739856702548195, 4.907111346745056, 8.600575342891254, 4.566498210009156, 2.2561765583005453, 3.463376975160033, -7.797920432710539, -8.890848169721009, -6.209933652316957, 2.9861869425529477, -4.527074115433893, 0.5442317009095028, 7.339525261087175, -9.813989910805589, 7.904299048240503, 7.737817483068866, -1.0514378091868188, -9.69755540747384, 7.205490584319037, 5.618974160789092, -1.4970988697163623, 0.2122226481011431, 7.573606635005454, 9.89061952827926, 7.657045367269756, -7.701665015248853, 0.291432805220488, -1.0282615822489571, -9.787875309033968, -0.8837630780293289, -8.393021812431043, 3.680365570527133, 2.1856328810750707, -5.120901057226148, 3.5479223254132073, -5.898235791402426, -1.3072190773879004, -0.10012155245541265, 5.551241730720269, -7.573729137213139, -5.988541187178981, 9.604779093894432, -8.27026592940493, -2.9766212926912017, 5.414330858586752, -9.47340744001907, 6.047446308023918, 0.7102803430305329, -1.8226496075085237, -8.21284073719834, 4.478210806674154, -1.923811519443401, -9.837298233728344, -6.182141891628515, 5.083886603880906, 0.11766676449360958, 4.269069034975404, 3.599775586864544, 1.2954248120495944, -1.3594545155389106, -5.930357518030444, 9.86712962599638, -4.3748937721554455, 7.146431701548753, -3.8423308172186914, 8.545485533761454, 7.061642621360392, -9.71888219577182, 3.5738132643548486, -1.7783880592652324, -8.5227090077073, 6.484285051510959, 7.239704163108833, 9.547459207555818, -5.683628447953993, 7.191095274325178, 5.340144729496, 0.4787787014345639, -3.4789812091569168, -5.906688120543615, -6.529619888871869, -7.751413073220794, 2.5685956730931636, 4.048567618943839, 4.109684889259437, 7.020048545363743, 4.734422636507453, 2.2727420420462003, 0.9387718324673138, 4.024250410535636, -7.148015994640766, -1.632749424350619, -9.303940237183156, 8.480986998447186, -8.69914054355701, 0.1799675688731135, 4.699775847960616, 4.480532336919701, -8.900155085904743, -9.717156392743078, 7.114734046378707, 0.8131444896677245, -1.7125894350100896, 5.8122856897731765, -2.572078804870208, -1.1468941698496167, -2.675886540320402, 6.325921770519788, 7.135980234023535, 4.274499311471839, -7.439818002967813, -2.4896804415657066, -4.755220437242011, 6.381056087800353, 0.5480976024512394, -5.931633161186847, -3.903274431030683, 0.281651705517028, -7.672762743428478, -1.5850283645226853, 2.1773072239654994, 2.8210905839185063, -0.06716802907737396, 5.837791936305088, 8.545146000903564, 7.572697184422697, 3.416525720001765, 8.653588760716762, -7.86406339324508, 2.424093139188761, 6.469347872324693, 0.9470529943087342, 6.034409817852424, 9.950901719630544, 1.8628816594562458, 9.058419361581716, -0.6491163933241761, -6.155671633299022, -7.140130651843577, 0.09068280314081179, -4.924683231765011, 7.681518776274668, -1.1348033126546575, -1.1386952591397481, -3.129076488659921, -2.32067857970232, 5.033312986827365, -3.548430596372018, -7.518325839735029, 4.951265496114143, 2.3561316236750773, -5.656395539236159, -4.763231562473862, 8.840274792633394, 5.399280321929753, -4.58641983499084, -7.793056690486022, 5.642429133689635, -6.972386709132423, 8.131506109679432, -1.2591072842317796, 6.742044432273964, 4.541182293015712, 3.7838933592174833, 1.6848439966192181, 7.725264113170084, -2.7479643072390347, -8.146163409850969, 5.632708904858619, -6.41377850591506, -5.74556608954145, -2.547192931199273, -3.4818045191552045, 6.380851035175482, -5.3563477019373344, 4.121906002256317, -1.1947183189137167, 1.1042287781077924, -3.811396059424932, 4.768161194080225, 1.2561384410092824, 8.883243752437071, 0.01108435463595292, -3.410266453816206, -7.1737468160552815, 5.238542759556568, -6.287330876195103, -4.331753242730301, -6.594788595238887, -3.0089894806110546, 5.8903152009381685, 6.470369141611702, 1.698606846373341, -5.810042799067336, -9.013057676511869, -4.89958954777215, -5.931131618746248, 3.9621936405430596, 0.6559390597412786, 0.7626392475992425, -2.219373491127268, 5.656161993579879, -1.9937519670764559, -2.2638087835332783, 6.563361225332407, -1.8294980253375357, 9.991326691982081, -7.1882332739913775, -0.6094077271821536, -1.633528652089602, -0.32136453861468084, 4.307635216632388, 3.6829582450719123, -1.711754824800968, 9.573363667658306, 6.404993315113217, 9.249025518584634, -6.059822287888091, 5.347679664977594, -5.106611688860177, -7.1305651830165795, -1.0681974614259193, -0.9581906898808672, -3.0393604025296366, 9.94547491392052, 9.427482538895116, 7.8900578730275654, 8.536534244811886, 8.826018120425683, 9.134807235198679, -2.7605666025056097, -1.1850875780866907, -5.420042248003614, 1.3334070428554625, 8.743499409844677, -4.289494900815789, 4.627137019624296, -9.60153245918563, 7.768255247914656, -2.5314791246796258, 5.273441702278079, 2.0249330198202173, 8.614195570727837, 0.15235990286205414, 8.605840511169415, -5.200215976579761, 8.946920191904269, 1.7352008861659929, 0.152027565383273, -4.7855869561795235, -4.303710830931915, 6.100253101267398, 5.9110532308842405, -6.014097588207412, 1.5819232122472844, -8.615242875253461, 7.693121373113144, -3.6682681533734263, 0.8243443904907934, -6.677986563055103, 9.570833839901635, -2.9897920381454828, 4.418440528837625, -4.516223842304958, -6.86554068694754, 2.601436367289679, 6.899328180254681, -7.838485306135803, 1.1097568743082888, 8.158538382132413, 8.080634654509925, 4.487018135611082, 4.162098943309111, 7.4138672976400635, -4.081594619004434, 7.437059931361702, -0.8497552820691308, -5.73699253923399, 3.9626400613347563, 0.7051343261443037, -3.4317131686411724, -1.1747766881314998, -4.4577376728138285, -8.886943549828477, -0.32688932880075683, 5.15676235943852, 9.429900276359685, 5.912173553648438, -8.281752687698095, -2.35537032254876, 1.6589853976543196, -0.2054147177229133, -7.861727660899305, 1.4304679901234518, -9.926093980544131, 8.734119522195776, 9.863288699005484, 0.4661668260359306, -4.242917426754406, 6.466573345265672, 2.3496617520177914, -6.837478008554026, 0.3754865196119912, 2.1276864583045008, -5.100486706350644, -3.723195932898302, -8.625030402212047, 5.244459578532384, 3.79101474920839, -2.2981335449332256, -0.9527507567307687, 7.076317325500678, 3.055791955989921, -0.8632563372962245, 0.4021746053010844, 9.90281245366521, -2.017222715338935, -7.493586887329933, -9.023721069615664, -6.739520139839847, 7.814213991273686, -6.06645405072106, 9.774782248936344, -6.451483281938566, -0.8167169088088571, 2.274104769534386, 7.06138661498747, 5.599332174500171, -9.772028771198311, -0.22432023578966565, -9.3315548806544, 8.944213634883802, 5.632048723413268, -4.333688884698099, 4.819092948628862, 6.475895155727159, 8.124231066402036, 0.2613763548569299, 5.28514015496469, -6.566081070902943, 7.60869133732168, -8.278472118535875, -0.8149627686892273, -1.3938630008498762, 8.901659248269553, 4.003936699137316, 7.468964158749628, 1.3862443478474322, -5.283372304547848, 1.7259887807286116, 6.978453004882155, 7.40295354785988, 8.348976167084132, -4.4986283195096455, -5.2717648486946445, -0.13784644067300889, 8.255600341134613, 3.1349561136260107, -3.2377337052083366, -2.413351709789133, -8.876757664372423, -4.521846871742394, -9.004458613283845, 5.843087634737046, 3.820802441112381, -8.75375500728878, 5.187670370310357, 4.410121402651512, -2.7671359641768456, -6.27997388330384, -2.596234701895483, -3.366225786352322, -5.234993291679575, 5.804326696107246, -3.4268957346080686, -7.4390740382386555, 5.312890851224525, -7.216473196332851, 0.19126346660174676, -2.232598192890263, -7.310044228707218, 0.28100790047927404, -1.8006272380402848, -6.402066856122277, 0.32067895510197175, 3.4980863450617363, -3.569389291694378, 6.817270617392705, 7.935650738530072, 7.248754010558432, 0.005869321014946749, -9.408197938864504, 5.59579135160835, 7.394673011341858, 3.1114080660986936, 9.670330774671811, 3.1763087714641998, 9.687747792682185, -0.2601449598516119, -6.945630053520587, 6.262204454835917, 6.535913615266406, -3.3450587378315078, -9.59505739637075, 5.520946746944945, 8.37217914260053, -6.058800202540214, -6.295413417826781, 7.655723740392567, 2.1734332000383674, -5.8713730841299245, -1.9385076105102073, 4.599620515033207, -5.577199826327471, -1.7840394980515857, 8.903050050947364, -5.218151954057532, 6.036858562539411, 7.163302816700657, 0.8849340960206593, 2.7290016510856514, -5.710123860247165, 2.996489356156527, -7.477142891224724, 9.833630980546381, 2.8171229147501897, 6.078066443576059, 5.624572672070977, 0.13270584832792665, -9.820921190038764, 2.3011518670059505, 2.1152043410754935]
BIASES_LIST = [-3.971247994532547, 0.14726466067617494, 1.6767301408144846, 8.007288655694236, 4.122227442982961, -6.537221567444127, 7.881393811011424, 1.0606280267147472, -0.8400769159534409, 6.419294029928352, -2.5515401057748877, 7.226559176348367, -1.80991291858186, -7.861665935758118, 6.636645370065345, 9.633062716619328, -7.998822623497848, 4.430542710746778, -4.486758067039727, -4.39008233419808, 4.552522726729055, -1.7944485173505864, 0.6808531824439221, 5.060642405565588, 8.99387712470353, 7.495608642733195, 9.938451148138139, -3.0081226275103345, -8.500282815632033, 1.565119515442877, -5.412252503549295, -9.268371508417857, 6.825409599870376, 2.7882546697116144, 4.186899562510405, -4.759265683250704]
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

