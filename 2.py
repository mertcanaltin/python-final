# -*- coding: cp1254 -*-
sd = 0
sy = 0
sb = 0

td = 0
ty = 0
tb = 0

fd = 0
fy = 0
fb = 0

def 


sd = input("Sosya Bilimler s�nav�ndaki do�ru say�n�z� giriniz: ")
sy = input("Sosya Bilimler s�nav�ndaki do�ru say�n�z� giriniz: ")

td = input("T�rk�e s�nav�ndaki do�ru say�n�z� giriniz: ")
ty = input("T�rk�e s�nav�ndaki do�ru say�n�z� giriniz: ")

fd = input("Fen Bilimleri s�nav�ndaki do�ru say�n�z� giriniz: ")
fy = input("Fen Bilimleri s�nav�ndaki do�ru say�n�z� giriniz: ")
   
if 120 > (sd+sy):
   sb = 120 - (sd+sy)
else:
   print "Hatal� giri� l�tfen tekrar giriniz"
   sd = input("Sosya Bilimler s�nav�ndaki do�ru say�n�z� giriniz: ")
   sy = input("Sosya Bilimler s�nav�ndaki do�ru say�n�z� giriniz: ")

if 120 > (td+ty):
   sb = 120 - (td+ty)
else:
   print "Hatal� giri� l�tfen tekrar giriniz"
   td = input("T�rk�e s�nav�ndaki do�ru say�n�z� giriniz: ")
   ty = input("T�rk�e s�nav�ndaki do�ru say�n�z� giriniz: ")

if 120 > (fd+fy):
   sb = 120 - (fd+fy)
else:
   print "Hatal� giri� l�tfen tekrar giriniz"
   fd = input("Sosya Bilimler s�nav�ndaki do�ru say�n�z� giriniz: ")
   fy = input("Sosya Bilimler s�nav�ndaki do�ru say�n�z� giriniz: ")   
   
print sd,sy,sb
   


