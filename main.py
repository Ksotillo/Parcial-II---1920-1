from pregunta1 import es_primo
from pregunta2 import main_pregunta2

def main():
    print('Bienvenido a la resolución del parcial II del trimestre 1920-1')
    continuar = True
    while continuar:
        seleccion = input('Elige la pregunta que desear ver: \n\t1\n\t2\n\t3\n\n\tSelección: ')
        if seleccion == '1':
            num = int(input('Indique el numero para determinar si es primo o no: '))
            if es_primo(num, num//2 + 1):
                print('El numero {} es primo'.format(num))
            else:
                print('El numero {} no es primo'.format(num))
        elif seleccion == '2':
            main_pregunta2()
        elif seleccion == '3':
            pass
        else:
            print('Por favor, ingrese una opción válida (1/2/3)')


main()