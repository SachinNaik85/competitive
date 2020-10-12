# arr = [-2, -3, 3, 4, -1, 6, -2, 3]
# sum = 13
#
# brr = [-1, -5, 4, 3, -9, 10, -1]
# sum = 10


def max_array_sum(arr):
    max_sum = arr[0]
    for i in range(len(arr)-1):
        j = len(arr)
        while j > i:
            if sum(arr[i:j]) > max_sum:
                max_sum = sum(arr[i : j])
            j -= 1
    return max_sum


def kadeans_method(arr):
    sum_ending_here = 0
    max_sum = -999999999

    for i in arr:
        sum_ending_here += i

        if sum_ending_here > max_sum:
            max_sum = sum_ending_here

        if sum_ending_here < 0:
            sum_ending_here = 0

    return max_sum


if __name__ == '__main__':
    print(kadeans_method(list(map(int, input('Enter an array : ').split()))))
