# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
# A subsequence of a string is a new string that is formed from the original string by 
# deleting some (can be none) of the characters without disturbing the relative positions
#  of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).


# j pointer for traversing through the substring
# i pointer for traversing through the string

def subSequence(s,t):
    S= len(s)
    T = len(t)
    if S>T: return False
    if S <=0: return True
    j = 0
    for i in range(len(t)):
        if t[i]==s[j]:
            if j == S-1:
                return True
            j+=1
    return False
        
    
s="rami"
t = "ramya"
print(subSequence(s,t))

    