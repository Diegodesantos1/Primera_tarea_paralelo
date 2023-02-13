urls = ["a.com", "b.com", "c.com", "d.com"] # creo una lista de urls

import random # importo la librería random
from time import sleep # importo la función sleep de la libreria time

def scrape(url):
    print("starting", url)
    duration = round(random.uniform(0,1),3) #arreglo el error de esta línea
    sleep(duration)
    print("finished", url, "time taken:", duration, "seconds")
    return url, duration

eleccion = int(input("¿Quieres ejecutar el programa en paralelo? 1: No, 2: Si: "))

if eleccion == 1: # main del programa sin paralelizar
    output = []
    for url in urls:
        result = scrape(url)
        output.append(result)
    print(output)

from multiprocessing import Pool # importo la clase Pool de la librería multiprocessing

pool = Pool(processes=4) # creo un pool de 4 procesos
data = pool.map(scrape, urls) # ejecuto la función scrape en paralelo
