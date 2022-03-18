
from langid import classify
from langid.langid import LanguageIdentifier, model

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

class LangIdBasedLID(LID):

    def __init__(self):
        super().__init__()
        self.identifier = LanguageIdentifier.from_modelstring(model, norm_probs=True)
        
    def detect(self,input):

        try:

            results=self.identifier.classify(input)
            if len(results) > 0:
                self.lang = results[0]
                self.score = results[1]
                self.lang_name = languages.get(alpha_2=self.lang).name
                return(True)
            else:
                return(False)

        except Exception as ex:
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(ex).__name__, ex.args)
            print(message)
            return(False)
        
   