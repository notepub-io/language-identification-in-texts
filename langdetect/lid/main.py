from lid import LangDetectBasedLID

script = "भगवंत मान ने पंजाब के 17वें मुख्यमंत्री पद की शपथ ली.  पंजाब विधानसभा चुनाव में आम आदमी पार्टी को प्रचंड जीत मिली है. भगवंत मान का शपथ ग्रहण भगत सिंह के गांव खटकर कलां में हो रहा है. बाकी मंत्रियों का शपथग्रहण बाद में होगा. "
obj = LangDetectBasedLID()
if obj.detect(script) == True:
    
    print(obj.get_confidence_score())
    print(obj.get_lang_code_iso639())
    print(obj.get_lang_name())
