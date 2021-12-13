# import MidiFile from mido module
from mido import MidiFile

from mido import MetaMessage

# open the file
myFile = MidiFile("A41emP.mid")

for i, track in enumerate(myFile.tracks):
    print('Track {}: {}'.format(i, track.name))
    for msg in track:
        if msg.is_meta:
          print(msg)

print("hello world")