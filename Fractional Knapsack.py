max=int(input("Enter Max Capacity: "))
x=0
weight=[]
profit=[]
w=0
p=0
n=int(input("Enter No. Of Items: "))
for i in range(n):
  weight.append(int(input("Enter Weight: ")))
for i in range(n):
  profit.append(int(input("Enter Profit: ")))
for i in range(n):
  if w+weight[i]<=max:
    w=w+weight[i]
    p=p+profit[i]
  else:
    x=(max-w)/weight[i]
    p=p+profit[i]*x
print("Max Profit: ",p)
