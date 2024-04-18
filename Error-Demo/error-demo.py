liste = ["1","2","5a","10b","abc","10","50"]

#-1 Liste elemanlari icindeki sayisal degerleri bulunuz.

# for x in liste:
#     try:
#         result = int(x)
#         print(result)
#     except ValueError:
#         continue



#-2 Kullanici 'q' degerini girmedikce aldiginiz her inputun sayi
#   oldugundan emin olunuz. Aksi halde hata mesaji yazin.

# while True:
#     sayi = input('Sayi: ')
#     if sayi == 'q':
#         break

#     try:
#         result = float(sayi)
#         print('Girdiginiz sayi: ', result)
#     except ValueError:
#         print("Gecersiz sayi")
#         continue



#-3 Girilen parola icinde turkce karakter hatasi veriniz.

# def check_password(psw):
#     import re
#     if re.search("[ğĞüÜşŞıİöÖçÇ]", psw):
#         raise Exception("Parola türkçe karakter içermemelidir.")

#     else:
#         print("Gecerli parola")

# password = input("Parola giriniz: ")

# try:
#     check_password(password)
# except Exception as ex:
#     print(ex)



#-4 Faktoriyel fonksiyonu olusturup fonksiyona gelen deger icin 
#   hata mesajlari verin.

def Faktoriyel(x):
    x = int(x)

    if x < 0:
        raise ValueError('Negatif deger')

    result = 1

    for  i in range(1, x+1):
        result *= i
    return result

for x in [5, 10, 20, -3, '10a']:
    try:
        y = Faktoriyel(x)
    except ValueError as err:
        print(err)
        continue

    print(y)

