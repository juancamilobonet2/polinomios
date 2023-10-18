import random
import math
import sys
class Poly_multiplier:
    def __init__(self, poly1, poly2):
        self.poly1 = poly1
        self.poly2 = poly2
        print("Primer polinomio:")
        self.print_poly(poly1)
        print("Segundo polinomio:")
        self.print_poly(poly2)

    def multiply_convolute(self):
        poly1 = self.poly1
        poly2 = self.poly2
        offset=0
        poly_result=[0 for _ in range(len(poly1)+len(poly2)-1)]
        for coef1 in poly1:
            for i in range(len(poly2)):
                poly_result[i+offset] += coef1*poly2[i]
            offset+=1
        poly_result.reverse()
        return poly_result
    
    def fft(self, x, inverse=False):
        N = len(x)
        if N <= 1:
            return x
        even = self.fft(x[0::2], inverse)
        odd = self.fft(x[1::2], inverse)
        T = [math.e**(-2j*math.pi*k/N) for k in range(N // 2)]
        if inverse:
            T = [1/t for t in T]
        return [even[k] + T[k] * odd[k] for k in range(N // 2)] + \
               [even[k] - T[k] * odd[k] for k in range(N // 2)]

    def multiply_fft(self):
        degree = len(self.poly1) + len(self.poly2) - 2
        n = 1
        while n < 2 * (degree + 1):
            n *= 2

        # Sample and pad to a power of 2
        sample_poly1 = self.sample_points(n, self.poly1)
        sample_poly2 = self.sample_points(n, self.poly2)

        # Perform FFT on the padded data
        fft_poly1 = self.fft(sample_poly1)
        fft_poly2 = self.fft(sample_poly2)

        # Pointwise multiplication
        fft_multiplied = [a * b for a, b in zip(fft_poly1, fft_poly2)]

        # Inverse FFT to get the polynomial result
        poly_result = self.fft(fft_multiplied, inverse=True)

        # Trim the result to the original size
        poly_result = poly_result[:degree + 1]

        return poly_result

    def sample_points(self, n, poly):
        points = []
        for i in range(n):
            x = i
            y = 0
            for j in range(len(poly)):
                y += poly[j]*x**j
            points.append(y)
        return points

    def print_poly(self, polynomial):
        str_poly = ''
        polynomial.reverse()
        for i in range(len(polynomial)):
            coef = polynomial[i]
            if coef != 0:
                str_poly += str(coef) + 'x^' + str(len(polynomial)-1-i) + ' + '
        print(str_poly[:-3])

def read_txt(file):
        poly1=[]
        poly2=[]
        with open(file, 'r') as f:
            for line in f:
                line = line.split()
                coef1 = int(line[0])
                coef2 = int(line[1])
                poly1.append(coef1)
                poly2.append(coef2)
        return Poly_multiplier(poly1, poly2)

def gen_polynomial_txts(grado):
    with open('grado'+str(grado)+'.txt', 'w') as f:
        for i in range(grado):
            f.write(str(random.randint(0, 1000)) + ' ' + str(random.randint(0, 1000)) + '\n')

if __name__ == '__main__':
    num = int(input("Subio un archivo con el polinomio (1) o desea generar un polinomio (2): "))
    if num == 1:
      file_path = sys.argv[1]
    elif num == 2:
      grado = int(input("Defina el grado del polinomio que desea generar: ")) # 5
      gen_polynomial_txts(grado)
      file_path = 'grado'+str(grado)+'.txt'
      print("Polinomio de grado" + str(num) + "aleatorio generado")
    try:
        alg = int(input("¿Qué algoritmo desea correr? Directo (1), ttf (2): "))
        if alg == 1:
            multiplier = read_txt(file_path)
            multiplied = multiplier.multiply_convolute()
            print("Resultado")
            multiplier.print_poly(multiplied)
        elif alg == 2:
            multiplier = read_txt(file_path)
            multiplied = multiplier.multiply_fft()
            print("Resultado")
            multiplier.print_poly(multiplied)
        else:
            print("Opción no válida")
            
    except FileNotFoundError:
        print("El archivo no se encontró en la ruta especificada.")
    except Exception as e:
        print("Ocurrió un error:", e)
