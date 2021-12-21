# Python script for TODO
# December 2021
# runs on Python 3.x on Mac OS 12.0.1

##################
# import libraries
##################

# sys module for command line arguments
import sys

# os for creating new directories and files
from pathlib import Path

# csv module for CSV
import csv

# mido module for MIDI
from mido import MetaMessage
from mido import MidiFile

###################
# default variables
###################

libraryPathOriginal = "library"
libraryPathNew = "libraryNew"

libraryCSVFileName = "libraryNew.csv"

##############################
# create files and directories
##############################

# if it doesnt exist, create new directory for storing the modified library
def createDirectories():
  Path("./" + libraryPathNew).mkdir(parents=True, exist_ok=True)

# create new file for 
def createFiles():
  newFile = open("./" + libraryPathNew + "/" + libraryCSVFileName, "w")
  writer = csv.writer(newFile)
  newFile.close()

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

# print the meta messages of it
def printMetaMessages(file):

  for i, track in enumerate(file.tracks):
    print('Track {}: {}'.format(i, track.name))
    for msg in track:
        if msg.is_meta:
          print(msg)

#########
# running
#########

# create directories and files
createDirectories()
createFiles()

# open a MIDI file
myFile = readMIDIFile("A41emP.mid")

# print meta messages
printMetaMessages(myFile)

# print the 1th argument of the command line
print(sys.argv[1:])