sayilar = [1,3,5,7,9,12,19,21]

#-1: sayilar listesini while ile ekrana yazdırınız.

# i = 0
# while (i < len(sayilar)):
#     print(sayilar[i])
#     i += 1



#-2: Başlangıç ve bitiş değerlerini kullanıcıdan alıp aradaki tüm tek sayıları ekrana yazdırın.

# x = int(input('Başlangıç değerini giriniz: '))
# y = int(input('Bitiş değerini giriniz: '))

# i = x
# while i <= y:
#     if i % 2 == 1:
#         print(i)
#     i += 1



#-3: 1-100 arasındaki sayılara azalan şekilde yazdırın.

# x = 100

# while x > 0:
#     print(x)
#     x -= 1



#-4: Kullanıcıdan alacağınız 5 sayıyı ekranda sıralı bi şekilde yazdırın.

# numbers = []

# i = 0

# while i<5:
#     sayi = int(input('Sayı giriniz: '))
#     numbers.append(sayi)
#     i += 1
# numbers.sort()
# print(numbers)
    


#-5: Kullanıcıdan alacağınız sınırsız ürün bilgisini ürünler listesi içinde saklayınız.
#   ** ürün sayısını kullanıcıya sorun.
#   ** dictionary listesi yapısı (name, price) şeklinde olsun.
#   ** ürün ekleme işlemi bittiğinde ürünleri ekranda for ile listeleyin.


urunListesi = []
x = int(input('Urun sayisini giriniz: '))

i = 0

while i < x :
    name = str(input('Urunun adini giriniz: ')).capitalize()
    price  = int(input('Urunun fiyatini giriniz: '))
    urunListesi.append({
        'name': name,
        'price': price
    })
    i += 1
for urun in urunListesi:
    print(f"Urun Adi: {urun['name']} => Urun Fiyati: {urun['price']}")



