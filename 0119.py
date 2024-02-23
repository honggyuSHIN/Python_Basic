#chr / ord
#a : 97/z : 122
#A : 65/Z : 90
st='''
Htwwjhy~ Z W xt Ljsnzx!! N lnaj Z uwjxjsy ktw ufxxnsl ymnx Vzjxy~ Gzy Dtz Mfaj Yt Xfd 'RTTDFMT' yt Rd Pfpft Yfqp Fhhtzsy. Mfmf~~
'''
n=int(input("키값 : "))



save=''
for n in range(-5,26):
    save=''
    for i in st:
        if 97 <= ord(i)<=122:           #소문자     #a : 97   z : 122
            #94는 120, 95는 121, 96은 122

            #ex)new는 95, n은 5일 때.
            new=ord(i)+n
            if new>122:
                new=new-26
                save+=chr(new)
            elif new<97:
                new=new+26
                save+=chr(new)
            else:
                save+=chr(new)


        elif 65<=ord(i)<=90:            #대문자         #A : 65  /  Z : 90
            new=ord(i)+n
            if new>90:
                new=new-26
                save+=chr(new)
            elif new<65:
                new=new+26
                save+=chr(new)
            else:
                save+=chr(new)


        else:
            save+=i

    print(n,save)

# -5 or 21
# Correct~ U R so Genius!! I give U present for passing this Quest~ But You Have To Say 
# 'MOOYAHO' to My Kakao Talk Account. Haha~~