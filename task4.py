import time
import matplotlib.pyplot as plt

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

def lucas(n):
    if n == 0:
        return 2
    if n == 1:
        return 1
    return lucas(n - 1) + lucas(n - 2)

def fib_with_lucas(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    i = n // 2
    j = n - i
    return (fib_with_lucas(i) + lucas(j)) * (fib_with_lucas(j) + lucas(i)) // 2

def lucas_with_fib(n):
    if n == 0:
        return 2
    if n == 1:
        return 1
    return fib_with_lucas(n - 1) + fib_with_lucas(n + 1)

n_values = list(range(1, 41))
times_fib = []
times_fib_lucas = []

for n in n_values:
    start = time.perf_counter()
    fibonacci(n)
    times_fib.append(time.perf_counter() - start)

    start = time.perf_counter()
    fib_with_lucas(n)
    times_fib_lucas.append(time.perf_counter() - start)

plt.plot(n_values, times_fib, label='fibonacci')
plt.plot(n_values, times_fib_lucas, label='fib_with_lucas')
plt.xlabel('n')
plt.ylabel('Время (сек)')
plt.legend()
plt.grid(True)
plt.show()