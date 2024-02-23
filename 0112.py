# num1=int(input("수 입력 : "))
# num2=int(input("수 입력 : "))

# if num1>num2:
#     for i in range(num2+1,num1):
#         if i%2==0:
#             print(i)

# elif num1<num2:
#     for i in range(num1+1,num2):
#         if i%2==0:
#             print(i)

# n=int(input("수 입력 : "))
# li=[]
# for i in range(1,n+1):
#     if i%7==0:
#         li.append(i)

# print(sum(li),len(li))
# print(li)




# n=int(input("수 입력 : "))
# su3=0
# su5=0
# for i in range(1,n+1):
#     if i%3==0:
#         su3+=1
#     if i%5==0:
#         su5+=1


# print(su3-su5)



###################################


#  li=['O', 'O', 'O', 'O', 'AB', 'B', 'A', 'A', 'O', 'AB', 'B', 'A', 'B', 'AB', 'AB', 'AB', 'O', 'A', 
#  'A', 'AB', 'B', 'AB', 'O', 'B', 'A', 'O', 'A', 'O', 'AB', 'O', 'AB', 'AB', 'O', 'B', 'B', 'O', 'O', 'AB', 'B', 'A']

# a=li.count('A')
# b=li.count('B')
# ab=li.count('AB')
# o=li.count('O')
# print(a,b,ab,o)

#2번째 방법
# for i in ["A","B","AB","B"]:
#     print(i,li.coumnt(i),"명")

#반복적이면 for문으로 돌릴 생각.

#####################3


# li=[6600, 4800, 3400, 3200, 4500, 5500, 3200, 
# 7800, 4200, 5300, 7500, 4200, 7200, 5600, 
# 6700, 8000, 7000, 6700, 6200, 6100, 4700, 
# 7200, 7100, 5700, 5900, 4300, 5200, 5600, 
# 5900, 6600, 4900, 5800, 7100, 5800, 4500, 
# 3200, 7800, 5300, 7200, 8000]

# su=0
# for i in li:
#     if i<=5000:
#         su+=1

# print(su)


######################


# li=[80, 70, 44, 66, 40, 80, 77, 57, 68, 
# 90, 75, 84, 99, 52, 45, 53, 54, 96, 59, 
# 47, 57, 68, 74, 68, 79, 60, 63, 67, 43, 
# 100, 43, 54, 77, 59, 75, 60, 97, 47, 100, 54]
# su=0
# for i in li:
#     if i<80:
#         su+=1

# print(su)

#######################

# n=int(input("단 입력 : "))
# for i in range(1,10):
#     print(n,'*',i,'=',n*i)

############################

# print('-'*20)
# n=int(input("몇 회 연산을 진행하시겠습니까?"))
# for i in range(n):
#     num1=int(input("수 입력 : "))
#     num2=int(input("수 입력 : "))

#     print('='*20)
#     print("1. 더하기")
#     print("2. 빼기")
#     print("3. 곱하기")
#     print("="*20)

#     point=int(input("연산 입력 : "))
#     if point==1:
#         print(num1,'+',num2,'=',num1+num2)
#     elif point==2:
#         print(num1,'-',num2,'=',num1-num2)
#     elif point==3:
#         print(num1,'*',num2,'=',num1*num2)
#     else:
#         print("그런 연산 없습니다.")


#####################


# li=[]

# su=0
# for i in range(2000,3001):
#     if i%400==0:
#         li.append(i)
#     elif i%100==0:
#         pass
#     elif i%4==0:
#         li.append(i)
    
# print(li[134])
# #사람이 생각하는 135번째는 리스트 인덱스에선 134







############################

# n=int(input("몇 회 입력하시겠습니까?"))
# for i in range(1,n+1):
#     x=int(input("수 입력 : "))
#     if x%2==0:
#         print(x,"짝수")
#     else:
#         print(x, "홀수")

##########################

# n=int(input("몇 회 입력하시겠습니까?"))
# li=[]
# for i in range(1,n+1):
    
#     su=int(input("수 입력 : "))
#     li.append(su)

# for i in li:
#     if i%2==0:
#         print(i,"짝수")
#     else:
#         print(i,"홀수")


###########################

# n=int(input("학생은 몇명인가요?"))
# li=[]
# for i in range(1,n+1):
#     score=int(input("점수 입력 : "))
#     li.append(score)

# avg=sum(li)/len(li)
# cnt=0
# for i in li:
#     if i<=avg:
#         cnt+=1

# print(len(li),"명의 평균 : ",avg)
# print("평균 이하인 학생 : ",cnt)

    
##################3


n=int(input(" 수 입력 : "))
st=""

for i in range(1,n+1):
    st+=str(i)




print(st,len(st))


# su=0
# for i in li:
#     print(i,end='')
#     su+=len(i)

# print(" >",su)
    



