from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import Dense, Dropout, Input
from tensorflow.keras.optimizers import Adam

class ModelBuilder:
    def __init__(self, input_shape, output_shape):
        self.input_shape = input_shape
        self.output_shape = output_shape
        self.__model = None

    def build(self):
        self.__model = Sequential()

        self.__model.add(Input(shape=(self.input_shape,)))

        self.__model.add(Dense(128, activation='relu'))

        self.__model.add(Dropout(0.5))
        self.__model.add(Dense(64, activation='relu'))
        self.__model.add(Dropout(0.5))
        self.__model.add(Dense(self.output_shape, activation='softmax'))

        adam = Adam(learning_rate=0.01)
        self.__model.compile(loss='categorical_crossentropy', optimizer=adam, metrics=['accuracy'])
        return self.__model