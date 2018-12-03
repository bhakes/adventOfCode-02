## Advent of Code 2018 Day 2

## imports
import os
import difflib

## parameters
fname = 'input.txt'
strArray = []

## get input
for line in open(fname, 'r'):
    if line.strip():           # line contains eol character(s)
        strArray.append(line)

index1 = 0
index2 = 0
diffArray = []
for index1 in range(0,len(strArray)):
    string1 = strArray[index1]
    for index2 in range(0,len(strArray)):
        string2 = strArray[index2]
        if string1 == string2:
            continue
        else:
            diffArray.append([enumerate(difflib.ndiff(string1, string2)),index1, index2,0])

for element in diffArray:
    for i,j in element[0]:
        if j[0]==' ': continue
        elif j[0]=='-':
            element[3] += 1
        elif j[0]=='+':
            element[3] += 1

candidateArray = []
## create candidate array
for element in diffArray:
    if element[3] <3:
        candidateArray.append(element)

print (candidateArray)
print (strArray[135])
print (strArray[227])

## nnfqdsvwryteogambzuchiwkpx ##31
## wnfqzsvwjyteogambduchirkpx ##116

## lnfqdsvwpyteogabbhuchirkpx ##30
## lnfqdsvwjyteogambzucczrgpx ##115
