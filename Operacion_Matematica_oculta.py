# Descripción del reto
# Encuentra la lógica de las siguientes operaciones y números:

# 5 + 4 = 19
# 8 + 2 = 610
# 10 + 8 = 218
# 12 + 9 = 321
# 18 + 2 = 1620
# 21 + 5 = 1626

#SOLUCION
# Encontramos en la operacion un patron que sigue restar A - B y concatenarlo a la operacion de suma A + B, despues pasarlo como número entero.

def solution(num1, num2):
    return int(f'{num1 - num2}{num1 + num2}')

print(solution(5, 4)) # => 19
print(solution(8, 2)) # => 610
print(solution(10, 8)) # => 218
print(solution(12, 9)) # => 321