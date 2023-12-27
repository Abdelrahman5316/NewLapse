import pandas as pd

df = pd.read_excel('output.xlsx')


#Libraries required for scrapping
import requests
import bs4


##Deep learning libraries and APIs
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

df2=pd.read_csv('good_badnews_NewsArticles.csv')


df2=df2.drop('URL',axis=1)
df2=df2.rename(columns={'Title':'text'})

df2['text']=df2['text'].astype(str)

#check the data info
df2.info()


df2=df2.rename(columns={'Majority Score':'label'})
df2['label'] = df2['label'].astype(str)
df2[0:3]

df2['label']=df2['label'].replace('3','0')
print(df2)

df2=df2[df2['label']!='2']
len(df2)

frames=[df2,df]
df3=pd.concat(frames,ignore_index=True)

data = df3.copy()

##store headlines and labels in respective lists
#text = list(data['text'])
#labels = list(data['label'])
text=np.asarray(df3['text'])
labels=np.asarray(df3['label']).astype(np.float32)
#Shuffle
#indices=np.arange(df3.shape[0])
#np.random.shuffle(indices)
#text=text[indices]
#labels=labels[indices]
##sentences
training_text = text[0:232116]
testing_text = text[232116:]

##labels
training_labels = labels[0:232116]
testing_labels = labels[232116:]

#preprocess
tokenizer = Tokenizer(num_words=10000, oov_token= "<OOV>")
tokenizer.fit_on_texts(training_text)
word_index = tokenizer.word_index
training_sequences = tokenizer.texts_to_sequences(training_text)
training_padded = pad_sequences(training_sequences, maxlen=153, padding='post', truncating='post')
testing_sequences = tokenizer.texts_to_sequences(testing_text)
testing_padded = pad_sequences(testing_sequences, maxlen=153, padding='post', truncating='post')

# convert lists into numpy arrays to make it work with TensorFlow
training_padded = np.array(training_padded)
training_labels = np.array(training_labels)
testing_padded = np.array(testing_padded)
testing_labels = np.array(testing_labels)

model3 = tf.keras.Sequential([
tf.keras.layers.Embedding(10000, 16, input_length=153),
tf.keras.layers.GlobalAveragePooling1D(),
tf.keras.layers.Dense(24, activation='relu'),
tf.keras.layers.Dropout(0.5),
tf.keras.layers.Dense(24, activation='relu'),
tf.keras.layers.Dropout(0.5),
tf.keras.layers.Dense(1, activation='sigmoid')
])
    ##compile the model
model3.compile(loss='binary_crossentropy',optimizer='adam',metrics=['accuracy'])

model3.summary()
num_epochs = 10
history = model3.fit(training_padded,
                    training_labels,
                    epochs=num_epochs,
                    validation_data=(testing_padded, testing_labels),
                    verbose=2)


print('validation accuracy: ',round(max(history.history['val_accuracy'])*100,2))
print('Trainig accuracy: ',round(max(history.history['accuracy'])*100),2)
print()

model3.save('trained_model')



