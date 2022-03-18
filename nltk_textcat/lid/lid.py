from nltk.classify import textcat
from pycountry import languages
from iso639 import languages
from pprint import pprint

class LID():

    def __init__(self):
        self.lang = None 
        self.score = None 
        self.lang_name = None 
        self.iso639 = {} 

    def get_lang_code_iso639(self):
        return(self.lang)
    
    def get_confidence_score(self):
        return(self.score)

    def get_lang_name(self):
        return(self.lang_name)

    def get_iso639(self):
        """
        {'inverted': 'Hindi',
        'macro': '',
        'name': 'Hindi',
        'names': [],
        'part1': 'hi',
        'part2b': 'hin',
        'part2t': 'hin',
        'part3': 'hin',
        'part5': ''}
        """
        return(self.iso639)

    def detect(self,input) -> bool:
        pass


class NLTKTextCatBasedLID(LID):

    def __init__(self):
        super().__init__()
        self.input = None 
        self.cls = textcat.TextCat()
        
    def detect(self,input) -> bool:
        self.input = input
        try:
            lang_iso693a3 = self.cls.guess_language(self.input)
            iso369obj = languages.get(part3=str(lang_iso693a3))
            self.lang = iso369obj.alpha2
            self.score = 0.99
            self.lang_name = iso369obj.name
            self.iso639 = iso369obj

            return(True)
        except Exception as ex:
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(ex).__name__, ex.args)
            print(message)
            return(False)

        return(False)