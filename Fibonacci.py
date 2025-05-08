print("Generador de la secuencia Fibonacci")

n = int(input("¿Cuántos números de Fibonacci quieres generar? (Mínimo 2): "))

fibonacci = [0, 1]

for i in range(2, n):
    siguiente_num = fibonacci[-1] + fibonacci[-2]
    fibonacci.append(siguiente_num)
    
print(f"\nLos primeros {n} números de Fibonacci son:")
print(fibonacci)