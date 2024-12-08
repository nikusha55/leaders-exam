#Create a function to find the missing number in a list of integers from 1 to n.

def find_missing_number(numbers):
    n=len(numbers) + 1
    missing = 1
    while missing <= n:
        if missing not in numbers:
            return missing 
        missing += 1
    
    #Test Cases:
print(find_missing_number([1, 2, 4, 5]) == 3)
print(find_missing_number([3, 5, 6, 1, 2]) == 4)
print(find_missing_number([2]) == [])
