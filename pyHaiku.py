import random

def Random_haiku():
    with open("haiku.txt", encoding="utf-8") as f:
        haiku_list = f.readlines()
    haiku_first = []
    haiku_second = []
    haiku_third = []
    for haiku in haiku_list:
        a,b,c = haiku.split(' ',2)
        haiku_first.append(a)
        haiku_second.append(b)
        haiku_third.append(c.replace("\n",""))
    maxNum = len(haiku_first)
    rand1 = random.randint(0,maxNum)
    rand2 = random.randint(0,maxNum)
    rand3 = random.randint(0,maxNum)
    return f"{haiku_first[rand1]} {haiku_second[rand2]} {haiku_third[rand3]}"

if __name__ == '__main__':
    print(Random_haiku())