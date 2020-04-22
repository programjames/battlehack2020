import random
import math

WEIGHT_LIST = [-7.166226185257929, 7.931439367477903, -6.132118871217667, 0.6877563173942178, -6.8472211216877525, -1.2687438566832583, -8.864990164499407, -7.463787134957711, 6.009514147931366, -5.729528305094576, 0.25151564154622896, 2.171370107849615, 8.778571904808665, -0.9959384993232216, -2.775215466169385, -6.512665158335955, -4.825661170734595, -3.3980067599991504, -3.235207653317378, -5.476777140518552, -3.9890487893350413, 0.5859584455015003, -0.5193496833462419, 0.3412572931518483, 2.8511560497387407, 2.5102136942471454, -9.75921832795478, 7.260376413488704, -1.7224522550010768, -2.0772353526584197, 2.4203685180317613, -9.061308838217032, -3.141557216443182, 5.579177872125703, -2.3541484772751753, -2.139832407493641, 5.116988581662561, -4.978946600795487, -0.52839680208697, -8.821638000331173, -1.2978767629448544, -2.4583456887873485, -8.935249755495233, -0.06013550237860166, 8.912739300271458, 4.044664951092944, -0.8191294124335169, -9.048019999952423, -0.44000317803657296, 7.821619140073615, -6.4699570175996834, 3.913973355588622, 8.472903613492452, -6.724365575478131, -3.967511845018814, 3.7493350697778087, 7.070445565993111, -2.729987344420291, -9.241569450252543, 3.1265363787440847, -8.118675811149476, 7.005558158558461, -8.491731555466453, -8.767634845323563, -8.76572222327592, -2.0233377599660196, -6.28510650772604, -5.629285458227407, -0.7087776704899635, 0.3030630546863655, -8.175463304550856, 2.023187006402532, -7.430837721614674, 6.1954746834379755, 7.621554961654546, 4.021721529447666, -0.4179581375899879, -8.90031835167196, -2.314664073348256, -3.287275895443287, 6.55884884068438, -9.786532829409932, -6.892736458723714, -7.305926037408767, 0.4385485269967724, -9.77194363694915, 3.186925002654524, 1.9009788583711202, 3.9441126420994337, -1.0483842714722442, 4.28357844298297, 7.961961051787526, 8.023346457434698, -6.227417972501272, 3.932723902986739, -9.249613956203342, 1.2805788368017197, -2.5129320521196448, 7.368481764655769, 6.808275091436016, 0.5577922116319183, 2.1541436921215116, -8.485025382462075, -7.786517304529612, 3.1385007329469907, 9.91535628114444, 9.498839192432868, -6.243353467335013, 4.318028987717348, -6.412367527816194, 1.9446429794955638, -1.3823365826485645, -4.891267437996836, -6.899374601940802, -8.734367711055455, -7.642154930415219, 0.35119938811429563, -6.941352881470464, -5.6005271122544436, -8.165184076274105, 5.461857857293941, -9.284955759353476, 3.5814329136988547, 4.029714771653982, 9.620042004204002, 0.7452788458101018, 5.672735456876783, -2.2081926545600243, 0.4185298946652516, 8.245602806367675, 5.8833076529672805, -9.3860324323981, 8.605778370464254, 5.661724238551443, -7.120237186273004, -3.3759421030155075, 3.3295458753834275, -0.8377724688788639, -4.935572508631482, -8.943746223158808, 7.674326347475628, -5.920359931214896, 4.453900854637787, -5.68245119551271, -1.9036775866434468, 2.573701662461346, 0.7860644508824706, 0.12482630134032391, -5.6032553236262235, 0.6600288905722085, 0.8038393666060593, -3.414035573383412, -6.793198576461579, -1.083095324038755, 3.7730992809506354, -1.974676332499234, 8.872096129613077, 9.521555927144455, 5.915130634285115, 8.965297427989391, -5.991894490929079, 8.003331218876014, -2.3915215745349965, -4.784743582871808, 0.2975291465651768, 3.069944198183057, 0.656949179447885, -0.8117791487518016, 6.593216252180682, -2.9051679048480006, 7.978642014971868, 3.1158952080202127, -1.05122735012975, -1.6683216524515725, -1.6070626890195943, 8.048614536501951, -3.09659808395166, 3.448625776785832, -1.9959300172441274, -6.056668262966247, -2.1183640402789683, 2.7119170989985175, -9.078765591850509, 1.3841688473735267, -9.062715152763252, -7.147540960378008, 8.342830690253045, 5.269302432937469, 8.378687927281636, -2.6933493570778992, -3.3361635986754568, -3.100434473447322, 6.743648944161318, 8.831799585396077, -9.629160668125245, -8.79597966937456, 6.290301903319261, 7.6806984743496045, -5.856302198922054, -6.453704887267502, 8.674914816722307, -7.999318498657422, -1.0648607392785117, -3.8722760247157018, -1.4167357897262267, -7.349887549771569, -5.292365181184378, -6.250538178259379, -3.681826893431639, 2.7886172249137164, 4.975076253956514, 2.511756026415785, -0.7485428373635443, 1.7616708462034119, 9.616512389794558, -8.382699440418698, 6.1626084482280135, 2.622008828912893, 6.550038548481009, -7.702604208899926, 8.415272546459626, 5.828024104505609, -4.2777065638178335, -9.024812158278696, 1.1853620115299712, -9.836036995917352, -2.849842817242405, -1.352923503247279, 7.136137679382635, -6.0925981141244545, -4.748399442976541, 5.159151678403804, 3.548936287831083, -8.104057013300196, -7.328616861406381, -8.93487237538283, 3.463103096623536, 1.9026368664709423, -3.9952653493686814, 9.795909025833723, -3.642437497300124, -2.1423038217337247, -9.767318661974262, -6.079520758834425, 9.019668318520274, 4.225373945727009, 9.906548540169123, 3.4761346564191147, -3.6197028795674546, 9.974262277692695, -5.121143678048734, 2.757879541854148, 2.6066821472593418, -5.970053556443943, -9.848399006332627, 7.122894185571123, 6.492711250207567, 8.074929260116171, 4.393206670581041, -0.24246110424207856, -0.34680961768274443, 9.699417422872116, 2.707663045227818, -0.19499608404545832, -7.490648414389172, -6.485099324601562, -0.8877449990008479, 1.8316439016930648, 8.371829425825744, -7.153479931417719, -5.808987869950295, 1.9034617411977202, 3.987016147588662, 5.393038025974841, -8.609850656692664, -3.5707243238657664, 6.212929856148545, 5.279988707338932, 5.338252448225383, 8.310860142823707, -8.261963913459503, -4.442311470189953, 7.334412605512352, -4.851075464801131, 0.6936381756303973, 8.075176709847106, -4.6933844482752, 0.7265921623317873, -3.116282788184259, -2.2747561188256675, 5.049895682544999, 6.335103849679101, 3.3536741988478465, 5.301038228897761, 6.09005334214444, 9.540226203767432, 3.4969309317461423, 3.868579945836771, 6.788247862765793, -6.469965735541816, -7.105992806170827, -0.5334092135784108, -8.194979178059732, 9.763249102923673, 4.392128108538053, -0.6334974028124325, -2.12844355550909, -1.2123736515762733, -4.850746596645914, 2.01757774889661, 6.180634332162466, 7.705859562374535, 8.964692128586762, -1.6407718237738607, 9.74380868873001, -4.131677136129442, 2.0571126398218613, 4.847052287061306, -9.691975139264905, 6.850635782998719, 1.2703390727224733, 9.989032724619037, 1.2409911253225019, 4.569879752127431, -4.938992996153546, 5.673409508709193, 3.116174490866177, -1.0290160942867104, 9.29757827223455, 1.2782667776123962, 5.855035915369717, -1.4651497630865151, 3.170213163475532, -3.440254480964418, 0.9222965215726138, -6.875895304712243, 3.99824385213436, -5.843777542685357, 3.6446353934838918, -7.631170478371709, -2.457528691501647, -9.220880447351998, -9.900382618100043, 0.4135620349343032, -0.7397337416241179, 6.70758388945692, 6.675977380432318, -6.529911889903084, -2.2750690970258436, 0.08272639536349402, 4.787738771119766, 5.6263781825635295, -9.494392883650601, 7.519033105686862, 1.913293066850395, -7.774694782157098, 4.065918518016877, 6.507571258310033, -6.903732552913382, 2.7997393687425376, 6.928508601671538, 6.253156298378052, -4.88231684474651, -5.273401045627725, 8.149212931322076, -1.386324990478471, 3.9137116577805813, -4.62780466318091, -9.818887163078724, 2.399048790538714, 0.17660374184171168, -0.5474764658438485, -0.6945025564288176, -8.247180249115747, 7.821180524234141, 2.8673950125731587, 3.3808199401138808, 4.127377830130715, 3.7517528029856013, -2.5877429479551406, -8.650045602628452, -6.2912544294653365, 3.5902185442279233, -6.892683105213968, 9.826551849956303, 8.064122812202395, 0.5392792945643379, -5.496812193638485, -6.510871540489842, -1.1551657265102335, 0.4220399818807401, 8.740855166554688, 8.242345828247778, -6.375507752861676, -9.88531609368258, -0.36560805619551573, 8.127675003636728, 7.061868654658486, 1.2540410224981642, -3.056884519762855, -4.858959339213116, 9.039888614115846, 9.751612606737599, -3.973662993320528, -8.676453065960342, -1.5395078364543036, -5.3409326509031345, 1.0656811651135136, -1.417748032941697, 0.9734601929870657, 3.4503486184715015, 7.715103435291489, -9.61964131739854, 2.7490165327281186, -9.441666835073814, -6.783290116850034, 0.6539492545601338, 2.686668200286256, -8.898206361819891, -1.6998518409008234, -6.573615000238322, -6.893010173876036, 4.705979466874524, -4.450155826214479, -0.4938423410918098, -9.114887320468949, 8.337981497451384, -4.818729948906424, -9.960982909505834, 7.736430720669841, -1.6530702912970767, 6.812676861048487, 1.0807941017953109, 0.8915973738033891, -6.0267444994654795, -0.9976904068140495, -0.9153043749665901, 8.181143158307606, -7.982345579021441, 8.135984426053348, -3.834855768546892, -9.443859114927974, 8.0878905232464, -4.681826100093474, 3.684887093641416, 0.906287866083801, 6.92123251561652, 2.012983024474778, 9.408883673787972, 5.342520692310025, -1.1811749891097616, 5.221411401284007, -7.856034737893445, -5.349478183175693, 6.375431232012488, 8.730173985612751, -6.797886028292637, -8.277240218906389, -5.233581486692174, -7.983011763934387, -3.0875101939195932, -3.9120210705971985, -5.198026794677499, -0.9319987697875227, 0.1792417116955196, -2.5639308366423545, 7.595298503606511, 8.5893950514056, -1.8144361704915468, -7.129016990905268, -3.1058809275111425, -8.916264689762652, 6.033772483319332, -2.032077964827259, 2.6977550803576307, -3.9844543249371593, 1.3529064198068603, -4.87632473616215, -5.125689643952594, -5.321510955271425, -4.615359576433409, -9.630375701399757, -1.467354955851368, -5.397737932769018, -0.6572185992188011, -9.156884615143282, 4.84125744929225, 5.100748879877674, 9.414500982263053, 8.03568674690468, 9.873588032138056, -8.652310199681581, 7.84890404548991, -3.798770199956463, 5.832095475857585, -4.63950253740766, -2.8668789499168312, 0.5074842493992033, -7.99842279906229, 7.590441117171071, 3.5972317699806116, -9.010175593112294, 8.928840539746254, 7.541399869486096, 1.940686200341526, 0.8256549511142772, -7.479092180908442, 6.205666837370934, 5.432698145390937, 5.8833009109280905, -3.5745957377493127, -5.242153264307683, -4.512636570642956, -0.11243394868965595, 2.033068792444668, 4.849521968426327, 0.5935805341378284, 6.083523864205393, -5.388871385855001, -1.8300616974584738, -2.9035999162659065, -0.8510848686776029, 0.3815960659677309, -8.371334538233235, -1.2921740199700693, 6.114324912462884, 6.761383199378688, -9.347334365657098, -9.2817253023662, -4.707521129604482, -6.5468974080488, -4.869882154200324, 2.4274575478294373, 9.880702257238639, 3.617734264409531, -7.969707727676356, 6.4002153686239325, 7.059524181682189, -9.309274003655588, -1.0378289291067802, 9.453450118669561, -0.30177125579882436, 6.666122473283181, 2.6358059872595447, 0.2194809246537215, 4.082526772073541, -1.8438008528973864, -1.1922786518596507, -7.356598144565476, -3.405075982282499, -6.804755205453228, 7.3642258788805215, 3.556527432169755, -4.54500678870458, -1.581293748099199, 1.6771411786505102, 4.555187519959112, 4.220103244189463, 5.89422013688778, -5.949876125413112, -2.695402923878108, -3.579184962362854, 1.4016748651475055, -6.914335320680147, -3.5737079625048818, 3.8024540149030592, 7.680264789576039, -0.9265899084799258, -0.5785684418853272, -6.9416969533550095, -3.692213035407004, -4.860116508720798, 9.916761207884694, 4.3552520835242365, 1.604501983182132, -9.500369398932879, -2.0738228168618855, -6.369212259166892, -7.810667173598517, -3.2808207556842834, -7.242105033784744, -4.4645403475696455, 5.349193730695667, -3.756119730092995, 2.543355253577051, -9.160271461734432, 5.214745698296291, 6.325478197264481, -7.180029164368067, -4.488146902391225, 0.679776164106574, 3.801294303330261, 8.529488578849836, -4.571565146839555, 1.8733509270992759, 9.41303161051297, 5.553748683514359, -6.185597936670448, 8.77394511446391, 0.7345918555696169, 9.95447192158515, 5.268780884495364, 0.9135757290322069, -4.554204946746667, -9.09923025142318, 0.04094959028100753, -5.24493120131411, 5.347021390458815, -2.4904369048339863, -3.0852525367066663, 6.937415353137098, -2.1958642810810147, 6.704878420930957, -8.437453887740741, 8.655032866338825, -6.879778330166857, 2.3139550872846666, 8.958464131468624, -3.7867327638915533, 3.685477784638291, 5.859352163210975, -4.958397015919751, 6.14344251805608, 8.359292867448762, 6.2386041373190935, -1.6067899305983975, 5.936419690248796, -6.794232680742452, 8.386919805556829, 7.203176263681602, 7.293779571376479, -3.1138511874008534, -2.7468055065208796, 1.9078787775632797, -8.593772244341045, -0.6355324910088083, 0.46827605641397163, -8.56836655013931, -3.530221524876202, -7.634790992236596, -7.261697258683051, -5.618067188868943, -3.6181930718251127, -6.2899601897388235, 0.738800663826618, 2.7883062286661904, -2.6276672408625252, 5.290757674788519, 6.855251518227416, 7.343211466124075, -7.342814319657105, 1.0038956603792126, 7.192351328821257, 3.6913687149292294, -3.3228294732311454, -8.51039559944837, -5.849336755021126, -4.350637008792, 8.59321685373438, 8.05689333898031, -1.1342527046141466, 6.827191615692783, -8.256592231160953, 9.670516903535379, 7.5366915810716115, -7.521345569374722, -6.260871072586691, 4.897698633990036, -2.7971884685904254, 0.9323885414264659, 7.365550115499101, -2.9529308438977786, -1.8129176732893058, 3.7872020848948402, 0.7695633957524208, 1.6417916478604369, 6.519744123913295, -8.485862705611043, -7.118885793949419, -4.298600078872948, -5.850123436991237, -5.592588376141907, 1.8047467386890421, 1.8101899927416554, -9.987251185217234, -0.717745870765949, -9.349945711272479, -3.7808951343365838, -0.895251044051502, 4.824614269637893, -7.93328102687714, -2.5933410547636537, 1.4606173960078124, -7.700309949652453, 0.570397480364111, 5.917198156378138, -3.704250589931261, -0.7177009432897385, -8.372367497906808, -7.445442283977042, -4.55329828959475, 6.549184385732062, 0.44334873057683843, 5.3014943582393315, 6.14608525998122, -4.607606290788198, -4.1035280905145815, 3.494498428886919, -1.8706051894454845, -1.1851054510533068, -0.02526036251038022, -6.080125025395686, 7.580621731135903, 9.363953628730862, -3.383748560688897, 9.355958666022318, -4.793135369824184, -0.1873732019448866, -0.4415425440851024, 0.5352042946083273, 4.353159236079481, 7.740937046487222, 0.30844691516414, -3.9805929025909492, -2.986860161088895, 6.351288136785669, 9.949039713407938, 6.33252312595334, 0.34255782125774914, -5.696695399100267, -2.976079458162612, 6.619399240547548, 0.2440461191171277, 9.23254444564757, -5.32310467638789, 6.750594260869409, 9.741632119238048, -2.5968896241492434, -5.005558746734245, -8.095073694378232, 1.1390045202577426, 4.131360734913665, 4.7040248830133855, 2.4423995742055933, -7.3022096020492056, 6.868587704049592, 8.517866952501727, 7.201596638559867, 5.7065031512717255, -6.250454137715513, 4.200433418284337, -8.839553152936766]
BIASES_LIST = [9.043333465692282, 2.349742272155142, -8.764247416199822, -4.156426090550431, -9.29569000615015, 0.7831696219174145, -4.986821912356126, -3.9438809161775428, 1.4739621154608056, -4.689187977053921, 8.069593213035073, 7.8586517242558855, 2.1520080652183555, 7.827301378718154, 0.4204471826594727, -4.448406679098252, -0.8258051904948083, 5.2696815563271215, 1.5877743111543818, -1.5186307472385963, -8.22761410400274, -7.945194436274992, 5.622673084062752, -6.207745420270838, -3.2532982077247885, 0.6429719201131423, 6.990698917276635, -0.14018639572596037, -2.6953980928402466, -4.3778691081359895, 1.188626349351125, 3.3449915224652607, -6.344903582333852, -2.8989278561123317, 4.345551323879352, 5.327116273508302]
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

