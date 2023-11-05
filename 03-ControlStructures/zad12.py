imie1 =(input('wprowadź pierwsze imię: '))
age1=int(input('wprowadź wiek pierwszej osoby:'))
imie2 =(input('wprowadź drugie imię: '))
age2 =int(input('wprowadź wiek drugiej osoby:'))

if age1 and age2 >=18:
    print(f'{imie1} i {imie2} są pełnoletni')
else:
    print(f'albo {imie1} albo {imie2} jest niepełnoletni')