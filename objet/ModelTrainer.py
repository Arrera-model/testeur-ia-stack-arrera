from tensorflow.keras.callbacks import ReduceLROnPlateau
from objet.ModelBuilder import *

class ModelTrainer:

    def __init__(self,**kwargs):
        self.__model = ModelBuilder(vectorizer=kwargs.get('vectorizer'),
                                    num_classes=kwargs.get('num_classes')).build()

    def train(self, train_x, train_y, epochs=150, batch_size=5):
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

    def save(self, filename='chatbot_model_fr.h5'):
        self.__model.save(filename)