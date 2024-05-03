'''write a function that count the number of strings where string length is 2 or more and the first and last characters are same'''
def count_strings(s):
    count=0
    for item in s.split():
        if len(item)>=2 and item[0]==item[-1]:
            count+=1
    return count

s=input('enter a string')
print(count_strings(s))

'''enter a stringappa amma aa akhil
3'''
