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

# shutil for copy and paste files
import shutil

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
libraryPathFiles = "files"

libraryCSVFileName = "libraryNew.csv"

libraryMetadataFilename = "All_Rolls"
libraryMetadataFolder = "DOCUMENTATION"
libraryMetadataExtensionOriginal = ".xls"
libraryMetadataExtensionNew = ".csv"

# variable for storing the names of each MIDI file
midiFilesNames = []
midiFilesPaths = []

# variable for storing a subset of MIDI files: only 1 word ones
midiFilesShortNames = []
midiFilesShortPaths = []

##############################
# create files and directories
##############################

# if it doesnt exist, create new directory for storing the modified library
def createDirectories():

  Path("./" + libraryPathNew + "/" + libraryPathFiles).mkdir(parents=True, exist_ok=True)

# create new file with CSV list
def createFiles():
  newFile = open("./" + libraryPathNew + "/" + libraryCSVFileName, "w")
  writer = csv.writer(newFile)
  newFile.close()

###########
# CSV files
###########

def readCSVFile(filename, column, delimiter):
  with open(filename, newline='') as myCSVFile:
    reader = csv.reader(myCSVFile, delimiter=delimiter, quotechar='|')
    result = []
    for row in reader:
      result.append(row[column])
    return result

def createListMIDIFiles():
  with open("./" + libraryPathNew + "/" + libraryCSVFileName, "w", newline="") as csvFile:
    csvWriter = csv.writer(csvFile, delimiter = " ", quotechar='|', quoting=csv.QUOTE_MINIMAL)
    for i in range(len(midiFilesShortNames)):
      csvWriter.writerow([midiFilesShortNames[i], midiFilesShortPaths[i]])

#################################
# parse metadata from AllRolls.xls
#################################

def readLibraryMetadata():

  # read Excel file with pandas
  readXLSFile = pd.read_excel("./" + libraryPathOriginal + "/" + libraryMetadataFolder + "/" + libraryMetadataFilename + libraryMetadataExtensionOriginal)

  # convert to CSV
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
        # append them to the list
        midiFilesNames.append(os.path.splitext(os.path.basename(filepath))[0])
        midiFilesPaths.append(os.path.relpath(filepath))
        # append to the shorter list if they are only one word
        if (len(os.path.splitext(os.path.basename(filepath))[0].split()) == 1):
          midiFilesShortNames.append(os.path.splitext(os.path.basename(filepath))[0])
          midiFilesShortPaths.append(os.path.relpath(filepath))

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

# copy MIDI files from original folder to new folder
# only do the 1 word ones
def copyMIDIFiles():
  # retrieve paths of original MIDI files
  midiPaths = readCSVFile("./" + libraryPathNew + "/" + libraryCSVFileName, column=1, delimiter=" ")
  # copy them to the new library
  for i in range(len(midiPaths)):
    shutil.copy(midiPaths[i], './' + libraryPathNew + "/" + libraryPathFiles)

def matchMIDIFiles():
  # go through every MIDI file with 1 word
  for i in range(len(midiFilesShortNames)):
    # check if the file is in the All_Rolls.csv file
    print(midiFilesShortNames[i])

  # read All_Rolls.csv
  AllRolls = readCSVFile("./" + libraryPathNew + "/" + libraryMetadataFilename + libraryMetadataExtensionNew, column=1, delimiter= ",")
  print(AllRolls)
    

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
# print(len(midiFilesNames))

# create CSV file with MIDI files
createListMIDIFiles()

# read metadata
readLibraryMetadata()

# copy MIDI files from original to new
copyMIDIFiles()

# see if there is a match in the MIDI files and the All_Rolls.csv file
matchMIDIFiles()

# open a MIDI file
myFile = readMIDIFile("A41emP.mid")

# print meta messages
# printMetaMessages(myFile)

# print the 1th argument of the command line
# print(sys.argv[1:])