import random

def main():
    # Bir kelime seç
    kelime = random.choice(["Python", "Java", "C++", "JavaScript"])

    # Kelimenin boşluklu bir versiyonunu oluştur
    gizli_kelime = ""
    for harf in kelime:
        gizli_kelime += "_"

    # Oyunu oyna
    can = 5
    while can > 0:
        # Kullanıcıdan bir tahmin iste
        tahmin = input("Bir harf tahmin et: ")

        # Tahmini kontrol et
        if tahmin in kelime:
            # Tahmin doğruysa, gizli kelimeyi güncelle
            for i in range(len(kelime)):
                if kelime[i] == tahmin:
                    gizli_kelime = gizli_kelime[:i] + tahmin + gizli_kelime[i + 1:]

            # Kullanıcıya geri bildirim ver
            print("Tahmin doğru! Gizli kelime şu şekilde: " + gizli_kelime)
        else:
            # Tahmin yanlışsa, canı azalt
            can -= 1
            print("Tahmin yanlış! Kalan can: " + str(can))

    # Oyunun sonucunu göster
    if can > 0:
        print("Tebrikler! Oyunu kazandın!")
    else:
        print("Kaybettin! Gizli kelime: " + kelime)

if __name__ == "__main__":
    main()
