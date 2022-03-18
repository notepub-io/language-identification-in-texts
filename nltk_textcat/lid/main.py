from lid import NLTKTextCatBasedLID

script=" را انتقاد مى کند و مى گويد که اعلام نتایج نهایی چهار حوزه انتخاباتی در روز گشايش شورا پرسش برانگيز است.ده بود و در روز افتتاح (ششم ثور) نتایج نهایی ولایات میدان وردک، بغلان، کندز و حوزه کوچی هاى اين جرگه را نيز اعلام کر"
obj = NLTKTextCatBasedLID()
if obj.detect(script) == True:
    print(obj.get_confidence_score())
    print(obj.get_lang_code_iso639())
    print(obj.get_lang_name())