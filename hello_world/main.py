det = {
    'name':'',
    'age':'',
    'password':'',
    'email':''
}
print(det)
n = input('Pls enter your name: ')
a = input('Pls enter your age: ')
p = input('Pls enter your password: ')
e = input('Pls enter yor email: ')

det['name'] = n
det['age'] = a
det['password'] = p
det['email']= e

y = input('Detail to fetch:')
print(det[y])