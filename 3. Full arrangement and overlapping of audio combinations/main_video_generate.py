from moviepy.editor import *
from pathlib import Path
from audio_generate import *

def main(name,isVideo=True):
    base_audio = read_audios(name)
    if not base_audio:
        print("please put your audios in this directory")
        print("And you can update read_audios() in audio_generate")
        return
    generate(base_audio)
    if isVideo:
        audio = Path(__file__).parent / "generate" / "final.wav"
        img = Path(__file__).parent / "img.bmp"
        if not img.exists():
            print("please put your image in this directory")
            return
        output = str(Path(__file__).parent / "generate" / "output.mp4")

        audio = AudioFileClip(audio)
        img = ImageClip(img).set_duration(audio.duration)
        img.audio = CompositeAudioClip([audio])

        img.write_videofile(output,fps=24)
    print("done")

main("xx")