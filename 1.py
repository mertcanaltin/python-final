# -*- coding: cp1254 -*-
ogrncno = []
ad = []
soyad = []
bolum = []
mat1 = []
mat2 = []
fizik1 = []
fizik2 = []
kimya1 = []
kimya2 = []
toplam = []
soru = "Hangisini yapmak istersin?\n Yeni kayit i�in 1'e bas�n\n Kay�tlar� g�r�nt�lemek i�in 2'ye bas�n\n Arama yapmak i�in 3'e bas�n \nCevap:"
cevap = input (soru)

if cevap == 1:
   ogrncno.append(input ("L�tfen ��renci numaran�z� giriniz: "))   
   ad.append(raw_input ("L�tfen Ad�n�z� giriniz: "))
   soyad.append(raw_input ("L�tfen Soyad�n�z� giriniz: "))
   bolum.append(raw_input ("L�tfen B�l�m�n�z� giriniz: "))
   mat1.append(input ("L�tfen Matematik 1.notunuzu giriniz: "))
   mat2.append(input ("L�tfen Matematik 2.notunuzu giriniz: "))
   fizik1.append(input ("L�tfen Fizik 1.notunuzu giriniz: "))
   fizik2.append(input ("L�tfen Fizik 2.notunuzu giriniz: "))
   kimya1.append(input ("L�tfen Kimya 1.notunuzu giriniz: "))
   kimya2.append(input ("L�tfen Kimya 2.notunuzu giriniz: "))
   print "***********************\n"
   cevap = input (soru)

if cevap == 2:
   print "***********************\n","��renciNo".rjust(15)+":",ogrncno
   print "Ad".rjust(15)+":",ad
   print "Soyad".rjust(15)+":",soyad
   print "Bolum".rjust(15)+":",bolum
   print "Mat1".rjust(15)+":",mat1
   print "Mat2".rjust(15)+":",mat2
   print "Fizik1".rjust(15)+":",fizik1
   print "Fizik2".rjust(15)+":",fizik2
   print "Kimya1".rjust(15)+":",kimya1
   print "Kimya2".rjust(15)+":",kimya2
   print "***********************\n"
   cevap = input (soru)
   
if cevap == 3:
   arama = input("Aramak istedi�iniz ��renci numar�n� giriniz: ")
   if arama in ogrncno:
      n = ogrncno.index(arama)
   print "***********************\n","��renciNo".rjust(15)+":",ogrncno[n]
   print "Ad".rjust(15)+":",ad[n]
   print "Soyad".rjust(15)+":",soyad[n]
   print "Bolum".rjust(15)+":",bolum[n]
   print "Mat1".rjust(15)+":",mat1[n]
   print "Mat2".rjust(15)+":",mat2[n]
   print "Fizik1".rjust(15)+":",fizik1[n]
   print "Fizik2".rjust(15)+":",fizik2[n]
   print "Kimya1".rjust(15)+":",kimya1[n]
   print "Kimya2".rjust(15)+":",kimya2[n]
   print "***********************\n"
   cevap = input (soru)
      
