import random

class Poly_multiplier:
    def __init__(self, poly1, poly2):
        self.poly1 = poly1
        self.poly2 = poly2
    
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

    def multiply_convolute(self):
        poly1 = self.poly1
        poly2 = self.poly2
        offset=0
        poly_result=[0 for _ in range(len(poly1)+len(poly2)-1)]
        for coef1 in poly1:
            for i in range(len(poly2)):
                poly_result[i+offset] += coef1*poly2[i]
            offset+=1
        return poly_result

    def multiply_fft(self):
        degree = len(self.poly1) + len(self.poly2) - 2
        #sampleamos puntos
        sample_poly1 = Poly_multiplier.sample_points(degree+1, self.poly1)
        sample_poly2 = Poly_multiplier.sample_points(degree+1, self.poly2)

        #multiplicamos los puntos
        sample_multiplied = []
        for i in range(len(sample_poly1)):
            sample_multiplied.append(sample_poly1[i]*sample_poly2[i])
        
        #hacemos la fft
        #TODO




    def sample_points(n, poly):
        points = []
        for i in range(n):
            x = i
            y = 0
            for j in range(len(poly)):
                y += poly[j]*x**j
            points.append(y)
        return points

    def print_poly(polynomial):
        str_poly = ''
        polynomial.reverse()
        for i in range(len(polynomial)):
            coef = polynomial[i]
            if coef != 0:
                str_poly += str(coef) + 'x^' + str(len(polynomial)-1-i) + ' + '
        print(str_poly[:-3])

def gen_polynomial_txts():
    with open('grado10.txt', 'w') as f:
        for i in range(10):
            f.write(str(random.randint(0, 1000)) + ' ' + str(random.randint(0, 1000)) + '\n')
    with open('grado100.txt', 'w') as f:
        for i in range(100):
            f.write(str(random.randint(0, 1000)) + ' ' + str(random.randint(0, 1000)) + '\n')
    with open('grado1000.txt', 'w') as f:
        for i in range(1000):
            f.write(str(random.randint(0, 1000)) + ' ' + str(random.randint(0, 1000)) + '\n')


if __name__ == '__main__':
    gen_polynomial_txts()
    multiplier = Poly_multiplier.read_txt('grado3.txt')
    multiplied = multiplier.multiply_convolute()
    Poly_multiplier.print_poly(multiplied)
