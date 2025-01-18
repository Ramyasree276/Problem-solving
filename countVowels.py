str = input("enter a string")
vowels="aeiouAEUIO"
vowelsCount = 0
consonants=0
for char in str:
    if char.isalpha():
        if char in vowels:
            vowelsCount +=1
        else:
            consonants+=1

print("vowels count: ",vowelsCount)
print("consonants count :",consonants)