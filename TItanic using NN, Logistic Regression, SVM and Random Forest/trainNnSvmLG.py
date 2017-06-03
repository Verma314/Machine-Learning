import pandas as pd
from sklearn import model_selection
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn import svm
import numpy as np

dataframe = pd.read_csv("trainX.csv", names = ['A','B','C','D','E','F','T'])
test = pd.read_csv("testY.csv", names = ['A','B','C','D','E','F'])

dataframe = dataframe.apply(pd.to_numeric)
array = dataframe.as_matrix()
array = dataframe.values

test = test.apply(pd.to_numeric)
array2 = test.as_matrix()
array2 = test.values
X = array[:,0:6]
Y = array[:,6]


mlp = MLPClassifier(hidden_layer_sizes=(10),solver='sgd',learning_rate_init=0.01,max_iter=500)
mlp.fit(X, Y)
resultsNN =  mlp.predict(array2)

modelSVM = svm.SVC(kernel='linear', C=1, gamma=1) 
modelSVM.fit(X, Y)
resultsSVM= modelSVM.predict(array2)

logistic = LogisticRegression()
logistic.fit(X,Y)
resultsLogistic = logistic.predict(array2)


clfRF = RandomForestClassifier(n_jobs=2)
clfRF.fit(X,Y)
resultsRF = clfRF.predict(array2)



results = []
counter = 0

id = 892
F = open("answerNNSVMLOGISTIC.csv", "w")
F.write("PassengerId,Survived\n")
for i,j,k,l in zip(resultsNN, resultsSVM, resultsLogistic, resultsRF):
    if ( int(i+j+k+l) >= 2):
        line = '%s,%s\n' % (id,int(1))
    else:
        line = '%s,%s\n' % (id,int(0))
    F.write(line)
    id+=1
            
F.close()



