import pandas as pd
from sklearn import model_selection
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn import svm

import numpy as np


test = pd.read_csv("testY.csv", names = ['A','B','C','D','E'])

dataframe = pd.read_csv("trainX.csv", names = ['A','B','C','D','E','T'])
dataframe.apply(lambda x: (x - np.mean(x)) / (np.max(x) - np.min(x)))
print ( dataframe.info() )


dataframe = dataframe.apply(pd.to_numeric)
array = dataframe.as_matrix()
array = dataframe.values




test = test.apply(pd.to_numeric)
array2 = test.as_matrix()
array2 = test.values
# Change dataframe to array
# separate array into input and output components
X = array[:,0:5]
Y = array[:,5]


modelSVM = svm.SVC(kernel='linear', C=1, gamma=1) 
modelSVM.fit(X, Y)

#Predict Output
predicted= modelSVM.predict(array2)
print(predicted)





k = open("anubhavvvvvvv.csv", "w")

id = 892
#print(results)

for i in predicted:
    line = '%s,%s\n' % (id,int(i))
    k.write(line)
    id+=1
    
        
k.close()



