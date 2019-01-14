import tensorflow as tf
from tensorflow import keras
from tensorflow.python.keras import layers
print(tf.__version__)

import uproot
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats
import numpy as np
import math

from keras.models import Sequential
from keras.layers import Dense
from keras.wrappers.scikit_learn import KerasRegressor
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline


### Add training and target variables here
inputVariables = ['gen_pt','gen_eta','pf_pt','pf_eta','pf_ecalFrac','pf_hcalFrac',"npf_nh","npf"]
spectVariables = ['gen_eta',"npf_nh","npf"]
targetVariable = 'gen_pt'
###
### Get data from inputTree
inputTree = uproot.open("pfstudy_histograms_K0S.root")["t1"]
dataset = inputTree.pandas.df(inputVariables)
dataset = dataset.dropna()
### to directly compare to TMVA
my_cut = (abs(dataset['gen_eta'])>2.5) & (abs(dataset['gen_eta'])<2.9) & (dataset['npf_nh']==1) & (dataset['npf']==1)
dataset = dataset[my_cut]
dataset = dataset.drop(columns=spectVariables)
dataset = dataset.reset_index()
dataset['50<x<70'] = ((dataset['pf_pt']> 50) & (dataset['pf_pt'] <= 70))*1.0
dataset['40<x<50'] = ((dataset['pf_pt']> 40) & (dataset['pf_pt'] <= 50))*1.0
dataset['30<x<40'] = ((dataset['pf_pt']> 30) & (dataset['pf_pt'] <= 40))*1.0
dataset['20<x<30'] = ((dataset['pf_pt']> 20) & (dataset['pf_pt'] <= 30))*1.0
dataset['10<x<20'] = ((dataset['pf_pt']> 10) & (dataset['pf_pt'] <= 20))*1.0
dataset['0<x<10'] = ((dataset['pf_pt']> 0) & (dataset['pf_pt'] <= 10))*1.0
#print dataset.tail()
### Compare to TMVA
TMVA = uproot.open("TMVAReg_PF.root")["dataset"]
TMVATree = TMVA["TestTree"]
compareData = TMVATree.pandas.df(['DNN','gen_pt','pf_pt'])
compareData = compareData.dropna()
###
### define Test and Train Data as well as the target
train_dataset = dataset.sample(frac=0.6,random_state=1)
#train_dataset = dataset.sample(n=1000, random_state=0)
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
    #keras.layers.Dropout(0.2),
    layers.Dense(8, activation=tf.nn.relu),
    #keras.layers.Dropout(0.2),
    layers.Dense(1, activation='linear', kernel_initializer='normal')
  ])
  #optimizer = tf.train.RMSPropOptimizer(0.001)
  optimizer  = 'adam'

  model.compile(loss='mse',
                optimizer=optimizer,
                metrics=['mae', 'mse'])
  return model

model = build_model()

###########################################
### Train the model
EPOCHS = 100

history = model.fit(
  normed_train_data, train_labels,
  epochs=EPOCHS, batch_size=2,
  validation_data=(normed_test_data,test_labels),
  verbose=0)

keras.utils.plot_model(model, to_file="model.png", show_shapes=True)

hist = pd.DataFrame(history.history)
hist['epoch'] = history.epoch

def plot_history(history):
  fig1 = plt.figure()
  plt.xlabel('Epoch')
  plt.ylabel('Mean Abs Error [Pt]')
  plt.grid(True)
  plt.plot(hist['epoch'], hist['mean_absolute_error'],
           label='Train Error')
  plt.plot(hist['epoch'], hist['val_mean_absolute_error'],
           label = 'Val Error')
  plt.ylim(top=10)
  plt.yscale('log')
  plt.legend()
  
  fig2 = plt.figure()
  plt.xlabel('Epoch')
  plt.ylabel('Mean Square Error [$Pt^2$]')
  plt.grid(True)
  plt.plot(hist['epoch'], hist['mean_squared_error'],
           label='Train Error')
  plt.plot(hist['epoch'], hist['val_mean_squared_error'],
           label = 'Val Error')
  plt.yscale('log')
  plt.legend()
  plt.show()

  fig1.savefig("mean_error_Drop.pdf")
  fig2.savefig("mean_square_error_Drop.pdf")

plot_history(history)


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
fig.savefig("perf_comparison.pdf")
plt.clf()
plt.close()

fig = plt.figure()
plt.hist([compareData['DNN'],test_predictions],
         25,
         density = True,
         histtype = 'step', 
         label = ['TMVA','Keras'])
plt.grid(True)
plt.legend()
plt.show()
fig.savefig("pt_comparison.pdf")
plt.clf()
plt.close()
##### testing profile plot in python

def setupBins(x,y):
  means_result = scipy.stats.binned_statistic(x, [y,y**2], bins=20, range=(0,100), statistic='mean')
  bin_count = scipy.stats.binned_statistic(x, [y,y**2], bins=20, range=(0,100), statistic='count')
  means, means2 = means_result.statistic
  standard_deviations = np.sqrt(means2 - means**2)/np.sqrt(bin_count.statistic)
  print 
  bin_edges = means_result.bin_edges
  bin_centers = (bin_edges[:-1] + bin_edges[1:])/2.
  return bin_centers, means, standard_deviations

x1, y1, yerr1 = setupBins(compareData['gen_pt'], compareData['DNN']/compareData['gen_pt'])
x2, y2, yerr2 = setupBins(test_labels, test_predictions/test_labels)

fig = plt.figure()
plt.errorbar(x=x1, y=y1, yerr=yerr1, xerr=2.5, linestyle='none', marker='.', label ='TMVA')
plt.errorbar(x=x2, y=y2, yerr=yerr2, xerr=2.5, linestyle='none', marker='.', label ='Keras')
plt.grid(True)
plt.legend()
plt.show()
fig.savefig("scale_comparison.pdf")

for i, label in enumerate(test_labels):
  if label < 10:
    print label, test_predictions[i]
