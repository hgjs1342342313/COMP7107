## Report of Assignment1

Author: Zheming Kang; Date: Jan.30th

### 1. Instructions to compiling and running codes

There is only one file of my code. At the beginning of my code, there is a variable called filepath. ``filePath="../data/covtype.data"`` Here you can change the address of the covtype.data file or put the covtype.data into the data folder.

The environment requirements are: python: 3.8, numpy: 1.24.

### 2. Document of my programs

At the beginning of my file, there was a function called readData(). This is the function that we used to read the covtype.data file from our disk, and store the data in the memory. I used np.loadtxt function to store the data in a numpy 2D array.

#### 2.1 Band Join

In the function named bandJoin(), I implemented an optimized band join function to calculate result.

First, I sorted the first column of the data. 

```python
sorted_indices=np.argsort(data[:, 0])
sorted_data=data[sorted_indices]
```

Then, I used a dictionary to count the number of each value in the first column of the data.

```python
valueCount = {}
for i in range(len(dataInUse)):
    if dataInUse[i] in valueCount:
        valueCount[dataInUse[i]] += 1
    else:
        valueCount[dataInUse[i]] = 1
```

After that, we can make a reference and calculate them directly. 

First, turn the dictionary into a list. Since the data is sorted, and we read the data line by line, this dictionary is also ordered, which will lead to a ordered list.

Then, we read them one by one. The number m represents how many records are there in the data with the value equals to what we are considering. n is m-1.

For a value, there must be (1+n)*n/2 records with the different = 0. This is simple mathematics. Then, for i+1, i+2,... if the differenct is smaller than k, we know there are m * t records also fits the requirement, where t is the number of how many records are there in the data with the value equals to i+j th element.

```python
values = list(valueCount.keys())
result = 0
for i in range(len(values)):
    n = valueCount[values[i]]-1
    m = valueCount[values[i]]
    result += (1+n)*n/2
    j = 1
    while i+j < len(values) and np.abs(values[i] - values[i+j]) <= k:
        result += m*valueCount[values[i+j]]
        j += 1
```

Finally, we add the results together, and we'll get the correct answer.

#### 2.2 Similarity

I implemented 2 functions to answer question 2: normalize, and similarity. The normalize function reads the data, and normalize the first 10 columns by ``data[:, i] = (data[:, i] -mincol)/(maxcol-mincol)`` . The similarity function calculates the similarity between each pair of datapoints. 

For the first 10 columns, the similarity is:

```python
for k in range(10):
    di = np.abs(data[i][k] - data[j][k])
    si = 1/(1+di)
    delta += 1
    similarity += si
```

and for the next several columns, the similarity is:

```python
for k in range(10, collen):
    if data[i][k] == data[j][k] and data[i][k] == 1:
    	similarity += 1
    	delta += 1
    if data[i][k] != data[j][k]:
    	delta += 1
```

which follows the idea from our lecture slides.

After calculating the sum similarity of one pair of data points, we still need to let the sum divided by delta, to get the pair similarity. We add the result to averageSimilarity and update the max, min values. After the calculation of all the pairs of records, we calculate the average similarity by ``averageSimilarity/(rowlen*(rowlen-1)/2)``

The following is the sample codes:

```python
... For each pairs of records:
	similarity = similarity/delta
	averageSimilarity += similarity
	minimumSimilarity = min(minimumSimilarity, similarity)
	maximumSimilarity = max(maximumSimilarity, similarity)
# After all pairs are done
averageSimilarity = averageSimilarity/(rowlen*(rowlen-1)/2)
```

Finally, I implemented a main function to help user select the functions they are looking for. For question2, you can choose "1" to select the similarity for all the data, or choose "2" to see the similarities from each types of data.

### Results

#### Results for question 1

##### K = 0

![1706594448800](image/README/1706594448800.png)

##### K = 1

![1706594484738](image/README/1706594484738.png)

##### K = 2

![1706594495681](image/README/1706594495681.png)

##### K = 3

![1706594504895](image/README/1706594504895.png)

#### Result for question 2

##### Similarity between all the data

![1706594538336](image/README/1706594538336.png)

##### Similarities between each type of the data

![1706594560473](image/README/1706594560473.png)

## Observations

### Observations for Q1

* When k is from 0 to 3, the answer is 1.99, 5.68, 9.37, 13.27 (* 10^8). We can see each time when k increase 1, there will be 4 * 10^8 more records.

### Observations for Q2

* From question 2, we could see the minimum similarity for all the data is exteremely smaller than each type. This is reasonable since data in one type should be more similar than each other rather than other types.
* The maximum simialrity seems not very far from the specific types. This is also reasonable because we might choose some data from one type of data.
* The average is slightly lower than those from each type of data. Even though the sample volume is high, which might let the difference not high, it is still lower than the similarity from one type.
