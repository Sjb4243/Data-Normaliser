"""
The concept for this code was taken from - https://github.com/XiaoMutt/XiaoImageJApp. 
The python rewrite for the Dr Tim Davies lab was primarily completed by:
Abdurrahmaan Iqbal - https://github.com/abmyii
Sam Bennett - Durham University
"""
from tkinter.filedialog import askopenfile
from tkinter.simpledialog import askinteger
from tkinter import Tk
import math
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
import time
NormalizedLength = askinteger("Normalise", "What length do you want to normalise to?")
print("Select a .CSV file")
base = askopenfile()
data = pd.read_csv(base)
path = os.path.abspath(base.name)
#initialising variables,list and writer
extension = path.split("/")[-1]
filename = extension.split(".")[0]
normalised_filename = filename + "_normalised" + ".xlsx"
writer = pd.ExcelWriter(normalised_filename, engine="xlsxwriter")

#reading in data

column_no = int(len(data.columns))
finallist = [[0] for i in range(column_no)]

for i in range(column_no):
    single_column = data.iloc[:, i]
    single_column = single_column.dropna()
    scale = (len(single_column) - 1.0) / (NormalizedLength - 1.0)
    x = np.interp(np.arange(0, len(single_column), scale), np.arange(0, len(single_column)), single_column)
    finallist[i] = x
    plt.plot(range(0, NormalizedLength), x)
print("Close plot to save excel file")
plt.show()
final = pd.DataFrame(finallist)
final = final.transpose()
final.to_excel(writer, sheet_name="sheet1")
print(f"Saving file to {normalised_filename}")
time.sleep(3)
writer.close()