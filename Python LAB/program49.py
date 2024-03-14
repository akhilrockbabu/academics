'''Accept a sentence from user and display the total count of vowels in the sentence.'''

def vowels(s):
    count=0
    for i in range(len(s)):
        if s[i]=='a' or s[i]=='e' or s[i]=='i' or s[i]=='o' or s[i]=='u':
            count+=1
    return count

s=input('enter a scentence')
print(vowels(s))
