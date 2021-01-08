import os
#select current dir
currentDir = os.path.dirname(__file__)
currentDir = os.path.join(currentDir, 'files' )
#our file name
tFile: str = "test.txt"
#create absolute path to file
absFilePath: str = os.path.join(currentDir, tFile)
#oper file reader in read mode
f = open(absFilePath, 'r')
#print file name
print(f.mode)

#close file reader  !! very important
f.close()

#context manager automatically closes file for us
with open(absFilePath, 'r') as ff:
    # ffContents = ff.read()
    # print(ffContents)
    # select size of read in characters
    #SIZE: int = 100
    #ffContents = ff.read(SIZE)

    #read one line nad move to the next
    # ffLine = ff.readline()
    # print(ffLine)

    #read all lines
    # ffLines = ff.readlines()
    #this is a list of all the lines
    # print(ffLines)

    #read all lines using for loop
    for line in ff:
        print(line, end='')


""" csv """

import csv

#our file name
cFile: str = "names.csv"
#create absolute path to file
absFilePath: str = os.path.join(currentDir, cFile)
#open file
with open(absFilePath, 'r') as csvFile:
    csvReader = csv.reader(csvFile)
    #csv.reader(file, delimeter=";") to change delimiter

    print(csvReader)
    #just an object in memory

    #skip header  (remember iterators? :)
    next(csvReader)
    #loop to read
    for line in csvReader:
        print(line)
        # notice that line is a list already


    