#%%

idade = int(input("Digite a sua idade: "))

if idade >= 0 and idade <= 12:
    print("Você é uma criança.")
elif idade >= 13 and idade <= 17:
    print("Você é um adolescente.")
elif idade >= 18 and idade <= 64:
    print("Você é um adulto.")
elif idade >= 65:
    print("Você é um idoso.")
else:
    print("Você nem existe.")

# %%

