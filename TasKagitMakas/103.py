# parametreli fonksinyon

def selamla(isim):
    print("Merhaba ", isim)

def tekrarla(tekrar_sayisi):
# tekrar_sayisi kadar işlem tekrar eder
    sayac = 1
    print("islem basladi")
    while sayac <= tekrar_sayisi:
        print("İşlem: ", sayac)
        sayac +=1
    print("islem bitti")

def listenin_ilk_ve_son_elemani(liste):
    print("ilk eleman : ", liste[0]) # listenin ilk elemanı
    print("son eleman : ", liste[-1]) #listenin son elemanı

def listenin_en_buyuk_degerini_yaz(liste):
    print("en büyük değer", max(liste))

def listenin_en_buyuk_degerini_don(liste):
    return max(liste)


selamla("Ömer")
selamla("Osman")

tekrarla(2)
tekrarla(16)

liste = [1,3,5,7,9]
listenin_ilk_ve_son_elemani(liste)

listenin_en_buyuk_degerini_yaz(liste)

listenin_en_buyuk_degeri = listenin_en_buyuk_degerini_don(liste)
print("listenin en buyuk degeri : ", listenin_en_buyuk_degeri)
print("listenin en buyuk degerinin iki kati : ", listenin_en_buyuk_degeri*2)
