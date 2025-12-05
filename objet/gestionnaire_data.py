from objet.tokeniser import Tokeniser
import json
import pickle
import random
import numpy as np

class gestionnaire_data:

    def __init__(self, intents_file):
        self.__intents_file = intents_file
        self.__tokeniser = Tokeniser()  # Utilisation de notre nouvelle classe
        self.__words = []
        self.__classes = []
        self.__documents = []
        self.__intents_json = {}
        self.__dirWorkPKLFile = 'words.pkl'
        self.__dirClassesPKLFile = 'classes.pkl'

    def setDirClassePKLFile(self,dir:str):
        self.__dirClassesPKLFile = dir

    def setDirWorkPKLFile(self,dir:str):
        self.__dirWorkPKLFile = dir

    def load_and_process(self):
        try:
            with open(self.__intents_file, 'r', encoding='utf-8') as f:
                self.__intents_json = json.load(f)
        except FileNotFoundError:
            return False

        for intent in self.__intents_json['intents']:
            for pattern in intent['patterns']:
                # Tokenisation via notre classe Tokeniser
                w = self.__tokeniser.tokenize(pattern)
                self.__words.extend(w)
                self.__documents.append((w, intent['tag']))

            if intent['tag'] not in self.__classes:
                self.__classes.append(intent['tag'])

        # Nettoyage et tri
        ignore_words = ['?', '!', '.', ',']
        # Stemming via notre classe Tokeniser
        self.__words = [self.__tokeniser.stem(w) for w in self.__words if w not in ignore_words]
        self.__words = sorted(list(set(self.__words)))
        self.__classes = sorted(list(set(self.__classes)))

        pickle.dump(self.__words, open(self.__dirWorkPKLFile, 'wb'))
        pickle.dump(self.__classes, open(self.__dirClassesPKLFile, 'wb'))
        return True

    def create_training_data(self):
        training = []
        output_empty = [0] * len(self.__classes)

        for doc in self.__documents:
            bag = []
            pattern_words = doc[0]
            # Stemming via notre classe Tokeniser
            pattern_words = [self.__tokeniser.stem(word) for word in pattern_words]

            for w in self.__words:
                bag.append(1) if w in pattern_words else bag.append(0)

            output_row = list(output_empty)
            output_row[self.__classes.index(doc[1])] = 1
            training.append([bag, output_row])

        random.shuffle(training)
        training = np.array(training, dtype=object)  # dtype object pour éviter warnings numpy

        train_x = list(training[:, 0])
        train_y = list(training[:, 1])

        return np.array(train_x), np.array(train_y)