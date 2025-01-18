s1 = input("enter the first string\n")
s2 = input("enter the second string\n")
def anagram(s1,s2):
    countdic={}
    if(len(s1)!= len(s2)):
        return "Not anagrams"
    for ch in s1:
        countdic[ch]=countdic.get(ch,0) +1
    for ch in s2:
        countdic[ch]=countdic.get(ch,0) -1
    for value in countdic.values():
        if(value!=0):
            return "Not anagrams"
    return "Anagram"
def anagram1(s1,s2):
    if(sorted(s1)== sorted(s2)):
        return "Anagrams"
    return "Not Anagrams"
print(anagram1(s1,s2))