# ogrenciler = {
#     '120': {
#         'ad': 'Ali',
#         'soyad': 'Yılmaz',
#         'telefon': '532 000 00 01'
#     },
#     '125': {
#         'ad': 'Can',
#         'soyad': 'Korkmaz',
#         'telefon': '532 000 00 02'
#     },
#     '128': {
#         'ad': 'Volkan',
#         'soyad': 'Yükselen',
#         'telefon': '532 000 00 03'
#     },
# }

#-1 Bilgileri verilen öğrencileri kullanıcıdan aldığınız bilgilerle dictionary içine saklayınız.

ogrenciler = {}

number = input("Öğrenci numaranızı giriniz: ")
name = input("Öğrenci adı: ")
surname = input("Öğrenci soyadı: ")
phone = input("Öğrenci telefonu: ")

# ogrenciler[number] = {
#         'ad': name,
#         'soyad': surname,
#         'telefon': phone

# }

ogrenciler.update({
    number: {
        'ad': name,
        'soyad': surname,
        'telefon': phone
    }
})

number = input("Öğrenci numaranızı giriniz: ")
name = input("Öğrenci adı: ")
surname = input("Öğrenci soyadı: ")
phone = input("Öğrenci telefonu: ")

ogrenciler.update({
    number: {
        'ad': name,
        'soyad': surname,
        'telefon': phone
    }
})

number = input("Öğrenci numaranızı giriniz: ")
name = input("Öğrenci adı: ")
surname = input("Öğrenci soyadı: ")
phone = input("Öğrenci telefonu: ")

ogrenciler.update({
    number: {
        'ad': name,
        'soyad': surname,
        'telefon': phone
    }
})

print('*'*50)

#-2 Öğrenci numarasını kullanıcıdan alıp ilgili öğrenci bilgisini gösterin.

ogrNo = input('Öğrenci numarası: ')

ogrenci = ogrenciler[ogrNo]

print(f"Aradığınız {ogrNo} nolu öğrencinin adı: {ogrenci['ad']} soyadı: {ogrenci['soyad']} ve telefonu ise {ogrenci['telefon']}")

