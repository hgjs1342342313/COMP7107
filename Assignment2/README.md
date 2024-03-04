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

#### 2.2 Task 2: range selection queries

In task 2, we are required to implement a range_selection function to range query the points. Let's break down the function and see the details.

First, for the function being more robustic, we are supposed to take the x_y min_max value from the dir file, and compute the interval for further localization. 

```python
firstline = file.readline()  # skip the first line
x_min, x_max, y_min, y_max = firstline.split()
x_max = float(x_max)
x_min = float(x_min)
y_max = float(y_max)
y_min = float(y_min)
x_interval = (x_max - x_min) / 10
y_interval = (y_max - y_min) / 10
```

Then, we read the file line by line. If the grid fits the requirement, i.e. is entirely covered by the range, we add add all the data points to the result. If there is only one axis fits the requirement, we search for all the points in the grid, and see if they can be added into the result list. Since python will ignore the '\'\n" character, we need to accumulate the count value to find the correct offset.

```python
if the grid is covered by the range:
	add all the points
elif the grid is partically covered:
	find all the points and add the proper ones
```

We have several units to evaluate the function. I computed the whole query and range query. For the whole query, the answer is equal to the total sum, for the range query, the answer is equal to the simple query. (The answer compares the number of results)

#### 2.3 Task3: nearest neighbor queries

In task 3, we are required to implement the nearest neighbor queries. In the first unit, I implement 2 distance function computing distance between the target and the grid or another point.

Then, in the second grid, I use heapq to create priority queue. Firstly, I implement a function that can convert the point location to the grid labels. 

Then, here comes the nearest neighbor function.

At the beginning, I set a priority queue called pq. Then, I use 2 set to mark the visited grids and points to avoid re-visiting. Giving a location within 2 axies( target_x, target_y), we firstly convert the point to the grid. Then, add the grid to the pq. 

Just like BFS, while pq is not empty, we pop out the first value. If the value is a grid, we put all the points in the grid into the pq, and put all the adjecent grids into the queue. If the value is a point, we yield(return) the location, and keep the status of the function for the next call.

In the next unit, I set k = 3, x = 39.856138, and y = 116.42394. Then, I run the iterator function k times, to see the answer. The output is, this unit give 3 nearest points( you can see from the distance).

Then, I also tried the nn function on a point in grid 1, and most of the answer are from grid (0, 0) and grid(1, 0). The output shows the function reasonable.

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
