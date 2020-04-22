import random
import math

WEIGHT_LIST = [0.55493409630386, 4.903978133242224, -2.3171978333766856, -3.5504126664999967, -2.3243505603820336, -5.284848521513007, 2.877353549901038, 1.8298374012230636, 0.8019753397585648, -1.0999589115997503, 2.5954747013755353, -0.009848088942224009, -0.9091359584016436, -0.7543741634619427, 0.23315450556200154, 4.93390549971534, 4.679734005037206, -2.978457515224948, 2.832565184766994, 1.8308853534215406, -0.37300195110464257, 4.350403545974283, 4.932210647059179, 5.411690843863428, -2.1147878967748226, 1.6159820773801719, -2.1889095637282456, -4.357494083712792, -4.90519258274912, 1.3863866882848486, 1.3655763166742598, -1.1248036385393276, -3.3966755603685677, 5.255134873624022, 0.9920172046243902, -2.495149242830004, 4.154001579991972, -3.2850147875068845, -3.750330874037491, -1.0276405695589308, 3.8248437022228936, -1.856127900709788, 0.439049939590798, 0.16151269281981576, -3.2619788852408487, 5.727682386984784, -7.87395273976446, -1.0369624925738294, -4.620111389662419, 0.8796048919432713, -3.8401077818997966, 0.682161516138071, -3.580456425750802, 1.8928581237622926, -2.2520575054220546, -1.5910970871137782, -0.40832725068283754, -1.9838835619688764, 4.891045322811893, 9.877733247859464, -2.192735320725229, -4.491857733065977, -4.3212700961664074, -3.5202590339262914, 0.7243103503266103, 0.20040241711493337, 5.3621673710631725, -2.197921431258681, 1.2321618344515801, -0.6848852812943159, 0.44516684236230825, -10.346359596122241, 0.4959792111932148, -3.6917662909072515, 0.03958282566107854, -0.9689157105591132, 3.389441991597887, -9.799181089997347, -0.06895071233112474, -0.5688592698863462, -2.415372800337202, -1.11193356587728, -3.253066213169347, -1.2122019638983086, 1.0172659510283886, 4.812778493352895, -1.8395639020176584, 3.993486838141082, 1.3681171940656989, -0.6826829088827558, 1.0020365483130986, 3.7875706956330526, -1.2483134168704968, -1.0592243895511702, -1.582739185176088, 0.5392150203023738, -1.7463882532368302, -1.1326513573599084, -0.6273951480580184, -3.6890735328129836, 4.1257763797750595, -4.823927541228296, -2.327200431872029, -3.614256505112586, 4.938961117373847, 0.7471007303863194, 2.7047824168837042, 2.6836382405098096, 4.96121284734681, 1.8936179746583552, 4.385134188520117, 0.6032542611502775, -0.5265423604206446, -4.311374415085852, 4.463009047440464, -1.7078454458943024, 2.5551736028210956, -2.775208491996786, 4.5648948986349, 0.5745394061848077, 0.6299375840568138, -0.16045636210297495, 3.595405503359746, 2.618604948352676, 7.0054266896582815, 2.446063896870547, -5.356399145443432, -5.6289847713718855, 2.551396620987256, 0.06229905943529017, 3.6292061209176403, 3.847346958903083, 6.498859845549856, -5.741080406410395, -5.191735113201263, -5.159460369653155, 5.244909179194681, 3.508722914050366, 3.5644991437225233, 4.553641758739808, 2.0694346291670764, 3.4827917119050342, -5.228004684706187, -1.057069482287549, -3.6849617747166246, 2.522137457720568, -3.9439910928735835, 2.4783807015507864, 0.4603323262854503, -2.483160593598502, -0.42637106701980293, -5.12069377741322, -2.4229146449949406, -0.00633929898236593, -4.15658069393821, -8.682533904610146, -0.22008740286742948, -1.818673324261719, 5.463220344604155, 3.8031137126083236, -0.94450126254093, 3.8425002112995212, -4.556932601992955, 4.489675062444725, -1.1228900666153736, 0.37177921613939646, 2.109018966166929, -1.6888265414563681, 3.3691325539436496, -2.6039407900446254, -3.4514118971917656, -2.4284266813368665, 2.0666287904057805, -3.2819502772751297, 1.8340616672343073, 0.19499659321145904, 7.301556969596586, 0.13908893295619296, -1.2333422226856452, -5.379158682867591, -3.2225845673881195, -1.8827440204394523, 2.150998837898412, 3.655292219125789, 5.117499154283961, 1.1306769963673908, -2.636145926745473, -6.114281655913401, -2.5098791409466195, -2.1317179731277554, 0.08183215236880231, -4.289209071270284, 4.5762624374079195, 3.2550202707882874, 1.914183932285826, -0.4293416720789264, 0.7528635652308389, -0.516573972277618, 1.6907613773163532, 1.7621739623987864, 0.13046010107361167, 0.7057427356266701, 3.031448486022168, 2.4239595489243664, 2.245105753889704, -1.3527758320794454, 1.0347281270484352, 10.580181897389348, 0.577512627716568, -1.1259295223404535, 0.6020611659359383, 0.7516943097433751, -2.9360890088321017, 1.3036135472921113, -0.6561804516691562, -1.7557397394741334, -1.6137725773838196, 0.3340884711232645, 1.2966763733159818, -0.7574824443900187, -3.918341553667449, 4.083806871780908, -1.5717770248481382, -0.9474083090896234, 4.251645142001137, -3.531732157384966, -5.023382342889857, -3.3203202419298252, 0.15883614102941399, 1.7449613169502212, -5.33766129163873, -1.7019040227697688, -4.68291373579129, -1.6441384994936237, 5.27620813228102, 2.4050411326762653, 4.2692250043616875, -1.1770241856937051, -3.623203284947886, -5.938407240775523, -2.5655373293822734, -2.5954300443439133, -3.593423575528994, 4.863292468399264, -2.604624717507123, 1.2132537787455264, 2.594677449072556, 0.21794401582992493, -0.07550721795269523, 7.120772499008111, -1.5399098314215707, -2.1114325059497143, -2.3021360783266362, -4.271109560309388, -4.8519471044957525, 1.0158317421847216, -0.4185570717171812, -0.3566798577619796, -5.807538351344123, -2.5123085661207423, -2.7310571853121317, -4.580208842795576, -1.8270224620593283, -5.904165254900474, -3.0656685768518837, 2.686916305990348, -2.3717663879981212, 0.5974598093336466, -3.7599146575444515, -0.5447742618304918, -1.6620983727869896, 0.170698816106501, -2.8946809829414892, -5.617668937793354, 1.5222087174536716, 2.0279684954415464, 0.20312846980693972, 0.9991156771085027, -0.7778122595184837, 0.3635732093428248, 3.949320861501534, -1.0339633131593935, -3.8965193776256526, 3.7516421313381034, 6.158820732645217, -0.07559479799027123, -3.3789521254355868, -1.8299481109417146, 2.6373353263249593, 1.7023879957204657, -2.980058439362653, -2.694018656870645, 2.554174869961787, -3.572527372604265, -2.2614261188812916, 2.3609031909725506, 8.831958786468954, 5.944137850415299, 1.8006130595792305, 2.0488490513912394, 4.562831062643502, -1.8758683094036752, -5.8450751373783545, -1.7659974223095047, -2.3774677241185977, -6.869009366871628, -2.881947909454886, 2.2942684751829123, 5.061914405610215, -1.4277325832065533, 0.6758778800815677, -3.918533156371541, -3.5977490162160413, 3.2613179098594944, 1.8473710184479493, -1.7841333575215494, -5.650118560349485, -2.4110976590537194, 1.2839769772209724, -5.5950597858174, -5.316301628291932, 1.2778560308845104, -6.799752120120124, 6.404253051969574, 3.4322497750849834, 4.600311748830825, 2.0005032774319873, 0.27864610899973424, -1.2651462071363, -5.568945773862273, 3.9648554720707407, -0.3387968081708014, -7.424863434907047, -0.10305795127463638, -5.029489504517757, -0.5107596211893988, -1.678571866073815, -3.4517544837220555, 6.512026382237493, -6.782721890521273, -3.23590331119247, 2.6625372172043225, 1.4764228668295443, 4.185187715847632, -5.696901250409374, -4.63529122631405, 1.7020027078154396, 4.805428153767024, -4.854573585615617, 4.650595069484219, 3.2510602238064266, -4.024591531303035, -3.4007721405511053, 2.3100026356691843, 2.335354754711695, -3.3844018159491154, 0.03565812819115054, -0.013663795857555092, 2.8136659743885115, 3.2407541069817682, -2.251727382428514, -2.8229594584608084, 4.924447671329771, 6.057006083550695, 5.286533241539641, 0.11292932893670393, -5.844203073150315, 4.262720818169086, 2.6003866391690185, 0.8568410548049807, -3.2241039926812896, -4.710408568972419, -3.6673705647558394, -0.8864767801505299, 0.33816337257499346, 2.073269804744832, 3.9163442442768197, 0.6798877983987744, -5.647868700841138, -5.260322702306268, 0.42576196890857615, 3.4250982929259717, -0.8752638353707644, 3.169395533930301, 0.12383903599094755, -2.872764400488346, -7.236713516862475, -7.879851067380435, -4.603541612266083, 2.4677179103980347, 5.608609875338305, -1.7020862885873638, 4.703572117789432, 0.5073430712420565, 1.4452422219607368, -1.2976264852859167, 0.3460128599953343, 1.1801264507656, 2.26266756892008, -1.5008781964664006, 4.291776189752858, 5.556273687406526, 2.7187204943470458, -3.4482806315460928, -1.7081161770422695, 4.544400377476544, 0.6979705869322681, -2.1495004033249687, 3.8652372841619487, -5.549511062088932, -0.2961831653055299, 0.7914515139200623, 0.9085468445242113, -3.2806455524332345, 0.9612217812190578, -5.685660691878813, 4.132414178205662, -1.5806325230183016, -0.7139457975776125, -0.9955649713908586, -7.3959405601479284, -1.8393213844502068, 0.7560371308257752, 5.224536936331974, -4.3498803429299695, -1.1502747268831475, 4.089198049094004, -2.741715367215753, 0.9161289085182507, -1.9435753668544615, 4.394154165330824, 2.782739060988733, 2.9916020451487135, -5.905787828135742, 4.937292937697109, 6.178701720575066, -0.732925561488577, 0.8067949943250757, 1.5853848899461376, -4.766852282357643, -1.615315054741248, 0.6519319537393337, 2.01392476682564, -1.8329200655233049, -0.3759342977826776, -4.3218931871256565, 0.7123311868099009, 7.982738166800613, 1.80451426936577, 2.933202375557751, 2.412985068240182, 4.5171571664876335, 4.9368774750405064, -4.361260309394533, 4.686067111472816, 0.004077390469512275, 3.6301245781532767, 2.559001724458278, -0.3816360759217692, 2.5141929551795306, -0.42117461377135135, -5.910879000622991, 7.692374985446037, 3.6807847404378693, -2.0487734449299406, 2.067464413891469, 1.49194076870493, 3.195967871123017, 1.3717789450925424, 3.0460501921799916, 5.183746753438283, 1.6544736584857285, -2.3188276324558568, -0.10142043667474343, 2.493657468440613, 1.3452626520944408, 1.5722598772235148, 6.845894784978911, -4.2741548186224385, -2.457886208247983, -1.1917577011812683, -5.079133418785069, 0.5677669411231201, -4.347067493686792, 2.7009379733113197, 0.40264554477106734, -4.411609761656196, -0.8140224812909927, 0.48453485442545996, 6.266090297842865, -3.28696214986093, -2.878309907033742, -0.698604469914086, -0.24037961135318114, -4.862168538429325, 1.3621789464438032, 2.6085225419216616, 1.8417320410658045, -0.3673409814811998, 2.725936220624147, -0.28441795283528615, 0.1136417952653968, 1.5468324695758793, -4.743715792214848, -1.6513580147092457, 3.6023447762852974, 2.8724654888704726, 0.49319843142115183, 4.259320455645935, -3.052073166878031, 1.822431714515475, 1.047042392748435, -3.7768440294069285, -1.7936482001193412, -4.903165549073649, -0.971196830194104, -3.991420052813236, -1.006616425202242, -5.969241553432943, 0.29944711938573415, -0.041170497508316514, 7.0075551709748085, -1.1888959752759358, 1.109246317973855, -4.0231353855649035, 6.957982795019829, -4.084015306667427, -4.1341510808174355, 2.04536398120918, 5.1038609770196475, -5.499453834209595, -6.406626965577588, 0.9117916941727374, 4.221131420107048, -0.9052810408576287, 8.076270654359877, 2.5251246886459393, -2.300069200992977, -3.329756836349107, -1.9921502450442918, 1.459123767291645, 1.0607368836355728, 1.434469157921859, 9.023516965088817, 3.8034302859939904, 0.5639499528765344, -1.2702202265561828, 1.8063494845272572, 1.5058564980569338, -0.5453929959690534, -0.2846137364925797, 5.973105377292375, -0.12472453416197844, -2.7921457708164463, 5.406107129555526, -7.758318576602378, 5.251927809175066, -3.882959376764312, 3.406131578620849, -1.0092943163224937, 7.805143797720508, 1.895509344356821, -2.2562661971998192, -2.181145661309987, 0.03205541073591228, -0.11520921586365451, -2.462298936753867, -4.417944218474714, 2.2154414548128147, 3.9595078424390486, 6.047509723789493, 4.879875401744632, 2.243344976734028, -2.151193438649726, 0.025682053747347812, 1.8470590280487342, 3.711133403367362, 8.940389052305276, 0.3942840258244947, 0.2241648188755521, 9.610240140525278, -0.6154986322622227, 0.5427322394642935, -3.1903029597796304, -2.54661331278211, 5.770309698472136, -2.350185105854691, -5.444508896909073, -0.2403531920053699, -7.366246008241801, 2.419588563047418, 3.0872135746394345, 6.1130434088792835, 4.948051692610369, -0.9520005376536341, 3.8079364516945975, 2.9120853688330954, 4.1148040396199965, 6.787385733647453, 1.3809820364287122, 2.303952707332939, -4.2529762845657935, 2.0141794507035224, -7.716447795547372, 2.159569440231856, 1.2636961926588037, 1.2182802890474045, -5.137870190987067, -4.545185568932131, 2.3624116783208433, 3.036965746220345, 4.271956308370701, -9.132561592556717, -2.418580172594914, 7.446082028277717, -1.3613562456132569, 1.4386428077002067, 5.830856156868602, -3.4666435255491046, 3.1611773168734416, -2.0134164903245613, -9.987466379743385, -1.0454624763223137, 1.471071779839116, 2.9082777119206558, -0.9093173450717125, -0.7008446216464759, -0.8044673582565356, 2.2757127308436593, 2.486240554054465, 3.227671700143003, 0.2850692939020218, -1.4190742284770792, -4.295412810364379, -3.2254400827602727, -3.42122694256904, -0.7127190466342493, 0.8629366591046388, 4.222333121013071, 1.9559973420410992, 3.1784111687749945, 3.10784278164001, -1.439472696619564, 0.15967510801376827, 0.9647056833501779, -3.0847301293434937, -1.6417876460549705, 3.4773631509977196, -4.020809929552746, 3.356239909899242, 0.5754749053873446, -3.6927036417982824, 3.4499531210589542, 5.922599348160213, -0.4404537829889172, 3.2233040151014394, 0.38354938795586074, 1.8505826020953542, -0.9138552425286401, -0.20175450805046416, -5.26022087229532, -3.35984752032906, -3.7076061371755595, 2.337624176095419, -3.8998346338627297, -1.5414255973309727, -1.1403602336274739, -2.0591546915010888, -4.904674546736351, -3.8685464045226476, 1.9872623657557507, 5.67677855693053, -0.2097380577490628, -1.8235775560531065, -1.3561230702598746, -4.280708602161426, 2.347380500055499, -1.5577319671270782, 6.689680117642213, -2.67024162370088, -4.747502907883772, 7.891575363559239, -2.0471849912861297, -3.2757995304274226, -5.157161032077461, 2.997768444038953, 1.5239033014622227, -3.5598506421475613, -1.3629067380518685, -1.5935534622297607, -4.8056716562356865, 3.3320130650250714, -1.30495070626814, 4.38049856371807, 4.626476648165782, 4.2946093793338385, -4.915294516792638, 3.646411612772715, 0.2349348616152552, -3.3931428204168834, -0.3563890750190123, -4.741329333567932, -3.535626527894252, -2.0667257976704123, 2.518454861609614, -3.4150354936318505, -4.681499441723935, 1.4299107862049243, -2.7561821658833474, 2.009514040018986, 0.4684855575732971, 1.6700239815003843, 3.9627207745746422, 2.9341479608367247, 2.791209520469279, -5.8672117109028, 6.989480832120991, -1.3596368510325616, -3.467352544716376, -2.8513318865190134, 0.15435247461039867, 1.4896301902868851, 3.0308141218631097, -3.592074114866731, -1.0552053880702068, -2.7617646730440333, 0.583438940620547, 2.1820876065515566, 6.124495509528287, -2.7575952144097418, 0.08736075019618292, 1.4727502254007019, -1.2535358110886294, 0.7328870301399945, -5.7333010426586295, -0.845200092339361, -2.388598366066141, 2.3561723564999366, 3.774166379610859, 6.9253593301844365, -0.8737305542225463, -2.235454502623413, -7.981717914350761, -4.326491236345399, 2.993770017570682, 4.220527287951856, -4.411564484926854, -1.7756985093433606, 0.9718780654760852, 7.596321547365791, 3.7535012020748026, 4.876432123201105]
BIASES_LIST = [-1.382969312814531, 3.7017669321023186, -3.6184624461161548, 4.800679544431515, 6.332813524787629, 2.770101252477236, 1.0986688745044788, -0.07788215816454477, -1.1107840933589297, 2.6543893300567403, 2.1216990748307234, -1.3727738857810772, -0.0026423517987332543, -2.6209743343400307, -5.506049023626963, 5.268706293371733, 4.822468017676282, 1.4768460780778818, -6.570912946747633, 0.02464367047500443, -5.070178731132011, -2.803065738180699, -4.063432348299795, -6.090880705151615, 3.9267043463029894, 2.6475302097005238, -4.025341875184015, 2.9183918368226736, -1.0774784553748955, 2.30047215028726, -0.34177376249233155, -2.292939370311173, 7.117626096409358, 1.8543584018791957, -1.684157077113194, 0.44857719754647096]
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

