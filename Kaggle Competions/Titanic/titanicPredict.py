import pandas as pd
from sklearn import model_selection
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
import numpy as np

train = pd.read_csv("trainNew2.csv")
test = pd.read_csv("testNew2.csv")
print train.head()



cols = ['A','B','C','D','E','F'] 

colsRes = ['T']

X = train[['A','B','C','D','E','F']]
y = train[['T']]
       
logistic = LogisticRegression()
logistic.fit(X,y)

cols2 = [1,	1,	30, 0	,0,	1]

Z = test[['A','B','C','D','E','F']]


results = logistic.predict(Z)

k = open("answer.csv", "w")
id = 892
for i in results:
    line = '%s,%s\n' % (id,i)
    k.write(line)
    id+=1
    
    
k.close()



