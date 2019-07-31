
import subprocess
startTime = '2s'
endTime = '6s'
subprocess.call([r'mkvmerge','-o','test1.mkv','test.mkv', '--split', 'timestamps:'+startTime+','+endTime])
