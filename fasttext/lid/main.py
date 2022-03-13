from lid import FastTextBasedLID

model="./models/lid.176.bin"
script = "This note series is designed to provide the insides of using open-source language identifiers to predict the natural language of a given input text."

obj = FastTextBasedLID(model)
if obj.detect(script) == True:
    print(obj.get_confidence_score())
    print(obj.get_lang_code_iso639())
    print(obj.get_lang_name())

