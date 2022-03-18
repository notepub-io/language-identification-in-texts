from lid import SparkNLPBasedLID

script = "དཔལ་ལྡན་སྲིད་སྐྱོང་མཆོག་གིས་ཨོསྟྲེ་ལི་ཡཱའི་གྲོས་ཚོགས་གོང་མའི་འཐུས་མི་ལྕམ་སྐུ་ཀིམ་བྷར་ལེ་ཀིཊ་ཆིན་མཆོག་སྐུ་ཚེའི་འཕེན་པ་རྫོགས་པར་ཐུགས་གསོ་གནང་བ།"

# Pretrained Model Online
pretrained_model_online="ld_wiki_tatoeba_cnn_375"
obj = SparkNLPBasedLID(model_identity=pretrained_model_online,mode="online",approach="pretrained_model")
if obj.detect(script) == True:
    print(obj.get_confidence_score())
    print(obj.get_lang_code_iso639())
    print(obj.get_lang_name())

# Pretrained Pipeline Online
pretrained_pipeline_online='detect_language_375'
obj = SparkNLPBasedLID(model_identity=pretrained_pipeline_online,mode="online",approach="pretrained_pipeline")
if obj.detect(script) == True:
    print(obj.get_confidence_score())
    print(obj.get_lang_code_iso639())
    print(obj.get_lang_name())

# Pretrained Model Offline
pretrained_model_offline='<Location>/lid/models/ld_wiki_tatoeba_cnn_375_xx_2.7.0_2.4_1607184873730'
obj = SparkNLPBasedLID(model_identity=pretrained_model_offline,mode="offline",approach="pretrained_model")
if obj.detect(script) == True:
    print(obj.get_confidence_score())
    print(obj.get_lang_code_iso639())
    print(obj.get_lang_name())

# Pretrained Pipeline Offline
pretrained_pipeline_offline='<Location>/lid/models/detect_language_375_xx_2.7.0_2.4_1607185980306'
obj = SparkNLPBasedLID(model_identity=pretrained_pipeline_offline,mode="offline",approach="pretrained_pipeline")
if obj.detect(script) == True:
    print(obj.get_confidence_score())
    print(obj.get_lang_code_iso639())
    print(obj.get_lang_name())

