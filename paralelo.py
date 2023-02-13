import random  # importo la librería random
import time # importo la librería time
from time import sleep  # importo la función sleep de la libreria time¡
from multiprocessing import Pool # importo la clase Pool de la librería multiprocessing
from introducir.numero import solicitar_introducir_numero_extremo # importo la función solicitar_introducir_numero_extremo del módulo introducir.numero
from colorama import Fore  # importo la librería colorama
import os # importo la librería os
import pathlib # importo la librería pathlib
actual_path = pathlib.Path(__file__).parent.absolute() # guardo la ruta absoluta del archivo en la variable actual_path

urls = ["a.com", "b.com", "c.com", "d.com", "e.com"]  # creo una lista de urls


def scrape(url): # función scrape
    print("starting", url) # imprimo el mensaje "starting" y la url
    duration = round(random.uniform(0, 1), 3)  # arreglo el error de esta línea
    sleep(duration) # duermo el programa durante el tiempo que dure la variable duration
    print("finished", url, "time taken:", duration, "seconds") # imprimo el mensaje "finished", la url, el tiempo que ha tardado en segundos
    return url, duration # devuelvo la url y el tiempo que ha tardado

def readlist1():
    with open(str(actual_path) + './tiempos_paralelo.txt', 'r') as f:
        lista = f.read()
        lista_paralelo = eval(lista)
        return lista_paralelo
def readlist2():
    with open(str(actual_path) + './tiempos_sin_paralelo.txt', 'r') as f:
        lista = f.read()
        lista_sin_paralelo = eval(lista)
        return lista_sin_paralelo
if __name__ == "__main__":
    lista1 = readlist1()
    lista2 = readlist2()
    if lista1 == '':
        lista1 = []
        lista2 = []
    def main(): # función main
        eleccion = solicitar_introducir_numero_extremo(Fore.CYAN +"¿Quieres ejecutar el programa en paralelo? 1: No, 2: Si, 3: Ver medias de tiempo de ejecución, 4: Guardar y Salir", 1, 4) ; print(Fore.RESET) # solicito al usuario que introduzca un número entre 1 y 3

        if eleccion == 1:  # main del programa sin paralelizar
            inicio = time.time() # guardo el tiempo en el que empieza el programa
            output = [] # creo una lista vacía
            for url in urls: # recorro la lista de urls
                result = scrape(url) # ejecuto la función scrape
                output.append(result) # añado el resultado a la lista vacía
            print(output) # imprimo la lista
            fin = time.time() # guardo el tiempo en el que termina el programa
            tiempo = fin - inicio # guardo el tiempo que ha tardado en ejecutarse el programa
            print("Tiempo de ejecución sin paralelizar: ", tiempo) # imprimo el tiempo que ha tardado en ejecutarse el programa
            lista1.append(tiempo)
            with open(str(actual_path) + './tiempos_sin_paralelo.txt', 'w') as f:
                f.write(str(lista1))
            main() # vuelvo a ejecutar el programa aplicando recursividad

        elif eleccion == 2:  # main del programa paralelizado
            inicio_paralelo = time.time() # guardo el tiempo en el que empieza el programa
            pool = Pool(processes=4)  # creo un pool de 4 procesos
            data = pool.map(scrape, urls)  # ejecuto la función scrape en paralelo
            pool.close()  # cierro el pool
            for row in data: # recorro la lista de resultados
                print(row) # imprimo los resultados
            fin_paralelo = time.time() # guardo el tiempo en el que termina el programa
            tiempo_paralelo = fin_paralelo - inicio_paralelo # guardo el tiempo que ha tardado en ejecutarse el programa
            print("Tiempo de ejecución en paralelo: ", tiempo_paralelo) # imprimo el tiempo que ha tardado en ejecutarse el programa
            lista2.append(tiempo_paralelo)
            with open(str(actual_path) + './tiempos_paralelo.txt', 'w') as f:
                f.write(str(lista2))
            main() # vuelvo a ejecutar el programa aplicando recursividad
        elif eleccion == 3:
            print("La media de tiempo de ejecución sin paralelizar es: ", sum(lista1) / len(lista1))
            print("La media de tiempo de ejecución en paralelo es: ", sum(lista2) / len(lista2))
            main()
        elif eleccion == 4:
            """ejecuta por terminal: git add ., git commit -m "Actualización de tiempos", git push"""
            os.system("git add .")
            os.system("git commit -m 'Actualización de tiempos'")
            os.system("git push")
            exit() # salgo del programa
    main()


"""Conclusiones:
Se puede ver que el programa paralelizado es mucho más rápido que el programa sin paralelizar, ya que el programa paralelizado tarda bastante menos en ejecutarse mientras que el programa sin paralelizar tarda más tiempo en ejecutarse, generando al ordenador utilizar una mayor cantidad de recursos durante más tiempo.
Por ello se puede concluir que el programa paralelizado es más eficiente que el programa sin paralelizar y es algo que a partir de ahora se tendré más en cuenta a la hora de programar."""