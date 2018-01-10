from keras.models import Sequential
from keras.layers import Flatten, Dense, Lambda, Cropping3D, Activation
from keras.layers.convolutional import Convolution3D
from keras.layers.pooling import MaxPooling3D

def getModel(input_shape=(3,160,320,3)):
    model = Sequential()
    model.add(Lambda(lambda x: (x/255.0) - 0.5, input_shape=input_shape))
    model.add(Cropping3D(cropping=((0,0), (50,20), (0,0))))
    model.add(Convolution3D(64, 1, 5, 5))
    #model.add(MaxPooling3D(pool_size=(1,2,2)))
    model.add(Activation('relu'))
    model.add(Convolution3D(32, 1, 5, 5))
    #model.add(MaxPooling3D(pool_size=(1,2,2)))
    model.add(Activation('relu'))
    model.add(Convolution3D(16, 1, 5, 5))
    #model.add(MaxPooling3D(pool_size=(1,2,2)))
    model.add(Activation('relu'))
    model.add(Flatten())
    model.add(Dense(1024))
    model.add(Activation('relu'))
    model.add(Dense(256))
    model.add(Activation('relu'))
    model.add(Dense(1))
    model.compile('adam', 'mean_squared_error', ['accuracy'])
    return model
