def alan_hacim (YC):
   alan = 4 * 3.14* YC **2
   hacim = 4/3 * 3.14 * YC**3
   return alan,hacim
yaricap = input ("Lutfen Kurenin yaricapini giriniz: ")

ka,kh = alan_hacim(yaricap)
print ka, kh
##Bu �ekilde ayr� ayr� tan�mlar

print alan_hacim(yaricap)
## Bu �ekilde bir demet olarak sonu� d�nd�r�r

sonuc = alan_hacim(yaricap)
print sonuc
## Bu �ekilde sonucu bir de�i�kene al�p �yle yazd�rd�k

print type(sonuc)
## Bu �ekilde sonucun de�erini ��rendik
