'''
1 Escribir una función que calcule el máximo común divisor entre dos números
'''

def mcd(a, b):
    divisores_a = [num for num in range(1, a+1) if a % num == 0]
    divisores_b = [num for num in range(1, b+1) if b % num == 0]
    divisores_a.reverse()
    divisores_b.reverse()
    for divisor_a in divisores_a:
        if divisor_a in divisores_b:
            return divisor_a


if __name__ == '__main__':
    print('\n1. MCD')
    print(f'12 y 16: {mcd(12, 16)}')
    print(f'225 y 300: {mcd(225, 300)}')