from lid import LangIdBasedLID

script = "It is designed in such a way because it may be entirely possible that the detect function input parameters and logics may be different for different language identification libraries. "
obj = LangIdBasedLID()
if obj.detect(script) == True:
    
    print(obj.get_confidence_score())
    print(obj.get_lang_code_iso639())
    print(obj.get_lang_name())
