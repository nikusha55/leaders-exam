#Create a function that finds the length of the longest substring without repeating characters.
def longest_unique_substring(s):
    max_length=0
    for i in range(len(s)):
        substring=""  
        for j in s[i :]:
            if j in substring:
                break
            substring += j
        max_length=max(max_length, len(substring))   
    return max_length     
      

#Test Cases:
print(longest_unique_substring("abcabcbb") == 3)
print(longest_unique_substring("bbbbb") == 1)
print(longest_unique_substring("") == 0)
print(longest_unique_substring("pwwkew") == 3)

