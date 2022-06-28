from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, BatchNormalization, MaxPool2D
from keras.layers import Activation, Dropout, Flatten, Dense
# from keras.regularizers import l2

# Now we will define function to get train the model and return the model summary and performance
def create_model(input_shape):
    model = Sequential()
    model.add(Conv2D(32, (3, 3), input_shape=input_shape))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))

    model.add(Conv2D(32, (3, 3)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))

    model.add(Conv2D(64, (3, 3)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))

    model.add(Flatten())
    model.add(Dense(64))
    model.add(Activation('relu'))
    model.add(Dropout(0.5))
    model.add(Dense(4))
    model.add(Activation('softmax'))

    model.compile(optimizer='rmsprop', loss='categorical_crossentropy',
                  metrics=['accuracy'])
    return model



def AlexNet(input_shape):
    model = Sequential()
    model.add(Conv2D(filters=96, kernel_size=(11,11), strides = (4, 4), activation='relu', input_shape=input_shape))
    model.add(BatchNormalization())
    model.add(MaxPool2D(2, strides=(2, 2)))

    model.add(Conv2D(256, (11,11),strides=(1,1), activation='relu',padding="same"))
    model.add(BatchNormalization())

    model.add(Conv2D(384, (3,3),strides=(1,1), activation='relu',padding="same"))
    model.add(BatchNormalization())

    model.add(Conv2D(384, (3,3),strides=(1,1), activation='relu',padding="same"))
    model.add(BatchNormalization())

    model.add(Conv2D(256, (3, 3), strides=(1, 1), activation='relu',padding="same"))
    model.add(BatchNormalization())

    model.add(MaxPool2D(2, strides=(2, 2)))
    model.add(Flatten())
    model.add(Dense(4096, activation='relu'))
    model.add(Dense(4096, activation='relu'))
    model.add(Dense(38, activation='softmax'))

    model.compile(optimizer='adam', loss='categorical_crossentropy',
                  metrics=['accuracy'])
    return model
