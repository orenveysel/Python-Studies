#-1 Girilen bir sayının 0-100 arasında olup olmadığını kontrol ediniz.

# x = float(input("Bir sayı giriniz: "))
# a = 0 < x < 100
# durum = f"Girdiğiniz sayının 0-100 arasında olma durumu: {a}"
# print(durum)


#-2 Girilen bir sayının pozitif çift sayı olup olmadığını kontrol ediniz.

# x = float(input("Bir sayı giriniz: "))
# a = (x >= 0) and (x % 2 == 0)
# durum = f"Girdiğiniz sayının pozitif çift sayı olma durumu: {a}"
# print(durum)


#-3 Email ve parola bilgileri ile giriş kontrolü yapınız.

# email = 'area@gmail.com'
# password = 'qweasd4321'

# x = input("Email giriniz: ")
# y = input("Şifre giriniz: ")

# a = (x == email) and (y == password)

# durum = f"Uygulamaya giriş başarılı mı: {a}"
# print(durum)


#-4 Girilen 3 sayıyı büyüklük olarak karşılaştırınız.

# x = int(input("1. sayıyı giriniz: "))
# y = int(input("2. sayıyı giriniz: "))
# z = int(input("3. sayıyı giriniz: "))

# a = (x > y) and (x > z)
# b = (y > x) and (y > z)
# c = (z > x) and (z > y)

# q = (x < y) and (x < z)
# w = (y < x) and (y < z)
# e = (z < x) and (z < y)

# durum1 = f"3 sayı arasında en büyük olan 1. sayıdır: {a}, 2. sayıdır: {b}, 3. sayıdır: {c}"
# durum2 = f"3 sayı arasında en küçük olan 1. sayıdır: {q}, 2. sayıdır: {w}, 3. sayıdır: {e}"

# print(durum1)
# print(durum2)


#-5 Kullanıcıdan 2 vize (%60) ve 1 final (%40) notunu alıp ortalama hesaplayınız.
#   Eğer ortalama 50 ve üstündeyse geçti, değilse kaldı yazdırın.
#   a-) Ortalama 50 olsa bile final notu en az 50 olmalıdır.
#   b-) Finalden 70 aldığında ortalamanın önemi olmasın.

# x = float(input("1. vize notunu giriniz: "))
# y = float(input("2. vize notunu giriniz: "))
# z = float(input("Final notunu giriniz: "))

# ort = (((x + y) / 2) * 0.6) + (z * 0.4)
# durum = (ort >= 50) and (z >= 50)
# kosul = (z >= 70)

# kalma = f"Koşulsuz geçme durumunuz: {kosul}, Dersi geçme durumunuz: {durum} ve ortalamanız: {ort:1.4} "
# print(kalma)


#-6 Kişinin ad, kilo ve boy bilgilerini alıp kilo indekslerini hesaplayınız.
#   Formül: (Kilo / boy uzunluğunun karesi)
#   Aşağıdaki tabloya göre kişi hangi gruba girmektedir ?
#   0-18.4      => Zayıf
#   18.5-24.9   => Normal
#   25.0-29.9   => Fazla Kilolu
#   30.0-34.9   => Şişman (Obez)

# x = input("Adınızı giriniz: ")
# y = float(input("Kilonuzu giriniz: "))
# z = float(input("Boyunuzu giriniz: "))

# formul = (y / (z ** 2))

# a = 0 <= formul < 18.5      # zayıf
# b = 18.5 <= formul < 25.0   # normal
# c = 25.0 <= formul < 30.0   # fazla kilolu
# d = 30.0 <= formul < 35.0   # obez

# index = f"Vücut kitle indeksiniz: {formul:1.4}"
# print(index)

# durum = f"{x} zayıf mıdır: {a}, normal midir: {b}, fazla kilolu mudur: {c}, obez midir: {d}"
# print(durum)


