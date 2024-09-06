# Vamos a tomar como base los números del 3 al 8 para multiplciarlos por un mismo factor desconocido (x) que nos da ciertos resultados.

# Entonces, dada una función que recibe un array númerico con los resultados debes encontrar el factor multiplicador (x) para obtener ese resultado multiplicando por los números del 3 al 8.

# Ejemplo:
# En el siguiente caso el factor sería 9.
# 3 * x =  27
# 4 * x =  36
# 5 * x =  45
# 6 * x =  54
# 7 * x =  63
# 8 * x =  72
# Si si un solo factor multiplicador difiere del resto se regresa false.

# En el siguiente ejemplo la función regresaria false porque hay una resultado que tiene como factor multiplicador el 6 en lugar del 9 como el resto.

# 3 * x =  27
# 4 * x =  36
# 5 * x =  45
# 6 * x =  54
# 7 * 6 =  42 <- 👈
# 8 * x =  72

# Input:
# solution([27, 36, 45, 54, 63, 72])
# solution([27, 36, 45, 54, 42, 72])

# Output:
# 9
# false

def solution(numbers):
    a = 3
    i = 0
    x = 1
    while True:
        # Comprueba si el el número a por x es igual al número en la posición dada por i
        if a * x == numbers[i]:
            # Hace una iteracion sobre toda la lista de números comprobando si todos aplican para este valor de x encontrado,
            for number in numbers:
                # si un número llega a no cumplir, este factor multiplicativo no se cumple y se retorna False
                if a * x != number:
                    return False
                # si el factor multiplicativo cumple para toda la lista, entonces significa que x es el factor multiplicativo de toda la lista y se retorna x
                if a == 8:
                    return x
                a += 1
        if x == 10:
            return False
        x += 1

print(solution([27, 36, 45, 54, 63, 72])) # => 9
print(solution([27, 36, 45, 54, 42, 72])) # => False
print(solution([15, 20, 25, 30, 35, 40])) # => 5
print(solution([15, 20, 25, 32, 35, 40])) # => False
print(solution([30, 40, 50, 60, 70, 80])) # => 10
print(solution([30, 40, 50, 60, 70, 70])) # => False
