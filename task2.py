def tribonacci(n):
    # Базовый случай
    if n == 0 or n == 1:
        return 0
    elif n == 2:
        return 1
     # Рекурсивный случай
    else:
        return tribonacci(n - 1) + tribonacci(n - 2) + tribonacci(n - 3)

print(tribonacci(0))
print(tribonacci(1))
print(tribonacci(2))
print(tribonacci(3))
print(tribonacci(4))
print(tribonacci(5))
print(tribonacci(6))