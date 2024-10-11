valores = [1, 2, 3, 4, 5, 6, 9.5]
valores_cuadrado = [n**2 for n in valores]
print(valores_cuadrado)


valores = [1, 2, 3, 4, 5, 6, 9.5]
valores_pares = [p for p in valores if p%2 == 0]
print(valores_pares)


temperatura_fahrenheit = [32, 212, 275]
grados_celsius = [(gc-32)*(5/9) for gc in temperatura_fahrenheit]
print(grados_celsius)