# r/learnpython Adventure Summary
  TEXT

## File Overview:
  File | SIZE | BRIEF
--- | --- | ---
README.md | ![GitHub file size in bytes](https://img.shields.io/github/size/Phillyclause89/reddit_scripts/input_shape_is_wrong_but_i_cant_work_out_why_help/README.md?style=plastic) | README.md file for this adventure.
requirements.txt | ![GitHub file size in bytes](https://img.shields.io/github/size/Phillyclause89/reddit_scripts/input_shape_is_wrong_but_i_cant_work_out_why_help/requirements.txt?style=plastic) | requirements.txt for this adventure.
MLing.py | ![GitHub file size in bytes](https://img.shields.io/github/size/Phillyclause89/reddit_scripts/input_shape_is_wrong_but_i_cant_work_out_why_help/MLing.py?style=plastic) | Main python file for debugging OP's issue
y_sinx.csv | ![GitHub file size in bytes](https://img.shields.io/github/size/Phillyclause89/reddit_scripts/input_shape_is_wrong_but_i_cant_work_out_why_help/y_sinx.csv?style=plastic) | CSV file for debugging OP's issue
  
## Source Link:
  * [ r/learnpython/.../input_shape_is_wrong_but_i_cant_work_out_why_help/ ]( https://www.reddit.com/r/learnpython/comments/dz64kt/input_shape_is_wrong_but_i_cant_work_out_why_help/ )
  
## Post Title:
  Input shape is wrong but I can't work out why, help please?
  
## Post Body:
  > I am attempting to build a basic neural network in TensorFlow/Keras.
  > 
  > Here is the original post I made to stack overflow https://stackoverflow.com/questions/58956330/building-basic-neural-network-with-tensorflow-keras-error-with-input-layer
  > 
  > Input Table that I am using
  > 
  > I get an error (tuple index out of range) with the input dimensions, but I can't work out why. If I try input_dim = 7, I get value error - expected to have shape (7,) but got array with shape (1,)
  > 
  > When I checked np.shape(x) , it said that x is (7,), so I can't work out what's wrong.
  > 
  > This is my coding attempt:
  > ```Python   
  > from tensorflow.keras.models import Sequential 
  > from tensorflow.keras.layers import Dense, Activation 
  > import pandas as pd 
  > import io 
  > import os 
  > import requests 
  > import numpy as np 
  > from sklearn import metrics  
  > df = pd.read_csv("C:\\Users\\Dan\\y_sinx.csv")  
  > x = df['x'].values 
  > y = df['y'].values  
  > model = Sequential() 
  > model.add(Dense(5, input_dim = x.shape[1], activation='relu')) 
  > model.add(Dense(3, activation='relu')) 
  > model.add(Dense(1)) 
  > model.compile(loss='mean_squared_error', optimizer = 'adam') 
  > model.fit(x, y, verbose = 2, epochs = 100)
  > ```
  

### My Comment(s):
  > Sorry for it being like several hours instead of a few. My commute home from work is like 2 hours because Seattle. u/PyDenver is correct when he said:
  > 
  > > Your input shape is the number of features you are training on, i.e. the number of columns you are feeding as inputs. In your case your input shape would be 1.
  > 
  > From reading their comment, you might have figured out by now that if you do:
  > ```Python
  > model.add(Dense(5, input_shape=(1,), activation='relu'))
  > ```
  > Then your code will run (on your example data set at least.) But it looked like from your original code you wanted a way to not have shape hard coded into your script, so I did some [digging](https://keras.io/search.html?q=shape) through the karas docs and found this [method](https://keras.io/backend/#shape). looks like if you import `karas.backend` then the below code without shape hardcoded will run:
  > ```Python
  > from tensorflow.keras.models import Sequential
  > from tensorflow.keras.layers import Dense, Activation
  > from keras import backend as K
  > import pandas as pd
  >   
  > df = pd.read_csv(r"y_sinx.csv")
  >   
  > x = df['x'].values
  > y = df['y'].values
  >   
  > model = Sequential()
  >   
  > model.add(Dense(5, input_shape=K.shape(x).shape, activation='relu'))
  > model.add(Dense(3, activation='relu'))
  > model.add(Dense(1))
  >   
  > model.compile(loss='mean_squared_error', optimizer='adam')
  >   
  > model.fit(x, y, verbose=2, epochs=100)
  > ```
  > My Output:
  > ```
  > Using TensorFlow backend.
  > WARNING:tensorflow:From My_site-packages_Path\site-packages\tensorflow\python\ops\init_ops.py:1251: calling VarianceScaling.__init__ (from tensorflow.python.ops.init_ops) with dtype is deprecated and will be removed in a future version.
  > Instructions for updating:
  > Call initializer instance with the dtype argument instead of passing it to the constructor
  > Epoch 1/100
  > 2019-11-20 20:19:17.340495: I tensorflow/core/platform/cpu_feature_guard.cc:142] Your CPU supports instructions that this TensorFlow binary was not compiled to use: AVX2
  > 6/6 - 0s - loss: 0.7397
  > Epoch 2/100
  > 6/6 - 0s - loss: 0.7302
  > Epoch 3/100
  > 6/6 - 0s - loss: 0.7208
  > Epoch 4/100
  > 6/6 - 0s - loss: 0.7115
  > Epoch 5/100
  > 6/6 - 0s - loss: 0.7025
  > ...
  > ...
  > Epoch 95/100
  > 6/6 - 0s - loss: 0.4123
  > Epoch 96/100
  > 6/6 - 0s - loss: 0.4116
  > Epoch 97/100
  > 6/6 - 0s - loss: 0.4110
  > Epoch 98/100
  > 6/6 - 0s - loss: 0.4103
  > Epoch 99/100
  > 6/6 - 0s - loss: 0.4097
  > Epoch 100/100
  > 6/6 - 0s - loss: 0.4090
  > ```
