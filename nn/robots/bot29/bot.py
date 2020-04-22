import random
import math

<<<<<<< HEAD
WEIGHT_LIST = [-5.778707618323735, -7.558613288551923, 1.283303702724126, 9.492291929953392, 8.781221301838915, 0.6702855948707338, 9.092504080012954, -5.748167236905464, -7.043054989937607, -9.349322029403996, -2.6575346026072992, 4.8882391861482795, -1.2793564754127082, -6.76372981819553, -5.649843964825378, -7.600601600219623, 4.526709306705559, -4.254476207228414, -1.535950880020751, 7.813596214324047, -7.855179574403868, 0.3806511763174427, 4.347038686805103, 7.851058956593558, -4.557567000645544, 9.358239570744825, -3.493273355170519, 8.560463651191306, -1.1072831108337446, 1.5529267540650267, 9.782444726255662, 9.022102086380286, -1.4638370616011454, -5.608888754706838, -8.14042797233591, 5.506558187242206, -7.21713448963079, -8.884480314350832, 3.9636035230422557, -8.81991393319874, -3.6386491819315943, 4.266313521224745, -1.3101816136445859, -8.67178227083352, 2.3998819429595954, 3.9500748723169288, 6.389159109257626, -1.7186607051867693, -2.1432509646457536, 4.23497281499974, 2.21496161872434, 7.686482056460548, 8.530168594336903, 3.568302123710369, -7.393788544440394, -4.187088980683855, 8.459868287527009, -0.013234772256563332, 3.341600670786475, -6.366776790113957, -5.0239596763169665, 0.44218197944541515, 5.945921598337003, 6.860028938318614, -3.742210175764294, 7.796315618322531, -8.603795560262027, -6.9896383851621895, 3.015077013982923, -2.5061059858057515, -9.183480005705235, -2.8187790077565644, 6.860169521465821, -3.930026134345532, -4.151643142722881, 0.6175483219257671, -0.15552296782391117, 1.7897978295111727, -3.5181769354500787, -3.8909791437642527, -9.32414995511007, -2.6492186564830806, 7.139141692419031, -7.868675641660936, -7.407331016919853, 6.852541587111311, 0.4410014105146409, 1.8612235797759418, -3.630354183643001, -8.380483706404675, 3.0336970024059617, -5.709833404753876, -4.4097592697798405, -5.795038648849973, -4.061003561518072, 9.521740194926736, -7.38088415785819, -3.1188906090519115, 8.483126432886017, 0.48972176742444873, 6.974926027052039, 8.13587009495939, -9.661713564026167, 3.7168075385840957, 5.005411337390427, -9.447503567965764, -0.4332273575303667, -1.8724416045511205, 3.65709134523466, 1.4083428011385646, 3.668465343077976, 4.079983401688983, -0.2839141727338834, -2.791377930121442, -1.9746534743021513, -0.4925008082970521, -1.5785020114117199, -4.131447972500166, 1.4984503887920742, 8.80851758022547, -3.86339120878481, 9.80970831632688, -6.846604151061452, 7.226789043713232, -0.8653013184587834, -2.6538932274264475, -8.236493267152511, -3.91034482826627, -0.25054112471599765, 9.804916057330082, -1.907087258858283, -2.4136686260304474, 2.7881375627609764, -8.811215510419618, 1.526533915289253, -4.339591519976969, -2.7558047473299485, -8.932602048469153, -8.361069964393458, -2.8390385180166504, -9.564708293867488, -9.484565065626622, 1.6568723966071452, -5.8065742827267215, -7.697960897214571, 3.4048617524273155, 6.252337045915915, 7.907852242907815, 4.747745467879463, -3.420627555160438, 3.568943228995529, 7.676829129210773, -4.806456146005587, 1.79076951988071, -0.8533406862481598, -5.657047275010109, 9.244245642456693, -1.344781029518515, -5.377771253052888, -1.73413611348521, 0.2032531155793844, 0.06395086266735639, 6.158697357771249, -9.382757714986012, 5.268136105561718, 8.022825917637611, 4.368614892153374, 6.167897214557719, 7.928714607240757, -5.196127016830506, -1.6845472118256488, -3.626511840997477, -4.340667347461331, 4.044751328433895, -0.4164102294527936, 2.053567532096901, 3.5231377865325797, -2.529469369770423, -2.2325045232644953, 6.652531491305975, 1.9851364246827323, 3.036997252358411, -5.713238719708132, 4.546208778245548, -7.049994422173869, 6.3680894968381025, 0.6516353614560515, -1.3183386946254938, -7.770101183146345, -7.690649861378953, -2.787931802142099, -5.12011040769925, -2.10158839467669, 0.9489722070508044, -1.957070113387683, 3.044221335985478, -2.22514720808271, 9.538607717696877, -7.62664065167078, -3.6294857107582867, -0.0886025656002154, 5.68743756628918, -1.741646944794418, 0.19318053086160702, 0.338161592815835, 9.166450085496564, 2.4639049017079433, 0.2954002865976122, 2.5365055027823047, 7.892087194854646, 7.360543305373874, 1.0318132690137176, -3.688995795381958, -7.886592623240389, -8.971958444839858, 4.020589229059176, -0.9850281324287913, 2.199294437852773, 3.8741086714383925, 0.5254993910949928, 7.452249800836778, -4.259727503077921, 9.500772145147007, 1.6129258183849196, -9.298942446632598, 7.533508436049029, -6.6322012095060074, -4.864688398488656, 1.523107977882443, 4.642297654956485, -5.017366474418187, -1.8621190377273393, 8.658138057059876, -5.426089524852918, -6.868061090069699, -6.063578434330987, -5.951638864441811, 6.5145464539897375, 4.744022592582631, -1.2357233901927565, 0.2207592685421904, -2.5392251814933786, -0.7499578527732442, 9.417895408155918, 3.0274344286409, -3.6910974999515496, 3.5808881517930207, 8.44341467901656, 4.966577471632171, -4.606634739624937, 6.289283542536843, 9.455056954732065, -6.079617703951971, -0.05355910600176372, 7.540164052411733, -5.714112836352296, 7.596154692085552, -7.657236707473876, 2.282817013094995, 9.712117726531677, 5.4302586292965405, 4.45740939652406, 7.251842617004879, 4.667027821479513, -9.332514790948455, -8.570772474471868, -3.8683102755035943, 2.0778262056053816, 7.353134692846247, 0.8556020402516751, 8.743078586185803, -5.241402759994342, 5.5467937448732805, 3.7221324774114137, -3.666537168708615, -0.04395840327597256, -8.396396422084138, 3.493382893188137, -1.7416362305372743, -1.6645819648951754, 1.364087892813373, 1.714604889089685, -1.6674452092000571, 5.841951070141365, -7.241580734257596, 6.518198582720586, -0.8421931167712575, -0.6929908760852292, 8.009531457554306, -0.7206733309079603, -8.038633679703587, -4.117916002065554, -9.433313967413245, -7.935342915981874, -8.318106814103858, -0.6323763445047561, 6.112050086482938, 6.853103126471133, -7.221322984510952, -1.5317276504163164, 6.576420262874926, -7.120449575433461, 3.0987292560793716, -5.701871458598244, -5.009196037975261, -1.8232411957694872, 1.4178429192375255, -7.914417518204379, 6.539356197345537, 5.336652801678248, -6.981010377714356, -5.914977372927915, 4.0605714979464835, 5.180853863997793, 5.7146061330667575, 3.1250615287016164, 8.831692472242207, -0.6422592036004033, -7.364033039922841, 4.277173662119594, -2.692400418340668, 1.4751282472296374, 9.502922269349341, -0.6881812995234053, 7.559187782748467, -4.82888960800556, -2.760511505050731, -3.9116189796846212, -3.4821919594995476, -1.899499586063385, 6.555896781764282, -7.786856332679275, 8.628062266838146, 5.867442319479775, 4.705451894063318, 3.293238404068772, 7.07358475843407, -2.723493226005898, -7.660641071657615, 2.6992022173022505, -5.594316561724446, 7.789151467378577, 9.660602396705691, 4.409648501857236, 3.904831293921113, -0.3754005699922036, 8.624662820268355, -3.360559511648229, 8.576058679626655, -5.786413939934163, -5.692271152155694, -4.147038890035204, 0.7729464555129901, 9.841109310713463, -0.11806804039473384, -6.781934013354023, 4.083677619875461, -3.809629477847823, -0.8884068976745354, 5.113711912856484, 0.36406720787293345, 6.977543511177011, 6.87613130160927, 0.05865183367440174, -5.373797874718318, 8.983357484375265, 0.8459890688645206, -0.23419637274401772, -3.9311056312988546, 6.202274547495804, 7.236035319037512, 2.0654347949785183, 8.991140032001248, -1.6643599934089899, -1.4579358343881168, -4.596329725987303, 2.033540323702832, 4.587256980562042, 9.88294285764368, 0.4777433774313611, 2.88451473861503, 3.5612366290683095, -9.784432696432972, -3.1973441439090644, -0.9214493008151763, 9.117115857850958, 6.67411008226895, 3.4834961244557014, -2.7546235307534017, -5.32070113132495, -3.1639379308844795, 0.43866125782306575, 4.298930052904279, 4.884770138037657, -0.2404976235640568, -2.1231571165456042, -8.56656862445675, -3.4994267870478595, 7.340704030477113, -5.646577427008914, 2.369897946134154, -1.4749826642565012, 9.764091168751673, -4.984655564444633, 3.835746408194435, -0.8631390649218709, 1.5564170177205412, -1.7460355671067767, -4.383351352421718, -3.845602173356262, -5.85368536232683, -8.802330347567706, -6.517100093860448, -5.716184652630087, 3.970569677611355, 3.4428725486706035, -1.020167935025336, 9.774647275348855, -8.991268458961159, 8.7584348066516, -2.882732438390823, -4.828657918145591, 8.5997884534662, -1.4311916881031888, 2.82876799479261, 5.4622196810069354, -4.767602598552967, 5.703993236034785, -8.262114423173745, 6.7995563557903935, 1.2052984400212203, -1.7817053942845362, -0.22875427321805653, 9.286715514460873, 5.255915875811015, -1.2413881200406092, -0.4054621229234314, 7.272495293409065, -6.257562155674734, -0.23144554877404744, -6.5270249435596455, -2.817325428659368, 7.729139101161323, 7.502459800076025, 2.9389585800749085, 1.164334688421926, -8.227803240678364, 2.5622051256189806, 1.9463133467497364, -2.332426534579108, 5.408398424851262, 6.279763094183576, 8.388076135758066, -1.1465778256383867, -6.718065572507297, 5.192671730103882, 8.671427426944597, -1.2426494156436618, 0.06431842420200162, 2.6121743210659716, -3.9587356112145144, -5.405312996283136, -8.847316251988158, 7.448671375407951, -2.9074965785307594, 3.4807956267692415, 0.17713552153798418, -5.872115750221402, -4.304093067700297, 8.085739107670019, -4.428172897044595, 9.134880707013629, 8.067344404739472, 3.387997393519342, 7.3063347121705, 3.4377582629119434, -4.048709501430217, -7.718229666766905, -3.875811774179903, 4.767598976710257, -4.200975470145558, 4.653293240102872, -2.6827854235090793, 3.7162305635008224, 7.817423306136618, 4.8439472340088905, -6.329247981966768, -4.251923949793022, 2.100487590380249, -4.985848321987998, 2.9216639752967737, -3.2446709507519866, 1.6130901426784412, -6.432291412114686, 5.948875381115556, -3.387848708222778, 8.291778793075672, 2.2750906508657565, 0.5649240197707073, -5.086716741713293, 7.312870056933196, 7.3117236521990385, -8.204906791653809, -7.0836348171849295, 9.873217660814642, 3.8739911172768675, -7.497501461625998, -0.11634230514537869, 7.470593748403381, -8.748749085284844, -7.211822043366918, -0.9222250700042487, 2.3716319687056497, 6.0208963721043425, 3.529644075728717, -9.630503753486074, -8.296335865433942, 5.545119062912507, 4.138635079689511, -6.79956175161043, -5.2576658864758, -2.839239656834323, -5.321936182192076, -7.655774292010003, 8.895522314753272, -3.3433256964206226, -6.384938476505138, -9.952439370253835, 1.9582968575008586, 4.529901057380613, -0.631715621578028, 1.5636896307501296, -6.345842660412366, 3.8775572902665374, -1.1145698536815374, 0.10048430282939336, 3.0416435284846504, -0.9048410343656492, -8.695892654764721, -9.042789093235656, -6.06292471753386, -0.09413993024712397, 3.9312712074216485, 4.876107776437365, 7.825251265402766, 9.359413911194984, -9.049670180073937, -9.05515763140825, -4.377557676429802, -4.003621924854032, 3.1730946809554634, 2.380019045910327, 0.38623607643083524, -2.41638522086223, 8.551444786624021, 6.1503614033527185, -0.61674304665212, 8.35627548207226, 6.840199791338659, 7.456412168592372, -8.5984871693633, -3.656557111756637, 9.999881967411909, -1.88686579342491, -2.1271139826227303, 2.2999480854082073, -5.150290723178439, -0.018423298593866377, -0.49364938040851847, -1.9629645514517797, -0.7415287390564345, -6.874786249117761, 1.5411428755816594, 0.9654606899586469, 8.644841652674764, -8.517299536449979, 2.025693377460687, 3.447523744728345, 7.864683775550283, -9.746257931634412, -5.11335788921339, -0.5574866699928034, -5.586059469029423, -9.766888359724518, 4.485011809150688, 7.134207723664105, -8.394258583603055, 0.6010722785880525, -8.071516667710801, 2.4759925567489773, 4.552523114168515, 8.653835129137317, 2.8188271056907244, -3.996054885566833, 5.233853090046786, 5.7803213352732925, 9.39200855422197, -7.31103658336643, 3.45762983947262, -5.528241146233828, -6.65751328830188, 1.5093006140778797, -1.5223926666292158, -7.540800237772361, -7.671273869482668, -1.409845459156827, 0.23195152827142174, 7.086714159772086, 6.6230846993208345, 7.386828171005742, 4.222897890116975, 1.8369608582720787, -6.322979056977038, 6.1105672201353585, -7.573532284825726, 3.4155124876542615, 5.771724454622211, -8.921477546470529, -0.43399304559244634, 4.139789922922802, 9.726039163124597, -8.564082785111856, -6.726259774136523, -8.29939439740118, 2.781314927178432, 7.0577369064153075, -4.969083059311434, 8.685366256084375, 3.027624181011788, -3.1645608524836693, -9.975710374537067, -1.970639612882417, -9.719026579340738, 9.549680775694728, -7.68625144668002, -0.477649983692805, 1.9698161106463292, -8.358439624571263, -1.751471059626045, -3.7146569758926296, -6.826080760186697, 3.1712849443922497, 0.9995694356933633, -8.675840002411041, -5.216612989812058, -6.051336278043145, -6.700869988921367, 3.070017536825624, -7.962670924671178, -7.028980034038909, 3.3104184402411647, -4.151274078189038, 8.830237938545121, -7.107847727586494, -7.047615288018192, 0.8767163263446882, 2.1693276095758147, 3.7884083242275786, -2.775115575094227, -3.1848577927687494, 2.190362576022391, -7.729708849611079, 4.681089300445166, -3.6067698294553967, 9.564036899207306, -9.558551641264781, 9.9657908030468, -0.5777407897203695, -8.923715696162377, 3.6707113265265985, -4.58216979143409, -6.932378570151614, -9.11540149483363, -7.834444175491573, -1.94560875422704, 4.509913022888117, 4.150041392257233, -3.7453180548194043, -7.806143915554431, 1.3543954137271754, -7.363275642955953, 4.482339541126571, 3.9978370318543632, -4.6296957066619875, -8.703726536003092, -2.01267254402012, 3.897853430239662, -5.616314796120106, 7.570065310700137, -5.377879763186462, -2.071463236186302, -1.1702669247678408, -6.75733381294749, -0.014590613599679614, 7.9166376435264425, -4.23749311605561, -4.804792392671078, -0.5137963581442371, -3.631150811583222, 7.7512393686493155, -8.348531174169743, -7.96680199082364, 5.468526641497542, 8.666888043308475, -8.737828088070085, -4.275187596107324, -8.734987481069279, 6.501974777287344, 6.0172672236548586, -1.6556249548875641, -2.932569293524603, -5.008384034930236, 2.964266600593156, 5.008724162682494, -6.035886204340657, 7.436192330054784, 4.816393490161236, 4.519960613844503, -5.711762860246443, -6.667581046153681, -0.9225522634414336, 7.550193995624667, -8.40816601428548, -3.4022047990999438, 8.486602899880612, -6.049543726878886, -9.60471180355247, 1.302316342068714, -0.4436527911441033, 4.498694063237046, 7.115394809128855, 3.1796745231693144, 0.8639425945101387, 9.531757687733645, -5.460478485774294, 4.362879717988108, 5.024246531947831, 2.98087438173466, -1.8842941728089038, 9.361023464700125, 1.5733449448491132, -5.871626628199809, -5.112100169455855, 2.0283178888246596, -0.5399053591528329, 3.6192810389941084, 8.688317173790399, -8.333703472229486, 0.8408111608956546, 0.65439684621502, 0.2887830268722773, -3.3390890336463075]
BIASES_LIST = [-7.737071700560543, -4.508150221414922, -6.197235436632187, -5.327575165715064, 6.089497278642103, -9.930815328684588, -7.145445388244962, -9.974258323484545, 7.19318112190534, 5.056499133266142, -1.0903481302373486, -8.423162911782068, 8.819138829377817, 8.970089223094021, 0.34308053403552563, 6.341853005450439, 7.875946134818346, -6.795135502906882, 0.10063530572271517, 9.583088832694983, -9.368479992426487, -0.10018983709382745, -7.867650656298791, -3.6833092223448594, 2.247608401479342, -8.70336645435314, 2.39607161907751, -1.1895446455167598, -3.0997537522430036, -2.71164499257093, -0.6683324214197572, 1.8288876549718136, -7.680632194869819, -6.22050950209061, 5.924931037095176, 7.2769703505323875]
SHAPE = [27, 16, 16, 4]
=======
WEIGHT_LIST = [-9.731607528298225, -8.147528629909644, -0.597925650428488, 0.8529148127367598, -0.7767175374074355, -3.999473532713047, 2.333802610401696, 5.514647443171221, -7.334554429156643, -7.42471310094047, -7.663374573896158, 8.413385644593113, -4.353070887565183, 6.700419591348734, -7.806694288032457, -0.7636140896359773, 9.855744255869702, -8.851402543752664, 5.429867530087405, -6.70310729435567, 4.407414599637345, 2.4542846002988767, 5.196940853207362, 5.102177071530365, -7.846926673118231, -6.571007808975553, -7.144075957771752, -2.141410973765227, -7.002300370613659, -4.065684733534633, -2.655117570496481, -1.4228570406394798, 6.330682521525318, -5.169389511576876, -6.87079763829741, 5.6218784441929355, -2.840416581622131, 2.1862353772931264, 6.296522008326704, -0.46505697230615795, -0.3836326250095432, -5.543928233016262, 0.8541275181378243, 7.87895319971339, 2.0690510301194553, 5.8029831445924085, -5.534282221253434, 9.389905254973637, 3.3490496609044325, -7.183192247605048, -9.70132605513798, -4.8455465219232625, -6.297929370704494, 3.9835269389752774, 0.3647819427967942, -1.3202072725730911, -1.1547783497058965, 6.362741365120634, -7.654601840126503, -0.5922411331218225, -6.840982491951431, -3.6286841540361037, 7.585325269941407, -4.471301890401338, -9.390762632617095, -5.310622749618192, -9.619539781015922, 4.691177670444837, -8.25379481028624, 3.8700370204150953, 5.097378638967831, 5.952214864302352, -1.6269157994252303, 6.657512929307892, -7.4334867208149795, -0.5204562080499677, -5.136788145034048, -2.0577366208548327, 8.049079643836293, 3.86927880517743, 4.48839636564138, 8.755129693867964, 0.4614798098086048, -5.473674321839839, -8.013800079223646, -8.66628940777364, -5.096104978705731, 3.867939305771042, 6.15903712953876, -4.4566822147128216, -7.2802041266093775, -3.4533747198742315, -6.308625375919088, 2.19089482920433, -9.574501443859194, 8.598839059521268, 8.624103585373575, 8.44862481748278, 8.253191929360327, 0.2311470449282922, 1.0564074438095155, -2.9123805969707073, 7.53082321003356, -6.402844555099268, -2.4329657934346365, -0.5372657485785695, -0.012597956740927785, 6.897190346572021, 7.630008523401173, -4.399733838940358, -9.552839864574693, -0.6497514529234749, -1.932485029889353, 5.248923239489072, 6.29475850014375, 1.3835111658718429, 9.449482944191242, -8.670632962780589, 9.936272836425385, -3.7589896504919214, 5.129860296986919, 7.839375835756197, -7.0285666692446895, 1.9727109455794984, -2.3984934883775555, -1.336227523960014, 8.049682007571889, -5.041716576399857, -6.133987520977923, -0.6211178576958076, -5.125864255844528, 9.975223144140365, 1.0099983882244423, -5.307131910690545, 5.8993822392200315, 9.286457959935532, -4.470349302709648, 6.402271119649431, -6.562618829334204, 5.174291256352056, -0.8696691283092619, -5.227406097069139, 3.362681461211361, 1.0630353193680193, 5.697124445965452, 5.7273643610433655, 9.66878961604198, -6.619101133402383, -5.250540825416234, -5.308799271213498, -0.2256516464739189, 5.339977027598671, -5.321827024538304, 9.57583013779492, 6.169791943136907, 3.4396923361959786, 4.264271748978562, -8.537816318660242, -7.669030521336195, -6.057547244701893, -1.8055868378580886, 9.320226998297578, 6.148747127304947, 4.623485865645797, -3.6519282306010803, 0.07792767869183237, -8.429956310575976, -6.833632667463769, -6.814222958691061, 9.393247443052921, 1.7405062359710612, 4.913150081433672, 6.982661685004551, -7.211706479262521, -1.9270460745903861, 3.7866204286255005, -3.492986328122054, 1.8595171672511306, -3.376733133560535, 9.059983555480922, -0.9324927523587228, -5.030767597881196, 8.06771264607043, 5.028903697294165, 0.659741159144918, -4.9256315354626, 0.9626158427133014, 5.7818262597644505, -8.501432500688622, -8.33199060691877, -3.1502274810295017, -2.6819154239221143, -8.636246092720544, -9.730841893104733, -2.977705179134551, -9.721492201529074, 6.602197594400433, -4.970703267512109, 3.802308163933226, -3.0793407245792697, 6.224002623799759, 6.549947471744979, 6.018309994273096, -2.1509908202423578, -0.44765711721573886, 1.1835413895016078, 0.22121266977807252, 8.567279115201373, 0.8811536603776808, -3.138467267415825, -7.43998747697453, -4.477759433329355, 5.36889966777704, -5.902755521142322, 1.0156839333910135, 8.801314452838906, -5.698593492196622, 5.138643979603923, -3.794154101447904, 2.065521767045082, 5.273857183703651, 6.589197989320262, -5.516896645611427, -5.273886131461191, -1.6585816962294366, -5.92885319000594, -7.872441037890638, 9.908803917723969, 9.905819472051721, 5.052414277708904, 6.78094073715193, 3.872933057406307, 6.537889951795286, 3.751661707297952, 1.4478345368710972, -5.5290811056959965, 5.005238570813615, -1.961715418590341, -0.46195619164005386, 4.726148431470554, 5.864922335833064, 6.627706404104067, -0.5435526955269143, 4.4413671025856765, 5.236719337234179, 5.452949997605925, -7.322983145994235, 4.579173366538027, 9.28959969825289, 5.235380569120171, 4.596723387691409, 6.571568272183612, 3.740182631016438, -1.112743141938303, -0.6053622090737338, 9.833001055341658, 9.39377549255656, -2.1608552068685993, -1.8762705885444753, 9.471499082676115, -4.0906929947361075, 0.964581900125614, -8.019977556995109, -1.6520828201106852, 9.75293294776776, -2.777726119856105, -2.5103609858521985, -9.90073104877031, 3.0515088830976786, -3.644558681853722, -6.8261277457479, 2.2509155227230533, -6.675563856537905, 2.328651326902623, -8.972993888267965, 0.8467186314540172, 8.530928845068942, 5.792820720042117, 6.2694377199317515, -8.160607491911485, -0.6139975933480208, 2.3718295059644756, -6.3597777367054515, 7.60754239982343, 6.242259552945338, 9.796837704927867, -5.915691494840698, -4.4953934073743795, 2.136530237828575, 7.030752590500441, -9.897161486206238, -5.273199624744292, 9.098122110733385, 0.9914378615574915, 0.35823217961872267, 2.3045477315500644, -2.6080280297224157, -8.293279070330135, -4.913150055697608, 7.979327245810474, -6.963089462457008, -1.7960402567649698, -1.23283879787855, 2.752457795437671, -4.228316661311434, 5.764069214147263, 4.607806076758203, -6.238394680427857, -2.9547148326856405, 7.752575484116221, -8.885681799854249, -8.530688710674488, 3.0136525739195683, -6.715610944200154, 4.67238920597384, -8.785766782636665, -9.61544752375234, 5.41652598740326, -6.0226977212028405, -4.846468947342773, 0.7921894664406253, -6.605576032293758, 0.9641354877776571, -8.305040014481264, -5.842807991304344, -7.263317842171599, 0.8109214049031266, -2.993693586461874, 0.9479405925318609, 8.144884208696269, -0.9279854483952867, 5.377188151530511, -1.2663782247171245, 1.4895172899438318, -1.3505602661098237, -9.853874782344175, 6.954233536373259, -6.843974345846289, 5.166611310011103, -8.256062069996329, 2.8734403324600866, 6.586693328955118, 9.759400908312536, 2.2734418220776593, 9.902953796198986, 7.955446399457948, -8.932889928581888, -4.206126424422701, 5.92113714524929, -9.558900269586099, 3.018226839880139, -2.423231965131711, 4.562310406981853, -2.249112600724585, 2.822091342033822, -0.8632672676964255, -9.787455798178698, -6.98432744032189, -4.760594284166122, 5.058304219187539, 7.315123076682713, 0.8371666521729786, -7.817564362002647, -6.958357413325134, 0.9757060344832489, 3.7647684667116206, -2.1876147214015145, -1.8570455512216633, -6.148980061727183, 0.1795016547423689, 5.576034840139091, 6.775626984858455, 3.642342646386858, -5.807017831803616, 2.0924198721030685, -2.48597097521273, 7.0403146724351515, 5.775631609601463, -5.516108057497375, 5.646184501790543, 4.472758323990655, 0.07015367554035024, 1.4411615051553284, -0.08168359947919868, 3.4931659818722576, -1.510415354819406, -8.461895130524862, 3.3076353675878103, 3.3670319685617898, -3.225286013986601, 9.154312618847285, -5.1074037911530805, 2.7444494412100227, 5.724996338299032, 0.5505731195775692, 3.060044341056802, 4.150460210377691, -5.482097624528352, 7.9952772436161474, 8.794779108048019, 3.630429157215856, 2.935065891374082, 8.913746297332402, -4.187227879710469, 5.5514456548244375, -3.329180158020371, -3.9595234126639722, 9.356082818462212, -3.6547329434573754, 6.847105291827628, -7.747236453363254, -3.1672664306329423, -4.989768425155008, 1.360902640544321, -9.531882244328937, -2.0254798501947153, -9.414884160635035, -4.314146834028061, -6.225894858805228, -7.175464044156161, -4.811597571066626, 7.054057307926232, -2.93982194546804, 9.201636409223276, 6.913882727754192, -5.3152311545994095, 3.9007779100857256, 5.738219356491374, 2.7141055538583796, 7.812936191320709, 9.749835678697355, 8.629172633066002, 6.996914232938192, 0.7903363009150066, 6.810634400302845, 7.990234103726074, -7.453800286627315, 2.6416503010279673, 4.940182038399243, -5.709058412573613, -2.9032967654778696, -0.7287765845302481, -4.638578294899391, -1.2772608837495092, -5.34379934752002, 4.510639690308267, -4.527289587933612, 0.8799856475467287, -5.779859547150032, 3.5193743137245637, -1.5007910999475271, -3.342511684764773, -3.2002141995444777, 2.909137871414895, 5.894783019995662, -7.8167236451633215, 0.06993634896063128, -9.219270178563423, 0.5947863970471658, -9.950453677734286, 9.15553021679479, 6.42440867992476, 3.157909221366914, 5.310685052142755, 6.364340659743771, -5.471239846030889, 0.4228147788506238, -4.848258792497813, 6.543544926931901, -9.733258830417375, -6.9377914193817585, 9.494775611455402, -8.087671737261257, 3.6185870927661234, 1.6103032348102992, -5.718170133218159, 7.931489889322901, -9.666220895001027, 1.0676457825138357, -0.31170297176809214, -1.508167845990318, -4.710788322199173, -0.21427653229526555, -3.7485981784278444, -7.7874746664524075, 4.852726499457482, 5.938253661149332, -0.03265811414023112, 9.206197656699125, -4.197957348332406, 6.183182184056406, -0.5295477000107969, -6.801931773265295, 3.6578476040235497, 8.3237881903155, 8.10626522015474, 9.90635370389262, 9.460427861595019, 5.632305907315551, -6.303492738513803, -5.24665983061449, 6.115342507006851, -9.725857117263999, -1.52002529874569, 3.5910839831986063, 1.1519940011502285, 3.9989611853177482, 8.777477947404854, -4.376226411781008, -8.771669948943902, -1.4284815161790743, 7.389378529583855, 2.2365343501614614, -3.2786913676883085, 2.7536383379057465, 4.03510020110078, -7.703000043534331, -0.19058040673696475, -2.9920001318802703, 0.44735956124340603, 3.4048137440200055, 9.163852352206543, 7.4381390641835665, -3.3193078886385585, 8.708417815959315, -2.742714327509253, 5.5644368967111895, -3.810344025461019, -4.439079074047854, -9.874055679532463, 5.823482463053807, -8.14042789486453, 4.729694230029725, -0.5250476290919632, -3.153403399219858, 1.98982316849985, -7.88888160632286, 5.032922109094255, 0.13566740245672548, 7.174496530713938, 3.3007783801304598, -5.953147093667557, 2.797952313862087, 9.664056285311155, -2.7494012735449065, 6.372884077183656, -7.902548593436127, -2.9302123942795033, -9.884635114391694, 5.167855728327728, -7.959092653806903, 2.1825117856806227, -7.784977325426592, -7.44030988418918, 5.914472522932705, 7.142836947674031, -1.3113246797485942, -8.30622167876193, 1.1142213040753788, -8.50365254574391, 5.327321607195227, 8.697086651053745, -5.413000100722085, -2.9936186446352213, -1.0044851222981457, -8.908487446653762, 8.560221292087153, 8.330451734853291, 6.731978452345629, 1.7021544705737224, -8.441939106728679, -0.08868399870858923, -2.904869808519801, 8.511961171194368, 4.683666407155725, 7.552361464924559, 0.27015161505802077, 6.882474834756028, -3.102999600715872, -6.593655168234765, 8.904968700822359, 8.098326164069, -0.7888246315418073, 2.418683245126596, -4.449915095102752, -7.148654386882924, 5.803288707789768, 3.425041354900525, 3.6679277472048, -5.879669042555169, -3.6333960431866608, -6.184860825923957, -4.657642352701821, -2.788782476273224, 8.260266496838192, 0.2734147119919399, -3.7685042741178076, -8.468544465640447, -3.823687127591522, -6.459124951521984, -8.848835381725044, -3.2928139847008957, -8.46041490512645, -9.48593247914134, 3.323034281108473, -3.838683783439862, -2.123532658480176, 9.360148350989007, 2.41443272396036, 9.775246947921918, -4.812945931098276, 6.017051259613364]
BIASES_LIST = [-6.217365211209936, -8.119318231520378, 4.348623488682664, 9.098723442373696, -8.46673025082177, 1.3787115127671594, -4.730488912924873, -7.551815309230776, -3.7951853614127877, -6.9823819379429946, -3.0825559834557925, -8.977411489608045, 4.173045691964148, -0.12027623266557086, -0.4491452774514837, -4.9452336246689255, -1.2429488601889709, 4.777791792101835, 5.734681690333996, -3.0341830848008673, 7.733136949414188, -4.450342108485912, -1.4338381617216793, -6.606818337630676, 8.772711522619343, 3.455941328520977, 5.150015552516793, -0.38701345917426977]
SHAPE = [27, 16, 10, 2]
>>>>>>> 7d31a6a87a720dfe4ed79aa94e6595884cb1bc5d

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

def list_to_weights(lis, shape=[27, 16, 10, 2]):
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

def list_to_biases(lis, shape=[27, 16, 10, 2]):
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

    if best_move == 1:
        if board[3][2] == 0:
            move_forward()
        return
    if board[3][1] == -1:
        capture(row + forward, col - 1)
        return
    if board[3][3] == -1:
        capture(row + forward, col + 1)
        return
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

