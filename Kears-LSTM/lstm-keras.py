from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.models import Sequential
from keras.layers import Dense, Flatten, LSTM, Conv1D, MaxPooling1D, Dropout, Activation
from keras.layers.embeddings import Embedding
from keras import utils
import plotly.offline as py
import plotly.graph_objs as go
import nltk
import string
import numpy as np
import pandas as pd
from nltk.corpus import stopwords
from sklearn.manifold import TSNE

'''read corpus'''
_corpus='train.txt'
_sep='\t'

df = pd.read_csv(_corpus, sep = _sep, names = ['labels', 'text'], error_bad_lines=False)
df= df.dropna()
df = df.sample(frac=1).reset_index(drop=True)

print("\n")
print(df.describe())
print("\n")
print(df.head(10))
print("\n")
print(data.shape)
print("\n")



'''convert sentences to sequences'''
vocabulary_size = 200000
tokenizer = Tokenizer(num_words= vocabulary_size)
tokenizer.fit_on_texts(df['text'])

sequences = tokenizer.texts_to_sequences(df['text'])


'''pad sequences'''
sum=0
for seq in sequences:
    sum += len (seq)
    
avg = int (sum / len(sequences))
print("average length of sentences: "+str(avg)) 

data = pad_sequences(sequences, maxlen= avg)


'''one-hot encoding'''
lbl=set()
for line in open(_corpus,"r"):
    line=line.strip().split()
    lbl.add(line[0])

classes=len(lbl)

labels = df['labels']
one_hot_labels = utils.to_categorical(labels, num_classes=classes)


'''model fitting'''
model_lstm = Sequential()
model_lstm.add(Embedding(vocabulary_size, 300, input_length=avg))
model_lstm.add(LSTM(100, dropout=0.2, recurrent_dropout=0.2))
model_lstm.add(Dense(classes, activation='softmax'))
model_lstm.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
 
history = model_lstm.fit(data, one_hot_labels, validation_split=0.1, epochs=3)

print("\n***History***")

print(history.history) 


'''Evaluation'''

print("\n***Evaluating***")

_corpus="validate.txt"
_sep="\t"
df2 = pd.read_csv(_corpus, sep = _sep, names = ['labels', 'text'], error_bad_lines=False)

vocabulary_size = 200000
tokenizer = Tokenizer(num_words= vocabulary_size)
tokenizer.fit_on_texts(df['text'])

sequences = tokenizer.texts_to_sequences(df2['text'])
x_test = pad_sequences(sequences, maxlen= avg)

labels = df2['labels']
y_test = utils.to_categorical(labels, num_classes=classes)

score = model_lstm.evaluate(x_test, y_test)

print('Test score:', score[0])
print('Test accuracy:', score[1])
