import string
import random
charcter=list(string.ascii_letters + string.digits + "!@#$%")
def bm():
    bm=int(input("how long would you set password:"))
    random.shuffle(charcter)
    password=[]
    for i in range(bm):
        password.append(random.choice(list(string.digits)) + random.choice(charcter))
    #random.shuffle(password)
    password="".join(password)
    print(password)
    print(len(password))
bm()

   