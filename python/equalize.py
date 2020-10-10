# program to count minimum number of +1 or -1 operations required to make all the elements of the array equal
# arr = [1, 2, 7, 4, 10]
"""
sum = 24
len = 5
mean = 24 // 5
mean = 4
[1, 2, 7, 4, 10] -mean
return sum([3, 2, 3, 0, 6])
"""


def equalize(arr):
    mean = sum(arr) // len(arr)
    return sum([abs(mean - i) for i in arr])


print('Min steps required  : ', equalize(list(map(int, input('Enter an array : ').split()))))
