#-1 Girilen 2 sayıdan hangisi büyüktür ?
# x = int(input("Bir x değeri giriniz: "))
# y = int(input("Bir y değeri giriniz: "))

# a = x > y
# b = y > x
# result1 = f"Büyük olan sayı x'dir => {a}"
# result2 = f"Büyük olan sayı y'dir => {b}"

# print(result1)
# print(result2)


#-2 Kullanıcıdan 2 vize (%60) ve 1 final (%40) notunu alıp ortalama hesaplayınız.
#   Eğer ortalama 50 ve üstündeyse geçti, değilse kaldı yazdırın.
# vize1 = float(input("1. vize notunu giriniz: "))
# vize2 = float(input("2. vize notunu giriniz: "))
# final = float(input("Final notunu giriniz: "))

# ort = (((vize1 + vize2) / 2) * 0.6) + (final * 0.4) 

# durum = f"Not ortalamanız {ort} ve dersi geçme durumunuz {ort>=50}"
# print(durum)


#-3 Girilen bir sayının tek mi çift mi olduğunu yazdırınız. 
# x = float(input("Bir değer giriniz: "))

# durum = f"Girdiğiniz değerin çift olma durumu: {x%2==0}"
# print(durum)


#-4 Girilen bir sayının negatif pozitif durumunu yazdırın.

# x = int(input("Bir değer giriniz: "))


# durum = f"Girdiğiniz değerin pozitiflik durumu: {x>=0} "
# print(durum)


#-5 Parola ve email bilgisini isteyip doğruluğunu kontrol ediniz.
#   (email: email@sadikturan.com  parola:abc123)

# x = input("Email giriniz: ".strip())        # emailde yazılan boşlukları düzeltir
# y = input("Parola giriniz: ".lower())       # yazılan parolayı komple küçük harf yapar

# email = "email@sadikturan.com"
# parola = "abc123"

# durum1 = f"Girdiğiniz emailin doğruluk durumu: {x==email}"
# durum2 = f"Girdiğiniz parolanın doğruluk durumu: {y==parola}"

# print(durum1)
# print(durum2)

