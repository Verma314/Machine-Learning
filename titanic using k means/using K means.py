import pandas as pd
from sklearn import model_selection
from sklearn.cluster import KMeans
from sklearn.neighbors import KNeighborsClassifier
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

kmeans = KMeans(n_clusters=2)
kmeans.fit(X)

centroid = kmeans.cluster_centers_
labels = kmeans.labels_

predicted = kmeans.predict(array2)
print(predicted)

k = open("k MEANS SOLUTION.csv", "w")

id = 892
#print(results)

k.write("PassengerId,Survived\n")
for i in predicted:
    line = '%s,%s\n' % (id,int(i))
    k.write(line)
    id+=1
    
        
k.close()



