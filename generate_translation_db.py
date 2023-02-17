import divatree
from tkinter.filedialog import askopenfilename
pv_db_location = askopenfilename()

new_toml_name = input("Please enter the name of the toml you want to generate. Do not include an extension. ")

with open (pv_db_location, "r", encoding="utf-8") as f:
    raw_pv_db = f.read()

#yes im fucking crazy
""" diva_standard_pvlist = ["pv_001", "pv_002", "pv_005", "pv_007", "pv_008", "pv_009", "pv_010", "pv_012", "pv_013", "pv_014", "pv_016", "pv_028", "pv_030", "pv_031", "pv_032", "pv_037", "pv_038", "pv_039", "pv_040", "pv_041", "pv_042", "pv_043", "pv_044", "pv_045", "pv_046", "pv_047", "pv_049", "pv_050", "pv_051", "pv_052", "pv_053", "pv_054", "pv_055", "pv_056", "pv_057", "pv_058", "pv_059", "pv_060", "pv_061", "pv_062", "pv_065", "pv_066", "pv_068", "pv_079", "pv_081", "pv_082", "pv_083", "pv_085", "pv_086", "pv_087", "pv_088", "pv_089", "pv_090", "pv_091", "pv_092", "pv_093", "pv_094", "pv_095", "pv_096", "pv_097", "pv_102", "pv_103", "pv_104", "pv_201", "pv_202", "pv_212", "pv_218", "pv_219", "pv_220", "pv_221", "pv_222", "pv_224", "pv_225", "pv_227", "pv_231", "pv_232", "pv_234", "pv_238", "pv_239", "pv_240", "pv_241", "pv_242", "pv_243", "pv_244", "pv_246", "pv_247", "pv_248", "pv_249", "pv_250", "pv_251", "pv_253", "pv_254", "pv_255", "pv_257", "pv_259", "pv_260", "pv_261", "pv_262", "pv_263", "pv_266", "pv_268", "pv_269", "pv_270", "pv_271", "pv_272", "pv_275", "pv_433", "pv_435", "pv_600", "pv_601", "pv_602", "pv_603", "pv_604", "pv_605", "pv_607", "pv_609", "pv_610", "pv_611", "pv_612", "pv_613", "pv_614", "pv_615", "pv_616", "pv_617", "pv_619", "pv_620", "pv_621", "pv_622", "pv_623", "pv_624", "pv_625", "pv_626", "pv_627", "pv_628", "pv_629", "pv_630", "pv_631", "pv_637", "pv_638", "pv_639", "pv_640", "pv_641", "pv_642", "pv_710", "pv_722", "pv_723", "pv_724", "pv_725", "pv_726", "pv_727", "pv_728", "pv_729", "pv_730", "pv_731", "pv_732", "pv_733", "pv_734", "pv_736", "pv_737", "pv_738", "pv_739", "pv_740", "pv_832"]
diva_mismatched_lyric_index_pvlist = ["pv_012", "pv_014", "pv_037", "pv_038", "pv_040", "pv_041", "pv_043", "pv_044", "pv_054", "pv_057", "pv_058", "pv_059", "pv_062", "pv_079", "pv_082", "pv_088", "pv_090", "pv_093", "pv_094", "pv_096", "pv_224", "pv_722", "pv_723", "pv_724", "pv_725", "pv_726", "pv_727", "pv_728", "pv_729", "pv_730", "pv_732", "pv_733", "pv_734", "pv_736", "pv_737", "pv_738", "pv_740"]
diva_dlc00_region_pvlist = ["pv_003", "pv_004", "pv_005", "pv_006", "pv_011", "pv_015", "pv_017", "pv_018", "pv_020", "pv_021", "pv_023", "pv_024", "pv_025", "pv_029", "pv_063", "pv_064", "pv_067", "pv_084", "pv_101", "pv_203", "pv_204", "pv_205", "pv_206", "pv_208", "pv_209", "pv_210", "pv_211", "pv_214", "pv_216", "pv_223", "pv_233", "pv_235", "pv_236", "pv_401", "pv_402", "pv_403", "pv_404", "pv_405", "pv_407", "pv_408", "pv_409", "pv_410", "pv_411", "pv_412", "pv_413", "pv_414", "pv_415", "pv_416", "pv_417", "pv_418", "pv_419", "pv_420", "pv_421", "pv_422", "pv_423", "pv_424", "pv_425", "pv_426", "pv_427", "pv_428", "pv_429", "pv_430", "pv_431", "pv_432", "pv_434", "pv_436", "pv_437", "pv_438", "pv_439", "pv_440", "pv_441", "pv_442", "pv_443", "pv_618"]
diva_other_cut_song_pvlist = ["pv_019", "pv_207"]
diva_other_x_song_pack_pvlist = ["pv_800", "pv_801", "pv_802", "pv_803", "pv_804", "pv_805", "pv_806", "pv_807", "pv_808", "pv_809", "pv_810", "pv_811", "pv_812", "pv_813", "pv_814", "pv_815", "pv_816", "pv_817", "pv_818", "pv_819", "pv_820", "pv_821", "pv_822", "pv_823", "pv_824", "pv_825", "pv_826", "pv_827", "pv_828", "pv_829", "pv_830", "pv_831"] """
pv_db = divatree.read(raw_pv_db)


