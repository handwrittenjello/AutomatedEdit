import os
import time
import subprocess
import sys
from shutil import copyfile

fileList = []
rootdir = "/Users/andrewlittlejohn/projects/AutomatedEdit/flask"
for root, subFolders, files in os.walk(rootdir):
    for file in files:
        theFile = os.path.join(root,file)
        fileName, fileExtension = os.path.splitext(theFile)
        if fileExtension.lower() in ('.avi', '.divx', '.flv', '.m4v', '.mkv', '.mov', '.mpg', '.mpeg', '.wmv'):
            print('Adding',theFile)
            fileList.append(theFile)

runstr = '/Users/andrewlittlejohn/bin/HandBrakeCLI -i "{0}" -o "{1}" --preset-import-file drew.json'

print('=======--------=======')

while fileList:
    inFile = fileList.pop()
    fileName, fileExtension = os.path.splitext(inFile)
    outFile = fileName+'1'+'.mkv'

    print('Processing',inFile)
    returncode  = subprocess.call(runstr.format(inFile,outFile),shell=True)
    time.sleep(5)
    print('Removing',inFile)
    os.remove(inFile)
    print('Renaming',inFile)
    os.rename(outFile,inFile)
    print('Copying ' + inFile + ' to NAS')
    filepath = inFile.split("/",)
    relativeFilename = filepath[-1]
    copyfile(inFile,'/Users/andrewlittlejohn/projects/AutomatedEdit/flask/NAS/'+relativeFilename)