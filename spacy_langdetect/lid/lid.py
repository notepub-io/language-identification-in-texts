import spacy
from spacy.language import Language
from spacy_langdetect import LanguageDetector
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

class SpacyLangdetectBasedLID(LID):

    def __init__(self):
        super().__init__()

        @Language.factory("language_detector")
        def get_lang_detector(nlp, name):
            return LanguageDetector()

        self.identifier = spacy.load("en_core_web_sm")
        self.identifier.add_pipe('language_detector', last=True)

    def detect(self,input):

        try:
            results=self.identifier(input)._.language
            print(results)
            if "language" in results:
                self.lang = results["language"]
                self.score = results["score"]
                self.lang_name = languages.get(alpha_2=self.lang).name
                return(True)
            else:
                return(False)

        except Exception as ex:
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(ex).__name__, ex.args)
            print(message)
            return(False)
        
   