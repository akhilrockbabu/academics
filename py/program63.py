#write a program to demostrate assert error in python for neg input

try:
    x=int(input('enter the number'))
    assert x>0,'too low value'

except AssertionError as ae:
    print(ae)
    
'''enter the number-34
too low value'''
