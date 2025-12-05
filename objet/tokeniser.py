import nltk
from nltk.stem.snowball import FrenchStemmer

class Tokeniser:
    def __init__(self):
        try:
            nltk.data.find('tokenizers/punkt')
        except LookupError:
            try :
                nltk.download('punkt', quiet=True)
            except Exception as e:
                print(f"Imposible de telecharger le punkt {e}")

        try:
            nltk.data.find('tokenizers/punkt_tab')
        except LookupError:
            try :
                nltk.download('punkt_tab', quiet=True)
            except Exception as e:
                print(f"Imposible de telecharger le punkt_tab {e}")

        try :
            self.__french_stemmer = FrenchStemmer()
            self.__stateStemmer = True
        except Exception as e :
            self.__stateStemmer = False
            print(f"Erreur du lancement du Stemmer : {e}")


    def tokenize(self, sentence):
        """Découpe une phrase en mots."""
        return nltk.word_tokenize(sentence, language='french')

    def stem(self, word):
        """Réduit un mot à sa racine si le stemmer est actif."""
        if self.__stateStemmer:
            return self.__french_stemmer.stem(word.lower())

    def clean_sentence(self, sentence):
        """Combine tokenisation et stemming pour une phrase complète."""
        tokens = self.tokenize(sentence)
        return [self.stem(w) for w in tokens]