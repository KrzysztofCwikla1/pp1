price=(float(input('enter price')))
discount=(float(input('enter discount %')))

discount_price=price * (1-discount/100)
price_diff=price-discount_price
print(f'Product Price:{price:.2f}')
print(f'discount:{discount:.2f}')
print(f'discounted price:{discount_price:.2f}')
print(f'price difference:{price_diff:.2f}')
