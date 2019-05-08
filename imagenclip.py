from pathlib import Path                                           
from moviepy.editor import *                                       

directorio =  Path('.')                                            

clips = []                                                         

for archivo in directorio.iterdir(): 
    if archivo.is_file() and archivo.name.endswith(('.jpg','.png', '.jpeg')): 
        archivo = str(archivo) 
        clip = ImageClip(archivo, duration=5) 
        clips.append(clip)                                                                    

final = concatenate_videoclips(clips)                              
final.write_videofile("mivideo.mp4", fps=15)

