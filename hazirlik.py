kayitListesi = {};



def KayitGir():
    numarasi = raw_input("Numaras� : ")
    adiSoyadi = raw_input("Ad� Soyad� : ")
    bolum = raw_input("B�l�m� : ")
    
    matVize = raw_input("Matematik Vize Notu : ")
    matFinal = raw_input("Matematik Final Notu : ")

    FizikVize = raw_input("Fizik Vize Notu : ")
    FizikFinal = raw_input("Fizik Final Notu : ")

    KimyaVize = raw_input("Kimya Vize Notu : ")
    KimyaFinal = raw_input("Kimya Final Notu : ")

    global kayitListesi
    
    kayitListesi[numarasi] = {"adSoyad":adiSoyadi,"bolum":bolum,"matV":matVize,"matF":matFinal,"fizV":FizikVize,"fizF":FizikFinal,"kimV":KimyaVize,"kimF":KimyaFinal}
    IslemSor()


def KayitGoruntule():
    print "G�r�nt�leye geldiniz! \n \r"
    kisi = raw_input("G�r�nt�lemek istedi�iniz kullan�c�n�n numaras� giriniz : ")

    global kayitListesi

    bulundumu = "hay�r"
    
    for key,val in kayitListesi.items():
        if key == kisi: ## and val == kisi:
            print "Numaras�".ljust(15),":" , kisi,"\r"
            print "Ad� Soyad�".ljust(15),":" , val["adSoyad"],"\r"
            print "B�l�m�".ljust(15),":" , val["bolum"],"\r"
            
            print "S�nav Notlar� \r"
            
            print "Matematik".ljust(15),val["matV"].ljust(5),val["matF"].ljust(5),"\r"
            print "Fizik".ljust(15),val["fizV"].ljust(5),val["fizF"].ljust(5),"\r"
            print "Kimya".ljust(15),val["kimV"].ljust(5),val["kimF"].ljust(5),"\r"
                        
            
            bulundumu = "evet"

    if bulundumu == "hay�r":
        print "aranan ki�i bulunamad� !"
    IslemSor()



def IslemSor():
    islem = raw_input("Kayit girmek i�in 'k' , kayit g�r�nt�lemek i�in 'g' yaz�n�z.")
    if islem == "k":
        KayitGir()
    elif islem =="g":
        KayitGoruntule()
    else:
        print "L�tfen ge�erli bir giri� yap�n�z."
        IslemSor()




if kayitListesi == {}:
    print "Program� yeni a�t���n�z i�in kay�t �ncelikle girmelisiniz!"
    print kayitListesi
    KayitGir()
    




