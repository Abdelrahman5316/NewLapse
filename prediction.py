##Deep learning libraries and APIs
import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

#To retrieve the Tokenizer
import pickle
def predict(input):
    #Using the heading to Predict whether it is good or bad news
    new_headline = []
    new_headline.append(input)
    
    # Load the tokenizer
    with open('tokenizer.pickle', 'rb') as handle:
        tokenizer = pickle.load(handle)
    #Load model
    loaded_model = tf.keras.models.load_model('trained_model')
    
    ##prepare the sequences of the sentences in question
    sequences = tokenizer.texts_to_sequences(new_headline)
    padded_seqs = pad_sequences(sequences, maxlen=153, padding='post', truncating='post')
    
    prediction=loaded_model.predict(padded_seqs,verbose=0)


    prediction=round(prediction[0][0])

    if prediction==1:
      return 'good'
    elif prediction==0:
      return 'bad'



