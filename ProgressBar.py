import fnmatch, os, tkinter, tqdm
from tkinter import filedialog
from tqdm import tqdm
root = tkinter.Tk()
root.withdraw()
print ("Please select the directory containing the LAS files you are using for the dataset.")
workingpath = filedialog.askdirectory()
las_count = len(fnmatch.filter(os.listdir(workingpath), '*.las'))
lasx_count = 0
pbar = tqdm(total = las_count)
while lasx_count != las_count:
	lasx_count = len(fnmatch.filter(os.listdir(workingpath), '*.lasx'))
	pbar.n = lasx_count
	pbar.update(0)
