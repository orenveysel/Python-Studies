# try:
#     file = open("newfile.txt","r")
#     print(file)
# except FileNotFoundError:
#     print("dosya okuma hatasi")
# finally:
#     print("Dosya kapandi.")
#     file.close()

file = open("newfile.txt","r", encoding = "utf-8")

# for dongusu

# for i in file:
#     print(i, end="")    

# ************ read() fonksiyonu

# content1 = file.read()

# print("icerik 1")
# print(content1)

# file = open("newfile.txt","r", encoding = "utf-8")
# content2 = file.read()

# print("icerik 2")
# print(content2)

# content = file.read(5)
# content = file.read(3)
# content = file.read(3)

# print(content)

# ************ readline() fonksiyonu

# print(file.readline(),end="")
# print(file.readline(),end="")
# print(file.readline(),end="")
# print(file.readline(),end="")
# print(file.readline())
# print(file.readline())
# print(file.readline())

# ************ readlines() fonksiyonu

liste = file.readlines()

print(liste)

file.close()
