#De Martonne İklim Sınıflandırması

# Aşağıda istenilen değerleri giriniz:

P = float(input("Yıllık Toplam Yağış Miktarı (mm): "))
T = float(input("Yıllık Ortalama Sıcaklık Değeri (°C): "))
p = float(input("En Kurak Ayın Yağış Miktarı (mm): "))
t = float(input("En Kurak Ayın Sıcaklık Değeri (mm): "))

# De Martonne iklim sınıflandırması aşağıdaki indeks formülü ile bulunur.

idmt = (P / (T + 10) + (12 * p) / (t + 10))/2

print("Yıllık Kuraklık İndeksi: " + str(idmt))
print("İklim Tipi:")

if 0 < idmt < 5:
    print("Çöl")
elif 5 < idmt < 10:
    print("Step (Yarı Kurak)")
elif 10 < idmt < 20:
    print("Step - Nemli arası")
elif 20 < idmt < 28:
    print("Yarı Nemli")
elif 28 < idmt < 35:
    print("Nemli")
elif 35 < idmt < 55:
    print("Çok Nemli")
elif 55 > idmt:
    print("Islak")
else:
    print("Kutupsal")


