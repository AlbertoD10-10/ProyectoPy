from pydub import AudioSegment
import multiprocessing as mp
import os
import time
import sys

def leer_cancion(cancion_path):
    cancion = AudioSegment.from_mp3(cancion_path)
    return cancion

def combinar_canciones(canciones, name):
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
    cancion_combinada.export(name, format='mp3')

    print("¡Las canciones se han combinado correctamente!")



def paralelo(file_1, file_2, name):
    
    start = time.time()

    #path_1 = "files/"+file_1
    #path_2 = "files/"+file_2

    # Obtener la lista de rutas de las canciones
    canciones_paths = [
        file_1,
        file_2
    ]


     # Cantidad de cores de la máquina
    cores = os.cpu_count()
    print("Su máquina tiene", cores, "cores.")

    # Crear el objeto Pool con la cantidad de procesos deseados
    with mp.Pool() as pool:

    # Leer las canciones en paralelo utilizando pool.map()
        canciones = pool.imap_unordered(leer_cancion, canciones_paths)
        print("¡Las lecturas se han ejecutado en paralelo!")
        pool.close()
        pool.join()
    # Combinar las canciones
        #combinacion = pool.imap_unordered(combinar_canciones, canciones)
    res = mp.Process(target=combinar_canciones, args = (canciones, name))
    res.run()
    end = time.time()
    print("\nLos archivos se leyeron en(s):", end - start)


    

def secuencial(file_1, file_2, name):
    start = time.time()

    #path_1 = "files/"+file_1
    #path_2 = "files/"+file_2

    #canciones_paths = [
    #    "files/Duvet.mp3",
    #    "files/UN_OWEN_WAS_HER.mp3"
    #]
    audio1 = leer_cancion(file_1)
    audio2 = leer_cancion(file_2)
    #audio3 = leer_cancion(canciones_paths[2])
    #audio4 = leer_cancion(canciones_paths[3])
    print("¡Las lecturas se han ejecutado de manera secuencial!")
    canciones = [audio1, audio2]
    combinar_canciones(canciones, name)
    end = time.time()
    print("\nEl archivo se leyo en(s):", end - start)


def main():
    # Recuperar los argumentos de línea de comandos
    argumentos = sys.argv
    print(argumentos)

    # Comprobar si se proporcionaron suficientes argumentos
    if len(argumentos) < 3:
        print("Se requieren al menos 2 archivo para realizar la mezcla")
        sys.exit(1)
    elif argumentos[1] == "-s":
        if len(argumentos) == 5:
            secuencial(argumentos[2], argumentos[3], argumentos[4])
        elif len(argumentos) == 4:
            secuencial(argumentos[2], argumentos[3], "audio_mixer.mp3")

    else:
        if len(argumentos) == 4:
            paralelo(argumentos[1], argumentos[2], argumentos[3])
        elif len(argumentos) == 3:
            paralelo(argumentos[1], argumentos[2], "audio_mixer.mp3")

        


if __name__ == '__main__':
    main()



   