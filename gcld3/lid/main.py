

from lid import GCLD3BasedLID

script1 = "དཔལ་ལྡན་སྲིད་སྐྱོང་མཆོག་གིས་ཨོསྟྲེ་ལི་ཡཱའི་གྲོས་ཚོགས་གོང་མའི་འཐུས་མི་ལྕམ་སྐུ་ཀིམ་བྷར་ལེ་ཀིཊ་ཆིན་མཆོག་སྐུ་ཚེའི་འཕེན་པ་རྫོགས་པར་ཐུགས་གསོ་གནང་བ།"
script2 = "این سومین نشست وزیران کشورهای منطقه است که در مورد بحران افغانستان طی کمتر از هفت ماه"
obj = GCLD3BasedLID()
if obj.detect(script1) == True:
    
    print("\nScript1")
    print(obj.get_confidence_score())
    print(obj.get_lang_code_iso639())
    print(obj.get_lang_name())
    

if obj.detect(script2) == True:
    
    print("\nScript1")
    print(obj.get_confidence_score())
    print(obj.get_lang_code_iso639())
    print(obj.get_lang_name())
