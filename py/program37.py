'''write a function to print all even numbers from a given list in the given order until you reach 237 or end of the list'''
def even_num(l):
    for i in l:
        if(i==237):
            break
        elif(not i%2):
            print(i)

n=map(int,input('enter the list of numbers').split())
even_num(n)
