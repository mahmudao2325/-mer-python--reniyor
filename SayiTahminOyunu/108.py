# kaç adımda tahmin edildiği eklendi
import random

tutulan_sayi = random.randint(1, 10)) # 1 ve 10 dahildir

sayac = 1 # sayac 1 den başlar
while True:
    tahmin = int("Sayıyı tahmin ediniz")

    if tahmin == tutulan_sayi: # 
        print("Tebrikler, tahmininiz doğru : ", tahmin, " ", sayac, " adımda tahmin ettiniz")
        break
    elif tahmin > tutulan_sayi:
        print("Daha küçük tahminde bulunun")
    elif tahmin < tutulan_sayi:
        print("Daha büyük tahminde bulunun")
    
    sayac = sayac + 1 # her döngü sonunda sayac 1 artar