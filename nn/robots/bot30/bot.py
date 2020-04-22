import random
import math

WEIGHT_LIST = [1.664192143586627, -6.380435477687922, 4.858417480046256, 6.138736572219873, -0.08351718726651747, -4.846109313502634, -9.159190170997856, 7.289163041994225, -6.355491934520943, -5.0155198711699285, 3.388225549981456, 5.762101398329788, 1.7607400309870656, -3.6057693500170025, 4.561328734488665, -6.929537821194865, -2.200921249416316, 0.9377530355984973, 0.8776824063809983, 4.868208551181198, 1.083820538258344, 9.913009365859018, 2.045805999411254, -4.300591007979198, 6.72276024247698, 4.0344701922738135, -1.1673563042611939, 7.650819138494803, 6.8249649891257, -2.0000936997664676, -2.7109808140104708, 7.297921976405078, -8.431690007932971, 3.0068511609363373, -0.32936009725430715, -8.092384427483328, 5.124531832608827, -5.333079392213098, 4.231218675227709, 9.022604585733912, 5.252460481488514, -3.426129549260475, 1.4377292515494293, -8.727053844003867, -7.851838670684865, -5.735047552802013, -9.486041748173594, 5.57398395538703, 9.66377656176019, 1.9649785643799476, -8.017710374136735, 6.590904186449599, 9.799718885384884, -2.1052239437874354, -4.901229973320831, -3.850194549789874, 4.412476671825784, 6.150765150473731, -4.055373800900773, -1.4928137322711414, 5.255039856744437, 5.563451987784971, -9.216140187014176, 3.33556375954676, -1.7428166606769668, 0.6875641183777699, 4.611535068525816, 4.732290168174817, -0.7005892200732404, -1.498764557722783, -5.374255760048934, -2.380661961879036, 4.502749809650817, -1.9045767143120056, -3.2269417470366673, 1.539280515709386, -3.988308787157953, 8.908872284592974, -4.874822630654984, 1.8728884781523796, -3.517182128789522, 8.738086496884922, -2.2428543697380103, 0.031356485505716236, 0.5869494273065321, -4.076771706423492, -7.014625969551311, -3.8611308157690027, -5.236528306693593, 8.728833105950976, 4.296227932648748, 2.4502692463554165, -5.639202469828386, -0.9495639244103256, -0.1104661404456646, 7.763149146002494, 1.6510642973709455, 6.687482353409489, -4.457884614291934, -0.09912604043591067, -2.7882624433566576, 3.3438638475962676, 2.6323078818052466, 5.128828041062398, 1.132673634437646, -5.869371203472635, 7.976843016390209, -9.797278668108637, 9.445205819654415, -3.861102251772957, -9.40142640210031, -0.7949830614486775, 6.550646672283747, 8.009729403831443, -7.428974100543487, -7.411656196875665, -5.676348360800077, 5.138294924556222, -2.970322538723731, -5.197544252106225, 7.090817080742241, -3.6755800371463154, -0.2201878561287991, -0.6204492657667124, 2.4988496014072137, 2.4799177563890744, -7.7162832929557945, 5.823973037936456, -4.189675545945084, -8.703983918332703, 0.9643072720877583, -8.92733377772074, 0.7716279102712491, 3.3406124361452516, 8.37507885848613, 4.64622336524592, -4.950774696321614, -5.740464606164711, -3.0318836314771342, 9.19944057842088, -1.1446140873316768, 6.879560406644082, 2.508996278966105, -0.824627634807868, 1.3270534906693534, 5.594927902820313, 2.290452824280102, 3.0499675588346697, 5.937925135211016, 6.545770238234319, -1.0458162006404628, 9.336589974857748, 2.958152376953338, -3.829269348505562, 1.8045191027792225, 4.226534922274617, -4.021259422382064, 6.128868770317126, 9.425062334301202, 4.026060672492832, -2.6486408015398872, -8.529656503525455, 1.526737358119611, -9.340522704057443, 2.907417622376382, -8.682456375205662, 2.3613335775453344, 3.3869357684293444, -6.739468544141037, -7.17199654875984, -5.802430692988305, 7.6399495960769315, -3.663654549320441, -4.705751352013716, 1.5911059863932664, -9.229905448361944, -6.687736945574418, -1.3282149940812626, 4.037855558291179, -5.3989700108448435, -9.875526890454193, 6.236158733786215, 4.309076610366343, -7.289590749949076, 1.6368309460492014, 3.409492495667294, 9.997897932982958, 5.814741831308359, -4.596583550126503, 4.3663737739635256, -0.5998765632180323, -6.66192235229839, -0.6005920667922098, -6.331313276303394, -4.756429113876061, 9.706479093495744, -7.082444924164384, 0.112408969041768, 8.487844046201687, 7.0406908717970005, -7.684174531552388, 7.914606815329716, 8.034342402178034, -9.078657946038382, 4.068591826842258, -7.171831623207476, -8.339559367210345, 7.069557608636494, 5.915329913436638, -7.754880295315811, 3.322741046463145, 8.066828038323056, -9.916304237502283, 8.862928646121404, -0.526955099796325, -9.66583885473412, 9.471218080050253, 3.6711096452394294, -2.8914565922231557, 0.1305682791855105, -7.638435011357057, 7.193189026191039, -3.9024007223930113, -6.743136196419766, -1.0577438772502425, 7.856486480128087, -1.3993114524318333, -4.354218838965727, -7.1496108140443475, 8.676808545602736, 8.614750876733797, -4.4180832717780465, 3.3471190968434392, -1.4675421486530844, -4.9614875105352425, 2.9574809388532373, 7.597660204470223, 7.431001034183314, -4.5590753091397, -6.9943246943288795, 5.326188433332728, 4.967856755262726, 1.9561982156243154, 5.247051241948329, -7.380692875322275, -5.821447814849439, 1.3446354651713133, 2.514345375645462, -7.3405553766083305, 6.720314577048189, -3.5120911241773367, 3.749306688508941, -3.401133980308493, -5.994716411691399, -8.551144043339661, 4.624001854215274, 2.8447271477544973, -5.172521085165429, -2.101101557590443, 9.455348287673225, -9.37973968253392, 4.040735959154993, -6.438147098769966, 3.3878595055003853, -5.33928663935606, 4.873800396978929, -4.605539062292725, -1.1129812441305447, 3.1463118293044516, -6.0425205286063255, 6.545711881523204, 0.7676456876869704, -9.526859899605917, -2.0843125796643847, 3.5149474910360627, 7.836157698656592, 7.100421751974846, 8.046092925667569, -5.216679134762265, -6.304384186939124, 1.0823470474139256, 0.9545047167909715, -9.249859488946752, -4.56450177404448, -4.0010946506132195, -9.449212451455766, -7.886273213199098, -1.5443341762829839, -2.0199019703071874, -2.6147673167590435, 6.299841324789124, 3.970483741729973, -7.363917243588416, 8.137408120743824, -9.827683669742262, -1.4118107321175728, 0.14646747092948154, -5.138672949037906, 7.437637742089567, -2.1248751874534877, 3.672353831009886, -6.506212164615189, -3.6407850264266823, 9.816832953845417, -0.2719230482830568, 1.2004607220231627, 2.4245389811546687, -3.3429519150911657, -0.5913422545685609, 1.1039323302474493, 6.020066562173927, 8.198948454458982, -2.062508247691188, -8.011162502242932, -1.9221603057642547, -2.051474418570427, 7.943429237398078, -5.6597114288375945, 4.457452769279531, -3.519776874687251, 5.731350924826003, -7.481592920288362, 8.260358664973698, -6.928063162087994, -9.493866601952847, -1.3002998859987773, -0.5984566458525933, 2.7100651810332685, -1.6429419882685448, -3.488415196236012, 0.09333647598251105, 3.907785396698424, -8.57830707921703, 7.997502452450011, -7.439419648488752, -4.22448144358774, 4.115135925376459, -3.978400196116585, -1.2788864943011458, 7.342918503248722, 9.44354338482265, 7.6145625043045655, 2.454858153727324, -2.8661345696439655, 1.8166975108777539, -9.342955372390625, -1.0800934383158314, -8.386459644923864, -9.482056792047224, 0.2897216384364132, 8.255236020977051, 6.5213031343592185, -2.7772540247264565, 5.886849146485373, -7.057285420303707, -7.257664116144483, -6.440882997542429, 5.81900197132642, -0.9450874524546489, 2.8205918116408775, 4.755811257218953, 5.097559604089794, 5.840626006371421, -0.31147223924839906, -2.1819305883510864, 6.616628666888907, 7.232939598982377, -1.9415603664066943, -0.04180130475711685, -9.54628466832178, -6.123164489837469, -3.8989748551098202, 1.4665022827369611, 4.170126875331784, 1.715257751838843, -8.376427436825262, -1.6680591324713383, -0.4898373122019688, -0.6228683607065584, -2.737087837482073, -3.868711736984922, 8.765891854088068, 8.927915087196055, 4.297496225622863, -0.29789133861392614, -9.034520216501791, 5.694036765075637, -1.6718560429266596, 4.83836192025489, -2.316865803888046, 2.5144874134987774, 5.579216447884406, 0.6437969038661535, 6.778118924657207, -0.3168130566785248, -6.938654771636134, -1.2617669098420627, 0.4145739465588818, -9.869576643142723, 2.1583567742646323, 2.5562435534469596, -2.956105557382691, -1.7868846143351451, 5.72270322748267, 0.4060098004094925, -4.825687385572062, 0.1895120744397243, 2.518546731527602, 6.455038111440569, -4.096290027628278, 2.8637531242652496, -2.6510092412917334, -6.525468305409163, 4.362205561528521, -9.186981119829785, -1.5155752828496087, 4.305706577115117, -0.40956725410097583, 7.806867833001586, -3.048582280301617, -3.0505924604828127, -0.3375056160827725, 0.25173259073175913, 2.0317242269384987, 4.02270772480685, 6.473512393554426, -5.670629607494837, 9.31014070663819, -6.821250637822125, 9.03410343194625, -6.952229196660749, 3.335557673336586, 0.46609483592683354, 2.537130024060282, 0.6215521224892626, -6.851808107167015, 7.223653508569626, 7.267624286124697, 7.2525065565169875, 4.6834562527418235, -3.5600364025675564, -7.78907667329507, 7.115733262640674, -0.32394088652845987, -2.674935654760504, 2.9717575421279605, 4.83740186046955, 4.440961065477682, 6.56673372239484, -9.121860840669676, -5.9678502288836, 0.057707070570387486, -1.410189617353005, 1.353404233436672, -6.410285094225461, 7.6047341586756225, 8.03187882486785, -6.3761882628347895, 9.184846118658424, -7.425056575533448, -3.541827095810934, 1.9041836767925027, -2.0575451750376335, -9.827870815886426, 3.2160618491813846, -5.843573708676331, 8.361968153930068, -7.31421903480628, -2.6692753394642406, -9.96768931910271, 8.527910344264413, 0.6182540700713979, -2.896054402151451, 6.880319125067238, -9.96482525291525, -8.918324473093865, 8.643317299460406, 1.9435407729577232, -9.32286894116267, -5.369184690916462, 3.3094039761922893, 3.4731255080572616, -5.24963232163322, 3.78338433312269, -8.742961720198199, -2.975469140203475, 0.05871948642106517, 7.947772563913546, -9.85062868984805, -7.652185747900344, -4.263170083498022, 2.097075497007614, 3.007344783862756, 6.671551007880748, 1.9087717567629525, -9.581331771025603, 1.08937182264828, -9.114093004895551, -7.753397156895014, -9.833085888189233, 3.288726523968853, 7.867640793483087, 1.5260733487663671, -3.7784415925527925, 0.4126629024063906, -6.9183984060516295, -1.5979521212830345, 5.26108060740791, 3.8515209835055124, 3.0891833598639984, -3.9143382184975124, -8.93971776535059, 8.683395303598623, 4.6534356498103655, 1.8923429183116642, 8.927246439302444, 2.664442679507342, 7.125445046721211, -7.9877385523514866, 6.482936342260164, 0.9333225676576653, -5.808002594661756, -1.716573314372713, 6.987207514597227, 5.231218099194496, -4.407857710002185, 7.21432391010682, -8.869360250650447, -2.24928896168048, 2.3178552498810205, 3.095417657372808, -5.452071493905468, 2.5628356861775075, -6.45282448449824, 7.568644911915527, -7.3827601781201535, -8.628261961311605, 1.8290936865276368, 6.186134858361829, 5.189429728323848, -9.257349234144073, -1.5876379982179785, 9.11389923834686, 5.2950225099436175, -8.677688571383904, -5.584898503731097, -4.807084293013883, 2.8715438701785185, 9.935854229616048, -7.776740163627411, 2.9760550087574504, 9.830252887920231, 2.7208414033469115, 4.563657991919726, 8.749097451171615, 1.7033753690714608, 4.34947304373674, -7.09813239612142, -0.4745118653928859, -2.0787240382189376, -6.099168894598323, -0.043581191259940866, 2.9562346666901913, -1.9291040121250802, 7.812198434449375, -4.909365545801978, -7.3569799953869275, 1.958928217758702, -8.555679941121026, -3.9841421770456016, -3.687103300056382, -2.889901290851915, 6.979628060094377, 3.9259622742861673, 3.891168898646285, 7.230312694299496, -8.352002552325244, -9.556943382397467, 4.930625107863191, -7.535717896414782, -0.09164496491899854, -5.888366555651141, -3.5672805171767337, 2.0980806386597024, 7.966083705664818, -5.3613835465425534, -5.184214843476509, -7.353572768751089, 2.8509870477932786, 8.772260911957869, -8.675163919386817, -5.554656813131073, -5.431021941901124, 7.518162881774646, 4.538020257276417, -6.489076719551368, -3.618471418332321, 1.2406771970631105, -2.437490724892948, -5.84767238703773, 1.3456660666203817, 5.024012522363819, 9.5208468983768, -5.978901083870882, 4.832306872419371, -2.5581614193441293, 4.410969191025131, 8.10913347742569, -3.2202529933911954, -1.5600944620359147, -3.4277244599962975, 1.8615770264148583, -4.723281768770473, 3.359117436065615, 0.7175915918880058, 4.1393933272944, 5.151147068413927, 4.789120160989475, 3.9379628890075544, 8.118554475508912, -9.81528537446797, 4.045336874319279, -9.2743674770844, 8.706918996467266, 7.354542036984487, 0.7527041734530311, 6.5200883103875, 8.181031999229887, -4.485957992278287, -0.4067496550234999, -6.461386277717098, -6.178580595829796, 0.04265834317833139, 8.124184668415637, -2.0231785398361417, 8.916006983499592, -2.550748684041528, -7.2795166906330095, 7.260307750625238, -0.6366514037561348, 3.824595508162778, -4.40577629892571, -2.8493198158686317, 6.471753970457485, 8.076848578609052, -4.380784058131768, -8.259343154595744, 1.3128626426140073, -4.472273337358725, -6.929429957570261, 2.570215737121888, 1.863273290898631, -2.679735273742092, -6.435831287080632, 5.1307848238085505, -9.529366894829977, 9.933808417285952, 9.179283946620671, -6.022671065632279, -6.707699814719148, 8.512963930695868, 5.942555986827978, -4.439428303553408, 4.2288786812792, 5.161527726086657, 0.8648988468005072, 0.11083700626601711, 1.525894381419473, -9.164346883743832, 4.998038198942625, -4.635099152395171, -4.340509659600182, 7.941729193506664, -8.767025227096791, 9.429068347895008, -9.750344273206505, -6.057031008928522, -7.4915556472745415, 7.405461749440185, 7.506351080313401, 2.364848357597211, 6.601691197181626, 1.9986551139949107, 1.6222929039756995, -4.483856897347809, 5.075262460332507, 2.2806017616977776, 9.216857214249636, -5.916721319604601, -4.623909400323294, 9.0043915316819, 4.429002751467429, -2.3789577856618216, 8.060779434086427, 8.676654995251692, -6.831684270810459, 4.710849076427184, 3.5095949203271317, 1.8669223607763819, 4.796986428766166, -9.668823528333776, -2.702000366649317, -0.5011930964198381, -2.576690183697041, 8.396496479859916, 1.681317747502856, 7.11388513765397, -6.576875765746141, 4.239803851456308, -4.6570437886175675, 4.142406515505037, -3.047563318900261, 2.136453733677996, -8.805473330205887, -4.504493488809176, -6.665886187037724, 6.349527120481067, 6.890815032936473, 6.917617740366655, -5.4944597790197935, -7.591692718377274, 7.604140609602155, -5.000789792402847, -7.1260759130422695, -9.194900847890286, -3.8617532783302266, -1.6703992704679003, 3.9287675485762286, 3.839257273416198, 1.5233922145893803, 3.0056489808028566, 5.814566400432788, 9.74832620486119, -4.5809734045269845, -9.414056188130948, -7.477762787131299, 6.445152959700792, -2.6373000697655353, 7.837343830645683, -9.785007321077206, -4.365446679492515, 1.4849702044922726, 9.167767351459545, -2.4841482363801415, 9.48769817627145, 7.805322390364257, -1.0731392954054861, 9.790681401536055, -7.89281303112433, 7.365833616011351, 6.660016817548389, -8.083028636520265]
BIASES_LIST = [-4.176346619645375, -4.0532214441906405, 9.443036334895638, -6.885655789776573, -2.1048306012220745, -0.4816797924579994, 6.394109418635754, 3.61012458178749, -1.4676339936986604, -5.6324595656547345, 9.92658014251958, -0.22378298696458288, -9.00844683420129, -3.522711508433991, -8.61450585220134, 2.809183113455463, 1.74690638136207, -4.752098756861429, 4.2757087302156656, 0.05990669210850008, 2.2071173689353607, 5.528129800548111, 0.45835337470280635, -6.95970588190673, 1.4496103015431956, 3.0360268527421113, -0.4558299860523878, 5.44499770630747, 9.778257184150409, -5.892740856762481, -5.879334672933165, 9.586322427744484, -1.1493503392750632, 6.205143547992634, 2.871744935680633, 2.80236595462074]
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

