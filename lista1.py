# Cálculo da média
notas = [6,7,5,6,10,4,9]
soma = 0
x = 0
while x < 7:
    soma += notas[x]
    x += 1
print(f'Média: {soma / x:5.2f}')
