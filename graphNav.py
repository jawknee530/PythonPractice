def nav_graph(graph, cur_row, cur_col, directions, weight):
    right_node = []
    below_node = []
    while cur_row < len(graph) or cur_col < len(graph):
        if cur_row < len(graph)-1:
            directions += 'd,'
            weight += int(graph[cur_row+1][cur_col])
            print('going down')
            below_node = nav_graph(graph, cur_row+1, cur_col, directions, weight)
            print('gone down')
            # below_node = int(graph[cur_row+1][cur_col])
        else:
            below_node = (0, 0, 0, 0, float('-inf'))

        if cur_col < len(graph)-1:
            directions += 'r,'
            weight += int(graph[cur_row][cur_col+1])
            print('going right')
            right_node = nav_graph(graph, cur_row, cur_col+1, directions, weight)
            print('gone right')
            # right_node = int(graph[cur_row][cur_col+1])
        else:
            right_node = (0, 0, 0, 0, float('-inf'))

        if right_node[1] > below_node[1]:
            return right_node
        else:
            return below_node
    if right_node[1] > below_node[1]:
        return [right_node[0], right_node[1]]
    else:
        return [below_node[0], below_node[1]]

def parse_graph(str):
    rows = str.split(';')
    graph = []
    for row in rows:
        graph.append(row.split(','))
    for row in graph:
        for col in row:
            print(col, end=' ')
        print()
    return nav_graph(graph, 0, 0, '', int(graph[0][0]))



# graph = input("""Input a string representing a graph.
# The format is row deliminated by ';'
# and column deliminated by ','""")

results = parse_graph('1,2,3;6,5,4;8,-7,9')
print(results)