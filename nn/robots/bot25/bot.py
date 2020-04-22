import random
import math

WEIGHT_LIST = [5.80600287074456, 3.942668480140741, -1.0117976180805783, -3.071067811961825, -3.2454592391114945, 4.635208745150514, 4.263500705105612, 0.7647722967751562, 1.4621195075200433, 3.290166571944688, -4.77182739396532, 9.801925413328558, -4.691841939925341, 1.4366462561504516, -8.091110550147098, 6.950629533811938, -1.1260517964473866, -2.7262127719207996, -6.449032485118876, -9.190388362506779, -9.482886723345976, 1.8568874193517377, -7.618762888005723, 6.346802764189626, -9.729458700143091, 1.0648545946910914, 5.600539296501745, -7.633598076218028, 1.656455802796991, 9.34419777104831, -2.145860507636696, -1.733233294081602, 2.3008282032379146, 6.905059176811733, -0.060820140483121676, -3.5327853169984946, -7.92834018693161, 5.687368884427466, 9.107690602838538, 5.403006104848213, -0.9334602095913773, 4.857333175877322, 4.010111332657738, 0.8827286740460458, -9.974891237673255, -1.942927126572867, 5.821354532085296, 3.2044576713777477, 2.544641884746939, -4.281948631553208, -4.606040344241804, 7.384838924905743, 7.454587665604919, 7.821014169839145, 4.741829714132157, -3.785148013136439, -8.0637111723244, -6.873294729235759, -5.515401356692782, 3.631004940030847, 4.58353827598666, -1.4179085507669065, -4.351923086078133, -8.507340260412429, -4.008633754918907, -8.134277778883895, 3.1000522328920237, -6.662350591691033, 9.990417308672114, -3.7856640169359306, 4.508614509691093, -8.816222052361585, -1.0173530804028132, 8.415835429102788, 5.402573738651446, 6.380938462331393, 7.022300841472166, 4.660978483623079, -2.6750389389605527, 3.4116350712027117, 0.9247936101735661, -5.302465619319696, -3.38409498629521, -4.459948543298302, 8.707782545412549, 3.9725784441325214, -1.6812026080596425, 6.576346141949077, -0.3147814278063503, 0.8273534180145283, 6.525227251279784, 3.892645768548997, 9.417284967173675, -3.8919357379869, 2.42668127898086, -8.922698175674766, -3.620404216657798, -5.754506779192326, 7.950767842518761, -1.9388983163584754, -7.874173395599198, 1.47663198336436, -5.919998461120837, 3.2017480683797235, 7.341985634914362, -8.016947255366285, -3.1076330055851002, -3.121489632223029, 6.96204629196513, 1.2682780663098026, -8.126420548366852, -8.1855723741153, 3.320232103564935, 8.851578279251523, -7.314984673894893, -1.1960057046686217, 8.46336881326527, -4.951284009812396, -8.491746179899447, 4.880266506324077, -0.11734078964020078, 8.89894620320511, 6.163500071376188, 1.9780091058076934, 2.576075573237704, -9.403143669954858, 1.9906331934109929, 6.781386947396115, 0.023045499873484587, 3.8430738594851377, -3.137305297425832, -0.3265584274548132, 1.2424637429653238, 8.5818398213828, -1.882328553100523, 7.483588309721505, 6.195121782378177, -3.9461933615507006, -7.020618865276315, 6.621786824469474, 5.583592377659052, 3.03158785230373, -3.1290754231449736, 6.945427100497199, -3.6305405270184927, -3.5525940512643555, -6.870888678896556, -4.13565267151359, -8.702491067204106, -6.042520321657321, -4.809535359039745, -9.024461124927514, -0.913903988933173, 8.08328482051543, 6.4759030067363454, 4.352245405980366, -9.045623745412726, 2.1733953689189622, -5.195584416663066, 8.784375688264, 9.061829791500099, -7.782047962213086, 7.5681881570011065, 6.93391358352897, -0.09999485397572982, -4.161053640641812, 2.9924673476495496, -9.679922154072715, 9.074079643280285, 6.368550485180322, 3.8744452410527686, -6.039104249485556, -8.464585577145645, -1.21275881257678, 7.821594461129916, -7.824008076983215, 1.2061583285421804, 7.045713027229194, 2.0906708890958665, -3.6856900164788957, 7.7321613657766335, -0.5308090693275087, 6.900540786737405, -4.976705896678579, -5.974553133238524, 2.119213074294759, -3.2640620697494915, -6.824610791244952, 8.081473439615088, 0.9002455889436689, -4.706350303335309, -4.712231406587238, -3.4824324529870783, -4.171305178495091, 3.1968055478729838, 0.5530267684282499, 5.175589419272402, -7.602465969115688, 4.079784005587781, -6.808764693811769, 2.800260915457372, -3.2675394148091836, -5.278300119618809, -9.153720809718335, -3.4355912087116263, 4.210483607747058, -4.053334140753016, 5.439104341810763, 2.413851846069088, -3.256126251374609, 5.2256978414553465, 8.388788399982044, 1.3737490562908476, 2.4574194613847737, -1.3864403783931483, -7.717007131124271, 1.5711896304906219, 8.643061266737838, -1.136158511232603, 4.489886060879851, -4.57500550422135, 6.741245191132165, -9.245243667111469, 4.729597116251739, -2.4455024512345886, 9.81412988407197, -9.920054864283198, 0.2368513805499255, 8.457134110241277, -0.6183166324753913, -1.3334666674294464, 7.503221709257279, 7.527143130744854, 9.30409372182783, -3.1964232301696693, -1.1757386629652782, 3.8618014801663048, 3.711794016446941, 0.5667051162996408, -0.4110610595451476, 8.116953363158355, -3.3983773597372497, 0.4034902630781545, 7.528535216662302, -7.8383186579664414, 5.862868615552188, 1.938052522010242, 2.4811569971557095, -8.039594876736128, 8.142524550088485, 0.40106502025149027, -6.028923270779034, -0.6995898984265398, 6.725348341132634, -4.780699021764816, -0.5982362441196987, -1.3598089199191499, -5.239064039973589, -3.1840604405907103, 5.1592042589103055, -9.895922981229408, -3.137424816290064, 5.995347668518214, 8.293072260803381, -4.070295900708876, -1.6810847529066724, 0.10252082785332028, 5.8374921833206095, -3.1521370493007073, 8.893242770828223, 1.6856201073644712, 6.1233313221424694, -2.7405125470796277, -1.2576634520941372, -0.39506933144028267, -3.193828716832801, 4.629920951513295, -9.509757778831743, -9.270287696364152, -8.206015455739603, 4.382607055583094, 9.291442464766803, 6.502694840096776, -6.07359200231127, -3.336587944460523, -9.810926443136287, 3.779480556843726, -0.9353014780349902, -4.876335103845286, 8.871561279201327, -1.4902003736197784, 8.081875730405876, -1.298323581340398, -3.493799475307542, 8.584199194265892, -2.612641306202443, 8.509689764776589, -9.868259557566487, 2.221036632137615, -9.170751169784001, -0.11990334823807913, 6.75177976976676, 3.833558644765972, -6.150866592289372, 5.259860792087638, 3.3481934463350544, 4.71971553764153, -9.957850776656059, 7.609629709920959, -9.390083525527452, -5.347739783591505, 1.389916673617451, 0.48428938888329753, 7.159458634236518, 7.370572090239364, 7.066499893807162, 4.99621901740349, -7.224730969058422, -8.15022652258798, -6.375349281573818, 3.6219716791107626, -5.356054108492387, -5.1493536912505995, 1.411178813418477, 5.690909933385843, -9.217763640162499, 9.987042220912599, -7.5928084145780605, 8.170255117950337, -2.6578345913382018, -8.882963080200813, -4.012131636517681, 3.5905699654645655, -4.123612611116243, -5.297323879890188, 6.50798126548019, 9.90238623191583, -4.324013632280561, -7.335147425490116, -6.946394220245216, -5.19284754005316, -6.201948983987902, 8.112255555687138, -0.08756497386595896, 6.2386275259862245, 3.881414998665953, 1.4031619452445696, -0.19731362365252636, -2.324178741881635, -0.03050860825385371, 4.827895226462706, -5.386442906350972, 8.637893549014645, -5.380876206195397, -0.7412043750957693, -5.502564107950891, -1.6832767196470595, 7.346982653429812, 6.884066938630966, -5.880969517419761, 4.502485835543361, 6.570279546544203, -3.832615828798307, 1.2463276947719333, 3.4034416159308023, 2.2607147923775663, 1.3701493790088186, 8.181365291045203, -0.2821984286622925, 8.530458005494406, 1.0230392882923045, -5.376903142940175, -8.49225090814172, 2.4867700432156106, -8.950647902184423, -9.536578949472009, 5.285771463019538, 0.03783841564169421, 1.6375394049021033, -0.04810740200913344, -6.54864079917036, -7.318645287178638, 0.8069170157375449, 6.692558718995155, 2.7592097758327068, 8.920069073038707, 5.664267107306166, -5.0304658064537255, -4.64976800845095, 8.087157182362933, 5.958526591618693, 9.993857479447431, -7.666472029200586, 0.6058384449858174, -3.569886687825652, -0.7552400761779161, -4.183658066732008, 8.595520552500172, -0.11691261731216152, 4.708978866738294, -8.905284457783853, -9.306048419907015, -2.832152077452685, -9.001816698551568, -1.4314500092203986, 9.769217766792018, 8.049608521358131, 8.436008862281636, 1.3547355936541745, -7.035375754776377, 7.519556985622394, -7.302325295097685, -1.4584690214106608, -6.480038797168461, -7.659082018382646, 1.4657749815391536, 4.597420582508079, 6.83245271715127, 7.1814285852391855, 6.485312255878213, 6.680344755322597, 9.29822826724774, -1.2690607774995613, -3.254683948167319, -9.611095399723613, 1.3618547141481496, 5.423062746933882, 2.920663065769947, -6.154205805241952, 3.6483640482404756, 7.2013703455119895, -2.093927340186461, 2.268783581428586, 5.785780542074637, 8.67020701070133, -5.6126420978353035, 7.8467594221680805, 5.2607625660913815, 8.960057580783165, -5.014161341575383, -9.315458036045221, -6.769232202579087, -1.1744833266385424, -0.36387003911048943, -3.212566888026731, 9.781482351561625, -3.1811336527721252, -8.966174881296027, 4.3195160974533415, 9.216015867473761, 5.377893130373179, 6.315752257724686, 5.26690952464244, -1.036790071147367, -7.1326645483218805, -5.200448535675055, 0.43806598660981066, 7.078112641993549, 3.9801237726463654, 6.1927833061884385, 4.763135209414994, 0.9296906269864653, -9.953507831163881, -1.653908322117756, -1.1207396007633807, 9.454814776840703, -0.2031776594910255, 6.968474073776743, 9.526029100197412, 8.556565339210294, -3.5941107976740305, 9.217334123681965, 2.017911259597094, 5.783430155336404, -5.007286431070696, -6.545204249679992, 0.0013664532576100896, 8.730422843283879, -5.8628450996362735, -7.910162906992479, 1.3691495451373097, -6.741916232953697, 7.383910551212011, -4.829286047263135, -9.94977074585919, 2.320674177231014, -5.0518266133320155, 2.7818149095971574, -7.418957740853463, -7.106110572230159, -8.65738435592502, -4.351489470950551, -0.8255571359548863, 8.902950875776597, 5.506834919407149, 9.085566070825273, -3.9026748920542076, -5.377140731906929, -4.244169494158068, -9.664482716422997, 8.425261951604604, -7.650679614775894, 5.471511519065114, 2.984128038878586, 4.114770051351172, -3.7678019159600424, 3.019040048672517, 8.190976322511716, -8.625601542163995, -3.2194331413554984, 8.32456077417526, 6.057821614230299, -6.920406494844043, 0.6848128156674065, 7.658306284114676, 3.825132345303956, -2.382908230964251, 6.551517726814016, -0.3419022255396076, 0.15450522507497944, 8.258119651861783, 4.334361162894458, 9.120972823650646, -3.0185086042098064, 3.8943687910408933, 1.1390012638403952, -8.182315459713635, 3.455300001648096, -4.59254167199318, 6.102929971209797, -1.9167501975066603, 0.3598429780335355, -1.211877977214698, -1.156148408403796, 2.1478247000897426, -3.8022045275981897, 3.9964185331044604, -1.1361629225427947, 2.656208155016934, 1.8992685042550939, 9.320623422127682, 8.885628672384918, 2.700699308894812, 3.7888608501800007, -2.100796042046653, 9.101438497435325, -0.9246000369300234, 7.728877284767012, -6.503229961966424, -8.530813671715329, -9.98880915980915, -1.2039619812652909, -4.182681595052764, 3.1266481604295606, 5.040171687358386, 0.377785345753324, -6.162187348359513, 6.5752116503056115, -4.451042179732603, 9.872808591127797, -1.1205607697156097, -5.723030481044877, 7.68958723395648, 5.75518646454681, 9.248836133056987, -3.235171285677878, -0.07740930348952624, -9.921885117801818, -1.4144253268928608, -7.684819420939794, 8.34575572343407, 0.5137772216959391, 8.406927578662742, 7.8969502891905705, 1.1866229345891828, -5.361041281413518, 8.43568902239111, 9.754370139881956, -0.42768739005592593, -2.3311834155279554, -2.335603165750248, 0.14135496770188283, -4.04076053641856, -1.1256921286122097, 1.607813522761747, 7.439213393462033, 4.535338253609391, -7.28506969814643, -0.4376336095130444, -2.62701510981411, -7.144219106227001, -6.4622232048477635, 3.0235713542979745, -2.008468087094246, -6.337236790404059, -3.5819915486882277, 5.306872210677584, -9.144528284998595, 8.120631206649037, -6.152006066015958, -0.41103412603300704, -4.184396837460504, 0.9172773617903509, 1.617585176325866, 3.11352397845393, 8.49868468589592, -7.587259860718638, 5.479257914390978, -9.066408044149657, 0.7797326818336501, -0.2192137323199148, 5.363680473267191, 8.854069988512279, -1.8565670990647387, 2.66437788612299, 6.673637965699307, -3.273791063990908, 5.077660218499155, -9.905883799613592, -7.166304818218292, -1.7175675025426678, -9.212425687771786, -1.8486623794510688, 7.88553310477322, 0.37447074947018066, 6.466876381335773, 1.2953949836249716, -3.0539191987900383, 2.7261127070393805, 3.8830105512613713, -9.16914893002634, 7.461954823870741, 0.335807762240103, -5.5468798265960935, 5.722791554690128, 5.400045477949497, -3.8167528683562635, -7.679596977167414, 1.8652941796451081, 9.234180907217194, 8.672828789909808, -3.205921427926654, -8.249789098572622, 6.684293491204301, 2.266359539981508, -0.4249479153615212, 5.011774223762133, 7.300882740137219, 4.432870206370447, -8.341836751161555, -2.7127058241656687, -0.4164431383610818, 1.8612955279400456, -0.3994899906255114, 4.698510662373682, 7.151964409103467, -7.44694046054075, 6.079747406268769, 7.664800991976254, 4.475411439495396, -1.8535015969384983, -7.721100635132238, 6.055882143182007, -7.387929042460108, 0.45907939636335726, -8.956772515411897, 3.4747487900040106, -8.683518715249694, 2.4259786480783987, -9.57315573884488, -6.821935697104971, -8.166874056264973, -3.5232001352542657, 5.632175315701907, 2.1566413549727095, -2.572701497757823, 4.183390175250514, 8.117619882906915, -2.0022743142467947, 9.98633045460241, 4.045072005174566, 3.119467856757222, -7.676182191882603, -9.6848721627308, -2.655027825956102, 2.9853767007216607, 1.9173008353010133, 0.2468604706647426, 1.0965998992635484, -4.675740123755281, -7.483492729562798, -1.1077290530916173, -1.1551852450104896, 8.563652627963691, -1.190285031746523, 1.477879262951534, 6.43674074932775, -4.581810276111646, -7.442250082919943, -1.2061000068624832, -3.0975188481545572, -1.4893851354164322, 8.234042822239697, -4.8589040280140345, 8.827024843966754, -4.847146015350039, -5.559519810634095, 0.4874717764442327, -5.703869786830984, -3.151658293615278, -6.14832096696563, -2.306169959403781, 4.667570983431196, -9.311498755063933, 5.768854460187729, 8.81492657416462, 2.775856086802211, 9.482022280783546, -7.015366407138979, 3.916398418656117, -9.714740339801102, -4.713782061743608, -9.66275912689359, -0.4656678995297199, -6.5586509376622315, -0.21564218897742116, -8.032944842006017, 8.890968282674635, -9.598233701904324, 0.20972589126667174, -6.07584830613675, 0.4724932199826739, 9.11787805246486, -2.5896593409820117, -6.922308705052103, -4.938569354214579, 3.4675647453945846, 5.081159829893853, -5.796409708506602, -9.238103089281404, -2.9863248251270846, -6.749630745081825, 3.0766318513092745, -2.7653588320810822, -6.909421423165405, 1.293548610295634, -7.7830137928774175, 6.853145836371077, -7.818511640469932, -4.057884230531361, -0.9034318438350333, -1.2248863538569807]
BIASES_LIST = [9.166696547301637, -6.719195602317574, 4.7898687222216765, -4.475199306281555, 0.4361657901261218, 6.3674782866480015, -7.347559774939906, 7.841070422305599, -1.434910279155531, -4.583994412102097, 0.5862753264798499, 3.029708304884755, -1.5442150024147665, -8.509027507143463, 9.12641341269683, -4.066420801684445, 8.934947372536527, -5.0206622173813376, -2.7732901915814567, 3.4580364475961787, 7.970480320369923, -6.829369767477653, -4.615962156594322, -9.190097476263468, 6.675356655334049, 6.167771972118349, -5.7677082357172775, 8.189627628127234, 9.361759023763685, 1.5220343225921784, 1.9391155733647008, -8.4556345727698, -3.3377447350387435, -4.641796562347869, -9.06264616160195, 7.4739977761598055]
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

