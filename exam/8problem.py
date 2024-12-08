def lon(nums):
    nums=set(nums)
    max_len=0
    for num in nums:
        if num - 1 not in nums:
            current_num=num
            current_len=1
            while current_num + 1 in nums:
                curent_num += 1
                curent_len +=1
            max_len=max(max_len, current_len) 
    return max_len           

print(lon([100, 4, 200, 1, 3, 2]) == 4)
print(lon([0, 0]) == 1)
print(lon([9, 1, 4, 7, 3, 2, 8, 5, 6]) == 9)
