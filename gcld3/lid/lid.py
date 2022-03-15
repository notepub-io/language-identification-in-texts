
from gcld3 import NNetLanguageIdentifier
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

class GCLD3BasedLID(LID):

    def __init__(self,input_min_limit=0,input_max_limit=20480):
        super().__init__()
        self.max_limit = input_max_limit
        self.min_limit = input_min_limit
        self.max_top_langs = 2
        self.detector = NNetLanguageIdentifier(min_num_bytes=self.min_limit, max_num_bytes=self.max_limit)

    def detect(self,input):
        return(self.__ndetect(input))

    def __detect(self,input):

        try:
            
            results=self.detector.FindLanguage(input)
            self.lang = results.language
            self.score = results.probability
            self.lang_name = languages.get(alpha_2=self.lang).name
            return(True)
            

        except Exception as ex:
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(ex).__name__, ex.args)
            print(message)
            return(False)
    
    def __ndetect(self,input):

        top_result = None

        try:
            
            results=self.detector.FindTopNMostFreqLangs(text=input,num_langs=self.max_top_langs)
            
            for i in results:

                if i.is_reliable == True:

                    if top_result == None:
                        top_result = i
                    else:
                        if top_result.probability < i.probability:
                            top_result = i

            if top_result != None:
                self.lang = top_result.language
                self.score = top_result.probability
                self.lang_name = languages.get(alpha_2=self.lang).name    
                return(True)
            else:
                return(False)
            
        except Exception as ex:
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(ex).__name__, ex.args)
            print(message)
            return(False)