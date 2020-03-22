class Ciudad():
    def __init__(self, nombre, area, descripcion):
        self.nombre = nombre
        self.area = area
        self.descripcion = descripcion

def calcular_distancia(recorrido, distancias):
    cont = 0
    for i in range(len(recorrido) - 1):
        cont += distancias[recorrido[i].nombre][recorrido[i+1].nombre]
    return cont


def main_pregunta2():
    continuar = True
    recorrido = []
    distancias = {
        'Caracas': {
            'Maracay': 120,
            'Valencia': 200,
        },
        'Maracay': {
            'Caracas': 120,
            'Valencia': 80,
        },
        'Valencia': {
            'Maracay': 80,
            'Caracas': 200,
        }
    }

    print('Bienvenido al programa principal de la empresa Regalos Claus.',
    '\nPor favor indique el recorrido que se debe de hacer para distribuir los juguetes en estas fechas decembrinas teniendo las siguientes ciudades',
    '\n\tCaracas\n\tMaracay\n\tValencia')

    while continuar:
        nom = input('Indique el nombre de la ciudad ')
        area = int(input('Indique el area de la ciudad '))
        desc = input('Indique el descripcion de la ciudad ')
        recorrido.append(Ciudad(nom.capitalize(), area, desc))
        respuesta = input('¿Desea registrar otra ciudad? (S/N)')
        if respuesta.lower() == 'n':
            continuar = False

    print('La distancias total sería de: ', calcular_distancia(recorrido, distancias))
