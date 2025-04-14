class Nota:
    def __init__(self, valor_inicial):
        self.valor_inicial = valor_inicial

    def evaluar_nota(self, nota):
        if nota >= 7:
            return "Aprobado"
        else:
            return "Desaprobado"

    def __repr__(self):
        return f"La nota es: {self.valor_inicial}"


# Variables para contar aprobados y desaprobados
aprobados = 0
desaprobados = 0

while True:
    # Pedir al usuario que ingrese una nota
    nota_ingresada = int(input("Ingrese una nota (0 para finalizar): "))

    # Finalizar el programa si se ingresa 0
    if nota_ingresada == 0:
        break

    # Crear una instancia de Nota y evaluar la nota
    nota = Nota(nota_ingresada)
    resultado = nota.evaluar_nota(nota_ingresada)
    print(f"Resultado: {resultado}")

    # Contar aprobados y desaprobados
    if resultado == "Aprobado":
        aprobados += 1
    else:
        desaprobados += 1

# Mostrar el total de aprobados y desaprobados
print(f"Total de aprobados: {aprobados}")
print(f"Total de desaprobados: {desaprobados}")
