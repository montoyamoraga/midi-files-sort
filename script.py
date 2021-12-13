# Python script for TODO
# December 2021
# runs on Python 3.x on Mac OS 12.0.1

# imports from mido module
from mido import MetaMessage
from mido import MidiFile



# open MIDI file
def readMIDIFile(filename):

  myFile = MidiFile(filename)

  for i, track in enumerate(myFile.tracks):
    print('Track {}: {}'.format(i, track.name))
    for msg in track:
        if msg.is_meta:
          print(msg)


def testing():
  print("hello world")

# print
testing()

# open a file
readMIDIFile("A41emP.mid")