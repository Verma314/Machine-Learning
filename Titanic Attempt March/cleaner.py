f=open('train.csv','r')

i=0
sum1=0
countT = 0

a = []

for line in f:
        
        line=line.split(',')
        
        if ( line[2] == '' ):
                line[2] = '30'
                
        if ( line[1]=='male'):
            line[1]='1'
        if ( line[1] == 'female'):
            line[1] = '0'
        
        
        a.append(line)

        countT +=1
        
f.close()


f = open('train2.csv', 'w')

for l in a:
        l = ",".join(l)
        f.write(l)

f.close()
