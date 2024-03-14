#write a csv file using python

import csv

f=open('prgrm70.csv','w+')
insert=csv.writer(f)
fields=input('enter the fields seperated with comma').split(',')
insert.writerow(fields)
n=int(input('enter the number of rows to insert'))
for i in range(0,n):
    print('row',i+1,' : ')
    rows=input('enter values seperated with comma').split(',')
    insert.writerow(rows)

f.close()

'''enter the fields seperated with commaName,Age,Gender
enter the number of rows to insert3
row 1  : 
enter values seperated with commaakhil,21,male
row 2  : 
enter values seperated with commadona,20,female
row 3  : 
enter values seperated with commaalbert,21,male'''
