import random
sag = 0
sol = 0
sayac = -1
while sayac <= 10:
    if sag >= sol:
        sol += random.randint(0, 51)
        if sol > sag:
            sayac += 1
    else:
        sag += random.randint(0, 51)
        if sag > sol:
            sayac += 1
    print(f"Değişim >>> {sayac}   Sol Kefe >>> [{sol}]   Sag Kefe >>> [{sag}]")
