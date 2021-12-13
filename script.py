# Python script for TODO
# December 2021
# runs on Python 3.x on Mac OS 12.0.1

# import MidiFile from mido module
from mido import MidiFile

# import M
from mido import MetaMessage


# open the file
myFile = MidiFile("A41emP.mid")

for i, track in enumerate(myFile.tracks):
    print('Track {}: {}'.format(i, track.name))
    for msg in track:
        if msg.is_meta:
          print(msg)

print("hello world")