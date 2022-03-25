from pydub import AudioSegment
from pathlib import Path

from full_arrangement import *

# Please choose file reading method yourself, I use pathlib to read
# And I used a combination of name and number to read the file
def read_audios(name,mainpath:Path=Path(__file__).parent,num=4,format="wav"):
    audios = []
    try:
        for i in range(1,num+1):
            audio_path = str(mainpath / f"{name}{i}.{format}")
            audio = AudioSegment.from_file(file=audio_path,format=format)
            audios.append(audio)
    except:
        ...
    return audios

def generate(audios,num=4,format="wav",save_path=None,expand=False,expand_minutes=1800):
    if not save_path:
        save_path = Path(__file__).parent / "generate"
        if not save_path.exists():
            save_path.mkdir(parents=True,exist_ok=True)
    arrange=overlay_arrangement(full_arrangement(num))
    final_audios = []
    for aa in arrange:
        sub_audios = []
        for a in aa:
            final = AudioSegment.empty()
            for i in a:
                final+=audios[int(i)]
            sub_audios.append(final)
        final = sub_audios[0]
        for i in sub_audios[1:]:
            final = final.overlay(i)
        final_audios.append(final)
    final = AudioSegment.empty()
    for i in final_audios:
        final+=i
    save_name = f"final.{format}"
    if expand:
        final_expand = final
        while final_expand.duration_seconds < expand_minutes:
            final_expand += final
        final = final_expand
    final.export(save_path/save_name,format=format)