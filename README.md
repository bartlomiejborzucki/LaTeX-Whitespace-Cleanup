# LaTeX-Whitespace-Cleanup

This repository contains a Python script for processing .tex files in a given directory, replacing single spaces after short Polish prepositions (like "w", "z", "o", "a", "u", "i") with a non-breaking space (~), to prevent these prepositions from appearing at the end of a line.

## Requirements
To use this script, you need Python 3.6 or later.

## How to Use
Clone this repository to your computer.
Open a terminal and navigate to the repository directory.
Run the script, passing the name of the directory containing the .tex files to process as an argument:
```
python main.py /path/to/directory
Replace /path/to/directory with the path to the directory you want to process.
```
Warning
This script operates "blindly" and it's always a good idea to manually check the results, especially on first run, to make sure it's working correctly for your documents. It's also always a good idea to backup your files before carrying out these kinds of bulk operations on them.