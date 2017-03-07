from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import time
from collections import Counter

def createExample():
    numberArrayExamples = open('numArEx.txt', 'a')
    numbersHave = range(0,10)
    VersionsHave = range(1,10)

    for eachNum in numbersHave:
        for eachVer in VersionsHave:
            imgFilePath = 'images/numbers/'+str(eachNum)+'.'+str(eachVer)+'.png'
            ei = Image.open(imgFilePath, mode="r")
            eiar = np.array(ei)
            eiar1 = str(eiar.tolist())

            lineToWrite = str(eachNum)+'::'+eiar1+'\n'

            numberArrayExamples.write(lineToWrite)


"""
def threshold(imageArray):
    balanceArr = []
    newArr = imageArray

    for eachRow in imageArray:
        for EachPixel in eachRow:
                avgNum = reduce(lambda x, y: x+y, EachPixel[:3])/len(EachPixel[:3])
                balanceArr.append(avgNum)

    balance =  reduce(lambda x, y: x + y, balanceArr)/len(balanceArr)

    for eachRow in newArr:
        for EachPixel in eachRow:
            if reduce(lambda x, y: x+y, EachPixel[:3])/len(EachPixel[:3]) > balance:
                EachPixel[0] = 255
                EachPixel[1] = 255
                EachPixel[2] = 255
                EachPixel[3] = 255
            else:
                EachPixel[0] = 0
                EachPixel[1] = 0
                EachPixel[2] = 0
                EachPixel[3] = 255
    return newArr
"""

def whatNumIsThis(filepath):
    matchedAr = []

    loadExamples = open('numArEx.txt', 'r').read()
    loadExamples = loadExamples.split('\n')


    i = Image.open(filepath)
    iar = np.array(i)
    iarl = iar.tolist()

    inQuestion = str(iarl)

    for eachExample in loadExamples:
        splitEx = eachExample.split('::')
        #print splitEx
        #print 'len is' + str(len(splitEx[0]))

        currentNum = splitEx[0]
        try:
            currentAr = splitEx[1]
        except:
            print('error')

        eachPixEx = currentAr.split('],')

        eachPixInQ = inQuestion.split('],')

        x = 0
        while x < len(eachPixEx):
            if eachPixEx[x] == eachPixInQ[x]:
                matchedAr.append(int(currentNum))

            x += 1

    print matchedAr
    x = Counter(matchedAr)
    print x

#createExample()
whatNumIsThis('images/test.png')
