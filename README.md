# midi-sort

## About

A commisioned project by Aarón Montoya-Moraga and Benjamín Rámila.

## Repository contents
* [assets/](./assets): graphic assets for the project
  * ampico.jpg: By Daderot - Own work, CC0, https://commons.wikimedia.org/w/index.php?curid=29195477. Cropped to a square 600x600.
  * duo-art.jpg: By sguastevi - Own work, CC BY-SA 3.0, https://commons.wikimedia.org/w/index.php?curid=42104088. Cropped to a square 600x600.
  * welte-licensee.jpg: By Les Chatfield - originally posted to Flickr as Steinway Welte, CC BY 2.0, https://commons.wikimedia.org/w/index.php?curid=11806616. Cropped to a square 600x600.
  * welte-t-100.jpg: CC BY-SA 3.0, https://commons.wikimedia.org/w/index.php?curid=625786. Cropped to a square 600x600.
* [midiSort.py](./midiSort.py): main file, Python 3 script.
* [midiSort.ipynb](./midiSort.ipynb): work-in-progress port to Jupyter Notebook, made to run on Google Colab.
* [requirements.txt](./requirements.txt): file for installing Python 3 dependencies.

## Database polishing

I went through all of the database
Replaced double quotes "" with parenthesis ()
Replaced ampersand & and slash / with dash -
Downloaded as All_Rolls_modified.xlsx

## Software installation

This script runs on Python 3. I recommend using a virtual environment for the dependencies.

To install all required modules, run:

```bash
pip install -r requirements.txt
```

## Folder setup

* Place the original library on a new folder called libraryOriginal/

## Running the script

notas cliente 14 febrero:

* cliente solamente pudo abrir 2 carpetas: la welte-licensee y la welte-t-100.
* las otras dos, ampico y duo-art, no pudo cargarlas, por formato de archivo.
* hay 4 columnas de info en el ipad, pero cliente ve 3, y de esas dejamos la mas importante fuera.
* nombre de la canción está bien
* la info del artista la pusimos en el álbum
* la info de álbum, cliente dice que debe ser compositor, la pusimos como tipo piano 
* la info del tipo de piano se podría poner en genre, que es la columna vacía
* segundo mensaje
* donde deberia estar el artista, esta en el album
* el album deberia ser donde esta el compositor
* en genre, que esta vacio, deberian estar los tipos de piano
* con eso, album seria compositor

## Last version 2022 March 03

* the code is working, after All_Rolls_modified.xlsx was created with typo corrections.
* there is still one redundant for loop, so after the library is sorted, there are still folders for each piano roll maker, "ampico, duo-art, welte-t-100, welte-licensee", that need to be deleted, that's it!

## Result

TODO: update to latest version

The script generates the folder libraryYYYMMDD-HHMMSS/, and inside of it:

* All_Rolls.csv: the file from libraryOriginal/ converted to CSV
* files/: all MIDI files with the new metadata from All_Rolls.csv
* libraryNew.csv: a CSV file with two columns: filename, and path. 

The contents of libraryNew/, there is a subfolder files/ with all of the files that 

## License

MIT