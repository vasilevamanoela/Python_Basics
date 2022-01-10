company_name = input()
number_adults = int(input())
number_kids = int(input())
net_price_adult = float(input())
price_tax = float(input())

net_price_kid = net_price_adult * 0.3
price_adult_with_tax = net_price_adult + price_tax
price_kid_with_tax = net_price_kid + price_tax

total_price_tickets = (number_adults * price_adult_with_tax) + (number_kids * price_kid_with_tax)
total_earn_company = total_price_tickets * 0.2

print(f"The profit of your agency from {company_name} tickets is {total_earn_company:.2f} lv.")