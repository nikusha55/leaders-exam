 #Create a function that takes a list of numbers, including fractions, and returns the sum of all positive numbers, floored to the nearest integer.
def sum_of_positive(numbers):
    total_sum=0
    for num in numbers:
        if num>0:
            floored_num=int(num)
            total_sum += floored_num
    return total_sum        

print(sum_of_positive([1, -4, 7, 12]) == 20)
print(sum_of_positive([-1.5, 2.7, -3.3, 4.8]) == 6)
print(sum_of_positive([]) == 0)
print(sum_of_positive([-1, -2, -3]) == 0)



