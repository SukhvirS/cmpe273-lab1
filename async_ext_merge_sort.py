import os
import asyncio

async def sort():
    """Sorts all text files in input dir and writes output to text files in output dir"""
    inputFiles = os.listdir('./input')
    tasks = []
    for f in inputFiles:
        tasks.append(asyncio.create_task(inputToSortedData('./input/'+f)))

    individualSortedData = []
    for task in tasks:
        individualSortedData += await task

    allSortedData = await mergesort(individualSortedData)
    await writeDataToFile(allSortedData, './output/async_sorted.txt')

async def inputToSortedData(filePath):
    """Sorts the data in the input file"""
    inputFile = open(filePath)
    fileData = [int(line) for line in inputFile.readlines()]
    sortedData = await mergesort(fileData)
    return sortedData

async def writeDataToFile(d, f):
    """Writes data d to file f"""
    outputFile = open(f, 'w')
    for x in d:
        outputFile.write(str(x)+'\n')

async def mergesort(data):
    """Divides data into smallest unit, then merges it"""
    if len(data) == 1:
        return data
    middle = int(len(data)/2)
    leftSide = await mergesort(data[:middle])
    rightSide = await mergesort(data[middle:])
    result = merge(leftSide, rightSide)
    a = await result
    return a

async def merge(leftSide, rightSide):
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

loop = asyncio.get_event_loop()
try:
    loop.run_until_complete(sort())
finally:
    loop.close()