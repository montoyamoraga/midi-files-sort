# midi-sort

## About

A commisioned project by Aarón Montoya-Moraga.

## Files

* [midiSort.py](./midiSort.py): main file, Python 3 script.
* [midiSort.ipynb](./midiSort.ipynb): work-in-progress port to Jupyter Notebook, made to run on Google Colab.

## Installation

This script runs on Python 3.

To install all required dependencies, run

```bash
pip install -r requirements.txt
```

Place the original library on a new folder called libraryOriginal/

## Result

The script generates the folder libraryNew/, and inside of it:

* All_Rolls.csv: the file from libraryOriginal/ converted to CSV
* files/: all MIDI files with the new metadata from All_Rolls.csv
* librartyNew.csv: a CSV file with two columns: filename, and path. 

The contents of libraryNew/, there is a subfolder files/ with all of the files that 

## License

MIT