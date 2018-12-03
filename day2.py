## Advent of Code 2018 Day 2

## import
import os

## parameters
fname = 'input.txt'
strArray = []
freqArray = []
match = 0

## get input
for line in open(fname, 'r'):
    if line.strip():           # line contains eol character(s)
        strArray.append(line)

# get key-value pairs for string
keyValueArray = []
for index in range(0, len(strArray)):
    keyValueArray.append(dict())
    string = strArray[index]
    tempDict = keyValueArray[index]
    for character in string:
        if character == '\n':
            continue
        elif character in tempDict:
            tempDict[character] = tempDict.get(character) + 1
        else:
            tempDict.update({character:1})

checkSum = [0,0]
for dicts in keyValueArray:
    if 2 in dicts.values():
        checkSum[0] += 1
    if 3 in dicts.values():
        checkSum[1] += 1

print(checkSum)
print("The CheckSum is [{0},{1}] = {2}" .format(checkSum[0],checkSum[1],checkSum[0] * checkSum[1]))
