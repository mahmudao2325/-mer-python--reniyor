# 1-10 arasındaki rastgele sayının tahmini
# sayı tahmin edilene kadar tekrar tekrar komut satırından girdi bekler
# tahmin için bir yönlendirme yok
import random

# kolay olması adına geçici olarak 1-10 arası random - rastgele sayı üretilir
tutulan_sayi = random.randint(1, 10)) # 1 ve 10 dahildir

while True:
    tahmin = int("Sayıyı tahmin ediniz")

    if tahmin == tutulan_sayi: # 
        print("Tebrikler, tahmininiz doğru : ", tahmin)
        break
    