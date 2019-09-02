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
#Enter Handbrake CLI Location here Handbrake preset should be in same directory
#runstr = 'handbrakecli -i "{0}" -o "{1}" --preset-import-file drew.json'

print('=======--------=======')

while fileList:
    inFile = fileList.pop()
    fileName, fileExtension = os.path.splitext(inFile)
    outFile = fileName +'.mp4'

#    print('Processing',inFile)
 #   returncode  = subprocess.call(runstr.format(inFile,outFile),shell=True)
#   time.sleep(5)
#    print('Removing',inFile)
#    os.remove(inFile)
#    print('Renaming',inFile)
#    os.rename(outFile,inFile)
#    time.sleep(5)
#    print('Copying ' + inFile + ' to NAS')
    filepath = inFile.split("\\",)
    relativeFilename = filepath[-1]
    renamedFilename = relativeFilename[7:]
    #print('Moving ' + renamedFilename + ' to Sorting Folder')
    #print(filepath[:-1])
    joinedFilepath = filepath[:-1]
    s = "\\"
    joinedFilename = s.join(joinedFilepath)
    trimmedFile = joinedFilename + "\\" + renamedFilename
    os.rename(inFile,trimmedFile)
    print('Renaming ' + trimmedFile)
#    print('relative filepath = ' +filepath[-1])
#    #sourcePath = r'Z:\media\The Sorting Folder\'
#    #networkPath = '\\media\\The Sorting Folder\\'
#    copy2(inFile,'Z:/media/The Sorting Folder/' + relativeFilename,follow_symlinks=True)