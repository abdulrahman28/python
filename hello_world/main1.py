det = {
    'name':'',
    'age':'',
    'password':'',
    'email':''
}
print(det)
det['name'] = input('Pls enter your name: ')
det['age'] = input('Pls enter your age: ')
det['password'] = input('Pls enter your password: ')
det['email'] = input('Pls enter yor email: ')

y = input('Data to fetch: ')
print(y+': '+str(det[y]))