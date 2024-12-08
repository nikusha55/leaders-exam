def three_sum(nums):
    nums.sort()
    result=[]
    for i in range(len(nums)-2):
        for j in range(i + 1, len(nums)-1):
            for k in range(j + 1,len(nums)-1):
                if nums[i] + nums[j] + nums[k]== 0 and [nums[i],[nums[j]],[nums[k]]]not in result:
                    return result
                
print(three_sum([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]])
print(three_sum([0, 0, 0]) == [[0, 0, 0]])
print(three_sum([1, 2, -2, -1]) == [])

               