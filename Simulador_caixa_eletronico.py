print("=" * 35)
print("        BANCO PYTHON")
print("=" * 35)

valor = int(input("Digite o valor que deseja sacar: R$ "))

total = valor
cedulas = [50, 20, 10, 5, 1]

print("\nNotas entregues:")

for cedula in cedulas:
    quantidade = total // cedula

    if quantidade > 0:
        print(f"{quantidade} nota(s) de R$ {cedula}")
        total -= quantidade * cedula

print("=" * 35)
print("Obrigado por usar o Banco Python! Volte sempre!")
