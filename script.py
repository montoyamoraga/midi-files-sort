# Python script for TODO
# December 2021
# runs on Python 3.x on Mac OS 12.0.1

################
# import modules
################

# sys for command line arguments
import sys

# os for listing files and directories
import os

# Path for creating new directories and files
from pathlib import Path

# csv for CSV files
import csv

# pandas for .xls to CSV
import pandas as pd

# mido for MIDI files
from mido import MetaMessage
from mido import MidiFile

###################
# default variables
###################

libraryPathOriginal = "libraryOriginal"
libraryPathNew = "libraryNew"

libraryCSVFileName = "libraryNew.csv"

libraryMetadataFilename = "All_Rolls"
libraryMetadataFolder = "DOCUMENTATION"
libraryMetadataExtensionOriginal = ".xls"
libraryMetadataExtensionNew = ".csv"

# variable for storing the names of each MIDI file
midiFilesNames = []
midiFilesPaths = []

##############################
# create files and directories
##############################

# if it doesnt exist, create new directory for storing the modified library
def createDirectories():
  Path("./" + libraryPathNew).mkdir(parents=True, exist_ok=True)

# create new file with CSV list
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

def createListMIDIFiles():
  with open("./" + libraryPathNew + "/" + libraryCSVFileName, "w", newline="") as csvFile:
    spamwriter = csv.writer(csvFile, delimiter = " ", quotechar='|', quoting=csv.QUOTE_MINIMAL)
    for i in range(len(midiFilesNames)):
      spamwriter.writerow([midiFilesNames[i], midiFilesPaths[i]])

#################################
# parse metadata from AllRolls.xls
#################################

def readLibraryMetadata():

  # read Excel file with pandas
  readXLSFile = pd.read_excel("./" + libraryPathOriginal + "/" + libraryMetadataFolder + "/" + libraryMetadataFilename + libraryMetadataExtensionOriginal)

  # conver to CSV
  readXLSFile.to_csv("./" + libraryPathNew + "/" + libraryMetadataFilename + libraryMetadataExtensionNew, index = None, header = True)

############
# MIDI files
############

# find all MIDI files in libraryOriginal
def findMIDIFiles():
  
  # get current working directory
  cwd = os.getcwd()

  for root, directories, files in os.walk(cwd + "/" +libraryPathOriginal + "/"):
    for filename in files:
      filepath = os.path.join(root, filename)
      # append if it is a filename
      if filepath.endswith(".mid") or filepath.endswith(".MID"):
        midiFilesNames.append(os.path.splitext(os.path.basename(filepath))[0])
        midiFilesPaths.append(filepath)

# open a MIDI file
def readMIDIFile(filename):

  myFile = MidiFile(filename)

  return myFile

# print the meta messages of MIDI file
def printMetaMessages(file):

  for i, track in enumerate(file.tracks):
    print('Track {}: {}'.format(i, track.name))
    for msg in track:
        if msg.is_meta:
          print(msg)

def matchMIDIFiles():
  # go through every MIDI file
  for i in range(len(midiFilesNames)):
    # check if the file is in the list
    print(midiFilesNames[i])

#########
# running
#########

# create directories and files
createDirectories()
createFiles()

# find all MIDI files
findMIDIFiles()

# check the contents and length
# print(midiFilesPaths)
# print(midiFilesNames)
# print(len(midiFilesPaths))
#print(len(midiFilesNames))

# create CSV file with MIDI files
createListMIDIFiles()

# read metadata
readLibraryMetadata()

matchMIDIFiles()

# open a MIDI file
myFile = readMIDIFile("A41emP.mid")

# print meta messages
# printMetaMessages(myFile)

# print the 1th argument of the command line
# print(sys.argv[1:])