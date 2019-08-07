import os
import time
import subprocess
import sys

fileList = []
rootdir = "E:\To Transfer From Storage\To Transcode"
for root, subFolders, files in os.walk(rootdir):
    for file in files:
        theFile = os.path.join(root,file)
        fileName, fileExtension = os.path.splitext(theFile)
        if fileExtension.lower() in ('.avi', '.divx', '.flv', '.m4v', '.mkv', '.mov', '.mpg', '.mpeg', '.wmv'):
            print('Adding',theFile)
            fileList.append(theFile)
#Enter Handbrake CLI Location here Handbrake preset should be in same directory
runstr = 'handbrakecli -i "{0}" -o "{1}" --preset-import-file drew.json'

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