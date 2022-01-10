number_locations = int(input())

for location in range(number_locations):
    expected_average_extraction = float(input())
    number_days = int(input())
    extraction_gold_day = 0

    for day in range(number_days):
        gold_extraction_per_day = float(input())
        extraction_gold_day += gold_extraction_per_day
    average_extraction = extraction_gold_day / number_days
    if average_extraction >= expected_average_extraction:
        print(f"Good job! Average gold per day: {average_extraction:.2f}.")
    else:
        print(f"You need {expected_average_extraction - average_extraction:.2f} gold.")
