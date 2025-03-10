# num = int(input("Me passe o número por favor "))
# if num % 2 == 0:
#     print("É par")
# else:
#     print("É impar")

n1 = float(input("Me passe uma nota = "))
n2 = float(input("Me passe uma nota = "))
n3 = float(input("Me passe uma nota = "))
n4 = float(input("Me passe uma nota = "))
n5 = float(input("Me passe uma nota = "))

media = (n1 + n2 + n3 + n4 + n5) / 5
if media >= 5:
    print ("Aprovado")    
elif media >= 2.5 and media < 5:
    print("Recuperação")
elif media < 2.5:
    print("Reprovado")