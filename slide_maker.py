"""imagenAvideoAudio

Usage:
    {} <directorio> [--duracion=<duracion>] [--audio=<audio>] [--tamaño=<tamaño>]

Options:
  -h --help                 Show this screen.
  --duracion=<duracion>     Duracion por imagen [default: 3].
  --tamaño=<tamaño>         Tamaño del video  [default=500, 600]

"""
from docopt import docopt
from pathlib import Path
from moviepy.editor import *


def imagen_clip(directorio, duracion, audio=None, tamaño=(500, 600)):
    directorio = Path(directorio)
    clips = []

    for archivo in directorio.iterdir():
        if archivo.is_file() and archivo.name.endswith(('.jpg','.png', '.jpeg')):
            archivo = str(archivo)
            clip = ImageClip(archivo, duration=duracion).resize(tamaño)
            clips.append(clip)

    final = concatenate_videoclips(clips)
    t = len(clips) * duracion
    if audio:
        miaudio = AudioFileClip(audio)
        miaudio = miaudio.set_duration(t)
        final = final.set_audio(miaudio)

    final.write_videofile(f'{directorio}.mp4', fps=15)


if __name__ == '__main__':
    argumentos = docopt(__doc__.format(__file__))
    #print(argumentos)
    duracion = float(argumentos['--duracion'])
    directorio = argumentos['<directorio>']
    audio = argumentos['--audio']
    tamaño = argumentos['--tamaño']
    tamaño = [int(v) for v in tamaño.split(',')]

    imagen_clip(directorio, duracion, audio, tamaño)
#python3 imagenAvideoAudio.py --duracion=3 --nombre_extension=aguspoli.mp4
