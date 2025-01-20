def permutations(string,i=0):
    if i == len(string):
        print("".join(string))
        return
    for j in range(i,len(string)):
        words = [c for c in string]
        words[i],words[j]=words[j],words[i]
        permutations(words,i+1)

string = input("enter the word")
print(permutations(string))