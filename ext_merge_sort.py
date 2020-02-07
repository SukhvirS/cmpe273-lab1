import os

def sort():
    """Sorts all text files in input dir and writes output to text files in output dir"""
    allInputFiles = os.listdir('./input')
    individualSortedData = []
    for f in allInputFiles:
        x = inputToSortedData('./input/'+f)
        individualSortedData += x
    allSortedData = mergesort(individualSortedData)
    writeDataToFile(allSortedData, './output/sorted.txt')

def inputToSortedData(filePath):
    """Sorts the data in the input file"""
    inputFile = open(filePath)
    fileData = [int(line) for line in inputFile.readlines()]
    sortedData = mergesort(fileData)
    return sortedData

def writeDataToFile(d, f):
    """Writes data d to file f"""
    outputFile = open(f, 'w')
    for x in d:
        outputFile.write(str(x)+'\n')

def mergesort(data):
    """Divides data into smallest unit, then merges it"""
    if len(data) == 1:
        return data
    middle = int(len(data)/2)
    leftSide = mergesort(data[:middle])
    rightSide = mergesort(data[middle:])
    return merge(leftSide, rightSide)

def merge(leftSide, rightSide):
    """Sorts and merges two lists"""
    result = []
    i = 0
    j = 0
    while i<len(leftSide) and j<len(rightSide):
        if leftSide[i] <= rightSide[j]:
            result.append(leftSide[i])
            i += 1
        else:
            result.append(rightSide[j])
            j+= 1
    result += leftSide[i:]
    result += (rightSide[j:])
    return result

sort()