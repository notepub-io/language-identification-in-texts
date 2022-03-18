from tkinter import E
import sparknlp
from sparknlp.pretrained import PretrainedPipeline
from sparknlp.base import *
from sparknlp.annotator import *

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

class SparkNLPBasedLID(LID):

    def __init__(self,model_identity,approach="pretrained_pipeline", mode="online",enable_gpu=False, expected_lang="xx"):
        
        super().__init__()

        self.status = False

        self.model = None

        self.model_identity = model_identity

        self.spark = None

        self.approach = approach
        # pretrained_pipeline, pretrained_models

        try:

            self.status = True    
            self.spark = sparknlp.start()
            print("\nVersion",sparknlp.version())

            if self.approach == "pretrained_pipeline":
                
                if mode == "offline":
                    self.model = PretrainedPipeline(self.model_identity,expected_lang,disk_location=self.model_identity)
                else:
                    self.model = PretrainedPipeline(self.model_identity,expected_lang)

            elif self.approach == "pretrained_model":
                
                if mode == "offline":
                    self.model = LanguageDetectorDL.pretrained(self.model_identity,remote_loc=self.model_identity)
                else:
                    self.model = LanguageDetectorDL.pretrained(self.model_identity)

            else:
                self.status = False 

        except Exception as ex:
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(ex).__name__, ex.args)
            print(message)
            self.status = False

    def detect(self,input) -> bool:
        
        if self.status == False:
            return(self.status)

        if self.approach == "pretrained_pipeline":
            return(self.__detect_pipeline(input))
        elif self.approach == "pretrained_model":
            return(self.__detect_model(input))
        else:
            return(False)

    def __detect_pipeline(self,input) -> bool:

        self.input = input
        try:
            if self.status:
            
                result = self.model.annotate(self.input)
                if "language" in result:
                    lang_list = result["language"]
                    print(lang_list)
                    if len(lang_list) == 1:
                        self.lang = lang_list[0]
                    self.score =0.99
                    self.lang_name = languages.get(alpha_2=self.lang).name
                    return(True)

        except Exception as ex:
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(ex).__name__, ex.args)
            print(message)
            return(False)
        
        return(False)

    def __detect_model(self,input) -> bool:

        if self.status:
               
            documentAssembler = DocumentAssembler()\
            .setInputCol("text")\
            .setOutputCol("document")
            language_detector = self.model\
            .setInputCols(["document"])\
            .setOutputCol("lang")\
            .setThreshold(0.8)\
            .setCoalesceSentences(True)

            languagePipeline = Pipeline(stages=[
            documentAssembler, 
            language_detector
            ])

            languagePipeline = Pipeline(stages=[documentAssembler, language_detector])
            light_pipeline = LightPipeline(languagePipeline.fit(self.spark.createDataFrame([['']]).toDF("text")))
            #result = light_pipeline.fullAnnotate(input)
            result = light_pipeline.annotate(input)
            if "lang" in result:
                lang_list = result["lang"]
                print(lang_list)
                if len(lang_list) == 1:
                    self.lang = lang_list[0]
                self.score =0.99
                self.lang_name = languages.get(alpha_2=self.lang).name
                return(True)

        return(False)