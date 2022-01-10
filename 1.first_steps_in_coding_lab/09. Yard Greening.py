square_meters_for_landscaping = float(input())

final_price = square_meters_for_landscaping * 7.61 * 0.82
discount = square_meters_for_landscaping * 7.61 * 0.18

print(f'The final price is: {final_price:.2f} lv.')
print(f'The discount is: {discount:.2f} lv.')