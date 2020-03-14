import pandas as pd
from gensim.models.fasttext import FastText

unlabeledData = pd.read_csv("../../corpus/Lankadeepa/comments_tagged_remove_all_punc_keep_question.csv", header=0, delimiter=";", quoting=3)