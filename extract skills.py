import pandas as pd
from pyspark.sql.types import *
import pyspark
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.ml.feature import Tokenizer, StopWordsRemover
from pyspark.sql.types import StringType
# from langdetect import detect, DetectorFactory
# import tensorflow_hub as hub
from sklearn.cluster import DBSCAN
# import google.generativeai as genai
import seaborn as sns
import matplotlib.pyplot as plt
import torch
from scipy.cluster.hierarchy import linkage, fcluster, dendrogram
# from sentence_transformers import SentenceTransformer
import tensorflow
import torch
from transformers import AutoTokenizer, AutoModelForTokenClassification


spark = SparkSession.builder.getOrCreate()
tokenizer = AutoTokenizer.from_pretrained("jjzha/jobbert_skill_extraction")
model = AutoModelForTokenClassification.from_pretrained("jjzha/jobbert_skill_extraction")
def chunk_text(text, max_length=512):
    tokens = tokenizer.tokenize(text)
    chunks = []
    for i in range(0, len(tokens), max_length - 2):  # Reserve space for [CLS] and [SEP]
        chunk = tokens[i:i + max_length - 2]
        chunks.append(tokenizer.convert_tokens_to_string(chunk))
    return chunks





def extract_skills(description):
    description = description.replace("\n", " ")
    description = description.replace("\r", " ")
    description = description.replace("\t", " ")
    chunks = chunk_text(description)
    skills = []
    for chunk in chunks:
        inputs = tokenizer(chunk, return_tensors="pt", truncation=True, padding=True, max_length=512)
        with torch.no_grad():
            outputs = model(**inputs)
        logits = outputs.logits
        predicted_class_ids = torch.argmax(logits, dim=2)
        tokens = tokenizer.convert_ids_to_tokens(inputs["input_ids"][0])
        predicted_classes = [model.config.id2label[class_id.item()] for class_id in predicted_class_ids[0]]

        skill = ""
        for token, predicted_class in zip(tokens, predicted_classes):
            if "#" not in token:
                if predicted_class == "B":
                    if skill:
                        skills.append(skill.strip())
                    skill = token
                elif predicted_class == "I":
                    skill += f" {token}"
        if skill:
            skills.append(skill.strip())
    return skills

if __name__ == "__main__":
    extract_skills_udf = udf(extract_skills, ArrayType(StringType()))
    pd_df = pd.read_csv("../JOINED_DATA.csv")
    df_with_clusters_named = spark.createDataFrame(pd_df)
    result_df = df_with_clusters_named.withColumn("skills1", extract_skills_udf("Description"))
