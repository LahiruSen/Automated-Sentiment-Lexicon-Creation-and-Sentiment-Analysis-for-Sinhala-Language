import pandas as pd
import numpy as np
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences

class inputHandler:
    def __init__(self,lankadeepa_data_path,gossip_lanka_data_path):
        self.lankadeepa = lankadeepa_data_path
        self.gossipLanka = gossip_lanka_data_path
        self.all_data = None
        self.labels = None
        self.comments = None
        self.vocab_size = None

    def load_data(self):

        lankadeepa_data = pd.read_csv(self.lankadeepa)[:9059]
        gossipLanka_data = pd.read_csv(self.gossipLanka).drop(columns=['Unnamed: 3'])

        self.all_data = pd.concat([lankadeepa_data, gossipLanka_data])

    def preprocesss_data(self):
        comments = self.all_data['comment']
        labels = self.all_data['label']

        comment_texts = []

        for comment in comments:
            lines = []
            try:
                words = comment.split()
                lines += words
            except:
                continue
            comment_texts.append(lines)

        t = Tokenizer()
        t.fit_on_texts(comment_texts)
        self.vocab_size = len(t.word_index) + 1

        encoded_docs = t.texts_to_sequences(comment_texts)

        max_length = len(max(encoded_docs, key=len))
        padded_docs = pad_sequences(encoded_docs, maxlen=max_length)

        comment_labels = np.array(labels)
        padded_docs = np.array(padded_docs)

        comment_labels = pd.get_dummies(comment_labels).values
        print('Shape of label tensor:', comment_labels.shape)

        self.comments = padded_docs
        self.labels = comment_labels

