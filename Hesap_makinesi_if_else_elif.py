#İf-Else-Elif ile hesap makinesi
#Kullanıcının yapmak istediği işlemi öğreniyoruz

print("Toplama İşlemi için               --> 1")
print("Çıkarma İşlmei için               --> 2")
print("Çarpma İşlemi için                --> 3")
print("Bölme İşlemi için                 --> 4")
print("Üs alma işlemi için               --> 5")
print("Karekök alma işlemi için          --> 6")
print("Sayının karesini alma işlemi için --> 7")
secim = int(input("Seçiminizi Yapınız: "))
#Toplama işlemi için
if secim == 1:
    sayi1 = int(input("Lütfen 1.Sayıyı Giriniz: "))
    sayi2 = int(input("Lütfen 2.Sayıyı Giriniz: "))
    sonuc1= sayi1 + sayi2
    print(f"Toplama işleminin sonucu: {sonuc1}")
#Çıkarma işlemi için
if secim == 2:
    sayi2 = int(input("Lütfen 1.Sayıyı Giriniz: "))
    sayi4 = int(input("Lütfen 2.Sayıyı Giriniz: "))
    sonuc2 = sayi3 - sayi4
    print(f"Çıkarma işleminin sonucu: {sonuc2}")
#Çarpma işlemi için   
if secim == 3:
    sayi5 = int(input("Lütfen 1.Sayıyı Giriniz: "))
    sayi6 = int(input("Lütfen 2.Sayıyı Giriniz: "))
    sonuc3 = sayi5*sayi6
    print(f"Çarpma işleminin sonucu: {sonuc3}")
#Bölme işlemi için   
if secim == 4:
    sayi7 = int(input("Lütfen 1.Sayıyı Giriniz: "))
    sayi8 = int(input("Lütfen 2.Sayıyı Giriniz: "))
    sonuc4 = sayi7/sayi8
    print(f"Bölme işleminin sonucu: {sonuc4}")
#Üs alma işlemi için   
if secim == 5:
    sayi9 = int(input("Lütfen 1.Sayıyı Giriniz: "))
    sayi10 = int(input("Lütfen 2.Sayıyı Giriniz: "))
    sonuc5= sayi9**sayi10
    print(f"Üst alma işleminin sonucu: {sonuc5}")
#Karekök alma işlemi için    
if secim == 6:
    sayi11 = int(input("Lütfen Karekökünü Almak İstediğiniz Sayıyı Giriniz: "))
    sonuc6 = sayi11**0.5
    print(f"Karekökünü alma işleminin sonucu: {sonuc6}")
#Karesini alma işlemi için    
if secim == 7:
    sayi12 = int(input("Lütfen Karesini Almak İstediğiniz Sayıyı Giriniz: "))
    sonuc7 = sayi12**2 
    print(f"Karesini alma işleminin sonucu: {sonuc7}")