def BilgiAl():
    #Sosyal ile ilgili k�s�m
    sosyalD = input("Sosyal bilimlerin DO�RU say�s�n� giriniz.")
    sosyalY = input("Sosyal bilimlerin YANLI� say�s�n� giriniz.")
    sosyalB = 0
    
    if sosyalD + sosyalY > 40:
        print "Yanl�� veri girdiniz tekrar deneyin !"
        BilgiAl()
    else:
        sosyalB = (40) - (sosyalD + sosyalY)
        gidenDogrularSos = sosyalY / 4.0
        sosyalD -= gidenDogrularSos
        sosyalY += gidenDogrularSos

    print "do�ru ",sosyalD,"\r"
    print "yanl�� ",sosyalY,"\r"
    print "bo� ",sosyalB

    #Turkce icin olan kisim
    turkceD = input("T�rk�e DO�RU say�s�n� giriniz.")
    turkceY = input("T�rk�e YANLI� say�s�n� giriniz.")
    turkceB = 0
    
    if turkceD + turkceY > 40:
        print "Yanl�� veri girdiniz tekrar deneyin !"
        BilgiAl()
    else:
        turkceB = (40) - (turkceD + turkceY)
        gidenDogrularTurk = turkceY / 4.0
        turkceD -= gidenDogrularTurk
        turkceY += gidenDogrularTurk

    print "do�ru ",turkceD,"\r"
    print "yanl�� ",turkceY,"\r"
    print "bo� ",turkceB

    #Fen icin olan kisim
    fenD = input("Fen Bilimleri DO�RU say�s�n� giriniz.")
    fenY = input("Fen Bilimleri YANLI� say�s�n� giriniz.")
    fenB = 0
    
    if fenD + fenY > 40:
        print "Yanl�� veri girdiniz tekrar deneyin !"
        BilgiAl()
    else:
        fenB = (40) - (fenD + fenY)
        gidenDogrularFen = fenY / 4.0
        fenD -= gidenDogrularFen
        fenY += gidenDogrularFen

    print "do�ru ",fenD,"\r"
    print "yanl�� ",fenY,"\r"
    print "bo� ",fenB


    #Hesaplama kismi
    toplamPuan = (sosyalD * 2.5) + (turkceD * 1.5) + (fenD * 2.0)
    print "Bu ��rencinin ald��� toplam puan ==> ",toplamPuan
    
BilgiAl()
