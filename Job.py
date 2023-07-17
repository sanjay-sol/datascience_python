import pandas as pd
n=int(input("enter no:of elements:"))
names=[]
print('Enter names:')
for i in range (n):
    names.append(input())
deadlines=[]
print('Enter deadlines')
for i in range (n):
    deadlines.append(int(input()))
profits=[]
print('Enter Profits')
for i in range (n):
    profits.append(int(input()))
df=pd.DataFrame(data=[names,deadlines,profits],index=['names','deadlines','profits'])
df_transpose=df.T
df1=df_transpose.sort_values(by='profits',ascending=False)
print(df1)
data = df1['deadlines'].tolist()
names = df1['names'].tolist()
slots = max(data)
jobLine = [0] * slots
for i in range(n):
    for j in range(deadlines[i]-1,-1,-1):
        if jobLine[j] == 0:
            jobLine[j] = names[i]
            break
print(jobLine)
maxprofit=0
for i in range(n):
    for j in range(len(jobLine)):
        if(jobLine[j]==df1.names[i]):
            maxprofit=maxprofit+df1.profits[i]
print("Max Profit=",maxprofit)