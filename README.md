# system-cleaner

## Description
System Cleaner:
  - organizes folders
  - cleans up temporary files

## Requirements
Requires Python 3.5.x+. No external packages required.

## Working
Files in the selected folder are sorted depending on their extension/size. Some categories: Videos, Music, Movies etc.

## Usage
Open the 'app-interface.pyw' file, and navigate to the required module. The file for the required module can also be run separately.

## Important Note
On non-Windows systems, the program will try to sort any folder selected, including folders that are crucial to system functioning. In Windows, although most important folders are added to exception, there might be exceptional cases or folders that I missed. Please make sure that you do not select any system folder.
(Meanwhile, any help with identifying system-important folders in different OSes will be appreciated)

## Adding/Modifying Sorting Rules
Sorting rules can be added/modified in the 'folder_sort_GUI.pyw' file.
In class 'App', the if conditions can be used to play around with the sorting rules.

## Debugging and Console
To open the programs with console, change file extensions to '.py'.

## Known Bugs
  - Program exits with fatal error when file names contain non-latin characters.
