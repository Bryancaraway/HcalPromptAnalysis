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
from sklearn.linear_model import LinearRegression


### Add training and target variables here
inputVariables = ['gen_pt','gen_eta','pf_pt','pf_eta','pf_ecalFrac','pf_hcalFrac',"npf_nh","npf"]
spectVariables = ['gen_eta',"npf_nh","npf"]
targetVariable = 'gen_pt'
###
### Get data from inputTree
inputTree = uproot.open("pfstudy_histograms_K0S.root")["t1"]
print inputTree
dataset = inputTree.pandas.df(inputVariables)
dataset = dataset.dropna()
### to directly compare to TMVA
my_cut = (abs(dataset['gen_eta'])>2.5) & (abs(dataset['gen_eta'])<2.9) & (dataset['npf_nh']==1) & (dataset['npf']==1)
dataset = dataset[my_cut]
dataset = dataset.drop(columns=spectVariables)
dataset = dataset.reset_index()
#dataset['50<x<70'] = ((dataset['pf_pt']> 50) & (dataset['pf_pt'] <= 70))*1.0
#dataset['40<x<50'] = ((dataset['pf_pt']> 40) & (dataset['pf_pt'] <= 50))*1.0
#dataset['30<x<40'] = ((dataset['pf_pt']> 30) & (dataset['pf_pt'] <= 40))*1.0
#dataset['20<x<30'] = ((dataset['pf_pt']> 20) & (dataset['pf_pt'] <= 30))*1.0
#dataset['10<x<20'] = ((dataset['pf_pt']> 10) & (dataset['pf_pt'] <= 20))*1.0
#dataset['0<x<10'] = ((dataset['pf_pt']> 0) & (dataset['pf_pt'] <= 10))*1.0
#print dataset.tail()
### Compare to TMVA
TMVA = uproot.open("TMVAReg_PF.root")["dataset"]
TMVATree = TMVA["TestTree"]
compareData = TMVATree.pandas.df(['DNN','gen_pt','pf_pt'])
compareData = compareData.dropna()
###
### define Test and Train Data as well as the target
train_dataset = dataset.sample(frac=0.7,random_state=1)
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
    layers.Dense(8, activation=tf.nn.relu, kernel_regularizer=keras.regularizers.l2(0.001), input_shape=[len(train_dataset.keys())]),
    #keras.layers.Dropout(0.2),
    layers.Dense(16, activation=tf.nn.relu, kernel_regularizer=keras.regularizers.l2(0.001)),
    keras.layers.Dropout(0.3),
    layers.Dense(1)
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
EPOCHS = 50

history = model.fit(
  normed_train_data, train_labels,
  epochs=EPOCHS, batch_size=64,
  validation_data=(normed_test_data,test_labels),
  verbose=0)

keras.utils.plot_model(model, to_file="model.png", show_shapes=True)

hist = pd.DataFrame(history.history)
hist['epoch'] = history.epoch

def plot_history(history):
  fig, [mean, mean_square] = plt.subplots(1, 2, figsize=(12, 6))
  mean.set_xlabel('Epoch')
  mean.set_ylabel('Mean Abs Error [Pt]')
  mean.grid(True)
  mean.plot(hist['epoch'], hist['mean_absolute_error'],
           label='Train Error')
  mean.plot(hist['epoch'], hist['val_mean_absolute_error'],
           label = 'Val Error')
  mean.set_ylim(top=10)
  mean.set_yscale('log')
  mean.legend()
  
  mean_square.set_xlabel('Epoch')
  mean_square.set_ylabel('Mean Square Error [$Pt^2$]')
  mean_square.grid(True)
  mean_square.plot(hist['epoch'], hist['mean_squared_error'],
           label='Train Error')
  mean_square.plot(hist['epoch'], hist['val_mean_squared_error'],
           label = 'Val Error')
  mean_square.set_yscale('log')
  mean_square.legend()
  
  plt.show()
  fig.savefig("mean_Drop.pdf")
  plt.clf()
  plt.close()

plot_history(history)

###################################
loss, mae, mse = model.evaluate(normed_test_data, test_labels, verbose=1)

print("Testing set Mean Abs Error: {:5.2f} Pt".format(mae))
###################################

### Predict 
test_predictions = model.predict(normed_test_data).flatten()
results = pd.DataFrame({'gen_pt':test_labels,'DNN':test_predictions})

