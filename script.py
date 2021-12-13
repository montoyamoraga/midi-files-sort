# Python script for TODO
# December 2021
# runs on Python 3.x on Mac OS 12.0.1

# imports from mido module
from mido import MetaMessage
from mido import MidiFile


# TODO add arguments for command line

###########
# CSV files
###########


############
# MIDI files
############


# open MIDI file
def readMIDIFile(filename):

  myFile = MidiFile(filename)

  return myFile

def printMetaMessages(file):

  for i, track in enumerate(myFile.tracks):
    print('Track {}: {}'.format(i, track.name))
    for msg in track:
        if msg.is_meta:
          print(msg)

#########
# running
#########

# open a file
readMIDIFile("A41emP.mid")