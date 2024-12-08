def anagrams(txt1, txt2):
    return sorted(txt1)==sorted(txt2)
        
         #Test Cases:
print(anagrams("listen", "silent") == True)
print(anagrams("hello", "world") == False)
print(anagrams("triangle", "integral") == True)
      