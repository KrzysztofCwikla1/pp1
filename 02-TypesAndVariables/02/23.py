registration=input("Enter your vehicle registration number:")
first_two=registration[:2]
if first_two =='KR' or first_two=='KK':
    print('Jesteś z krakowa')
else:
    print('nie jesteś')
    
