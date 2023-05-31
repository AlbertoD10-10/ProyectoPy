from pydub import AudioSegment
import multiprocessing as mp
import time
import numpy as np
ganancia = 0.5

def leer_cancion(cancion_path):

    cancion = AudioSegment.from_mp3(cancion_path)

    return cancion

def combinar_canciones(canciones):
    start = time.time()
    
    # Combinar las canciones
    listaCanciones = list(canciones)

    arrayaudio1 = listaCanciones[0].get_array_of_samples()
    arrayaudio2 = listaCanciones[1].get_array_of_samples()

    sizearrayaudio1 = len(arrayaudio1)
    sizearrayaudio2 = len(arrayaudio2)
    

    
    if(sizearrayaudio1 > sizearrayaudio2):   

        for i in range(sizearrayaudio1-sizearrayaudio2):
            arrayaudio2.append(0)

        
        
    else:

        for i in range(sizearrayaudio2-sizearrayaudio1):
            arrayaudio1.append(0)


    temp = np.array(arrayaudio1)
    for i in range(len(temp)):
        #resultado_array[i] = np.int16((audio1_array[i]+audio2_array[i])*ganancia)
        temp[i] = (arrayaudio1[i] + arrayaudio2[i])*ganancia
    resultado_audio = AudioSegment(
        temp.tobytes(),
        frame_rate=listaCanciones[0].frame_rate,
        sample_width=2,
        channels=listaCanciones[0].channels
    )


        
    #cancion_combinada = longer.overlay(shorter)


    # Guardar la canción combinada en un archivo MP3
    resultado_audio.export("files/f3.mp3", format='mp3')
    print("combinacion exitosa")
    end = time.time()
    print("Las canciones se combinaron en(s):", end - start)



def paralelo():
    
    
    # Obtener la lista de rutas de las canciones
    canciones_paths = [
        "files/acapella.mp3",
        "files/instrumental.mp3",
    ]



    # Crear el objeto Pool con la cantidad de procesos deseados
    with mp.Pool() as pool:

    # Leer las canciones en paralelo utilizando pool.map()
        canciones = pool.imap_unordered(leer_cancion, canciones_paths)
        print("Las lecturas se han ejecutado en paralelo")
        pool.close()
        pool.join()

    # Combinar las canciones
    res = mp.Process(target=combinar_canciones,args=(canciones,))
    res.run()

def secuencial():
    start = time.time()
    canciones_paths = [
        "files/dross.mp3",
        "files/september.mp3"
    ]
    audio1 = leer_cancion(canciones_paths[0])
    audio2 = leer_cancion(canciones_paths[1])


    canciones = [audio1,audio2]
    combinar_canciones(canciones)
    end = time.time()
    print("\nEl archivo se leyo en(s):", end - start)

def main():
    start = time.time()
    paralelo()
    end = time.time()
    print("El tiempo total es(s):", end - start)


if __name__ == '__main__':
    main()