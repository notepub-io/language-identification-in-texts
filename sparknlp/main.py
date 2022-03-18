import sparknlp
from sparknlp.pretrained import PretrainedPipeline

#create or get Spark Session

spark = sparknlp.start()

sparknlp.version()
spark.version

#download, load and annotate a text by pre-trained pipeline

pipeline = PretrainedPipeline("detect_language_375", lang = "xx")

print(pipeline.annotate("French author who helped pioneer the science-fiction genre."))

