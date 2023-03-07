import numpy as np
import tensorflow as tf

# 2 x m
X = np.array([[200.0, 18.0]])

# 3 x m
# sets up the number of nodes for the 1st layer
layer_1 = tf.keras.layers.Dense(units=3, activation="sigmoid")

# The Dense class actually has a self.call() method,
# which allows the instantiation of a class to be used as a function
# <Dense object>(X) calculates activation vector A1 given inputs X
A1 = layer_1(X)

# 1 x m
layer_2 = tf.keras.layers.Dense(units=1, activation="sigmoid")
A2 = layer_2(A1)

model = tf.keras.Model()


# X is a 4 x 2 matrix, but can it be reshaped 
# to 2 x 4 like how we represented the inputs 
# of neural networks as a column vector?
X = np.array([[200.0, 17.0],
              [120.0, 5.0],
              [425.0, 20.0],
              [212.0, 18.0]])

# can Y be a 1 x m row vector rather than a 1D vector?
Y = np.array([1, 0, 0, 1])
layer_1 = tf.keras.layers.Dense(units=3, activation="sigmoid")
layer_2 = tf.keras.layers.Dense(units=1, activation="sigmoid")
model = tf.keras.Sequential([layer_1, layer_2])

# compiles and builds the simple neural network model
model.compile()

# trains the model using the data
model.fit(X, Y)

# predict the 
# model.predict(<test dataset X>)


