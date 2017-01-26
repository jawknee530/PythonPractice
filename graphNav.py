def nav_graph(graph, cur_row, cur_col, directions, weight):
    if cur_row < len(graph)-1:
        below_weight = weight + int(graph[cur_row+1][cur_col])
        below_node = nav_graph(graph, cur_row+1, cur_col, directions+'d,', below_weight)
    else:
        below_node = [directions, weight]

    if cur_col < len(graph)-1:
        right_weight = weight + int(graph[cur_row][cur_col+1])
        right_node = nav_graph(graph, cur_row, cur_col+1, directions+'r,', right_weight)
    else:
        right_node = [directions, weight]

    if right_node[1] > below_node[1]:
        return [right_node[0], right_node[1]]
    else:
        return [below_node[0], below_node[1]]


def parse_graph(str):
    rows = str.split(';')
    graph = []
    for row in rows:
        graph.append(row.split(','))
    print('Grid:')
    for row in graph:
        for col in row:
            print(col, end=' ')
        print()
    return nav_graph(graph, 0, 0, '', int(graph[0][0]))


print('Find the highest weighted path through a grid of numbers')
results = parse_graph('1,2,3;6,5,4;8,-7,9')
results[0] = results[0][:-1]
print('Results:')
print(results)