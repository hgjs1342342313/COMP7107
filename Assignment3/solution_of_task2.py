import pandas as pd
import heapq
import datetime
import argparse
import pytz



# 执行 Dijkstra 算法
# 执行 Dijkstra 算法
import sys

def dijkstra(adjacency_list, source, target, tstart):
    # 初始化距离字典和路径字典
    distances = {node: sys.maxsize for node in adjacency_list}
    previous = {node: None for node in adjacency_list}
    distances[source] = tstart
    # 创建优先队列
    priority_queue = [(tstart, source)]

    while priority_queue:
        # 从优先队列中取出具有最小距离的顶点
        current_distance, current_node = heapq.heappop(priority_queue)

        # 如果已经访问过目标节点，可以提前退出
        if current_node == target:
            break

        # 遍历当前顶点的邻接顶点
        for neighbor in adjacency_list[current_node]:
            # 如果邻居没有出度且不是目标节点，跳过
            if (neighbor[1] not in adjacency_list) and (neighbor[1] != target):
                continue
            neighbor_timestamp, neighbor_node = neighbor

            # 判断是否满足时间顺序条件
            if neighbor_timestamp >= current_distance:
                new_distance = neighbor_timestamp

                # 如果新距离小于已知距离，更新距离和路径
                if new_distance < distances[neighbor_node]:
                    distances[neighbor_node] = new_distance
                    previous[neighbor_node] = current_node
                    heapq.heappush(priority_queue, (new_distance, neighbor_node))

    # 如果找到了路径，从目标节点开始回溯并构建最短路径
    path = []
    if distances[target] != sys.maxsize:
        node = target
        while node is not None:
            path.append(node)
            node = previous[node]
        path.reverse()

    return path, distances[target]

# 主函数
def main():
    # 创建命令行参数解析器
    parser = argparse.ArgumentParser(description='Dijkstra Algorithm')

    # 添加命令行参数
    parser.add_argument('--filename', type=str, default='graph.tsv', help='Graph data filename')
    parser.add_argument('--source', type=str, default='source_subreddit', help='Source subreddit name')
    parser.add_argument('--target', type=str, default='target_subreddit', help='Target subreddit name')
    parser.add_argument('--tstart', type=str, default='2024-04-09 10:00:00', help='Start timestamp')

    # 解析命令行参数
    args = parser.parse_args()

    # 从命令行参数获取输入
    filename = args.filename
    source = args.source
    target = args.target
    tstart_str = args.tstart
    tstart = datetime.datetime.strptime(tstart_str, '%Y-%m-%d %H:%M:%S')

    # print("filename:", filename)
    # print("source:", source)
    # print("target:", target)
    # print("tstart:", tstart)
    tstart = int(tstart.timestamp())
    
    # print("tstart:", tstart)
    # read dict.tsv and make a dictionary

    # 读取dict.tsv,将source和target转换为id
    dictionary = {}
    with open('dict.tsv', 'r') as file:
        for line in file:
            line = line.strip().split('\t')
            key = line[0]
            value = line[1]
            dictionary[value] = key
    # print(dictionary)
    source = dictionary[source]
    target = dictionary[target]
    
    adjacency_list = {}

    with open(filename, 'r') as file:
        for line in file:
            line = line.strip().split('\t')
            source_id = line[0]
            triples = line[1:]
            
            if source_id not in adjacency_list:
                adjacency_list[source_id] = []
            
            for triple in triples:
                timestamp, target_id, emotion = triple.split(',')
                timestamp = int(timestamp)
                if emotion == '1':
                    adjacency_list[source_id].append((timestamp, target_id))
        # 输出adjecency_list第25行
        # print(adjacency_list['36'])



    # 执行 Dijkstra 算法
    result = dijkstra(adjacency_list, source, target, tstart)

    # 构建dictionary
    # 读取dict.tsv
    dictionary = {}

    with open('dict.tsv', 'r') as file:
        for line in file:
            line = line.strip().split('\t')
            key = line[0]
            value = line[1]
            dictionary[key] = value

    
    

    
    path, distance = result
    if len(path) == 0:
        print("无法找到满足条件的最短路径")
    else:  
        # 将distance转换为时间格式
        distance = datetime.datetime.fromtimestamp(distance)
        print("最短路径到达时间:", distance)
        print("最短路径:")
        for node in path:
            print(dictionary[node], end=' -> ')


if __name__ == '__main__':
    main()