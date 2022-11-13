NESNE_TAS = "TAS" # 1
NESNE_KAGIT = "KAGIT" # 2
NESNE_MAKAS = "MAKAS" # 3

skor_kullanici = 0
skor_bilgisayar = 0 

def sayi_nesne_donusumu(sayi):
    nesne_adi = ""
    if sayi == 1:
        nesne_adi = NESNE_TAS
    elif sayi == 2:
        nesne_adi = NESNE_KAGIT
    elif sayi == 3:
        nesne_adi = NESNE_MAKAS
    
    return nesne_adi

def nesne_karsilastir(kullanici_secimi, bilgisayar_secimi):
    # değişkenler global olmalı
    global skor_bilgisayar, skor_kullanici
    
    print("Bilgisayar secimi: ", bilgisayar_secimi)
    print("Kullanici secimi: ", kullanici_secimi)
    
    if kullanici_secimi == bilgisayar_secimi:
        pass # seçimler aynıdır bir işlem yapma, berabere
    if kullanici_secimi == NESNE_TAS:
        if bilgisayar_secimi == NESNE_KAGIT:
            skor_bilgisayar +=1
        if bilgisayar_secimi == NESNE_MAKAS:
            skor_kullanici +=1
    elif kullanici_secimi == NESNE_KAGIT:
        if bilgisayar_secimi == NESNE_TAS:
            skor_kullanici +=1
        if bilgisayar_secimi == NESNE_MAKAS:
            skor_bilgisayar +=1
    elif kullanici_secimi == NESNE_MAKAS:
        if bilgisayar_secimi == NESNE_KAGIT:
            skor_kullanici +=1
        if bilgisayar_secimi == NESNE_TAS:
            skor_bilgisayar+=1

def bilgisayar_nesne_sec():
    
    import random
    rastgele_sayi = random.randint(1,3) # 1,2,3 sayısından biri seçilir
    return sayi_nesne_donusumu(rastgele_sayi)

def skor_yaz():
    print("##### SKOR #####")
    print("## Bilgisayar : ", skor_bilgisayar)
    print("## Kullanıcı : ", skor_kullanici)

def oyun_bitti():
    print("Oyun bitti!")
    skor_yaz()
    
    if skor_bilgisayar > skor_kullanici:
        print("Bilgisayar kazandı")
    elif skor_bilgisayar < skor_kullanici:
        print("Kullanıcı kazandı")
    elif skor_bilgisayar == skor_kullanici:
        print("Berabere")

def oyun_baslat():
    
    while True:
        secim = int(input("Nesne seçiniz: 1-TAS, 2:KAGIT, 3:MAKAS. oyunu sonlandırmak için 0'a basınız : "))
        if secim == 0:
            break
        
        bilgisayar_secimi = bilgisayar_nesne_sec()
        kullanici_secimi = sayi_nesne_donusumu(secim)
        
        nesne_karsilastir(kullanici_secimi, bilgisayar_secimi)
        
        skor_yaz()
    
    oyun_bitti()

oyun_baslat()

        
