import os

d={}

while True:
    print("="*20)
    print("1. 단어검색")
    print("2. 단어추가")
    print("3. 단어수정")
    print("4. 단어삭제")
    print("5. 종료")
    print("="*20)
    ch=int(input("메뉴 입력 >"))
    os.system("cls")

    if ch==1:
        word=input("검색할 단어를 입력해주세요 : ")
        if word in d:
            print(f"{word}의 뜻은",d[word],"입니다.")
            
        else:
            print("등록된 단어가 아닙니다.")
            
    elif ch==2:
        print("검색할 단어를 입력해주세요 :")
        word=input()
        if word in d:
            print("이미 등록된 단어입니다.")
        else:
            
            mean=input(f"{word}의 뜻을 입력해주세요 : ")
            d[word]=mean
            print("단어 추가 완료")
            

        
    elif ch==3:
        word=input("수정할 단어를 입력해주세요 : ")
        if word in d:
            print(word,"의 뜻을 입력해주세요 : ")
            mean=input()
            if d[word]==mean:
                print(f"이미 {mean}라고 저장이 되어있어요!!")
            else:
                d[word]=mean
                print("단어의 뜻이 수정되었습니다!!")
        else:
            print("등록되지 않은 단어입니다.")
        
    elif ch==4:
        word=input("검색할 단어를 입력해주세요 : ")
        if word in d:
            del d[word]
            print(f"{word}가 사전에서 삭제됩니다.")
        else:
            print("등록되어 있지 않은 단어입니다.")
    elif ch==5:
        print("빠잇!")
        break
    else:
        print("잘못 입력하셨습니다.")




