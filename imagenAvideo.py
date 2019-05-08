"""imagenAvideo

Usage:
  imagenAvideo.py --duracion=<duracion> --nombre_extension=<nombre_extension>

Options:
  -h --help     Show this screen.

"""
from docopt import docopt
from pathlib import Path          
from moviepy.editor import *

def imagen_clip(duracion, nombre_extension):
    directorio = Path('.')
    clips = []

    for archivo in directorio.iterdir():
        if archivo.is_file() and archivo.name.endswith(('.jpg','.png', '.jpeg')):
            archivo = str(archivo)
            clip = ImageClip(archivo, duration=duracion)
            clips.append(clip)
    final = concatenate_videoclips(clips)
    mivideo = nombre_extension
    final.write_videofile(mivideo, fps=15)

if __name__ == '__main__':
    argumentos = docopt(__doc__)
    #print(argumentos)
    duracion = float(argumentos['--duracion'])
    nombre_extension = argumentos['--nombre_extension']
    imagen_clip(duracion, nombre_extension)
#python3 imagenAvideo.py --duracion=3 --nombre_extension=aguspoli.mp4
