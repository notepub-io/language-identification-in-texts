import fasttext
from pycountry import languages

class LID():

    def __init__(self):
        self.lang = None 
        self.score = None 
        self.lang_name = None 

    def get_lang_code_iso639(self):
        return(self.lang)
    
    def get_confidence_score(self):
        return(self.score)

    def get_lang_name(self):
        return(self.lang_name)

    def detect(self,input) -> bool:
        pass

class FastTextBasedLID(LID):

    def __init__(self,pretrained_model_path):
        
        super().__init__()
        fasttext.FastText.eprint = lambda x: None

        self.pretrained_model = pretrained_model_path
        try:
            self.model = fasttext.load_model(self.pretrained_model)

        except Exception as ex:
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(ex).__name__, ex.args)
            print(message)
            self.model = None

    def detect(self,input) -> bool:

        self.input = input
        try:
            if self.model:
                predictions = self.model.predict(self.input,k=1)
                if predictions:
                    self.lang = predictions[0][0].split("__label__")[1]
                    self.score =predictions[1][0]
                    self.lang_name = languages.get(alpha_2=self.lang).name
                    return(True)
        except Exception as ex:
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(ex).__name__, ex.args)
            print(message)
            return(False)
        
        return(False)
