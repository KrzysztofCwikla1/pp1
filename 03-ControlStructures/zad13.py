number1=int(input('wprowadź liczbę:'))
number2=int(input('wprowadź drugą liczbę:'))
if number1 >=0 or number2 >=0:
    print(f'conajmniej jedna z liczb{number1} i {number2} nie jest ujemna')
else:
    print(f'obydwie z liczb{number1} i {number2} są ujemne')