#23. Write a function to check if two strings are anagrams.
def anagram(s1,s2):
    return sorted(s1)==sorted(s2)
s1="listen"
s2="silent"
res=anagram(s1,s2)
print(res)

