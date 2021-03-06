#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 29 16:12:16 2018

@author: Allen
"""

#part 1 - 
from keras.models import Sequential
from keras.layers import Convolution2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense
import scipy.ndimage
#initializing the CNN

classifier = Sequential()
#step 1 - convolui
classifier.add(Convolution2D(32,(3,3),activation = 'relu',input_shape = (64,64,3)))

#step2 - max pooling
classifier.add(MaxPooling2D(pool_size = (2,2)))

#adding a second convolutional layer

classifier.add(Convolution2D(32,(3,3),activation = 'relu'))
classifier.add(MaxPooling2D(pool_size = (2,2)))

# Step 3 flattening
classifier.add(Flatten())


#step 4 full connect
classifier.add(Dense(units =  128,activation = 'relu'))
classifier.add(Dense(units =  1,activation = 'sigmoid'))

#compiling the CNN
classifier.compile(optimizer = 'adam',loss = 'binary_crossentropy',metrics = ['accuracy'])


#part2 - fitting the cnn to the images

from keras.preprocessing.image import ImageDataGenerator

train_datagen = ImageDataGenerator(
        rescale=1./255,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True)

test_datagen = ImageDataGenerator(rescale=1./255)

training_set = train_datagen.flow_from_directory(
                            'dataset/training_set',
                            target_size=(64, 64),
                            batch_size = 32,
                            class_mode='binary')

test_set = test_datagen.flow_from_directory(
                            'dataset/test_set',
                            target_size=(64, 64),
                            batch_size=32,
                            class_mode='binary')

classifier.fit_generator(
        training_set,
        steps_per_epoch=250,
        epochs=25,
        validation_data=test_set,
        validation_steps=62.5)



