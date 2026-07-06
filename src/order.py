def calcular_total(preco, quantidade):
    if preco < 0 or quantidade < 0:
        return 0
    return preco * quantidade