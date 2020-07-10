import collections
import pickle
import gensim
from gensim.models.keyedvectors import KeyedVectors
import numpy as np
import re
import random
import numpy as np
import sys
import os
import pandas as pd
from sklearn.model_selection import train_test_split
from collections.abc import Iterable
from gensim.models import Word2Vec
from gensim.test.utils import get_tmpfile
from gensim.models import KeyedVectors
from gensim.models import word2vec

def make_dir(path):
    if not os.path.exists(path):
        os.mkdir(path)
        print('made directory %s' % path)
make_dir("parsed_data")

def insert_word(dataset, all_words):
    for lines in dataset:
      if isinstance(lines, Iterable):
        for l in lines:
          if isinstance(l, Iterable):
            all_words+=l


def convert_words_to_number(dataset_text, dataset_label, common_word):
    transformed_text = []
    transformed_label = []
    for lines, labels in zip(dataset_text, dataset_label):
        new_x = []
        new_label = []
        for l, label in zip(lines, labels):
            words = [common_word[w] if w in common_word else 1 for w in l]

            new_x += [words]
            new_label += [label]

        transformed_text += [new_x]
        transformed_label += [new_label]
    return transformed_text, transformed_label


def text_preprocessing(train_data, test_data):
    train_data_texts = train_data['comment']
    train_data_labels = train_data['label']
    test_data_texts = test_data['comment']
    test_data_labels = test_data['label']

    comment_texts = []
    comment_labels = []

    train_text = []
    test_text = []
    train_labels = []
    test_labels = []

    for label in train_data_labels:
        if label == "POSITIVE":
            train_labels.append(1)
        else:
            train_labels.append(0)
    comment_labels.append(train_labels)

    for label in test_data_labels:
        if label == "POSITIVE":
            test_labels.append(1)
        else:
            test_labels.append(0)
    comment_labels.append(test_labels)

    for comment in train_data_texts:
        lines = []
        try:
            words = comment.split()
            lines += words
        except:
            continue
        train_text.append(lines)
    comment_texts.append(train_text)

    for comment in test_data_texts:
        lines = []
        try:
            words = comment.split()
            lines += words
        except:
            continue
        test_text.append(lines)
    comment_texts.append(test_text)

    return comment_texts, comment_labels

