# 1

# math=int(input("수학 점수 입력 : "))
# sci=int(input("과학 점수 입력 : "))
# avg=(math+sci)/2

# if avg>90:
#     print("A")
# elif avg>80:
#     print("B")
# elif avg>70:
#     print("C")
# else:
#     print("D")


# 2
# num1=int(input("수 입력 : "))
# num2=int(input("수 입력 : "))
# point=input("연산자 입력 : ")

# if point=='+':
#     print(num1+num2)
# elif point=='-':
#     print(num1-num2)
# elif point=='*':
#     print(num1*num2)
# elif point=='/':
#     print(num1/num2)
# else:
#     print("연산자가 이상해요")


#####################################


# num1=int(input("월을 입력하세요 : "))

# if 1<=num1<=12:

#     if 3<=num1<=5:
#         print(num1,"은 봄입니다.")
#     elif 6<=num1<=8:
#         print(num1,"은 여름입니다.")
#     elif 9<=num1<=11:
#         print(num1,"은 가을입니다.")
#     else:
#         print(num1,"은 겨울입니다.")

# else:
#     print("입력이 올바르지 않습니다.")


##################################

# 아이디=input("아이디 입력 : ")
# if 아이디=="admin":
#     패스워드=input("패스워드 입력 : ")
#     if 패스워드=="admin":
#         print("로그인 성공")
#     else:
#         print("패스워드가 틀렸습니다.")
# else:
#     print("계정이 존재하지 않습니다.")



###############################

#4
# num1=int(input("수 입력 : "))

# if num1<0:
#     print("절대값은",-num1,"입니다.")
# else:
#     print("절대값은",num1,"입니다.")


#######################################


# apple=int(input("구입할 사과 개수 : "))
# pear=int(input("구입할 배 개수 : "))
# money=int(input("지금 소지하고 있는 금액 : "))

# plus=3000*apple+2000*pear
# if plus<money:
#     print("잔돈은",money-plus,"입니다.")
# else:
#     print("구매 불가")

# num1=int(input("수 입력 : "))

# if num1%15==0:
#     print("15의 배수입니다.")
# elif num1%5==0:
#     print("5의 배수입니다.")
# elif num1%3==0:
#     print("3의 배수입니다.")


###########################################



# print('='*15)
# print("1. 아메리카노")
# print("2. 카페라떼")
# print('='*15)

# menu=int(input("메뉴선택 : "))

# if 1<=menu<=2:
#     print('='*15)
#     print("1. ice")
#     print("2. hot")
#     print('='*15)
#     temp=int(input("온도 선택 : "))

#     if 1<=temp<=2:
#         if menu==1:
#             if temp==1:
#                 print("아이스 아메리카노")

#             elif temp==2:
#                 print("뜨거운 아메리카노")


#         elif menu==2:
#             if temp==1:
#                 print("아이스 카페라떼")
#             elif temp==2:
#                 print("뜨거운 카페라떼")
#     else:
#         print("온도선택이 잘못되었습니다.")

# else:
#     print("메뉴선택이 잘못되었습니다.")


###########################################

#part2
###############################################



# num1=int(input("생년월일 입력 : "))
# num2=num1%12
# #묘=나머지7
# if num2==1:
#     print("닭띠입니다.")
# elif num2==2:
#     print("개띠입니다.")
# elif num2==3:
#     print("돼지띠입니다.")
# elif num2==4:
#     print("쥐띠입니다.")
# elif num2==5:
#     print("소띠입니다.")
# elif num2==6:
#     print("호랑이입니다.")
# elif num2==7:
#     print("토끼띠입니다.")
# elif num2==8:
#     print("용띠입니다.")
# elif num2==9:
#     print("뱀띠입니다.")
# elif num2==10:
#     print("말띠입니다.")
# elif num2==11:
#     print("양띠입니다.")
# elif num2==0:
#     print("원숭이띠입니다.")


############################################


# N=int(input("며칠인가?"))
# num1=N%4

# if num1==1:
#     print("A")
# elif num1==2:
#     print("B")
# elif num1==3:
#     print("C")
# elif num1==0:
#     print("D")


#############################################

# day=int(input("며칠 후인가?"))
# num1=day%7

# if num1==0:
#     print("오늘은 화요일")
# elif num1==1:
#     print("오늘은 수요일")
# elif num1==2:
#     print("오늘은 목요일")
# elif num1==3:
#     print("오늘은 금요일")
# elif num1==4:
#     print("오늘은 토요일")
# elif num1==5:
#     print("오늘은 일요일")
# elif num1==6:
#     print("오늘은 월요일")


#################################


# year=int(input("년도 입력 : "))
# num1=year%4
# num2=year%100
# num3=year%400

# if num3==0:
#     print("윤년입니다.")
# elif num1==0 and num2!=0:
#     print("윤년입니다.")
# else:
#     print("윤년이 아닙니다.")


###################################


# num1=int(input("N입력 : "))
# num2=num1%8

# if num2==1:
#     print("A")
# elif num2==2 or num2==0:
#     print("B")
# elif num2==3 or num2==7:
#     print("C")
# elif num2==4 or num2==6:
#     print("D")
# elif num2==5:
#     print("E")

# A   1,9,17,25 
#     1 1 1  1

# B   2,8,10,16,18,24,26
#     2 0 2  0  2  0
# C   3,7,11,15,19,23,27
#     3 7 3  7  3  7  3
# D   4,6,12,14,20,22,28
#     4 6 4  6  4  6  4

# E   5,13,21,29
#     5 5  5  5


##########################################


# hour=int(input("몇 시?"))
# min_=int(input("몇 분?"))

# total=hour*3600+min_*60
# totalminus=total-1800
# totalhour=totalminus//3600
# totalmin=int(totalminus%3600/60)
# print(totalhour,"시",totalmin,"분")


######################################


# A=int(input("A 입력 : "))
# B=int(input("B 입력 : "))

# A1=A//100
# A10=(A%100//10)*10
# A100=(A%10)*100
# newA=A100+A10+A1

# B1=B//100
# B10=(B%100//10)*10
# B100=(B%10)*100
# newB=B100+B10+B1

# if newA>newB:
#     print(newA)
# elif newA<newB:
#     print(newB)
# else:
#     print(newA,"같다.")


##################################

# hour=int(input("시간 입력 : "))
# min_=int(input("분 입력 : "))
# total=hour*3600+min_*60
# N=int(input("N분 전 입력 : "))
# newN=N*60
# newtotal=total-newN
# newhour=newtotal//3600
# newmin_=(newtotal%3600)//60
# print(newhour,"시간",newmin_,"분")

#############################

n=int(input("N일 째 : "))
num1=n%12


if 1<=num1<=3:
    print("A")
elif 4<=num1<=6:
    print("B")
elif 7<=num1<=9:
    print("C")
else:
    print("D")







