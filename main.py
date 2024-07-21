import trieTree
import heap
import radixSort

n = int(input())
resturants = []
tree = trieTree.Trie()
queries = []

for i in range(n):
    x, y = input().split()
    resturants.append([int(y), x])


heap.heapify(resturants)
resturantsStack = []

q = int(input())
for i in range(q):
    nearest, prefix = input().split()
    queries.append([int(nearest), prefix])

flag = False
for i in range(q):

    if flag:
        if queries[i][0] > queries[i-1][0]:
            pops = queries[i][0] - queries[i-1][0]
            for k in range(pops):
                item = (heap.heappop(resturants))
                tree.insert(item[1])
                resturantsStack.append(item)
        if queries[i][0] < queries[i - 1][0]:
            pushes = queries[i-1][0] - queries[i][0]
            counter = queries[i][0]
            for y in range(pushes):
                tree.delete(resturantsStack[counter][1])
                heap.heappush(resturants, resturantsStack[counter])
                resturantsStack.remove(resturantsStack[counter])

    else:
        for j in range(queries[i][0]):
            item = (heap.heappop(resturants))
            tree.insert(item[1])
            resturantsStack.append(item)

        flag = True

    answer = tree.query(queries[i][1])

    if answer == []:
        print("NO restaurant found!")
    else:
        answer = radixSort.radix_sort_letters(answer)
        for s in range(len(answer)):
            print(answer[s])




