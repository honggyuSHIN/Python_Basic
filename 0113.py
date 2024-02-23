
n=int(input("수 입력 : "))


for i in range(3,n+1):
    li=[]
    for j in range(1,i+1):
        
        if i%j==0:
            li.append(j)

    print(i,"의 약수 : ",li)

