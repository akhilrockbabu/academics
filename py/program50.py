'''Write a program that print numbers from 1 to 20. For every multiple of 3, print 'Fizz', for every multiple of 5, print 'Buzz'
and for every multiple of both 3 and 5 print 'FizzBuzz', instead of the original number.'''

l=[]
for i in range(1,21):
    if not i%3 and not i%5:
        l.append('fizzbuzz')
    elif not i%3:
        l.append('fizz')
    elif not i%5:
        l.append('buzz')
    else:
        l.append(i)
print(l)


'''[1, 2, 'fizz', 4, 'buzz', 'fizz', 7, 8, 'fizz', 'buzz', 11, 'fizz', 13, 14, 'fizzbuzz', 16, 17, 'fizz', 19, 'buzz']'''
