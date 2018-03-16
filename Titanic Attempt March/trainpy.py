import pandas as pd
from sklearn import model_selection
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler
import numpy as np


test = pd.read_csv("test2.csv", names = ['A','B','C','D','E','F'])

dataframe = pd.read_csv("train2.csv", names = ['A','B','C','D','E','F','T'])


dataframe = dataframe.apply(pd.to_numeric)
#pd.DataFrame(dataframe).fillna(dataframe.mean())
array = dataframe.as_matrix()
array = dataframe.values

array = np.nan_to_num(array)

test = test.apply(pd.to_numeric)
#pd.DataFrame(test).fillna(dataframe.mean())
array2 = test.as_matrix()
array2 = test.values

array2 = np.nan_to_num(array2)


# Change dataframe to array




# separate array into input and output components
X = array[:,0:6]
Y = array[:,6]


#mlp = MLPClassifier(hidden_layer_sizes=(1000),solver='sgd',learning_rate_init=0.01,max_iter=500)
#mlp.fit(X, Y)
#results =  mlp.predict(array2)




logistic = LogisticRegression()
logistic.fit(X,Y)


logistic_results = logistic.predict(array2)
print(logistic_results)


 









k = open("answerNNNNNN.csv", "w")

id = 892


for i in logistic_results:
    line = '%s,%s\n' % (id,int(i))
    k.write(line)
    id+=1
    
        
k.close()

