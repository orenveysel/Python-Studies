'''
Soru: Girilen bir sayının asal olup olmadığını bulun.
**  Asal Sayı 1 ve kendisi hariç tam böleni olmayan
    sayılara denir.
'''

# x = int(input("Sayı: "))
# asalMı = True

# if x == 1:
#     print("Sayı asal değildir.")


# for i in range(2, x):
#     if (x % i == 0):
#         asalMı = False
#         break


# if asalMı:
#     print("Sayı asaldır.")
# else:
#     print("Sayı asal değildir.")

y = int(input("Kaça kadar kontrol edelim: "))
x = 0
asallar = [2,]
asalMı = True

while x < y:
    x += 1
    if x == 1:
        continue
    elif x > 1:
        for i in range(2, x):
            if (x % i == 0):
                continue
            elif (x % i != 0):
                asallar.append(x)
            x += 1
    else:
        print("Hata!")
print(asallar)
