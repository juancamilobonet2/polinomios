# Import the FFT and multiply functions
import math
import cmath

def fft(a, invert):
    n = len(a)
    if n == 1:
        return

    a0 = a[::2]
    a1 = a[1::2]
    fft(a0, invert)
    fft(a1, invert)

    ang = 2 * math.pi / n * (-1 if invert else 1)
    w = complex(1, 0)
    wn = complex(math.cos(ang), math.sin(ang))
    
    for i in range(n // 2):
        a[i] = a0[i] + w * a1[i]
        a[i + n // 2] = a0[i] - w * a1[i]
        if invert:
            a[i] /= 2
            a[i + n // 2] /= 2
        w *= wn

def multiply(a, b):
    fa = a[:]
    fb = b[:]
    n = 1
    while n < len(a) + len(b):
        n <<= 1
    fa += [0] * (n - len(fa))
    fb += [0] * (n - len(fb))

    fft(fa, False)
    fft(fb, False)
    for i in range(n):
        fa[i] *= fb[i]
    fft(fa, True)

    result = [round(x.real) for x in fa]
    return result

# Example usage
a = [6, 7, -10, 9]  # Representing the polynomial 1 + 2x + 3x^2
b = [-2, 4, -5]  # Representing the polynomial 2 + x^2

result = multiply(a, b)

# Output the result
print(result)  # Should print [2, 4, 7, 3, 1]