def plot_perf(results,cut,title):
  results = (results[cut] if str(cut) != 'None' else results)
  plt.scatter(results['gen_pt'], results['DNN'], marker='+', label=title)
  plt.xlabel('True Values [Pt]')
  plt.ylabel('Predictions [Pt]')
  #plt.title(title)
  plt.grid(True)
  #plt.axis('equal')
  #plt.axis('square')
  plt.xlim([0,100])
  plt.ylim([0,100])
  plt.legend()
  plt.plot([-200, 200], [-200, 200])

fig = plt.figure(figsize=(12, 6))
#plot_perf(results,None,"All")
[plot_perf(results,
           (results['gen_pt']>(i*10)) & (results['gen_pt']<((i+1)*10)),
           "label[pt]>"+str(i*10)+" & label[pt]<"+str((i+1)*10)) for i in range(0,9)]
linear_regressor = LinearRegression()
linear_regressor.fit(results['gen_pt'].values.reshape(-1, 1),results['DNN'].values.reshape(-1, 1))
fit = linear_regressor.predict(results['gen_pt'].values.reshape(-1, 1))
plt.plot(results['gen_pt'].values.reshape(-1, 1),fit,'--k')
fig.savefig("model_acc.pdf")
plt.show()
plt.clf()
plt.close()

###compare performance of the networks
def plot_hist_compare(x,bins,labels,xlabel,fig_name):

  fig = plt.figure()
  plt.hist(x, 
           bins,
           density = True,
           histtype = 'step', 
           label = labels)

  plt.xlabel(xlabel)
  plt.grid(True)
  plt.legend()
  plt.show()
  fig.savefig(fig_name)
  plt.clf()
  plt.close()

### compare resonpse ###
res_DNN   = (compareData['DNN']-compareData['gen_pt'])/compareData['gen_pt']
res_Keras = (test_predictions-test_labels)/test_labels
plot_hist_compare([res_DNN,res_Keras],100,['TMVA','Keras'],"(Pred-True)/True [Pt]","perf_comparison.pdf")
### compare pt distribution ###
plot_hist_compare([compareData['DNN'],test_predictions],25,['TMVA','Keras'],"Pt","pt_comparison.pdf")

##### testing profile plot in python

def profile_plot_compare(x1,y1,label_1,x2,y2,label_2,bins,xmin,xmax,xlabel,ylabel,fig_name):
  def setupBins(x,y,bins,xmin,xmax):
    means_result = scipy.stats.binned_statistic(x, [y,y**2], bins=bins, range=(xmin,xmax), statistic='mean')
    bin_count = scipy.stats.binned_statistic(x, [y,y**2], bins=bins, range=(xmin,xmax), statistic='count')
    means, means2 = means_result.statistic
    standard_deviations = np.sqrt(means2 - means**2)/np.sqrt(bin_count.statistic)
    bin_edges = means_result.bin_edges
    bin_centers = (bin_edges[:-1] + bin_edges[1:])/2.
    return bin_centers, means, standard_deviations

  x1, y1, yerr1 = setupBins(x1, y1, bins, xmin, xmax)
  x2, y2, yerr2 = setupBins(x2, y2, bins, xmin, xmax)

  fig = plt.figure()
  plt.errorbar(x=x1, y=y1, yerr=yerr1, xerr=xmax/(2*bins), linestyle='none', marker='.', label =label_1)
  plt.errorbar(x=x2, y=y2, yerr=yerr2, xerr=xmax/(2*bins), linestyle='none', marker='.', label =label_2)
  plt.xlabel(xlabel)
  plt.ylabel(ylabel)
  plt.grid(True)
  plt.legend()
  plt.show()
  fig.savefig(fig_name)
  plt.clf()
  plt.close()

### Pred/True vs True ###
profile_plot_compare(compareData['gen_pt'], compareData['DNN']/compareData['gen_pt'], 'TMVA',
                     test_labels, test_predictions/test_labels, 'Keras',
                     20, 0, 100,
                     "True [PT]", "Pred/True [Pt]", "scale_comparison.pdf")
### Response vs True ###
profile_plot_compare(compareData['gen_pt'], (compareData['DNN']-compareData['gen_pt'])/compareData['gen_pt'], 'TMVA',
                     test_labels, (test_predictions-test_labels)/test_labels, 'Keras',
                     20, 0, 100,
                     "True [PT]", "(Pred-True)/True [Pt]", "response_comparison.pdf")
##### Debug low pt #####
if False:
  for i, label in enumerate(test_labels):
    if label < 10:
      print label, test_predictions[i]
