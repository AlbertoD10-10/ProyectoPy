from pydub import AudioSegment
import multiprocessing as mp
import time
import sys
import os

def leer_cancion(cancion_path):

    cancion = AudioSegment.from_mp3(cancion_path)

    return cancion

def combinar_canciones(canciones):
    start = time.time()
    
    # Combinar las canciones
    listaCanciones = list(canciones)
    if(listaCanciones[0].duration_seconds > listaCanciones[1].duration_seconds):   #Es mas rapido usar .duration_seconds que len()
        longer = listaCanciones[0]
        shorter = listaCanciones[1]
    else:
        longer = listaCanciones[1]
        shorter = listaCanciones[0]
    cancion_combinada = longer.overlay(shorter)


    # Guardar la canción combinada en un archivo MP3
    cancion_combinada.export("f3.mp3", format='mp3')
    print("combinacion exitosa")
    end = time.time()
    print("Las canciones se combinaron en(s):", end - start)



def paralelo(file1,file2):
    
    
    # Obtener la lista de rutas de las canciones
    canciones_paths = [
        file1,
        file2,
    ]



    # Crear el objeto Pool con la cantidad de procesos deseados
    with mp.Pool() as pool:

    # Leer las canciones en paralelo utilizando pool.map()
        canciones = pool.imap_unordered(leer_cancion, canciones_paths)
        print("Las lecturas se han ejecutado en paralelo")
        pool.close()
        pool.join()

    # Combinar las canciones
        #pool.imap(combinar_canciones, canciones)
        #combinar_canciones(canciones)
    res = mp.Process(target=combinar_canciones,args=(canciones,))
    res.run()

def secuencial(file1,file2):
    start = time.time()
    canciones_paths = [
        file1,
        file2
    ]
    audio1 = leer_cancion(canciones_paths[0])
    audio2 = leer_cancion(canciones_paths[1])

    canciones = [audio1,audio2]
    combinar_canciones(canciones)
    end = time.time()
    print("\nEl archivo se leyo en(s):", end - start)

def main():
    argumentos = sys.argv
    print(argumentos)

    # Comprobar si se proporcionaron suficientes argumentos
    if len(argumentos) < 3:
        print("Se requieren al menos 2 archivo para realizar la mezcla")
        sys.exit(1)
    elif argumentos[1] == "-s":
        secuencial(argumentos[2], argumentos[3])
    else:
        paralelo(argumentos[1], argumentos[2])


if __name__ == '__main__':
    main()