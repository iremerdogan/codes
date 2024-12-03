class Sehir:
    def __init__(self, isim, sicaklik):
        self.isim = isim
        self.sicaklik = sicaklik

class HavaDurumu:
    def __init__(self):
        self.sehirler = []

    def sehir_ekle(self):
        isim = input("Şehir adı giriniz: ")
        sicaklik = int(input("Sıcaklık bilgisi giriniz: "))  # Burada int dönüşümü
        sehir = Sehir(isim, sicaklik)
        self.sehirler.append(sehir)
        print(f"Şehir: {sehir.isim}, Sıcaklık: {sicaklik}°")  # `sehir.isim` ile obje ismi alınıyor

    def sicaklik_guncelle(self):
        isim = input("Şehir adı giriniz: ")
        yeni_sicaklik = int(input("Yeni sıcaklık bilgisi giriniz: "))  # Burada da int dönüşümü
        for sehir in self.sehirler:
            if sehir.isim == isim:
                sehir.sicaklik = yeni_sicaklik
                print(f"{isim} şehrinin sıcaklığı güncellendi. Yeni sıcaklık: {yeni_sicaklik}°")
                return
        print(f"{isim} şehri bulunamadı!")

    def tavsiye_ver(self):
        isim = input("Tavsiye almak istediğiniz şehrin adını giriniz: ")
        for sehir in self.sehirler:
            if sehir.isim == isim:
                if sehir.sicaklik < 0:
                    print("Soğuk, sıkı giyinin")
                elif sehir.sicaklik > 15:
                    print("Hava güzel, rahat giyinin")
                else:
                    print("Serin, mont almayı unutmayın")
                return
        print(f"{isim} şehri için bilgi bulunamadı!")

hava_durumu = HavaDurumu()
hava_durumu.sehir_ekle()
hava_durumu.sicaklik_guncelle()
hava_durumu.tavsiye_ver()