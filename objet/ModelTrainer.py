from tensorflow.keras.callbacks import ReduceLROnPlateau
from objet.ModelBuilder import *

class ModelTrainer:

    def __init__(self):
        self.__model = None
        self.__modelLoaded = False

    def createModel(self,**kwargs):
        self.__model = ModelBuilder(vectorizer=kwargs.get('vectorizer'),
                                   num_classes=kwargs.get('num_classes')).build()
        self.__modelLoaded = True

    def loadModel(self,model):
        self.__model = model
        self.__modelLoaded = True

    def train(self, train_x, train_y, epochs=150, batch_size=5):
        if self.__modelLoaded:
            lr_schedule = ReduceLROnPlateau(monitor='loss', factor=0.5, patience=5, min_lr=0.0001)

            # Entraînement
            history = self.__model.fit(
                train_x,
                train_y,
                epochs=epochs,
                batch_size=batch_size,
                verbose=1,
                callbacks=[lr_schedule]
            )
            return history
        else :
            return None

    def save(self, filename='arrera_model.keras'):
        try :
            self.__model.save(filename)
            return True
        except :
            return False