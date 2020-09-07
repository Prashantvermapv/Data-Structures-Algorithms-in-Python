def partition(arr, l, r):
    pivot = arr[r]
    point = l
    for j in range(l, r):
        if arr[j] <= pivot:
            arr[point], arr[j] = arr[j], arr[point]
            point += 1
    arr[point], arr[r] = arr[r], arr[point]
    return point
    
def QuickSearch(arr, l, r, k):
    if l <= r:
        index = partition(arr, l, r)
        if index +1 == k :
            print(index, k,len(arr),arr[index])
            print(arr[::1])
            print(arr[index])
            return arr[index]
        elif index > k:
            print(index, k,l,'l')
            QuickSearch(arr, l, index-1, k)
        else:
            print(index, k,r,'r')
            print(arr[index])
            QuickSearch(arr, index+1, r, k)

T = int(input())
for i in range(T):
    n = int(input())
    arr = list(map(int, input().strip().split()))[:n]
    print(arr[::1])
    k = int(input())
    print(QuickSearch(arr, 0, n-1, k))