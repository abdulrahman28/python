#To retrieve

mno = '15/30gr002'

f = open('name','r')
a = f.readlines()
i = 0
while i <= len(a)-1:
    a[i] = a[i].replace('\n','')
    i+=1

j = False
i = 0
while i <= len(a)-1:
    b = a[i].split(',')
    for x in b:
        if x == mno:
            name = b[1]
            age = b[2]
            email = b[3]
            j = True
    if j == True:
        break
    i+=1
    
print('Name: '+name+', age: '+age+', email: '+email)