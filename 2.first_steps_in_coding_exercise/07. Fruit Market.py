strawberries_price = float(input())
bananas_quantity = float(input())
oranges_quantity = float(input())
raspberries_quantity = float(input())
strawberries_quantity = float(input())

raspberries_price = strawberries_price * 0.5
oranges_price = raspberries_price * 0.6
bananas_price = raspberries_price * 0.2

raspberries_sum = raspberries_price * raspberries_quantity
oranges_sum = oranges_price * oranges_quantity
bananas_sum = bananas_price * bananas_quantity
strawberries_sum = strawberries_price * strawberries_quantity

total_sum = raspberries_sum + oranges_sum + bananas_sum + strawberries_sum

print(total_sum)