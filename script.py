# Python script for TODO
# December 2021
# runs on Python 3.x on Mac OS 12.0.1

##################
# import libraries
##################

# sys for command line arguments
import sys

# csv module for CSV
import csv

# mido module for MIDI
from mido import MetaMessage
from mido import MidiFile

###########
# CSV files
###########

def readCSVFile(filename):
  with open(filename, newline='') as myCSVFile:
    reader = csv.reader(myCSVFile, delimiter='', quotechar='|')
    for row in reader:
      print(', '.join(row))

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

# open a MIDI file
readMIDIFile("A41emP.mid")

# print the 1th argument of the command line
print(sys.argv[1])