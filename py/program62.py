#prgrm that accpets an integer from user and raises valueerror with arg abnormal condition if the reading is not with 90-120
try:
    x=int(input("enter a number"))
    if x<90 or x>120:
        raise ValueError
    else:
        print(x)
except ValueError:
    print("abnormal condition")

'''enter a number12
abnormal condition'''
