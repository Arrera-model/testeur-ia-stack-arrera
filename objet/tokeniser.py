import ssl
import nltk
from nltk.stem.snowball import FrenchStemmer

class Tokeniser:
    def __init__(self):
        if hasattr(ssl, '_create_unverified_context'):
            ssl._create_default_https_context = ssl._create_unverified_context

        try:
            nltk.data.find('tokenizers/punkt')
        except LookupError:
            try :
                nltk.download('punkt', quiet=True)
            except Exception as e:
                raise ValueError(f"Imposible de telecharger le punkt {e}")

        try:
            nltk.data.find('tokenizers/punkt_tab')
        except LookupError:
            try :
                nltk.download('punkt_tab', quiet=True)
            except Exception as e:
                raise ValueError(f"Imposible de telecharger le punkt_tab {e}")

        try :
            self.__french_stemmer = FrenchStemmer()
            self.__stateStemmer = True
        except Exception as e :
            self.__stateStemmer = False
            raise ValueError(f"Erreur du lancement du Stemmer : {e}")


    def tokenize(self, sentence):
        try :
            return nltk.word_tokenize(sentence, language='french')
        except Exception as e:
            raise ValueError(f"Erreur methode tokenize objet Tokeniser erreur {e}")

    def stem(self, word):
        try :
            if self.__stateStemmer:
                return self.__french_stemmer.stem(word.lower())
            else :
                return word.lower()
        except Exception as e:
            raise ValueError(f"Erreur methode stem objet Tokeniser erreur {e}")


    def clean_sentence(self, sentence):
        try :
            tokens = self.tokenize(sentence)
            return [self.stem(w) for w in tokens]
        except Exception as e:
            raise ValueError(f"Erreur methode clean_sentence objet Tokeniser erreur {e}")