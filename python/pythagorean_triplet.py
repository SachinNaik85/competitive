# arr = [1, 2, 3, 4, 5, 12, 13, 15]
# output : (3, 4, 5) (5, 12, 13)
import math 


def find_triplets1(arr):
    dix = {}
    for i in arr:
        dix[i*i] = 1
    
    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            try:
                if dix[arr[i]*arr[i] + arr[j] * arr[j]]:
                    print(arr[i], arr[j], int(math.sqrt(arr[i]*arr[i] + arr[j]*arr[j])))
            except KeyError:
                pass


def find_triplets2(arr):
    squares = [i*i for i in arr]
    squares.sort()
    # print(squares)

    for i in range(len(squares)-1, 1, -1):
        j = 0
        k = i-1
        while j < k:
            if squares[i] == squares[j] + squares[k]:
                print(int(math.sqrt(squares[i])), int(math.sqrt(squares[j])), int(math.sqrt(squares[k])))
                j += 1
            elif squares[i] < squares[j] + squares[k]:
                k -= 1
            else:
                j += 1


arr = list(map(int, input("Enter array : ").split()))
find_triplets2(arr)
