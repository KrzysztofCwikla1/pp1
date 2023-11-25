import random
a=random.randrange(1,7)
liczba=(int(input('guess number')))
if liczba==a:
    print('True')
else:
    print('False')