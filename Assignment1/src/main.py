import numpy as np
# Navigate to src file, and the filePath should be correct
filePath = "../data/covtype.data"
#filePath = "../data/test.data"

# Create a 2D array to store data
# data = np.zeros((581012, 55))

# def readData():
#     # Read data from the file
#     print("Reading data from file...")

#     with open(filePath, "r") as f:
#         for i in range(581012):
#             line = f.readline()
#             line = line.split(',')
#             for j in range(55):
#                 data[i][j] = line[j]
#     print("Reading data - Finished")

def readData():
    # Read data from the file
    print("Reading data from file...")

    data = np.loadtxt(filePath, delimiter=',')  # 使用 NumPy 的 loadtxt() 函数加载数据
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




    # Simple solution
    # print("Calculating result...")
    # for i in range(581012):
    #     j = 1
    #     record = 0 # 1 is the record itself
    #     while i+j < 581012 and np.abs(dataInUse[i] - dataInUse[i+j]) <= k:
    #         j += 1
    #         record += 1
    #     # result.append(record)
    #     answer += record
    #     print(i)
    # print("Calculating result - Finished")
    # # print("The result is: ")
    # # print(result)
    # print("The sum of the result is: ")
    # print(answer)
    



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
            similarity(selectedData)
    else:
        print("Wrong input.")







