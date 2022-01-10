price_skumria = float(input())
price_caca = float(input())
quantity_palamud = float(input())
quantity_safrid = float(input())
quantity_midi = int(input())

price_palamud = price_skumria * 0.6 + price_skumria
price_safrid = price_caca * 0.8 + price_caca
midi_total = quantity_midi * 7.50
palamud_total = price_palamud * quantity_palamud
safrid_total = price_safrid * quantity_safrid

total_costs = palamud_total + safrid_total + midi_total

print(f'{total_costs:.2f}')
