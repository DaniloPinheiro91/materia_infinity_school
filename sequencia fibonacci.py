fibonacci_a = 0
fibonacci_b = 1
contador = 1

print(f'sequencia: {contador} resultado: {fibonacci_a}')
print(f'sequencia: {contador} resultado: {fibonacci_b}')
while contador < 20:
    sequencia = fibonacci_a + fibonacci_b
    contador += 1
    print(f'sequencia: {contador} resultado: {sequencia}')
    fibonacci_a = fibonacci_b
    fibonacci_b = sequencia
