f=open('test.csv','r')

i=0
sum1=0
countT = 0

a = []

for line in f:
        
        line=line.split(',')
        
        if ( line[3] == '' ):
                line[3] = '30'
                
        if ( line[2]=='male'):
            line[2]='1'
        if ( line[2] == 'female'):
            line[2] = '0'
        
        if ( line[6] == ''):
            line[6]='0'
        elif ( line[6] =='Cabin'):
                line[6] ='Cabin'
        else:
                line[6] = '1'
        
        a.append(line)

        countT +=1
        
f.close()


f = open('testNew2.csv', 'w')

for l in a:
        l = ",".join(l)
        l +='\n'
        f.write(l)

f.close()
        
