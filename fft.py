def fft_modulo(x, omega, m):
    n = len(x)
    if n == 1:
        return x
    else:
        x_pair = [x[i] for i in range(n) if i % 2 == 0]
        x_impair = [x[i] for i in range(n) if i % 2 == 1]
        y_pair = fft_modulo(x_pair, omega ** 2, m)
        y_impair = fft_modulo(x_impair, omega ** 2, m)
        y = [0] * n
        for i in range(n):
            y[i] = (y_pair[i % (n // 2)] + omega ** i * y_impair[i % (n // 2)]) % m
        return y


x = [1, 2, 3, 4, 4, 3, 2, 1]
modulo = 17
w = 2
x_hat = fft_modulo(x, w, modulo)
print("Final result:", x_hat)
