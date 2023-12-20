def fft_modulo(x, omega, m, verbose=True, depth=0):
    n = len(x)
    indent = "  " * depth
    if n == 1:
        if verbose:
            print(f"{indent}Depth : {depth}")
            print(f"{indent}n = 1 - Stop recursion")
            print(f"{indent}x: {x}")
            print("-" * 40)
        return x
    else:
        x_pair = [x[i] for i in range(n) if i % 2 == 0]
        x_impair = [x[i] for i in range(n) if i % 2 == 1]
        if verbose:
            print(f"{indent}Depth {depth} \u2193")
            print(f"{indent}n = {n}")
            print(f"{indent}x: {x}")
            print(f"{indent}\u03C9: {omega}")
            print(f"{indent}x_pair: {x_pair}")
            print(f"{indent}x_impair: {x_impair}")
            print("-" * 40)
        y_pair = fft_modulo(x_pair, omega ** 2, m, verbose, depth + 1)
        y_impair = fft_modulo(x_impair, omega ** 2, m, verbose, depth + 1)
        y = [0] * n
        for i in range(n):
            y[i] = (y_pair[i % (n // 2)] + omega ** i * y_impair[i % (n // 2)]) % m
        if verbose:
            print(f"{indent}Depth {depth} \u2191")
            print(f"{indent}n = {n}")
            print(f"{indent}x_pair: {x_pair}")
            print(f"{indent}x_impair: {x_impair}")
            print(f"{indent}y_pair: {y_pair}")
            print(f"{indent}y_impair: {y_impair}")
            print(f"{indent}y: {y}")
            print("-" * 40)
        return y


x = [1, 2, 3, 4, 4, 3, 2, 1]
modulo = 17
w = 2
x_hat = fft_modulo(x, w, modulo)
print("Final result:", x_hat)
