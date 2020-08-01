from gensim.models.keyedvectors import KeyedVectors
from gensim.models.fasttext import FastText
from gensim.models import word2vec

import numpy as np
from numpy import zeros
import pickle

class embeddingConfig(object):
    embedding_type = 'fasttext'
    embedding_size = 300
    data_path = None
    keyedvectors_path = None
    embedding_matrix_path = None
    vocab_size = None


class wordEmbeddingHandler:
    def __init__(self, embeddingConfig):
        self.embedding_matrix = None
        self.config = embeddingConfig

    def generate_embedding_matrix(self):
        if (self.config.embedding_type == 'fasttext'):
            word_embedding_model = FastText.load(self.config.data_path)
        else:
            word_embedding_model = word2vec.Word2Vec.load(self.config.data_path)

        word_vectors = word_embedding_model.wv
        word_vectors.save(self.config.keydvectors_path)
        word_vectors = KeyedVectors.load(self.config.keyedvectors_path, mmap='r')

        embeddings_index = dict()
        for word, vocab_obj in word_vectors.vocab.items():
            embeddings_index[word] = word_vectors[word]

        # create a weight matrix for words in training docs
        embedding_matrix = zeros((self.config.vocab_size, self.config.embedding_size))
        for word, i in t.word_index.items():
            embedding_vector = embeddings_index.get(word)
            if embedding_vector is not None:
                embedding_matrix[i] = embedding_vector

        pickle.dump(embedding_matrix, open(self.config.embedding_matrix_path, 'wb'))
        self.embedding_matrix = embedding_matrix

        return embedding_matrix

    def load_embedding_matrix(self):
        f = open(self.config.embedding_matrix_path, 'rb')

        return np.array(pickle.load(f))
