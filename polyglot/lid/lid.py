from polyglot.detect import Detector
from polyglot.utils import pretty_list

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

    def supported_langs(self):
        pass 

class PolyGlotBasedLID(LID):

    def __init__(self):
        super().__init__()
        self.input = None 

    def detect(self,input) -> bool:
        self.input = input
        try:
            detector = Detector(self.input)
            str_lst = str(detector.language).split(" ")
            if str_lst:
                str_lst = [st for st in str_lst if st != ""]
                self.lang = str_lst[3]
                self.score = float(str_lst[5])/100
                self.lang_name = str_lst[1]
                return(True)
        except Exception as ex:
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(ex).__name__, ex.args)
            print(message)
            self.status = False

        return(False)
    
    def supported_langs(self):
        print(pretty_list(Detector.supported_languages()))
