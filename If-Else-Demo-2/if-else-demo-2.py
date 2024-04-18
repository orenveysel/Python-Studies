#-1 Girilen bir sayinin 0-100 arasinda olup olmadigini kontrol ediniz.

# sayi = float(input('sayi: '))
# result = (sayi > 0) and (sayi<=100)
# print(f'sayi 0-100 arasinda mi: {result}')

# x = int(input('Bir sayi giriniz: '))

# if (0 < x <100):
#     print(f"{x} sayisi 0-100 arasindadir.")
# else:
#     print(f"{x} sayisi 0-100 arasinda degildir.")



#-2 Girilen bir sayinin pozitif cift sayi olup olmadigini kontrol ediniz.

# sayi = int(input('sayi: '))
# result = (sayi > 0) and (sayi % 2 == 0)
# print(f'Girilen sayi pozitif cift sayi mi: {result}')

# x = int(input('Bir sayi giriniz: '))
# durum = (x > 0) and (x % 2 == 0)

# if (x > 0):
#     if (x % 2 == 0):
#         print("Girilen sayi pozitif cift sayidir.")
#     else:
#         print("Girilen sayi pozitif tek sayidir.")
# elif (x==0):
#     print("Girilen sayi notr cift sayidir.")
# else:
#     print("Girilen sayi negatiftir.")



#-3 Email ve parola bilgilari ile giris kontrolu yapiniz.

# email = 'email@gmail.com'
# password = 'abc123'

# girilenEmail = input('email: ')
# girilenPassword = input('password')

# result = (girilenEmail == email) and (girilenPassword == password)
# print(f'uygulamaya giris basarili mi: {result}')

# email = 'email@gmail.com'
# password = 'abc123'

# x = input('email: ')
# y = input('password: ')
# durum = (x==email) and (y==password)

# if (durum):
#     print('Giris basarili!')
# else:
#     print('Giris basarisiz!')
    


#-4 Girilen 3 sayiyi buyukluk olarak karsilastiriniz.

# a = int(input('a: '))
# b = int(input('b: '))
# c = int(input('c: '))

# result = (a > b) and (a > c)
# print(f'a en buyuk sayidir: {result}')

# result = (b > a) and (b > c)
# print(f'b en buyuk sayidir: {result}')

# result = (c > a) and (c > b)
# print(f'c en buyuk sayidir: {result}')

# a = int(input('a: '))
# b = int(input('b: '))
# c = int(input('c: '))

# result1 = (a > b) and (a > c)
# result2 = (b > a) and (b > c)
# result3 = (c > a) and (c > b)

# if (result1):
#     print("En buyuk sayi a'dir.")
# elif (result2):
#     print("En buyuk sayi b'dir.")
# elif (result3):
#     print("En buyuk sayi c'dir.")



#-5 Kullanicidan 2 vize (%60) ve final (%40) notunu alip ortalama hesaplayiniz. 
#   Eger ortalama 50 ustundeyse gecti degilse kaldi yazdirin
#   a-) Ortalama 50 olsa bile final notu 50 olmalidir
#   b-) Finalden 70 aldiginda ortalamanin onemi olmasin. 

#   vize1 = float(input('vize 1: '))
#   vize2 = float(input('vize 2: '))
#   final = float(input('final:  '))

# ortalama = ((vize1+vize2)/2)*0.6 + (final * 0.4)
# result = (ortalama>50) and (final>=50)
# result = (ortalama>50) or  (final>=70)

# print(f'ogrencinin ortalamasi: {ortalama} ve gecme durumu: {result}')

# vize1 = float(input('vize 1: '))
# vize2 = float(input('vize 2: '))
# final = float(input('final:  '))

# ort = ((vize1+vize2)/2)*0.6 + (final * 0.4)
# a1 = ((ort>50) and (final>=50)) or  (final>=70)

# if (a1):
#     print("Dersi gectiniz!")
# else:
#     print("Seneye yine bekleriz!")

# print(f"Notunuz: {ort}")

#-6 Kisinin ad, kilo ve boy biglilarini alip kilo indekslerini hesaplayiniz.
#   Formul: (Kilo / boy uzunlugunun karesi)
#   Asagidaki tabloya gore kisi hangi gruba girmektedir.
#   0-18.4      => Zayif
#   18.5-24.9   => Normal
#   25.0-29.9   => Fazla Kilolu
#   30.0-34.9   => Sisman (obez)

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

# x = input("Adınızı giriniz: ").capitalize()
# y = float(input("Kilonuzu giriniz: "))
# z = float(input("Boyunuzu giriniz: "))

# formul = (y / (z ** 2))

# a = 0 <= formul < 18.5      # zayıf
# b = 18.5 <= formul < 25.0   # normal
# c = 25.0 <= formul < 30.0   # fazla kilolu
# d = 30.0 <= formul < 35.0   # obez

# index = (f"Vücut kitle indeksiniz: {formul:1.4}")

# if (a):
#     print(f'{x} zayiftir.')
# elif (b):
#     print(f'{x} normaldir.')
# elif (c):
#     print(f'{x} fazla kiloludur.')
# elif (d):
#     print(f'{x} obezdir.')
# else:
#     print("Hatali veya asiri yuksek veri girisi!!")

# print(index)


