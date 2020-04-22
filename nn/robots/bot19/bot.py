import random
import math

WEIGHT_LIST = [0.5571418455425092, 4.906497617786401, -2.3177570666143295, -3.544746084800578, -2.3212539895026527, -5.286726097973353, 2.875029962884306, 1.8258526844728271, 0.8003350203360703, -1.1051632692884352, 2.603342238570166, -0.013217565874291811, -0.9001365814854432, -0.7573536022532478, 0.23393052352174165, 4.932363875388414, 4.681016894097745, -2.9757382776970953, 2.828991733363573, 1.825235785229997, -0.37013388784748646, 4.353455452756383, 4.931516227825511, 5.410989112669377, -2.1136461071176913, 1.6148588749707014, -2.1875481805298356, -4.35797160157734, -4.907375021024724, 1.383802304963365, 1.3641378317748063, -1.1193402275240925, -3.3957259850539065, 5.259484896064236, 0.9984822718137588, -2.498598662791009, 4.157327245266308, -3.2840818372722587, -3.753675051890976, -1.0341047618937258, 3.828522540523204, -1.857862083064053, 0.4340307254581671, 0.16090694562106705, -3.257850491555495, 5.726861748577539, -7.885573734672631, -1.0402675280006832, -4.613296174979399, 0.8763529751418973, -3.8395596772225637, 0.6773271242327983, -3.5764178223831395, 1.892666103792844, -2.2513246433211123, -1.5907728654183197, -0.4154790170562818, -1.9775104922315616, 4.892549909186555, 9.874737744096203, -2.192408447700256, -4.489781023104334, -4.316506468244922, -3.5180323848819777, 0.7305658777595831, 0.1996538606989146, 5.35729924156858, -2.1937996723342024, 1.2330888661368022, -0.6839445732720034, 0.4506295598928724, -10.34403828650444, 0.49229822717838584, -3.6908491561592713, 0.04853092427378784, -0.9673577376931336, 3.393192403936228, -9.800872736962525, -0.0720477575129486, -0.5712984729181052, -2.4115571846086397, -1.1089806700925273, -3.2515429587324745, -1.212498658194347, 1.0179146304225224, 4.813381191601531, -1.8394661262843737, 3.9943853005246144, 1.363638952124216, -0.6865324214258636, 1.0036227778048905, 3.785195471565598, -1.2510646999017816, -1.0620595347663602, -1.5824315368262192, 0.534220426449365, -1.7550428440936687, -1.134386938764731, -0.6254091725367603, -3.6853303804265853, 4.123017041455275, -4.822214350439458, -2.3298884237088267, -3.609642122090311, 4.931947666152477, 0.7462585365232821, 2.7040651015787143, 2.6859350060507494, 4.966719334109137, 1.890104501479756, 4.388708348281708, 0.6046574533623581, -0.533375220931961, -4.311973587831503, 4.463566156212404, -1.7101284466103437, 2.549805295388548, -2.7687831617614505, 4.56541186359424, 0.570651981694452, 0.6338642305043437, -0.16104104466392932, 3.599117857391104, 2.614517203325849, 7.010777764941157, 2.44538972181082, -5.3660194333192495, -5.630415975676742, 2.558617754919779, 0.06368578918883747, 3.628810812167838, 3.8452061065803465, 6.49624751298481, -5.744245385992287, -5.194611458433404, -5.160360054217324, 5.244432178091404, 3.514977733695169, 3.566417298249186, 4.55293564049302, 2.0791360308450315, 3.477649473222264, -5.223260355454765, -1.057179024705446, -3.6877563456535065, 2.5128970327175213, -3.94897462754603, 2.4828774573837578, 0.46550019458960545, -2.4787105525846216, -0.42675085121632145, -5.123931321518376, -2.420827490918199, 0.00033760651117444203, -4.157497144631206, -8.685962787316022, -0.22120074546446006, -1.820782916794609, 5.459864080553519, 3.8036087478394536, -0.9479278742803289, 3.8419882574876416, -4.556209406188334, 4.488750059028024, -1.1253226172650135, 0.36175907309321237, 2.108412098231329, -1.6912760550484414, 3.3682405075729402, -2.6073074495561777, -3.449584296440557, -2.4200676961686156, 2.0676923218347842, -3.284766810219581, 1.8345332225269035, 0.19556702415855653, 7.307372317525851, 0.13545940316319413, -1.2332329365447388, -5.377317273670514, -3.2251193211004248, -1.8835998505170273, 2.1515605872612134, 3.6565090863835907, 5.11555098009601, 1.1337091668138308, -2.63462638771806, -6.113380947115427, -2.507631239498864, -2.1344868385569216, 0.08170548894994645, -4.286163699280173, 4.585803963952528, 3.2532971097994214, 1.9123576914917586, -0.4251618416220037, 0.7564720799095483, -0.5175808725926423, 1.6929450272624826, 1.7735201952025186, 0.13214945260985525, 0.7057709038867649, 3.03789749079766, 2.4240655039384906, 2.2435340813492117, -1.351777172315602, 1.037082404482164, 10.582809408010698, 0.5805188776509826, -1.1242278242268595, 0.6072730238621199, 0.7530455776826485, -2.932782594707475, 1.3030765166778635, -0.6538288594304414, -1.7539523608119696, -1.6081725781950025, 0.33463828445210364, 1.2952868657672965, -0.7589376444130017, -3.9245943124454046, 4.083396279550503, -1.5768649508196608, -0.9552453821190195, 4.2505373147103995, -3.5231609343457935, -5.029980358239536, -3.323325757312353, 0.16026128896010067, 1.7415844589250848, -5.33444691248573, -1.7035194828013642, -4.689035588085812, -1.6476316308304624, 5.269586026450226, 2.403992683870208, 4.273001734108727, -1.1645471040138022, -3.6218950801420564, -5.934266479468262, -2.5694486750079952, -2.5864779730866236, -3.5936103741257037, 4.862233265018539, -2.5997311846985416, 1.212261418350324, 2.5981691820972155, 0.22171439392696476, -0.07374786199556836, 7.120683346160408, -1.5440288077359325, -2.1164566585925115, -2.3018488763537115, -4.267521365606873, -4.849261641705112, 1.02365291278053, -0.42151254959743034, -0.3508595914629573, -5.812805266788582, -2.513594528732354, -2.732483104338469, -4.574368783203363, -1.8291182953200005, -5.899825363206303, -3.065933638206276, 2.69310781311299, -2.3637907992873504, 0.5974126495892181, -3.759626607366794, -0.5551475261289954, -1.662322008195385, 0.1629832497030958, -2.899812891804234, -5.62265216734803, 1.5207747709858903, 2.025156396777115, 0.20498797331991717, 0.9972920174047181, -0.7784598551488576, 0.36373923021420673, 3.9436784304780783, -1.035514960182317, -3.899861629829009, 3.7498879220281376, 6.1609817294699525, -0.0753809519664038, -3.380322608668212, -1.8223887834388044, 2.6407476173599718, 1.7015829959809288, -2.9781799228008503, -2.6949952060577043, 2.54799348744499, -3.5730272086137504, -2.260739828493122, 2.359476063583103, 8.827635388047533, 5.946883995090477, 1.79642923798352, 2.0532423796675867, 4.562277266577672, -1.8774510288129729, -5.850244752119811, -1.7755860730013915, -2.375115762470961, -6.8685838384826035, -2.884846526686084, 2.295516963933215, 5.0640271093452345, -1.4296322446777228, 0.6786834492924096, -3.918569785709017, -3.5973188025157183, 3.2613304088876385, 1.8443382597930904, -1.7819717137604514, -5.6498807689299895, -2.407612959398984, 1.2865978889622625, -5.594755265452127, -5.3226334359469165, 1.2717393574470777, -6.7995728476001975, 6.401151313982675, 3.4306914669531072, 4.605915011450745, 1.9975883419841618, 0.2737267805849195, -1.2662468522392794, -5.563115833522742, 3.9656437025393645, -0.3327752846665548, -7.429210148840689, -0.10126630242143082, -5.028295203518638, -0.5051930357032796, -1.6766249357877228, -3.4524968863497163, 6.513432175559408, -6.781657984023392, -3.2362800739692137, 2.6630194484115273, 1.4768037118162463, 4.186042758629128, -5.690700485217513, -4.638478961390106, 1.7040747457269474, 4.803782089638073, -4.853684065677947, 4.652033562101128, 3.256036307339192, -4.024209200357495, -3.4043295030767586, 2.3115170832534218, 2.3339566540589574, -3.3929552327075725, 0.033403984488595564, -0.015545328053794138, 2.8176115272804, 3.2406134245203497, -2.247067671277928, -2.8233098270585417, 4.9154448332555996, 6.048284735616537, 5.291448706378165, 0.11426965610008491, -5.846591500628361, 4.256551249182341, 2.6061123146420813, 0.8514822291124204, -3.2274524948971166, -4.71599043657288, -3.667482005113702, -0.8876169976936152, 0.3353528278142959, 2.0734716805663505, 3.912304506549371, 0.685103359614414, -5.647639276085155, -5.260476170824824, 0.42450971732410897, 3.4245578299776893, -0.8717661591644031, 3.1652932857597746, 0.1251267907737912, -2.869569463622628, -7.23633885155306, -7.8890543500002694, -4.5941478683684, 2.460892742038565, 5.612080260285702, -1.70125442468736, 4.710848488777254, 0.5085115617254053, 1.4377570164683398, -1.296758844756355, 0.3474802431886832, 1.1794746870038242, 2.259982207295764, -1.495744152546785, 4.288395935296824, 5.560534242418672, 2.7192836531082696, -3.45365600284497, -1.7144578725059216, 4.5411288563644865, 0.6979294695558851, -2.146632339448225, 3.865437432554882, -5.546929358050926, -0.30151879246006386, 0.781986748886519, 0.9013217829604463, -3.285137811214231, 0.9640393109012207, -5.683330579282412, 4.134860346063558, -1.5757879905215677, -0.710498851823521, -0.99026407701021, -7.3920696260816685, -1.8319666205496918, 0.7594852499586481, 5.227569432258297, -4.348484903978602, -1.1469565309624945, 4.085337498609036, -2.7442116143770874, 0.9142273838716957, -1.9431823369472003, 4.39237303778555, 2.7870772865126225, 2.995247913832013, -5.91488030574256, 4.930774204896934, 6.184061999770953, -0.730272314313838, 0.8088029788104849, 1.580173979913706, -4.762005943739684, -1.6222769981763911, 0.6516389706701006, 2.0114472525937233, -1.83517116331231, -0.37441679650116055, -4.327946677322626, 0.7145816221935115, 7.98690801403846, 1.8079468872537787, 2.932650231477624, 2.4085561952452776, 4.520893677404318, 4.933136501836751, -4.363443071044048, 4.687869928497748, 0.003994057280710832, 3.625914824917907, 2.5536154356914653, -0.38268408363597106, 2.5167477491669197, -0.41825065924754706, -5.911290255910633, 7.699932899767559, 3.6852952505469907, -2.0455361807988965, 2.06835058606679, 1.4984026737462532, 3.189766595071548, 1.3728946733049836, 3.044696978462516, 5.177432604049872, 1.654998874188725, -2.319441109073365, -0.10805021734976245, 2.498451847048451, 1.350997473023132, 1.573360498356694, 6.846974652268305, -4.272088135613121, -2.458713157221568, -1.1919851098101917, -5.078008807930447, 0.5644946157353535, -4.346298341342176, 2.6933637450549144, 0.4027502354211035, -4.415249212864516, -0.816115710366262, 0.47752322622925863, 6.262839473218671, -3.2819995949912277, -2.877242386358501, -0.6903382463235855, -0.24736373205436937, -4.862479551759738, 1.3661794917495345, 2.6085688401195117, 1.8342253044033163, -0.37573852401546665, 2.7252024091933764, -0.29142375710694146, 0.11279639712692616, 1.5461074613613015, -4.739790972467024, -1.651273132834596, 3.6089287260090868, 2.86928028261144, 0.4950198029375167, 4.256521984082485, -3.0562010589349504, 1.8206327001519635, 1.0529602768283652, -3.776069144132179, -1.7959632568965072, -4.910213108123397, -0.9745619537225808, -3.9872441761653623, -1.0040137869053603, -5.970091728408155, 0.2985523267172314, -0.043153416601691794, 7.007560631302206, -1.1876816409189959, 1.1131219533644092, -4.020717537518869, 6.956093699627471, -4.081335625361987, -4.126250368031729, 2.043033026707838, 5.103534240898451, -5.504344811068822, -6.403576872555891, 0.9107935451135203, 4.222575027750353, -0.9011646713857836, 8.069827286064863, 2.529147043848813, -2.2967703810761937, -3.3374550034176176, -2.0007133630822866, 1.46315716890734, 1.0620546218908062, 1.4377692609138955, 9.024995383493632, 3.806610336110229, 0.568230899085635, -1.2656957876457406, 1.8068375911892178, 1.5045833181791968, -0.5504921301205097, -0.28389597183617493, 5.979802146393205, -0.1234848723820188, -2.7880854092227234, 5.40453694613753, -7.763977514574315, 5.2503315927145655, -3.883802761859034, 3.3986934641461235, -1.0118513353134744, 7.808655887447041, 1.899409753726102, -2.2536591550644065, -2.187958614595222, 0.03173059610216358, -0.12136071054553454, -2.457546483952117, -4.421923385309859, 2.206996038891227, 3.9647159262313107, 6.041446413478747, 4.877790003615074, 2.2482398517748488, -2.1541196591864735, 0.03426247265680804, 1.8491117744478345, 3.7088822175298786, 8.937570436094639, 0.3984697103404028, 0.2298712637257644, 9.606226027122128, -0.6112204565046622, 0.5327582370917042, -3.18890140976019, -2.551082673375376, 5.7682027071842334, -2.3470459850492036, -5.4458969552909124, -0.23869743064072232, -7.369325269191311, 2.419500782761808, 3.077100783887069, 6.10828919979875, 4.949668016425947, -0.9508928533298203, 3.803882288776329, 2.912347856585436, 4.116690892284518, 6.783269060544359, 1.3820005620822318, 2.3026261120906892, -4.253267231889265, 2.017474118568456, -7.718836959607983, 2.1646277173713058, 1.2672075042930708, 1.2137884457518897, -5.142308665384769, -4.542864483058124, 2.3546190160615432, 3.0345665037447143, 4.269748895058665, -9.142811289674917, -2.422175525829183, 7.442280781980967, -1.3583841724268593, 1.4402625402528753, 5.832019454158214, -3.4648135277986833, 3.161879602198975, -2.0117077491587763, -9.986046807478452, -1.0514491187485508, 1.4764646641850492, 2.9078158541752726, -0.9028393758233332, -0.7051479810997165, -0.8065909007997305, 2.2764848270185496, 2.494684234088446, 3.2250729078720415, 0.2835287337641138, -1.4151392436037704, -4.294631621953818, -3.230694095110346, -3.4220937456131173, -0.7131099632426623, 0.8630410025509415, 4.219911650698189, 1.9534153492892135, 3.1787150492126344, 3.1118985142023203, -1.4419818685002626, 0.16036489180266142, 0.9661503200684531, -3.088148505896181, -1.646888161087299, 3.4794010983382226, -4.017717603625192, 3.354933235551909, 0.5724254152871759, -3.684251809500219, 3.444818630377036, 5.925108384731037, -0.44443399733074096, 3.2297941922954503, 0.37917490310636986, 1.854106554319799, -0.9184770601729125, -0.20028083879844127, -5.262123619561638, -3.358530422834622, -3.7089598717419205, 2.3403645854623454, -3.896985627649858, -1.5400823753217268, -1.1409591907172123, -2.0631802575771783, -4.902930908191139, -3.86369641402326, 1.988873420378845, 5.677422193867271, -0.20247675816136715, -1.8289330058744058, -1.358293454590282, -4.28615435496051, 2.349669440570638, -1.5501413601589025, 6.689113467837966, -2.67728467195305, -4.7436417687743555, 7.8839907607563235, -2.04347835409409, -3.2800884715341234, -5.1578322075589975, 2.999469254422544, 1.5179994245399804, -3.552901538750644, -1.3588985229620685, -1.5937036110474636, -4.805784729296102, 3.3352075482299135, -1.306631484024081, 4.37874349259729, 4.626219369277506, 4.286658967916371, -4.91131743748666, 3.646228431311988, 0.2383856258695409, -3.3984833759893083, -0.36085889490391043, -4.7401802600589145, -3.5373017457300047, -2.06722724864973, 2.526505328207156, -3.4117220368854313, -4.680575424374928, 1.4355272026316712, -2.7568643469682343, 2.009839113376057, 0.47559920670634775, 1.6734772028264058, 3.9656997100351465, 2.9342733963408802, 2.7934095950139306, -5.861713189672643, 6.9838106251746925, -1.361339001618871, -3.4676119455403165, -2.8458935862605905, 0.15049368323843912, 1.487366588567691, 3.0330249290902556, -3.595929589229058, -1.0555009165400349, -2.763134746361477, 0.5800060816041499, 2.1890108661168277, 6.120869381228145, -2.75781956672677, 0.08500115883707336, 1.4818254591256683, -1.2521747320664742, 0.7323252299932986, -5.733343329459415, -0.8350294491311564, -2.37942291814957, 2.3564223132819584, 3.7727122751965814, 6.927505409025411, -0.8706662372094292, -2.233744636273039, -7.980307108870692, -4.3303408018986795, 2.998874203189314, 4.218563623409299, -4.41641487567625, -1.7776305727057553, 0.9719811168695855, 7.601760546039304, 3.753860708600769, 4.882943570487095]
BIASES_LIST = [-1.3811096283984898, 3.7103842142108037, -3.6186703621772223, 4.798421171516815, 6.336826670538399, 2.773006089953225, 1.105599310399897, -0.07791742828383397, -1.1021830108815296, 2.6557653408714006, 2.123279809576891, -1.3722340153181536, -0.0072530827932461486, -2.6223596204294624, -5.4992465062096825, 5.263449563902469, 4.820822343549869, 1.481686753586692, -6.5688758080800485, 0.024057391316167295, -5.073527686055702, -2.8028511425910234, -4.064495987785636, -6.100634202982054, 3.9221948018456, 2.6559045695880066, -4.025605901047984, 2.919984803637645, -1.077766966674259, 2.307417825859905, -0.3454426042204085, -2.2910455759556823, 7.118411758043757, 1.853137897490095, -1.68644434958456, 0.44372907279505713]
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

