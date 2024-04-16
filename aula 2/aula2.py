#%%

graus = int(input("Digite a temperatura: "))

if graus >= 0 and graus <= 15:
    print("Frio.")
elif graus > 15 and graus <= 25:
    print("Calor.")
elif graus > 25:
    print("Tá no Acre.")
else:
    print("Congelou.")

# %%

times = ["Campinense", "Real Madrid", "Liverpool", "Borussia Dortmund"]

for time in times:
    print(time)

# %%

for numero in range(1, 11):
    print(numero)

# %%
