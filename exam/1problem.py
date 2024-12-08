 #Create a function that takes a list of numbers and returns the sum of all positive numbers.
def positive_sum(arr):
    ress = 0
    for i in arr:
        if i > 0:
            res+=i
    return ress       
    
#Test Cases:
#assert problem_1_sum_of_positive([1, -4, 7, 12]) == 20
#assert problem_1_sum_of_positive([-1, -2, -3, -4]) == 0
#assert problem_1_sum_of_positive([]) == 0


