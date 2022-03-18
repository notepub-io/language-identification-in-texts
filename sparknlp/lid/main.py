from lid import SparkNLPBasedLID

#pretrained_pipeline='/home/mmaurya/Development/lid/sparknlp/lids/models/detect_language_375_xx_2.7.0_2.4_1607185980306'
pretrained_pipeline='detect_language_375'

#pretrained_model='/home/mmaurya/Development/lid/sparknlp/lids/models/ld_wiki_tatoeba_cnn_375_xx_2.7.0_2.4_1607184873730'
pretrained_model="ld_wiki_tatoeba_cnn_375"

script1=" My name is manoj را انتقاد مى کند و مى گويد که اعلام نتایج نهایی چهار حوزه انتخاباتی در روز گشايش شورا پرسش برانگيز است.ده بود و در روز افتتاح (ششم ثور) نتایج نهایی ولایات میدان وردک، بغلان، کندز و حوزه My name is manoj کوچی هاى اين جرگه را نيز اعلام کر"
script2 = "My name is manoj"
script3 = "དཔལ་ལྡན་སྲིད་སྐྱོང་མཆོག་གིས་ཨོསྟྲེ་ལི་ཡཱའི་གྲོས་ཚོགས་གོང་མའི་འཐུས་མི་ལྕམ་སྐུ་ཀིམ་བྷར་ལེ་ཀིཊ་ཆིན་མཆོག་སྐུ་ཚེའི་འཕེན་པ་རྫོགས་པར་ཐུགས་གསོ་གནང་བ།"
obj = SparkNLPBasedLID(model_identity=pretrained_model,mode="online",approach="pretrained_model")
#obj = SparkNLPBasedLID(model_identity=pretrained_model,mode="online",approach="pretrained_model")


if obj.detect1(script1) == True:
    print("LID: SparkNLPBasedLID")
    print(obj.get_confidence_score())
    print(obj.get_lang_code_iso639())
    print(obj.get_lang_name())

if obj.detect1(script2) == True:
    print("LID: SparkNLPBasedLID")
    print(obj.get_confidence_score())
    print(obj.get_lang_code_iso639())
    print(obj.get_lang_name())

if obj.detect1(script3) == True:
    print("LID: SparkNLPBasedLID")
    print(obj.get_confidence_score())
    print(obj.get_lang_code_iso639())
    print(obj.get_lang_name())
