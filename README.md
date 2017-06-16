# system-cleaner

## Description
System Cleaner:
  - organizes folders
  - cleans up temporary files

## Requirements
Requires Python 3.5.x+. Should work in 3+ versions, but not tested.
No external packages required.

## Working
Files in the selected folder are sorted depending on their extension/size. Some categories: Videos, Music, Movies etc.

## Usage
Open the 'app-interface.pyw' file, and navigate to the required module. The file for the required module can also be run separately.

## Important Note
On non-Windows systems, the program will try to sort any folder selected, including folders that are crucial to system functioning. In Windows, although most important folders are added to exception, there might be exceptional cases or folders that I missed. Please make sure that you do not select any system folder.
(Meanwhile, any help with identifying system-important folders in different OSes will be appreciated).

## Adding/Modifying Sorting Rules
Sorting rules can be added/modified in the 'folder_sort_GUI.pyw' file.
In class 'App', the if conditions can be used to play around with the sorting rules.

## Opening GUI Window without console
This can be done easily on Windows by simply changing the file extensios to '.pyw'.  
**Remember**: This only works on Windows.

## Debugging and Console
Simply launch the script from the terminal:
```bash
python3 app_interface.py
```
Errors and exceptions (if any) will be printed on the terminal window.

## Contributing
Clone the repository locally:
```bash
git clone https://github.com/nikramakrishnan/system-cleaner.git
```
and dive into the code! The code relatively is simple to understand with lots of comments that explain what that function/line does.  
If you have fixed bugs or added new features, please fork the repository and open a pull request!

## Known Bugs
  - All known bugs have been fixed. Please check the **Issues** tab for more information and new bugs.
