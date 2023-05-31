from pydub import AudioSegment
import numpy as np

def mezclar_audios(audio1, audio2, ganancia):
    # Cargar los archivos de audio
    audio1 = AudioSegment.from_file(audio1, format="mp3")
    audio2 = AudioSegment.from_file(audio2, format="mp3")

    # Obtener las duraciones de los archivos de audio
    arrayaudio1 = audio1.get_array_of_samples()
    arrayaudio2 = audio2.get_array_of_samples()
    sizearrayaudio1 = len(arrayaudio1)
    sizearrayaudio2 = len(arrayaudio2)
    
    print("duracion audio1: ",sizearrayaudio1)
    print("duracion audio2: ",sizearrayaudio2)    #diferencia_duracionesms = (duracion_audio2 - duracion_audio1) *1000 # conversion a ms
    # Ajustar la duración del audio más corto agregando silencio al final
    if len(arrayaudio1) < len(arrayaudio2):
    
        for i in range(len(arrayaudio2)-len(arrayaudio1)):
            arrayaudio1.append(0)

        print("duracion audio1: ",len(arrayaudio1))
        print("duracion audio2: ",len(arrayaudio2))
        #print(audio1.duration_seconds)
    #    audio1 = audio1 + AudioSegment.silent(duration=diferencia_duracionesms)
        #print(audio1.duration_seconds)
    elif len(arrayaudio1) > len(arrayaudio2):

        for i in range(sizearrayaudio1-sizearrayaudio2):
            arrayaudio2.append(0)
        
        print("duracion audio1: ",len(arrayaudio1))
        print("duracion audio2: ",len(arrayaudio2))
    else:
        print("son iguales")
    # Obtener los datos de audio como arrays numpy
    audio1_array = np.array(arrayaudio1,dtype=np.int16)
    audio2_array = np.array(arrayaudio2,dtype=np.int16)

    # Mezclar los audios sumando los arrays y aplicando la ganancia
    resultado_array = np.copy(audio1_array)
    for i in range(len(audio1_array)):
        #resultado_array[i] = np.int16((audio1_array[i]+audio2_array[i])*ganancia)
        resultado_array[i] = (arrayaudio1[i] + arrayaudio2[i])*ganancia
    # Crear un nuevo objeto AudioSegment a partir del array mezclado
    resultado_audio = AudioSegment(
        resultado_array.tobytes(),
        frame_rate=audio1.frame_rate,
        sample_width=2,
        channels=audio1.channels
    )

    return resultado_audio

# Ejemplo de uso
audio1_path = "/home/simon/dev/organizacion_computadores/proyecto_audio2/files/dross.mp3"
audio2_path = "/home/simon/dev/organizacion_computadores/proyecto_audio2/files/september.mp3"
ganancia = 0.2  # Ajusta el valor de la ganancia según tus necesidades

audio_resultante = mezclar_audios(audio1_path, audio2_path, ganancia)
audio_resultante.export("files/audio_resultanteNew.mp3", format="mp3")