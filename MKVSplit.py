
import subprocess
print('Please enter the name of the file you would like to edit:')
filenameInput = input()
print('Please enter the start of the First Fight')
firstFightStartInput = input()
firstFightStart = firstFightStartInput[:2] + ':' + firstFightStartInput[2:4] + ':' + firstFightStartInput[4:6]
print(firstFightStart)
print('Please enter the end of the First Fight')
firstFightEndInput = input()
firstFightEnd = firstFightEndInput[:2] + ':' + firstFightEndInput[2:4] + ':' + firstFightEndInput[4:6]
print(firstFightEnd)
#endTime = str(input())
subprocess.call([r'mkvmerge','-o', filenameInput + 'split.mkv', filenameInput + '.mkv', '--split', 'timestamps:'+firstFightStart+','+firstFightEnd])
