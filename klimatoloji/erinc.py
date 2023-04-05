# Erinç İklim Sınıflandırması

# Aşağıda istenilen değerleri giriniz:

P = float(input("Yıllık Toplam Yağış Miktarı (mm): "))
Tom = float(input("Yıllık Ortalama Maksimum Sıcaklık Değeri (°C): "))

# Yağış Etkinlik İndeksi aşağıdaki formül ile bulunur.

Im = P / Tom

print("Yağış Etkinlik İndeksi: " + str(Im))

# Bulunan indeks değeri aşağıdaki şekilde sınıflandırılmıştır.
print("İklim Tipi:")

if Im < 8:
    print("Tam Kurak")
elif 8 < Im < 15:
    print("Kurak")
elif 15 < Im < 23:
    print("Yarı Kurak")
elif 23 < Im < 40:
    print("Yarı Nemli")
elif 40 < Im < 55:
    print("Nemli")
else:
    print("Çok Nemli")

# Kaynak: Erinç, S. (1965). Yağış müessiriyeti üzerine bir deneme ve yeni bir indis. İstanbul: İstanbul Üniversitesi Coğrafya Enstitüsü Yayınları No:41.
