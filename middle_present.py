import tflearn
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder

##### WARNING 없애기 ######
import warnings
import os
import tensorflow as tf
##### WARNING 없애기 ######

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
warnings.filterwarnings(action='ignore')
tf.logging.set_verbosity(tf.logging.ERROR)

# XLS = pd.read_csv('./../Leapmotion/Test_Leap/middle_test.csv', encoding = 'euc-kr')
XLS = pd.read_csv('C:\\Users\\user\\PycharmProjects\\Leapmotion\\Test_Leap\\middle_test.csv', encoding = 'euc-kr')
XLS = XLS.round(3)
# XLS = XLS[-4:]

fingerList = ['Thumb','Index','Middle','Ring','Pinky']
for i in range(len(fingerList)):
    XLS[fingerList[i] + '_x'] = XLS[fingerList[i] + '_x'] * 100
    XLS[fingerList[i] + '_y'] = XLS[fingerList[i] + '_y'] * 100
    XLS[fingerList[i] + '_z'] = XLS[fingerList[i] + '_z'] * 100



data = XLS.drop('Lable',1)
label = XLS['Lable']

x_data = data.as_matrix()
y_data = label.as_matrix()



enc = OneHotEncoder(handle_unknown='ignore')
y_data = enc.fit_transform(y_data.reshape(-1,1)).toarray()


n_inputs = 26
n_hidden1 = 8
n_hidden2 = 13
n_outputs = 3

n_epochs = 50
batch_size = 32


he = tflearn.initializations.variance_scaling()
inputs = tflearn.input_data(shape=[None, n_inputs])
hidden1 = tflearn.fully_connected(inputs, n_hidden1, activation='relu',weights_init= he, name='hidden1')
hidden2 = tflearn.fully_connected(hidden1 , n_hidden2, activation='relu',weights_init= he,name='hidden2')
softmax = tflearn.fully_connected(hidden2, n_outputs, activation='softmax',weights_init= he, name ='output')
net = tflearn.regression(softmax)

model = tflearn.DNN(net)
# model.load("LeapTest/hidden(8,13)_new_init.tfl")
model.load("C:\\Users\\user\\PycharmProjects\\untitled\\LeapTest\\hidden(8,13)_new_init.tfl")

acc_test = model.predict(x_data)

print(acc_test)