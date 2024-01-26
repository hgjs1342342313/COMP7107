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
    











































print("This is the solution of assignment 1.")
print("Please input a number to choose solution.")
print("1. Band Join")
# print("2. TBD ")

# Get input from user
solutionIndex = input("Please input a number: ")

# Call solution
if solutionIndex == "1":
    print("You are choosing Band Join.")
    print("It will take a integer as parameter, please input a integer.")
    k = input()
    k = int(k)
    bandJoin(filePath, k)