for pv in pv_db:
    if "lyric_en" in pv_db[pv]:
        lyric_en_range = range(len(pv_db[pv]["lyric_en"]))
        lyric_new_trash_range = range(len(pv_db[pv]["lyric_new"]))
        if lyric_en_range == lyric_new_trash_range:
            for lyric in range(len(pv_db[pv]["lyric_en"])):
                if str(pv_db[pv]["lyric_en"][lyric]) == "" or (str(pv_db[pv]["lyric_en"][lyric]) == str(pv_db[pv]["lyric_new"][lyric])):
                    pass
                else:
                    if '"' in str(pv_db[pv]["lyric_en"][lyric]) \
                    or '"' in str(pv_db[pv]["lyric_new"][lyric] \
                    or '\\' in str(pv_db[pv]["lyric_en"][lyric]))\
                    or '/':
                        #print("DEBUG: " + '' + pv + ' ' + "lyric at index {}: ".format(lyric) + '' + str(pv_db[pv]["lyric"][lyric]))
                        create_unique_array_name = pv + ' ' + "lyric_index: {}".format(lyric)
                        cleaned_str_old = str(pv_db[pv]["lyric_en"][lyric])
                        cleaned_str_new = str(pv_db[pv]["lyric_new"][lyric])
                        cleaned_str_old = cleaned_str_old.replace('\\', '\\\"')
                        #cleaned_str_new = cleaned_str_new.replace('/', '/\\')
                        cleaned_str_old = cleaned_str_old.replace('"', '\\"')
                        cleaned_str_new = cleaned_str_new.replace('"', '\\"')
                        base_array = ("""
[[translation]]
#{}
old = "{}"
new = "{}"
""".format(create_unique_array_name, cleaned_str_old, cleaned_str_new))
                        with open("{}.toml".format(new_toml_name), 'a+', encoding="utf-8") as f:
                            f.write(base_array)
                        #print(base_array)
#                     else: 
#                         create_unique_array_name = pv + ' ' + "lyric_index: {}".format(lyric)
#                         cleaned_str_old = str(pv_db[pv]["lyric_en"][lyric])
#                         cleaned_str_new = str(pv_db[pv]["lyric_new"][lyric])
#                         base_array = ("""
# [[translation]]
# #{}
# old = "{}"
# new = "{}"
# """.format(create_unique_array_name, cleaned_str_old, cleaned_str_new))
#                         with open("diva_main_region_pv_db.toml", 'a+', encoding="utf-8") as f:
#                             f.write(base_array)
        if lyric_en_range != lyric_new_trash_range:
            print(pv + " must be manually fixed. The lyric indexes between the two do not match.")
            #create_unique_array_name = tomlarray()
            #pv_lyric_array.add_line("old", cleaned_str_old)
           # pv_lyric_array.add_line("new", cleaned_str_new)
   # print(pv_db[pv]["lyric"][0])