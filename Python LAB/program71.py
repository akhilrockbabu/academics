#program to read csv file using python

import csv

f=open('prgrm70.csv','r')
file=csv.reader(f)
for lines in file:
    if lines:
        print(lines[0],'\t',lines[1],'\t',lines[2])


'''Name 	 Age 	 Gender
akhil 	 21 	 male
dona 	 20 	 female
albert 	 21 	 male'''
