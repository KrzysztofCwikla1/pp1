def month(n):
    months=['january', 'february', 'march', 'april', 'may', 'june', 'july','august','september','october','november','december' ]
    return months[n-1]

if __name__=='__main__':
    print(month(1))
    print(month(9))
    print(month(12))
