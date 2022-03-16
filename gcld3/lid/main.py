

from lid import GCLD3BasedLID

obj = GCLD3BasedLID()
    
script = "این سومین نشست وزیران کشورهای منطقه است که در مورد بحران افغانستان طی کمتر از هفت ماه"
if obj.detect(script) == True:
    
    print(obj.get_confidence_score())
    print(obj.get_lang_code_iso639())
    print(obj.get_lang_name())
