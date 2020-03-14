import pandas as pd
from gensim.models import word2vec
from gensim.models.fasttext import FastText

labeledData = pd.read_csv("../../corpus/Lankadeepa/comments_tagged_remove_all_punc_keep_question.csv", \
                            header=0, delimiter=";", quoting=3)

num_features = 300 # Word vector dimensionality1
context = 10  # Context window size
word2vec_model = "../../word_embedding/wordvec/from_lankadeepa/comments_tagged_" \
                 + str(num_features) + "_" + str(context)
fasttext_model = "../../word_embedding/fasttext/from_lankadeepa/comments_tagged_" \
                 + str(num_features) + "_" + str(context)



# split a comment into sentences of words
def to_separate_sentences(comment):
    sentences = []
    raw_sentences = str(comment).split(".")
    for raw_sentence in raw_sentences:
        if len(raw_sentence) > 2:
            sentences.append(raw_sentence.split())
    return sentences


def generate_word_embedding():
    comments = []
    for comment in labeledData["comment"]:
        comments += to_separate_sentences(comment)

    print("# of comments taken for building the model: " + str(len(comments)))

    downsampling = 1e-3  # Downsample setting for frequent words
    min_word_count = 1  # Minimum word count - if not occurred this much remove
    num_workers = 4  # Number of threads to run in parallel

    # generate word2vec
    # model = word2vec.Word2Vec(comments, workers=num_workers, size=num_features, min_count=min_word_count,
    #                           window=context, sample=downsampling, sg=1)

    # generate fasttext
    model = FastText(comments, workers=num_workers, size=num_features, min_count=min_word_count,
                              window=context, sample=downsampling, sg=1, iter=50)

    model.init_sims(replace=True)  # If you don't plan to train the model any further
    # model.save(word2vec_model)
    model.save(fasttext_model)

    check_model_qulity(model, 'නැහැ')
    check_model_qulity(model, 'හොඳයි')
    check_model_qulity(model, 'ඔබට')
    return

def check_model_qulity(model, word):
    for s in model.most_similar(word):
        print(s[0])
    # for s in model.wv.most_similar(positive=['ගෑණි', 'ඔබතුමන්ට'], negative=['මිනිහා']):
    #     print(s[0])


def main():
    generate_word_embedding()
    return

# main()

model = word2vec.Word2Vec.load('../../word_embedding/wordvec/from_lankadeepa/comments_tagged_300_10')
check_model_qulity(model, 'නැහැ')