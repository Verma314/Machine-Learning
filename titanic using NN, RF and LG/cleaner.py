f = open ( 'testX.csv', 'r')

f2 = open('testY.csv', 'w')


#missing age is put as 30
# Pclass	Sex	Age	SibSp	Parch	Fare	Cabin	Survived

count = 0
for i in f:
    line = i.split(',')
    
    if ( line[1] == 'male'):
        line[1] = '1'

    if ( line[1] == 'female'):
        line[1] = '0'
        
    line = ','.join(line)
    
    f2.write(line)

f.close()
f2.close()
    
    
