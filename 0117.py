import time

input("게임을 시작합니다 [ENTER]")
t = time.time()

input("5초가 된거 같다면 눌러주세요 [ENTER]")
user = round( time.time() - t , 2 )

if 4.5 < user < 5.5:
    print("CLEAR!!")

print(user, "초 지남!!")
