from sinling import SinhalaTokenizer,word_splitter, preprocess, word_joiner
import pandas as pd
import pickle
import re

#lankadeepa data
lankadeepa_data_path = '../../corpus/new/preprocess_from_isuru/lankadeepa_tagged_comments.csv'
lankadeepa_save_path = '../../corpus/new/preprocess_from_isuru/lankadeepa_tagged_comments'
lankadeepa_data = pd.read_csv(lankadeepa_data_path)[:9059]

#gossiplanka data
gossiplanka_data_path = '../../corpus/new/preprocess_from_unicode_values/gossip_lanka_tagged_comments.csv'
gossiplanka_save_path = '../../corpus/new/preprocess_from_isuru/gossip_lanka_tagged_comments'
gossiplanka_data = pd.read_csv(gossiplanka_data_path)


#combined
all_save_path = '../../corpus/new/all_tagged_comments'


tokenizer = SinhalaTokenizer()

def tokenize_tagged_comments(data):
    tokenized_comments = []
    labels = []
    non_string_comments = 0
    for index, row in data.iterrows():
        comment = row['comment']
        label = row['label']
        if isinstance(comment, str):
            comment = re.sub(r'\.+', ".", comment) # replace multiple fulstop with single fulstop
            comment = comment.replace('\u200d','').replace('\u200b','')  # these characters are not filtered in SinhalaTokenizer
            tokens = tokenizer.tokenize(comment)
            # print(tokens)
            tokenized_comments.append(tokens)
            labels.append(label)
        else:
            non_string_comments += 1

    print("non string comments found : ", non_string_comments)
    print("length of tokenized comments : ",len(tokenized_comments))
    return tokenized_comments,labels

lankadeepa_comments_tokenized, lankadeepa_labels = tokenize_tagged_comments(lankadeepa_data)
gossip_lanka_comments_tokenized , gossiplanka_labels = tokenize_tagged_comments(gossiplanka_data)

lankadeepa_comments_tokenized.extend(gossip_lanka_comments_tokenized)
lankadeepa_labels.extend(gossiplanka_labels)

dict = {
    "comment" : lankadeepa_comments_tokenized,
    "label" : lankadeepa_labels
}

print(dict['comment'][:10])
print(dict['label'][:10])


with open(all_save_path, 'wb') as fp:
    pickle.dump(dict, fp)

with open (all_save_path, 'rb') as fp:
    dict = pickle.load(fp)
    print(dict['comment'][:10])
    print(dict['label'][:10])


