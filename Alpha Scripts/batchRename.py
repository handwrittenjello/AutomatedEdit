import os
import time
import subprocess
import sys
from shutil import copy2

fileList = []
current = os.getcwd()
rootdir = current
for root, subFolders, files in os.walk(rootdir):
    for file in files:
        theFile = os.path.join(root,file)
        fileName, fileExtension = os.path.splitext(theFile)
        if fileExtension.lower() in ('.avi', '.divx', '.flv', '.m4v', '.mkv', '.mov', '.mpg', '.mpeg', '.wmv', '.mp4'):
            print('Adding',theFile)
            fileList.append(theFile)



print('=======--------=======')

while fileList:
    inFile = fileList.pop()
    fileName, fileExtension = os.path.splitext(inFile)
    #File name extention will need to be updated
    outFile = fileName +'.mp4'

    #Splits file int to multiple directory and convers them to list to extract the filename
    filepath = inFile.split("\\",)
    relativeFilename = filepath[-1]
    renamedFilename = relativeFilename[7:]
    
    joinedFilepath = filepath[:-1]
    s = "\\"
    joinedFilename = s.join(joinedFilepath)
    trimmedFile = joinedFilename + "\\" + renamedFilename
    os.rename(inFile,trimmedFile)
    print('Renaming ' + trimmedFile)
