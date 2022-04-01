#coding: utf_8
import csv
import glob
import os
import datetime
import pathlib
import sys

targetPath = sys.argv[1]
files = glob.glob(targetPath+"*")

with open("./output.csv","w") as f:
    writer = csv.writer(f)
    writer.writerow(["No.","Document Name","UpdateDate","Path"])
    num = 1

    for file in files:
        print(file)
        fileName = file.split('\\')[-1].split('.')[0]
        updateDate = datetime.datetime.fromtimestamp(os.path.getmtime(file)).strftime("%Y/%m/%d")
        fullPath = pathlib.Path(file).resolve()
        writer.writerow([num,fileName,updateDate,fullPath])
        num = num + 1



