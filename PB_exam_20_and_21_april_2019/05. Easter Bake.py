import math
import sys

number_kozunaks = int(input())
total_sugar = 0
total_flour = 0
max_sugar = -sys.maxsize
max_flour = -sys.maxsize

for n in range(number_kozunaks):
    sugar_spent = int(input())
    flour_spent = int(input())

    if sugar_spent > max_sugar:
        max_sugar = sugar_spent

    if flour_spent > max_flour:
        max_flour = flour_spent

    total_sugar += sugar_spent
    total_flour += flour_spent

sugar_packets = math.ceil(total_sugar / 950)
flour_packets = math.ceil(total_flour / 750)

print(f"Sugar: {sugar_packets}")
print(f"Flour: {flour_packets}")
print(f"Max used flour is {max_flour} grams, max used sugar is {max_sugar} grams.")
