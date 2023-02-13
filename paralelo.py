import random  # importo la librería random
from time import sleep  # importo la función sleep de la libreria time¡
from multiprocessing import Pool # importo la clase Pool de la librería multiprocessing

urls = ["a.com", "b.com", "c.com", "d.com", "e.com"]  # creo una lista de urls


def scrape(url):
    print("starting", url)
    duration = round(random.uniform(0, 1), 3)  # arreglo el error de esta línea
    sleep(duration)
    print("finished", url, "time taken:", duration, "seconds")
    return url, duration


if __name__ == '__main__':
    def main():
        eleccion = int(input("¿Quieres ejecutar el programa en paralelo? 1: No, 2: Si: "))

        if eleccion == 1:  # main del programa sin paralelizar
            output = []
            for url in urls:
                result = scrape(url)
                output.append(result)
            print(output)
            main()

        elif eleccion == 2:  # main del programa paralelizado
            pool = Pool(processes=4)  # creo un pool de 4 procesos
            data = pool.map(scrape, urls)  # ejecuto la función scrape en paralelo
            pool.close()  # cierro el pool
            pool.join()  # espero a que todos los procesos terminen
            pool.close()
            for row in data:
                print(row)
            main()
        else:
            print("Opción no válida")
            main()
