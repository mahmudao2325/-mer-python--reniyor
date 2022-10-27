import random

tutulan_sayi = random.randint(1, 100))

sayac = 1 
while True:
    tahmin = int("Sayıyı tahmin ediniz")

    if tahmin == tutulan_sayi: # 
        print("Tebrikler, tahmininiz doğru : ", tahmin, " ", sayac, " adımda tahmin ettiniz")
        break
    elif tahmin > tutulan_sayi:
        print("Daha küçük tahminde bulunun")
    elif tahmin < tutulan_sayi:
        print("Daha büyük tahminde bulunun")
    
    sayac = sayac + 1