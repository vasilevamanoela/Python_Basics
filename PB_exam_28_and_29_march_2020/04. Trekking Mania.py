number_groups = int(input())
total_ppl = 0
ppl_musala = 0
ppl_monbai = 0
ppl_kilimandjaro = 0
ppl_k2 = 0
ppl_everest = 0

for i in range(number_groups):
    number_ppl = int(input())
    if number_ppl <= 5:
        ppl_musala += number_ppl
    elif 6 <= number_ppl <= 12:
        ppl_monbai += number_ppl
    elif 13 <= number_ppl <= 25:
        ppl_kilimandjaro += number_ppl
    elif 26 <= number_ppl <= 40:
        ppl_k2 += number_ppl
    elif number_ppl >= 41:
        ppl_everest += number_ppl

    total_ppl += number_ppl

percent_musala = ppl_musala / total_ppl * 100
percent_monbai = ppl_monbai / total_ppl * 100
percent_kilimandjaro = ppl_kilimandjaro / total_ppl * 100
percent_k2 = ppl_k2 / total_ppl * 100
percent_everes = ppl_everest / total_ppl * 100

print(f'{percent_musala:.2f}%')
print(f'{percent_monbai:.2f}%')
print(f'{percent_kilimandjaro:.2f}%')
print(f'{percent_k2:.2f}%')
print(f'{percent_everes:.2f}%')
