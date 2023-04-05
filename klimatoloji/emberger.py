# Emberger İklim Sınıflandırması

# Aşağıda istenilen değerleri giriniz:

P = float(input("Yıllık Ortalama Toplam Yağış Miktarı (mm): "))
M = float(input("En sıcak ayın en yüksek sıcaklık ortalaması (°C): "))
m = float(input("En soğuk ayın en düşük sıcaklık ortalaması (°C): "))

# Emberger iklim sınıflandırması aşağıdaki indeks formülü ile bulunur.

iemb = 2000*P / ((M+m+546.4)*(M-m))

print("Emberger İklim İndeksi: " + str(iemb))
print("İklim Tipi:")

if iemb < 20:
    print("Çok Kurak Akdeniz")
elif 20 < iemb < 32:
    print("Kurak Akdeniz")
elif 32 < iemb < 63:
    print("Yarı Kurak Akdeniz")
elif 63 < iemb < 98:
    print("Az - Yağışlı Akdeniz")
else:
    print("Yağışlı Akdeniz")
