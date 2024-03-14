'''Create a class Time with private attributes hour, minute and second
. Overload *+' operator to find sum of 2 time.'''

class Time:
    def __init__(self,h=0,m=0,s=0):
        self.__h=h
        self.__m=m
        self.__s=s
    def __add__(self,other):
        total_s=(self.__h*3600)+(self.__m*60)+self.__s+(other.__h*3600)+(other.__m*60)+other.__s
        total_h=total_s//3600
        rem_s=total_s%3600
        total_m=rem_s//60
        total_s=rem_s%60
        return total_h,total_m,total_s

t1=Time(1,55,46)
t2=Time(4,23,12)
r=t1+t2
print(r[0],'h : ',r[1],'m : ',r[2],'s')


# 6 h :  18 m :  58 s
