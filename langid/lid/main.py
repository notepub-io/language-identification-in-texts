from lid import LangIdBasedLID

script1=" My name is manoj را انتقاد مى کند و مى گويد که اعلام نتایج نهایی چهار حوزه انتخاباتی در روز گشايش شورا پرسش برانگيز است.ده بود و در روز افتتاح (ششم ثور) نتایج نهایی ولایات میدان وردک، بغلان، کندز و حوزه My name is manoj کوچی هاى اين جرگه را نيز اعلام کر"
script2 = "My name is manoj kumar"
script3 = "དཔལ་ལྡན་སྲིད་སྐྱོང་མཆོག་གིས་ཨོསྟྲེ་ལི་ཡཱའི་གྲོས་ཚོགས་གོང་མའི་འཐུས་མི་ལྕམ་སྐུ་ཀིམ་བྷར་ལེ་ཀིཊ་ཆིན་མཆོག་སྐུ་ཚེའི་འཕེན་པ་རྫོགས་པར་ཐུགས་གསོ་གནང་བ།"
obj = LangIdBasedLID()
if obj.detect(script1) == True:
    
    print(obj.get_confidence_score())
    print(obj.get_lang_code_iso639())
    print(obj.get_lang_name())
    print("\n")

if obj.detect(script2) == True:
    
    print(obj.get_confidence_score())
    print(obj.get_lang_code_iso639())
    print(obj.get_lang_name())
    print("\n")

if obj.detect(script3) == True:
    
    print(obj.get_confidence_score())
    print(obj.get_lang_code_iso639())
    print(obj.get_lang_name())
    print("\n")
