#-1 Kullanıcıdan isim, yaş ve eğitim bilgilerini isteyip ehliyet alabilme durumunu kontrol ediniz.
#   Ehliyet alma koşulu en az 18 ve eğitim durumu lise ya da üniversite olmalıdır.

# name = input('Adınız: ').capitalize()
# age = int(input("Yaşınız: "))
# edu = input("Eğitim durumunuz: ").lower()       # i harfini büyük yazınca lower yapmasına rağmen kabul etmiyor nedenini bilmiyorum!!!

# # kosul = (age >= 18) and (edu=='lise' or edu=='üniversite')
# # if kosul:
# #     print(f"{name} ehliyet almaya uygundur.")
# # else:
# #     print(f"{name} ehliyet almaya uygun değildir.")

# if (age >= 18):
#     if (edu=='lise' or edu=='üniversite'):
#         print(f"{name} ehliyet almaya uygundur.")
#     else:
#         print("Eğitim durumunuz uygun değildir.")
# else:
#     print("Yaşınız ehliyet almaya uygun değildir.")


    
#-2 Bir öğrencinin 2 yazılı 1 sözlü notunu alıp hesaplanan ortalamaya göre
#   not aralığına karşılık gelen not bilgisini yazdırınız.
#   0 -24   => 0
#   25-44   => 1
#   45-54   => 2
#   55-69   => 3
#   70-84   => 4
#   85-100  => 5

# quiz1 = float(input("1. yazılıyı girin: "))
# quiz2 = float(input("2. yazılıyı girin: "))
# sozlu = float(input("Sözlüyü girin: "))

# tNot = (quiz1 + quiz2 + sozlu) / 3

# if 0 <= tNot < 25:
#     print("Not bilgisi: 0") 
# elif 25 <= tNot < 45:
#     print("Not bilgisi: 1")
# elif 45 <= tNot < 55:
#     print("Not bilgisi: 2")
# elif 55 <= tNot < 70:
#     print("Not bilgisi: 3")
# elif 70 <= tNot < 85:
#     print("Not bilgisi: 4")   
# elif 85 <= tNot < 100:
#     print("Not bilgisi: 5")  
# else:
#     print("Hatalı bilgi girdiniz. Tekrar deneyin.") 

# print(f"Net notunuz: {tNot:1.4}") 



#-3 Trafiğe çıkış tarihi alınan bir aracın servis zamanını aşağıdaki bilgilere göre hesaplayınız.
#   1. Bakım => 1. yıl
#   2. Bakım => 2. yıl
#   3. Bakım => 3. yıl
#   ** Süre hesabını alınan gün, ay, yıl bilgisine göre gün bazlı hesaplayınız.
#   *** datetime modülünü kullanmanız gerekiyor.
#   (simdi) - (2018/8/1) => gün

import datetime

T = input("Aracınızın trafiğe çıkış tarihini giriniz (yyyy/mm/dd): ")
T = T.split("/")
# print(T[0])
# print(T[1])
# print(T[2])

trafik = datetime.datetime(int(T[0]), int(T[1]), int(T[2]))
simdi = datetime.datetime.now()
fark = simdi - trafik
time = fark.days

print(f"Trafikte geçirilen gün sayısı: {fark.days}")


if (0 < time < 365):
    print("1. bakım aralığı")
elif (365 <= time < (365*2)):
    print("2. bakım aralığı")
elif ((365*2) <= time < (365*3)):
    print("3. bakım aralığı")
else:
    print("Hatalı süre!!")


