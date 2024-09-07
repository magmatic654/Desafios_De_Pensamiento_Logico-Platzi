# En este desafío te damos como entrada un número positivo mayor a cero y debes regresar un arreglo con todos los números primos menores o iguales a ese número de entrada ordenados de menor a mayor.

# Recuerda que un número es primo si es solo divisible por 1 y por si mismo.

# Nota: Todos los números primos son números impares a excepción del número 2. El número 1 no es primo porque no cumple con las dos condiciones mencionadas arriba.

# Input
# solution(5);

# Output
# [2, 3, 5]

def solution(nums):
    new_nums = list()
    for num in nums:
        x = 1
        c = 0
        if num == 2:
            new_nums.append(num)
        else:
            while x <= num:
                x += 1
                if num % x == 0:
                    c += 1
                x += 1

            if c == 2:
                new_nums.append(num)
    return new_nums

print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]))