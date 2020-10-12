def digit_sum(num):
    dig_sum = 0
    for i in str(num):
        dig_sum += int(i)
        if dig_sum > 10:
            dig_sum = digit_sum(dig_sum)
    return dig_sum


def digit_sum1(num):
    while len(str(num)) > 1:
        dig_sum = 0
        for i in str(num):
            dig_sum += int(i)
        num = dig_sum
    return num


print(digit_sum(int(input('Enter a number : '))))
