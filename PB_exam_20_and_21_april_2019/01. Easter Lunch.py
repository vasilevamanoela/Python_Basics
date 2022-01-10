number_kozunak = int(input())
number_eggs = int(input())
biscuits = int(input())

total_kozunak = number_kozunak * 3.2
total_eggs = number_eggs * 4.35
total_biscuits = biscuits * 5.4
total_paint = number_eggs * 12 * 0.15

total_sum = total_kozunak + total_eggs + total_biscuits + total_paint
print(f'{total_sum:.2f}')
