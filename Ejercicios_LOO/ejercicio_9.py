"""Sumados: Sumar los 1000 primeros números naturales (1 + 2 + 3 + 4 + … + 1000),
 imprimiendo por cada suma el resultado parcial obtenido"""

def main():
    """main"""
    suma = 0
    for i in range(1, 1001):
        suma += i
        print("Suma parcial: ", suma)

if __name__ == "__main__":
    main()
