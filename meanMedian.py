import csv
with open('SOCR-HeightWeight.csv', newline= '') as f:
    reader= csv.reader(f)
    file_data = list(reader)
file_data.pop(0) 
new_data=[]
for i in range(len(file_data)):
    n_num=file_data[i][1]
    new_data.append(float(n_num))

#getting the mean
n=len(new_data)
total= 0
for x in new_data:
    total+=x
mean= total/n
print("Mean is " + str(mean))

#getting the median
new_data.sort()

#using floor division to get the nearest number 
if n%2==0:
    #getting the first number
    median1= float(new_data[n//2])
    median2= float(new_data[n//2-1])
    median= (median1+median2)/2
else:
    median= new_data[n//2]
    print(n)
print("Median is "+ str(median)) 
