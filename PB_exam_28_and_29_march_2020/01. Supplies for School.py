number_pens = int(input())
number_markers = int(input())
cleaning_gel = float(input())
discount = int(input())

price_pens = number_pens * 5.80
price_markers = number_markers * 7.20
price_cleaning_gel = cleaning_gel * 1.20

total_price = price_pens + price_markers + price_cleaning_gel
total_with_discount = total_price - ((total_price * discount) / 100)

print(f'{total_with_discount:.3f}')
