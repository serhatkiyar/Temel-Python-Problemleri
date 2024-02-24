yazi = "ProgramlamaÖdeviİleriSeviyeVeriYapılarıveObjeleripynb"
tekrar = {}
print(type(tekrar))
for i in yazi:
    tekrar[i] = 0
    for j in yazi:
        if i == j:
            tekrar[i] += 1

print(tekrar)
for i in range(len(tekrar)):
    print(f"{list(tekrar.keys())[i]} sayısı yazıda {list(tekrar.values())[i]} defa tekrar ediyor.")
