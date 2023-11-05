def different(n1,n2,n3):
    if n1!=n2 or n1!=n3 or n2!=n3:
        return True
    else:
        return False

n1=(int(input("input first number:")))
n2=(int(input("input second number:")))
n3=(int(input("input third number:")))

if different(n1,n2,n3)==True:
        print(f'Numbers {n1},{n2}, and {n3} are different')
else:
    print(f'Numbers {n1},{n2}, and {n3} are the same')


