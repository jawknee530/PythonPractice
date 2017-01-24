def nav_graph(graph, cur_row, cur_col, directions, weight):
    while cur_row < len(graph)-1 or cur_col < len(graph)-1:
        cur_node = int(graph[cur_row][cur_col])
        if cur_row < len(graph)-1:
            directions += 'd,'
            cur_row += 1
            weight += int(graph[cur_row][cur_col])
            below_node = (graph, cur_row, cur_col, directions, weight)
            # below_node = int(graph[cur_row+1][cur_col])
        else:
            below_node = float('-inf')
        if cur_col < len(graph)-1:
            directions += 'r,'
            cur_col += 1
            weight += int(graph[cur_row][cur_col])
            right_node = (graph, cur_row, cur_col, directions, weight)
            # right_node = int(graph[cur_row][cur_col+1])
        else:
            right_node = float('-inf')
        if right_node > below_node:
            return right_node[3], right_node[4]
        else:
            return below_node[3], below_node[4]
        # if right_node > below_node:
        #     directions += 'r,'
        #     cur_col += 1
        #     return nav_graph(graph, cur_row, cur_col, directions, weight)
        # elif below_node > right_node:
        #     directions += 'd,'
        #     cur_row += 1
        #     weight += int(graph[cur_row][cur_col])
        #     return nav_graph(graph, cur_row, cur_col, directions, weight)



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