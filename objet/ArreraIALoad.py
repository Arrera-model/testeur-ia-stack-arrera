import json
import pickle
import numpy as np
import random
from tensorflow.keras.models import load_model
from objet.tokeniser import Tokeniser

LISTMODELSUPPROT = [
    "arrera_model_2026"
]

class ArreraIALoad:
    def __init__(self):
        self.__model_type = None
        self.__model = None
        self.__tokeniser = None

    # Methode private

    def __loadArreraModel2026(self, model_path, words_path, classes_path, intents_path):
        if not all([words_path, classes_path, intents_path]):
            raise FileNotFoundError("Pour 'arrera_model_2026', les chemins 'words_path', 'classes_path', et 'intents_path' sont requis.")

        self.__model = load_model(model_path)
        self.__words = pickle.load(open(words_path, 'rb'))
        self.__classes = pickle.load(open(classes_path, 'rb'))
        self.__intents = json.loads(open(intents_path, encoding='utf-8').read())
        self.__tokeniser = Tokeniser()


    def __sendRequetteArreraTextModel(self, sentence: str) -> str:
        # 1. Créer le sac de mots à partir de la phrase
        sentence_words = self.__tokeniser.clean_sentence(sentence)
        bag = [0] * len(self.__words)
        for s_word in sentence_words:
            for i, word in enumerate(self.__words):
                if word == s_word:
                    bag[i] = 1

        # 2. Prédire l'intention avec le modèle Keras
        res = self.__model.predict(np.array([bag]), verbose=0)[0]

        # 3. Filtrer les prédictions sous un seuil et trier
        ERROR_THRESHOLD = 0.25
        results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]
        results.sort(key=lambda x: x[1], reverse=True)

        # 4. Formater la liste des intentions
        return_list = []
        for r in results:
            return_list.append({"intent": self.__classes[r[0]], "probability": str(r[1])})

        # 5. Obtenir une réponse textuelle
        if not return_list:
            return "Je ne suis pas sûr de comprendre. Pouvez-vous reformuler ?"

        tag = return_list[0]['intent']
        for intent_data in self.__intents['intents']:
            if intent_data['tag'] == tag:
                return random.choice(intent_data['responses'])

        return "Erreur interne : Intention trouvée mais pas de réponse associée."

    # Methode public

    def loadModel(self,type_model:str="arrera_model_2026",model_directory:str="model",nameModel:str="model.keras"):
        if type_model in LISTMODELSUPPROT:
            if type_model == LISTMODELSUPPROT[0]:
                self.__model_type = LISTMODELSUPPROT[0]

                wordFile = model_directory+"/words.pkl"
                classFile = model_directory+"/classes.pkl"
                intentFile = model_directory+"/intents.json"
                modelFile = model_directory+"/"+nameModel

                try :
                    self.__loadArreraModel2026(model_path=modelFile,
                                               words_path=wordFile,
                                               classes_path=classFile,
                                               intents_path=intentFile)
                    return True
                except Exception as e:
                        raise ValueError(f"Erreur lors du chargement du modèle : {e}")
            else :
                return False

        else :
            return False

    def send_request(self, prompt: str) -> str:
        if not self.__model:
            return "Erreur : Aucun modèle n'est chargé. L'initialisation a probablement échoué."

        if self.__model_type == LISTMODELSUPPROT[0]:
            return self.__sendRequetteArreraTextModel(prompt)

        else:
            return f"Erreur : Pas de méthode de prédiction définie pour le type '{self.__model_type}'."