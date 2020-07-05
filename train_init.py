training = []
output_empty = [0] * len(classes)
for doc in documents:
    #initalizing bag of wards
    bag = []
    #list of tokenized words for the patterns
    patterns_words = doc[0]
    #lemmatize each word - dreate base word, in attempt to represent related ignore_words
    patterns_words = [lemmatizer.lemmatize(word.lower()) for word in pattern_words]
    #create our bag of words array with 1, if word match found in current patterns
    for w in words:
        bag.append(1) if w in pattern_words else bag.append(0)

    # output is a '0' for each tag and '1' for current tag (for each pattern)
    output_row = list(output_empty)
    output_row[classes.index(doc[1])] = 1

    training.append([bag, output_row])
#shuffle our features and turn into np.array
random.shuffle(training)
training = np.array(training)
# create train and test lists. X - patterns, Y - intents
train_x = list(training[:,0])
train_y = list(training[:,1])
print("Training data created")
