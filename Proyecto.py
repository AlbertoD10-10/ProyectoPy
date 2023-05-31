from pydub import AudioSegment
import multiprocessing as mp
import time

def leer_cancion(cancion_path):

    cancion = AudioSegment.from_mp3(cancion_path)

    return cancion

def combinar_canciones(canciones):
    
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
    cancion_combinada.export("f5.mp3", format='mp3')
    print("combinaciom exitosa")



def paralelo():
    
    start = time.time()
    # Obtener la lista de rutas de las canciones
    canciones_paths = [
        
        "files/september.mp3",
        "files/dross.mp3"


    ]



    # Crear el objeto Pool con la cantidad de procesos deseados
    with mp.Pool() as pool:

    # Leer las canciones en paralelo utilizando pool.map()
        canciones = pool.imap_unordered(leer_cancion, canciones_paths)
        print("Las lecturas se han ejecutado en paralelo")

    # Combinar las canciones
        pool.imap(combinar_canciones, canciones)
        #combinar_canciones(canciones)
    end = time.time()
    print("\nEl archivo se leyo en(s):", end - start)

def secuencial():
    start = time.time()
    canciones_paths = [
        "files/dross.mp3",
        "files/september.mp3",
        "files/Duvet.mp3",
        "files/UN_OWEN_WAS_HER.mp3"

    ]
    audio1 = leer_cancion(canciones_paths[0])
    audio2 = leer_cancion(canciones_paths[1])

    canciones = [audio1,audio2]
    combinar_canciones(canciones)
    end = time.time()
    print("\nEl archivo se leyo en(s):", end - start)

def main():
    paralelo()

if _name_ == '_main_':
    main()