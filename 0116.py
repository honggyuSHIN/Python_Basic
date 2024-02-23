rest=0
cnt=0
while True:
    print("----Menu---")
    print("1. 콜라 / 300")
    print("2. 사이다 / 300")
    print("3. 커피 / 200")
    print("4.돈 넣기")
    print("5.잔돈 반환")
    print("6.종료")
    print("----------------")
    print("현재 금액 : ",rest)
    print()
    menu=input("메뉴 선택 : ")

    if menu.isnumeric():
        menu=int(menu)
        if 1<=menu<=6:
            if menu==1:
                if rest>=300:
                    print("콜라가 나옵니다.")
                    rest-=300
                else:
                    print()
                    print("잔돈이 부족합니다.")
                    print()
            if menu==2:
                if rest>=300:
                    print("사이다가 나옵니다.")
                    rest-=300
                else:
                    print()
                    print("잔돈이 부족합니다.")
                    print()
            if menu==3:
                if rest>=200:
                    print("커피가 나옵니다.")
                    rest-=200
                else:
                    print()
                    print("잔돈이 부족합니다.")
                    print()
            if menu==4:
                print()
                money=int(input("돈을 넣어주세요  "))
                print()
                rest+=money
            if menu==5:
                print()
                print("잔돈은",rest,"이 반환됩니다.")
                rest=0
                print()
            if menu==6:
                print()
                print("잔돈은",rest,"입니다.")
                print("프로그램을 종료합니다.")
                break

            
        else:
            print()
            print("숫자를 다시 입력해주세요")
            cnt+=1
            print()
    else:
        print()
        print("숫자를 입력해주세요")
        print()
        cnt+=1
    if cnt==3:
        print("오류 횟수 3회, 프로그램 종료")
        break



