from sys import stdin


def prefix(lis):
    tot = 0
    output = []
    for i in lis:
        tot += i
        output.append(tot)
    return output


n = int(stdin.readline())
trees = []
for i in range(n):
    trees.append(int(stdin.readline()))

trees_prefix = prefix(trees)

queries = int(stdin.readline())
for query in range(queries):
    i, j = map(int, stdin.readline().split())
    if i > 0:
        print(trees_prefix[j] - trees_prefix[i-1])
    else:
        print(trees_prefix[j])
