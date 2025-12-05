from tensorflow.keras.callbacks import ReduceLROnPlateau

from objet.ModelBuilder import *

class ModelTrainer:

    def __init__(self, input_shape, output_shape):
        self.__input_shape = input_shape
        self.__output_shape = output_shape
        self.__model = ModelBuilder(input_shape, output_shape).build()

    def train(self, train_x, train_y, epochs=150, batch_size=5):
        lr_schedule = ReduceLROnPlateau(monitor='loss', factor=0.5, patience=5, min_lr=0.0001)
        self.__model.fit(train_x, train_y, epochs=epochs, batch_size=batch_size, verbose=1, callbacks=[lr_schedule])

    def save(self, filename='chatbot_model_fr.h5'):
        self.__model.save(filename)