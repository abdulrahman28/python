a = int(input('Enter the Multiplication Value: '))
i = int(input('Enter where to start from: '))
d = int(input('Enter where to terminate: '))
while i <= d:
    c = a * i
    print(str(a)+' x '+ str(i) + ' = ' + str(c))
    i += 1
print('Completed')

