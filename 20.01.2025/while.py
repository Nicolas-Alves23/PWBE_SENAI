numero_anterior = 0
while True:
    n = int(input("Me passe um número = "))
    if n > numero_anterior:
        numero_maior = n
    numero_anterior = n
    if n < 0:
        print("É negativo")
        print(f"Seu número maior é {numero_maior}")
        break