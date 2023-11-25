cena=(float(input('input brutto')))
withvat=(cena*1.23)
vat=withvat-cena
print(f'amount: {withvat:.2f} vat: {vat:.2f}')