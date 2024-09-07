# En este desafío vas a recibir un número que tendrás que reducir a uno en la menor cantidad de pasos posibles aplicando las siguientes opreraciones:

# Si es número par puedes divdir por 2
# Si es número impar puedes sumar 1 o restar 1. (n+1) o (n-1).

# Input
# solution(15)

# Output
# 5
def solution(num):
    if num <= 1:
        return 0
    steps = 0
    while True:
        if num % 2 == 0:
            num /= 2
        else:
            num += 1
        steps += 1

        if num == 1:
            return steps
        
print(solution(15)) 