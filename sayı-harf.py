# -*- coding: cp1254 -*-
## Girilen 4 basamakl� bir say�y� yaz� ile yazd�rabilir misiniz
## Girilen 5 basamakl� bir say�y� yaz� ile yazd�rabilir misiniz
## Girilen n basamakl� bir say�y� yaz� ile yazd�rabilir misiniz
##  415   d�rty�zonbe�
##  416   d�rty�zonalt�

def terscevir(x):
    y = ''
    deger = str(x)
    for i in deger:
        y=i+y
    return y

##def terscevir1(y):
##    x = str(y)
##    for i in range(len(x)/2):
##        x[i], x[len(x)-i-1] = x[len(x)-i-1], x[i]
##    return x
y = ['bin','milyon','milyar']
bb = {0 : '', 1:'bir', 2:'iki',3:'��',4:'d�rt',5:'be�',6:'alt�',7:'yedi',8:'sekiz',9:'dokuz'}
ob = {0 : '', 1:'on', 2:'yirmi',3:'otuz',4:'k�rk',5:'elli',6:'altm��',7:'yetmi�',8:'seksen',9:'doksan'}
sayi = 6442926000
sayi = terscevir(sayi)
metin = ''
for basamak,x in enumerate(sayi):
    if basamak == 0:
        metin = bb[int(x)] + metin
    elif basamak in [1,7]:
        metin = ob[int(x)] + metin
    elif (basamak in [2,5,8]):
        if (x not in ['0','1']):
            metin = bb[int(x)]+'y�z'+metin
        elif x =='1':
            metin = 'y�z'+metin
    elif basamak in [3,6,9]: 
        if int(x) == 1 and len(sayi)>4:
            metin = bb[int(x)]+ y[basamak/4] + metin
        elif int(x) == 1 and len(sayi)==4:
            metin = y[basamak/4]+metin
        elif int(x) in range(0,10):
            metin = bb[int(x)] + y[basamak/4] + metin
    elif basamak == 4:
        metin = ob[int(x)]+metin
print metin
##print ob[int(sayi[4])],bb[int(sayi[3])]+'bin',bb[int(sayi[2])]+'y�z',ob[int(sayi[1])],bb[int(sayi[0])]


