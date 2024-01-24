import numpy as np
# Navigate to src file, and the filePath should be correct
filePath = "../data/covtype.data"


def bandJoin(filePath, k):
    # Create a 2D array to store data
    data = np.zeros((581012, 55))
    # Read data from the file
    print("Reading data from file...")

    with open(filePath, "r") as f:
        for i in range(581012):
            line = f.readline()
            line = line.split(',')
            for j in range(55):
                data[i][j] = line[j]
    print("Reading data - Finished")

    # Sort data by the first column
    sorted_indices = np.argsort(data[:, 0])
    sorted_data = data[sorted_indices]
    # print(sorted_data)
    print("Sorting data - Finished")

    # Create a record to store the result
    dataInUse = sorted_data[:, 0]
    # result = []
    answer = 0
    print("Calculating result...")
    for i in range(581012):
        j = 0
        record = 0 # 1 is the record itself
        while i+j < 581012 and np.abs(dataInUse[i] - dataInUse[i+j]) <= k:
            j += 1
            record += 1
        # result.append(record)
        answer += record
        print(i)
    print("Calculating result - Finished")
    # print("The result is: ")
    # print(result)
    print("The sum of the result is: ")
    print(answer)
    











































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





