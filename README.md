# LASDProgressBar
This python script will generate a more accurate progress bar for the Create LAS Dataset tool in ESRI's ArcGIS Pro.


To use, verify that you have the python package tqdm installed. 
If not installed, open PowerShell, cd to your python scripts directory ("cd C:\Python38\Scripts") and run the command "pip install tqdm".
Now open command prompt and run the python script ("python C:\Users\USERNAME\Downloads\ProgressBar.py)
When the file explorer window opens, select the directory in which the .las files reside that you will be using to generate your LAS Dataset.
This script can be started before or after the Create LAS Dataset tool is started. The closer you start the script to the tool, the more accurate the timer.
