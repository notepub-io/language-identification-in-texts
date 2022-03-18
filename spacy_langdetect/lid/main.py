from lid import SpacyLangdetectBasedLID

script = "সদ্য সমাপ্ত পৌৰ নিৰ্বাচনত নিৰঙ্কুশ সংখ্যা গৰিষ্ঠতা অৰ্জনৰ পৰৱৰ্তী সময়ত এই বিষয়টোৱে ঢকুৱাখনাৰ শাসক দলৰ মজিয়াত সৰ্বাধিক ভাবে চৰ্চিত আৰু আলোচিত বিষয় হিচাবে ধৰা দিছে"

obj = SpacyLangdetectBasedLID()
if obj.detect(script) == True:
    
    print(obj.get_confidence_score())
    print(obj.get_lang_code_iso639())
    print(obj.get_lang_name())