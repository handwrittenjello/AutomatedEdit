import csv
import pandas
"""
with open('chapters.csv', 'r') as f:
		reader = csv.reader(f)
		your_list = list(reader)
print (your_list)
"""
df = pandas.read_csv('chapters.csv')
print(df)

columns = df.columns

print(columns)
thirdColumn = columns[2]
print(thirdColumn)
df1 = df[thirdColumn]
df1 = df1.drop(0, axis=0)
print(df1)

startTimes = df1.values.tolist()

#print(startTimes)

listLength = len(startTimes)
#print(listLength)

### Chapter Titles
titles = pandas.read_excel('chapterTitles.xls')
titles = list(titles.Chapter)
print(titles)



f = open('chapter.txt','w+')
i = 1
while i <= listLength:
	#print('CHAPTER0' + str(i))
	f.write("CHAPTER0%d=%s\r\nCHAPTER0%dNAME=%s\r\n" % (i,startTimes[i-1],i,titles[i-1]))
	i += 1
