# minha_string = input("Uma palavra por favor :")
# def palavra_ao_contrario(minha_string):
#     lista = []
#     for caractere in minha_string:
#         lista.insert(0,caractere)
#     aocontrario = ''.join(lista)
#     print(aocontrario)
# palavra_ao_contrario(minha_string)

def contar_carcteres(s):
    dicionario = {}
    for i in s:
        if i in dicionario:
            dicionario[i] += 1
        else:
            dicionario[i] = 1
    print(dicionario)
contar_carcteres("banana")