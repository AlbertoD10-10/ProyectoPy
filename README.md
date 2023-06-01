# ProyectoPy
Proyecto final Organizacion de Computadores

## Tutorial para correr el programa:
Se debe tener instalado la libreria de python "pydub" y la aplicaion de "ffmpeg".
Existen dos versiones del programa, en la primera version hacemos la mezcla manualmente, sumando bit por bit los dos archivos de audio y multiplicandolo por la ganancia. En la segunda version usamos la funcion de pydub "overlay)
para hacer la mezcla.

Para correr la version 1 en paralelo, se escribe desde la terminal:
```
python audiomixer1.py ruta_del_archivo1.mp3 ruta_del_archivo_2.mp3 rutadel_archivo_mezclado.mp3
```
y en secuencial:
```
python audiomixer1.py ruta_del_archivo1.mp3 -s ruta_del_archivo_2.mp3 rutadel_archivo_mezclado.mp3
```

Para correr la version 2 en paralelo, se escribe desde la terminal:
```
python audiomixer2.py ruta_del_archivo1.mp3 ruta_del_archivo_2.mp3 rutadel_archivo_mezclado.mp3
```
y en secuencial:
```
python audiomixer2.py ruta_del_archivo1.mp3 -s ruta_del_archivo_2.mp3 rutadel_archivo_mezclado.mp3
```

En este excel podemos ver la mejora de rendimiento al usar paralelismo, la mejora sería mas significativa si tuvieramos que leer más datos
![image](https://github.com/AlbertoD10-10/ProyectoPy/assets/67118511/62d6970f-1afe-42f4-941a-25cc42d50b9a)
