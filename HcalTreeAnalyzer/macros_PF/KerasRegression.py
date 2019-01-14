import tensorflow as tf
from tensorflow import keras
from tensorflow.python.keras import layers

print(tf.__version__)

import uproot
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

### Add training and target variables here
inputVariables = ['gen_pt','pf_pt','pf_eta','pf_ecalFrac','pf_hcalFrac',"npf_nh","npf"]
targetVariable = 'gen_pt'
###
### Get data from inputTree
inputTree = uproot.open("pfstudy_histograms_K0S.root")["t1"]
dataset = inputTree.pandas.df(inputVariables)
dataset = dataset.dropna()
### Compare to TMVA
TMVA = uproot.open("TMVAReg_PF.root")["dataset"]
TMVATree = TMVA["TestTree"]
compareData = TMVATree.pandas.df(['DNN','gen_pt','pf_pt'])
compareData = compareData.dropna()
###
### define Test and Train Data as well as the target
train_dataset = dataset.sample(frac=0.9,random_state=0)
test_dataset  = dataset.drop(train_dataset.index)

train_labels = train_dataset.pop(targetVariable)
test_labels  = test_dataset.pop(targetVariable)

###
train_stats = train_dataset.describe()
train_stats = train_stats.transpose()
### need to normalize the data due to scaling/range differences in variable set
def norm(data):
  return (data - train_stats['mean']) / train_stats['std']
normed_train_data = norm(train_dataset)
normed_test_data = norm(test_dataset)

############################################
### Build the model
def build_model():
  model = keras.Sequential([
    layers.Dense(16, activation=tf.nn.relu, input_shape=[len(train_dataset.keys())]),
    #keras.layers.Dropout(0.3),
    layers.Dense(16, activation=tf.nn.relu),
    #keras.layers.Dropout(0.3),
    layers.Dense(1)
  ])
  optimizer = tf.train.RMSPropOptimizer(0.001)
  #optimizer  = 'adam'

  model.compile(loss='mse',
                optimizer=optimizer,
                metrics=['mae', 'mse'])
  return model

model = build_model()
###########################################
### Train the model
EPOCHS = 300

history = model.fit(
  normed_train_data, train_labels,
  epochs=EPOCHS, validation_split = 0.1, verbose=0)

hist = pd.DataFrame(history.history)
hist['epoch'] = history.epoch

def plot_history(history):
  fig1 = plt.figure()
  plt.xlabel('Epoch')
  plt.ylabel('Mean Abs Error [Pt]')
  plt.plot(hist['epoch'], hist['mean_absolute_error'],
           label='Train Error')
  plt.plot(hist['epoch'], hist['val_mean_absolute_error'],
           label = 'Val Error')
  plt.legend()
  
  fig2 = plt.figure()
  plt.xlabel('Epoch')
  plt.ylabel('Mean Square Error [$Pt^2$]')
  plt.plot(hist['epoch'], hist['mean_squared_error'],
           label='Train Error')
  plt.plot(hist['epoch'], hist['val_mean_squared_error'],
           label = 'Val Error')
  plt.legend()
  plt.show()

  fig1.savefig("mean_error_Drop.pdf")
  fig2.savefig("mean_squared_error_Drop.pdf")

#plot_history(history)


loss, mae, mse = model.evaluate(normed_test_data, test_labels, verbose=1)

print("Testing set Mean Abs Error: {:5.2f} Pt".format(mae))


### Predict 
test_predictions = model.predict(normed_test_data).flatten()
#fig3 = plt.figure()
#plt.scatter(test_labels, test_predictions)
#plt.xlabel('True Values [Pt]')
#plt.ylabel('Predictions [Pt]')
#plt.axis('equal')
#plt.axis('square')
##plt.xlim([0,plt.xlim()[1]])
##plt.ylim([0,plt.ylim()[1]])
#plt.plot([-200, 200], [-200, 200])
#plt.show()
#
#fig3.savefig("Drop.pdf")

###compare performance of the networks
res_DNN   = (compareData['DNN']-compareData['gen_pt'])/compareData['gen_pt']
res_Keras = (test_predictions-test_labels)/test_labels
fig = plt.figure()
x = plt.hist([res_DNN,res_Keras], 
             100,
             density = True,
             histtype = 'step', 
             label = ['TMVA','Keras'])

plt.grid(True)
plt.legend()
plt.show()
fig.savefig("keras_performance.pdf")


