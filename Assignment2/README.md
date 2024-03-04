## Report of Assignment1

Author: Zheming Kang; Date: Mar. 4th

### 1. Instructions to compiling and running codes

The "Solution.ipynb" contains all my codes and comments. Please run the cells one by one, and you'll see the output under each cell. Please put the Solution.ipynb and the "Beijing_restaurant.txt" under the same folder so that the path can finds the text well. Also you can see the output of mine under the cells in the "Solution.ipynb" file.

The environment requirements are: python: 3.8, pandas 2.

### 2. Document of my programs

I wrote the subtitles for the solution so that you can find the 3 tasks. 

#### 2.1 Task 1: Index development

In task one, we are required to generate 2 files: grid.grd and gird.dir, where the grd file describes the grids and the locations and the dir file describes the directions of the grids in the grd file. Here's the further explaination.

##### 2.1.1 Works for .grd file

First, I loaded the data by pandas.read_csv function and set the x, y, and id attributes.

```python
filename = "Beijing_restaurants.txt"
data = pd.read_csv(filename, header = None, skiprows = 1, delimiter=" ", names = ["x", "y"])
data["id"] = range(1, len(data)+1)
```

Then, I get the maximum and minimum values and compute the intervals for further assignment. I assign the grid by "(x-x_min)//10" to get the id of x axis, and do the same thing on y axis. After that, we can sort them by x and y grid label. Finally, we write the informatin of the data points with .6f format to remain the format.

##### 2.1.2 Works for .dir file

For the dir file, we are required to compute the offset of the data points in characters. Since the python will ignore the '\'\n" character, we need to add one offset manually. By using the following function, we can compute the offsets correctly.

```python
def get_line_offset(file_path, n):
    with open(file_path, 'r') as file:
        offset = 0
        line_number = 0
        for line in file:
            if line_number == n:
                return offset
            offset += len(line)
            line_number += 1
	return -1
```

Finally, we can write the information into the dir file. I take an index i to get the value since all the variables are sorted.

```python
grid_dir = open("grid.dir", "w")
grid_dir.write(str(x_min) + " " + str(x_max) + " " + str(y_min) + " " + str(y_max) + "\n")
i = 0
for grid in grid_count.itertuples():
    grid_dir.write(str(grid.x_grid) + " " + str(grid.y_grid) + " "+str(offsets[i]) +" "+ str(grid.count) + "\n")
    i += 1
```

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
