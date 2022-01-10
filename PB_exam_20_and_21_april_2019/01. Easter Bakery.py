price_flour = float(input())
flour_kg = float(input())
sugar_kg = float(input())
eggs_boxes = int(input())
maq_number = int(input())

total_flour = price_flour * flour_kg
total_sugar = sugar_kg * price_flour * 0.75
total_eggs = eggs_boxes * price_flour * 1.1
total_maq = maq_number * price_flour * 0.75 * 0.2

total_sum = total_flour + total_sugar + total_eggs + total_maq

print(f'{total_sum:.2f}')
