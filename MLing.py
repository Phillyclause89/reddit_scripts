from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation
from keras import backend as K
import pandas as pd

df = pd.read_csv(r"y_sinx.csv")

x = df['x'].values
y = df['y'].values

model = Sequential()

model.add(Dense(5, input_shape=K.shape(x).shape, activation='relu'))
model.add(Dense(3, activation='relu'))
model.add(Dense(1))

model.compile(loss='mean_squared_error', optimizer='adam')

model.fit(x, y, verbose=2, epochs=100)
