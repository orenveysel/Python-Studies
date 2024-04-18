# Dosya açmak ve oluşturmak için open() fonksıyonu kullanılır.
# Kullanımı: open(dosya_adi,dosya_erisme_modu)
# dosya_erisme_modu => dosyayı hangi amaçla açtığımızı belirtir.


# "w": (Write) yazma modu. 
#    ** Dosyayı konumda oluşturur.
#    ** Dosya icerigini siler ve yeniden ekleme yapar.

# file = open("newfile.txt","w")
# file = open("C:/users/veysi/desktop/newfile.txt","w")
# file.close()

# file = open("newfile.txt","w",encoding='utf-8')   # ---encoding='utf-8'--- turkce karakter sikintisi icin 
# file.write("Veysel ÖREN")
# file.close()


# "a": (Append) ekleme. Dosya konumda yoksa oluşturur.

# file = open("newfile.txt","a",encoding='utf-8')
# file.write("\nVeysel OREN")
# file.write("Veysel OREN\n")
# file.close()


# "x": (Create) oluşturma. Dosya zaten varsa hata verir.

# file = open("newfile2.txt","x",encoding='utf-8')


# "r": (Read) okuma. varsayılan. dosya konumda yoksa verir.


