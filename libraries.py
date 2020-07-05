import nltk
nltk.download('punkt')
nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer
lemmatizer = WoedNetLemmatizer()
import json
import pickle

import numpy as np
from keras.nodles import Sequential
from keras.layers import Dense, Activaton, Dropout
from Keras.optimizers import SGD
import random
