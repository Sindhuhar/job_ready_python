def compute_sum(*numbers):
    total = 0
    for n in numbers:
        total += n
    return total

numbers = 1,2,3,4,5,4,56,7,6,9,8,12,34,54,67,90
summation = compute_sum(*numbers)
print(summation)
