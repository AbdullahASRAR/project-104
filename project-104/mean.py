import csv
with open("height-weight.csv")as f:
    reader=csv.reader(f)
    fileData=list(reader)
fileData.pop(0)
newData=[]  
for i in range(len(fileData)):
    nun=fileData[i][1]
    newData.append(float(nun))
n=len(newData)
total=0       
for i in newData:
    total=total+i
mean=total/n
print("The mean is "+str(mean))       


