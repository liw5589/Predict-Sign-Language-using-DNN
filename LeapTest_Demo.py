import tflearn
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder

XLS = pd.read_csv('LeapTest/leap_demo_test.csv', encoding = 'euc-kr')
XLS = XLS.round(3)

fingerList = ['Thumb','Index','Middle','Ring','Pinky']
for i in range(len(fingerList)):
    XLS[fingerList[i] + '_x'] = XLS[fingerList[i] + '_x'] * 100
    XLS[fingerList[i] + '_y'] = XLS[fingerList[i] + '_y'] * 100
    XLS[fingerList[i] + '_z'] = XLS[fingerList[i] + '_z'] * 100

data = XLS.drop('Lable',1)
label = XLS['Lable']

x_data = data.as_matrix()
y_data = label.as_matrix()

x_train, x_test, y_train, y_test = train_test_split(x_data,y_data, train_size= 0.8, random_state=30)

enc = OneHotEncoder(handle_unknown='ignore')
y_train = enc.fit_transform(y_train.reshape(-1,1)).toarray()
y_test = enc.fit_transform(y_test.reshape(-1,1)).toarray()

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

model = tflearn.DNN(net,checkpoint_path="LeapTest/hidden(8,13)_bew_init.ckpt")
model.fit(x_train, y_train, validation_set=None, n_epoch=n_epochs,batch_size=batch_size)
model.save("LeapTest/hidden(8,13)_new_init.tfl")
acc_train = model.evaluate(x_train, y_train, batch_size)
acc_test = model.evaluate(x_test, y_test, batch_size)
print("accuracy for test data => " + str(acc_test))
