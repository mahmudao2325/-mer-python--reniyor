# kodların çıktısını gördüğümüz ortama komut satırı veya terminal veya konsol diye belirteceğiz (tam olarak cli - command line interface yani komut satırı ara yüzü denir)

# komut satırından bir veri almak için küçük örneğe bakalım
# komut satırından 1234 girildiğinde şifre doğru yazan kod parçası
# burada komut satırında bir kez denenir. 
sifre = input("Lütfen şifreyi giriniz")

if sifre == "1234":
    print("Şifre doğrı")
else:
    print("Şifre hatalı")