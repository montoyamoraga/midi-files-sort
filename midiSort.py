# Python script for TODO
# December 2021
# runs on Python 3.x on Mac OS 12.0.1

################
# import modules
################

# import datetime
from datetime import datetime

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

################################
# retrieve current date and time
################################

def getCurrentDate():
  # retrieve system date
  now = datetime.now()

  # parse
  year = now.strftime("%Y")
  month = now.strftime("%m")
  day = now.strftime("%d")
  hour =  now.strftime("%H")
  minute =  now.strftime("%M")
  second = now.strftime("%S")

  # return YYYYMMDD-HHMMSS
  currentDate = year + month + day + "-" + hour + minute + second
  return currentDate

###################
# default variables
###################

libraryPathOriginal = "libraryOriginal"
libraryPathNew = "library" + getCurrentDate()
libraryPathFiles = "filesRaw"

libraryPathWithSoft = "withSoft"
libraryPathWithoutSoft = "withoutSoft"

libraryCSVFileName = "libraryNew.csv"

libraryMetadataFilename = "All_Rolls"
libraryMetadataFolder = "DOCUMENTATION"
libraryMetadataExtensionOriginal = ".xls"
libraryMetadataExtensionNew = ".csv"

libraryRollsSuffixes = ["emP", "emR"]

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

  Path("./" + libraryPathNew + "/" + libraryPathFiles + "/" + libraryPathWithSoft).mkdir(parents=True, exist_ok=True)

  Path("./" + libraryPathNew + "/" + libraryPathFiles + "/" + libraryPathWithoutSoft).mkdir(parents=True, exist_ok=True)

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
  readXLSFile.to_csv("./" + libraryPathNew + "/" + libraryMetadataFilename + libraryMetadataExtensionNew, index = None, header = True, sep = "\t")

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
    # sort them between with and without soft pedal, according to suffix
    if midiPaths[i][len(midiPaths[i])-7:-4] == "emP":
      shutil.copy(midiPaths[i], './' + libraryPathNew + "/" + libraryPathFiles + "/" + libraryPathWithSoft)
    elif midiPaths[i][len(midiPaths[i])-7:-4] == "emR":
      shutil.copy(midiPaths[i], './' + libraryPathNew + "/" + libraryPathFiles + "/" + libraryPathWithoutSoft)

# check if any of the copied files matches with an entry on AllRolls.csv
def matchMIDIFiles():

  # read All_Rolls.csv, retrieve these columns:

  # column 0 for title
  AllRollsTitles = readCSVFile("./" + libraryPathNew + "/" + libraryMetadataFilename + libraryMetadataExtensionNew, column=0, delimiter= "\t")

  # column 1 for composer
  AllRollsComposer = readCSVFile("./" + libraryPathNew + "/" + libraryMetadataFilename + libraryMetadataExtensionNew, column=1, delimiter= "\t")

  # column 2 for pianist
  AllRollsPianist = readCSVFile("./" + libraryPathNew + "/" + libraryMetadataFilename + libraryMetadataExtensionNew, column=2, delimiter= "\t")

  # column 5 for filenames
  AllRollsNames = readCSVFile("./" + libraryPathNew + "/" + libraryMetadataFilename + libraryMetadataExtensionNew, column=5, delimiter= "\t")

  print(AllRollsNames)

  matches = 0

  print(len(midiFilesShortNames))

  # go through every MIDI file with 1 word
  for i in range(len(midiFilesShortNames)):

    # retrieve filename
    name = midiFilesShortNames[i]

    # check if the filename ends on the suffixes emR or emP
    if name[-3:] in libraryRollsSuffixes:
      # retrieve the name without suffix
      name = name[:-3]

    # go through filenames in All_Rolls
    for i in range(len(AllRollsNames)):

      # check if there is a match
      if (AllRollsNames[i] == name):
        # add to counter
        matches = matches + 1

        # print(AllRollsTitles[i], AllRollsNames[i])

  print(len(AllRollsNames))
  print(matches)

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
# myFile = readMIDIFile("./libraryDummy/A41emP.mid")

# print the 1th argument of the command line
# print(sys.argv[1:])