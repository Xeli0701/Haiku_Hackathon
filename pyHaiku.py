import random

def Random_haiku():
    with open("haiku.txt", encoding="utf-8") as f:
        haiku_list = f.readlines()
    haiku_first = []
    haiku_second = []
    haiku_third = []
    for haiku in haiku_list:
        a,b,c,d,e = haiku.split(' ',4)
        haiku_first.append(a)
        haiku_second.append(b)
        haiku_third.append(c.replace("\n",""))
    maxNum = len(haiku_first)
    rand1 = random.randint(0,maxNum)
    rand2 = random.randint(0,maxNum)
    rand3 = random.randint(0,maxNum)
    return haiku_first[rand1],haiku_second[rand2],haiku_third[rand3]

def Kisetsu_haiku(season):
    with open("haiku.txt", encoding="utf-8") as f:
        haiku_list = f.readlines()
    haiku_first = []
    haiku_second = []
    haiku_third = []
    for haiku in haiku_list:
        a,b,c,d,e = haiku.split(' ',4)
        if e.rstrip('\n') == season:
            haiku_first.append(a)
            haiku_second.append(b)
            haiku_third.append(c.replace("\n",""))
    maxNum = min(len(haiku_first),len(haiku_second),len(haiku_third))
    rand1 = random.randint(0,maxNum-1)
    rand2 = random.randint(0,maxNum-1)
    rand3 = random.randint(0,maxNum-1)
    return haiku_first[rand1],haiku_second[rand2],haiku_third[rand3]

if __name__ == '__main__':
    a,b,c = Random_haiku()
    print(f"{a} {b} {c}")
    print(Random_haiku())
    print(Kisetsu_haiku("春"))
    print(Kisetsu_haiku("夏"))
    print(Kisetsu_haiku("秋"))
    print(Kisetsu_haiku("冬"))