import csv

r = csv.reader(open('train.csv','r'))
r.next()

edges = set()
#commutative_graph = dict()
for edge in r:
    edges.add((edge[0], edge[1]))
#    commutative_graph.setdefault(edge[0], set()).add(edge[1])
#    commutative_graph.setdefault(edge[1], set()).add(edge[0])

missing_edges = set()
for edge in edges:
    if (edge[1], edge[0]) not in edges:
        missing_edges.add((edge[1], edge[0]))

missing_graph = dict()
for edge in missing_edges:
    missing_graph.setdefault(edge[0], set()).add(edge[1])

r = csv.reader(open('test.csv','r'))
r.next()

test_list = list()
for line in r:
    test_list.append(line[0])

test_lists = dict()
for node in test_list:
    test_lists[node] = list(missing_graph.get(node, set()))

file = open('output.csv','w')
w = csv.writer(file)
w.writerow(['source_node','destination_nodes'])
for node in test_list:
    w.writerow([node, " ".join(test_lists[node][0:10])])
file.close()