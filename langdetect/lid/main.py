from lid import LangDetectBasedLID

script = "དཔལ་ལྡན་སྲིད་སྐྱོང་མཆོག་གིས་ཨོསྟྲེ་ལི་ཡཱའི་གྲོས་ཚོགས་གོང་མའི་འཐུས་མི་ལྕམ་སྐུ་ཀིམ་བྷར་ལེ་ཀིཊ་ཆིན་མཆོག་སྐུ་ཚེའི་འཕེན་པ་རྫོགས་པར་ཐུགས་གསོ་གནང་བ།"
obj = LangDetectBasedLID()
if obj.detect(script) == True:
    
    print(obj.get_confidence_score())
    print(obj.get_lang_code_iso639())
    print(obj.get_lang_name())
    print("\n")

