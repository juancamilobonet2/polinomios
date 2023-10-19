import random
import math
import sys
import time

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
    
    def fft(self, a, invert):
        n = len(a)
        if n == 1:
            return

        a0 = a[::2]
        a1 = a[1::2]
        self.fft(a0, invert)
        self.fft(a1, invert)

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

    def multiply_fft(self):
        fa = self.poly1[:]
        fb = self.poly2[:]
        n = 1
        while n < len(self.poly1) + len(self.poly2):
            n <<= 1
        fa += [0] * (n - len(fa))
        fb += [0] * (n - len(fb))

        self.fft(fa, False)
        self.fft(fb, False)
        for i in range(n):
            fa[i] *= fb[i]
        self.fft(fa, True)

        result = [round(x.real) for x in fa]
        result.reverse()
        arr_sin_ceros = [x for x in result if x != 0]
        print(arr_sin_ceros)
        return arr_sin_ceros

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
            t0 = time.time()
            multiplier = read_txt(file_path)
            multiplied = multiplier.multiply_convolute()
            print("Resultado")
            multiplier.print_poly(multiplied)
            tf = time.time()
            print("Tiempo de ejecución: ", tf-t0)
        elif alg == 2:
            t0 = time.time()
            multiplier = read_txt(file_path)
            multiplied = multiplier.multiply_fft()
            print("Resultado")
            multiplier.print_poly(multiplied)
            tf = time.time()
            print("Tiempo de ejecución: ", tf-t0)
        else:
            print("Opción no válida")
            
    except FileNotFoundError:
        print("El archivo no se encontró en la ruta especificada.")
    except Exception as e:
        print("Ocurrió un error:", e)
