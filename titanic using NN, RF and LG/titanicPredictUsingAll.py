import pandas as pd
from sklearn import model_selection
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
import numpy as np


test = pd.read_csv("testY.csv", names = ['A','B','C','D','E','F'])

dataframe = pd.read_csv("trainX.csv", names = ['A','B','C','D','E','F','T'])


dataframe = dataframe.apply(pd.to_numeric)
array = dataframe.as_matrix()
array = dataframe.values



test = test.apply(pd.to_numeric)
array2 = test.as_matrix()
array2 = test.values




# Change dataframe to array




# separate array into input and output components
X = array[:,0:6]
Y = array[:,6]

mlp = MLPClassifier(hidden_layer_sizes=(1000),solver='sgd',learning_rate_init=0.01,max_iter=500)
mlp.fit(X, Y)
results =  mlp.predict(array2)




logistic = LogisticRegression()
logistic.fit(X,Y)

logistic_results = logistic.predict(array2)
print(logistic_results)


# Create a random forest classifier. By convention, clf means 'classifier'
clfRF = RandomForestClassifier(n_jobs=2)

# Train the classifier to take the training features and learn how they relate
# to the training y (the species)
clfRF.fit(X,Y)
 
rf_results = clfRF.predict(array2)
print ( rf_results)



combo = []
k2 = open("answerFINAL.csv", "w")
id = 892

asc = 0
for i in results:
    print(i)
    combo.append(int(i))
    asc += 1

asc = 0
for i in logistic_results:
    combo[asc] += int(i)
    asc += 1

asc = 0
for i in rf_results:
    combo[asc] += int(i)



for i in combo:
    if ( i >= 2):
        line = line = '%s,%s\n' % (id,int(1))
    else:
        line = '%s,%s\n' % (id,int(0))
    k2.write(line)
    id +=1
k2.close()





k = open("answerNNNNNN.csv", "w")

id = 892
print(results)

for i in rf_results:
    line = '%s,%s\n' % (id,int(i))
    k.write(line)
    id+=1
    
        
k.close()



