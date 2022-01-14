# midi-sort

## About

A commisioned project by Aarón Montoya-Moraga.

## Repository contents

* [midiSort.py](./midiSort.py): main file, Python 3 script.
* [midiSort.ipynb](./midiSort.ipynb): work-in-progress port to Jupyter Notebook, made to run on Google Colab.
* [requirements.txt](./requirements.txt): file for installing Python 3 dependencies.

## Software installation

This script runs on Python 3. I recommend using a virtual environment for the dependencies.

To install all required modules, run:

```bash
pip install -r requirements.txt
```

## Folder structure

Place the original library on a new folder called libraryOriginal/

## Result

The script generates the folder libraryNew/, and inside of it:

* All_Rolls.csv: the file from libraryOriginal/ converted to CSV
* files/: all MIDI files with the new metadata from All_Rolls.csv
* librartyNew.csv: a CSV file with two columns: filename, and path. 

The contents of libraryNew/, there is a subfolder files/ with all of the files that 

## License

MIT