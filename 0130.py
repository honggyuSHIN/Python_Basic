from bs4 import BeautifulSoup
import requests
import os


res=requests.get("https://pokemongo.inven.co.kr/dataninfo/pokemon/")
soup=BeautifulSoup(res.text,"html.parser")


def 폴더생성(st):
    if not os.path.isdir(st):
        os.mkdir(st)

def 제거(st):
    for i in "/\\\"?*<>|:":
        st = st.replace(i, "")
    return st



폴더생성('pokemon')


for i in soup.select(".pokemonicon"):

    name=제거(i.select_one("span").text)

    link='https:'+i.select_one("img").get("src")
    
    r=requests.get(link)
    f=open(f"pokemon/{name}.png","wb")
    f.write(r.content)
    