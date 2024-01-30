import numpy as np
# Navigate to src file, and the filePath should be correct
filePath = "../data/covtype.data"

def readData():
    # Read data from the file
    print("Reading data from file...")
    data = np.loadtxt(filePath, delimiter=',') 
    # print(data)
    print("Reading data - Finished")
    return data


def bandJoin(filePath, k):
    # read data from file
    data = readData()
    datalen = len(data)
    datawid = len(data[0])
    # Sort data by the first column
    sorted_indices = np.argsort(data[:, 0])
    sorted_data = data[sorted_indices]
    # print(sorted_data)
    print("Sorting data - Finished")

    # Create a record to store the result
    dataInUse = sorted_data[:, 0]
    # result = []
    answer = 0
    # Optimized solution
    # First, scan the data and calculate the number of each value
    print("Calculating result...")
    print("Scanning Data for All Values...")
    # valueSet = {}
    valueCount = {}
    for i in range(len(dataInUse)):
        if dataInUse[i] in valueCount:
            valueCount[dataInUse[i]] += 1
        else:
            valueCount[dataInUse[i]] = 1
    print("Scanning Data for All Values - Finished")
    # Since the dataInUse is ordered(sorted), the valueCount set is also ordered.

    # Calculate result
    print("Calculating result...")
    # First, turn the dictionary into a list
    values = list(valueCount.keys())
    # print(valueCount)
    result = 0
    for i in range(len(values)):
        n = valueCount[values[i]]-1
        m = valueCount[values[i]]
        result += (1+n)*n/2
        j = 1
        while i+j < len(values) and np.abs(values[i] - values[i+j]) <= k:
            result += m*valueCount[values[i+j]]
            j += 1
    print("Calculating result - Finished")
    print("The result is: ")
    print(result)


# the similarity function: normalize data
def normalize(filePath):
    data = readData()
    datalen = len(data)
    datawid = len(data[0])


    print("Normalizing data...")
    # Normalizing data
    for i in range(10):
        maxcol = np.max(data[:, i])
        mincol = np.min(data[:, i])
        data[:, i] = (data[:, i] - mincol)/(maxcol - mincol)
    print("Normalizing data - Finished")
    return data


def similarity(data):
    print("data shape is: ", data.shape)
    data = data[:, :-1]
    collen = len(data[0])
    print("The number of columns is: ", collen)
    rowlen = len(data)
    print("The number of rows is: ", rowlen)
    minimumSimilarity = 1
    maximumSimilarity = 0
    averageSimilarity = 0
    # similarityMatrix = np.zeros((rowlen, rowlen))
    print("Calculating similarity...")
    for i in range(rowlen):
        for j in range(i+1, rowlen):
            similarity = 0
            delta = 0
            for k in range(10):
                di = np.abs(data[i][k] - data[j][k])
                si = 1/(1+di)
                delta += 1
                similarity += si
            for k in range(10, collen):
                if data[i][k] == data[j][k] and data[i][k] == 1:
                    similarity += 1
                    delta += 1
                if data[i][k] != data[j][k]:
                    delta += 1
            similarity = similarity/delta
            averageSimilarity += similarity
            minimumSimilarity = min(minimumSimilarity, similarity)
            maximumSimilarity = max(maximumSimilarity, similarity)
    averageSimilarity = averageSimilarity/(rowlen*(rowlen-1)/2)

    print("Calculating similarity - Finished")
    print("The minimum similarity is: ")
    print(minimumSimilarity)
    print("The maximum similarity is: ")
    print(maximumSimilarity)
    print("The average similarity is: ")
    print(averageSimilarity)
    return minimumSimilarity, maximumSimilarity, averageSimilarity
    # return  minimumSimilarity, maximumSimilarity, averageSimilarity
    
def main():
    print("This is the solution of assignment 1.")
    print("Please input a NUMBER to choose solution.")
    print("1. Band Join")
    print("2. The similarity function ")

    # Get input from user
    solutionIndex = input("Please input a number: ")

    # Call solution
    if solutionIndex == "1":
        print("You are choosing Band Join.")
        print("It will take a integer as parameter, please input a integer.")
        k = input()
        k = int(k)
        bandJoin(filePath, k)

    elif solutionIndex == "2":
        print("You are choosing The similarity function.")
        data = normalize(filePath)
        print("Please input a number to choose random saple from: 1. all data; 2. each type of the data")
        x = input()
        if x == "1":
            # Random sample from all data
            print("You are choosing random sample from all data.")
            # Randomly sample 1000 data from dataset
            np.random.shuffle(data)
            selectedData = data[:1000]
            similarity(selectedData)
        elif x == "2":
            foo = [] # The array to store answers
            for i in range(1,8):
                print("You are choosing random sample from type ", i)
                # Randomly sample 1000 data from dataset where type = i
                typedata = data[data[:, 54] == i]
                np.random.shuffle(typedata)
                boundary = len(typedata)
                if boundary < 1000:
                    print("The number of data is less than 1000, so we will use all data.")
                    selectedData = typedata
                else:
                    print("The number of data is more than 1000, so we will sample 1000 datapoints.")
                    selectedData = typedata[:1000]
                mins, maxs, avgs = similarity(selectedData)
                tmp = [mins, maxs, avgs]
                foo.append(tmp)
            for i in range(7):
                print("Type ", i+1, " min similarity ", foo[i][0], " max similarity ", foo[i][1], " average similarity ", foo[i][2])
        else:
            print("Wrong input.")

if __name__ == "__main__":
    main()







