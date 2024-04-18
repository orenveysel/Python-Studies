# with open ("newfile.txt","r+", encoding="utf-8") as file:
#     file.seek(20)
#     file.write("deneme")

# with open ("newfile.txt","r+", encoding="utf-8") as file:
#     print(file.read())

# ***** Sayfa sonunda guncelleme *****

# with open ("newfile.txt","a", encoding="utf-8") as file:
#     file.write("\nEmel Turan")

# ***** Sayfa basinda guncelleme *****

# with open ("newfile.txt","r+", encoding="utf-8") as file:
#     content = file.read()
#     content = "Efe TURAN\n" + content
#     file.seek(0)
#     file.write(content)

# ***** Sayfa ortasinda guncelleme *****

with open ("newfile.txt","r+", encoding="utf-8") as file:
    list = file.readlines()
    list.insert(1,"Yilmaz Aygun\n")
    file.seek(0)
    file.writelines(list)
    
with open ("newfile.txt","r", encoding="utf-8") as file:
    print(file.read())
# with open ("newfile.txt","r+", encoding="utf-8") as file:
#     file.seek(20)
#     file.write("deneme")

# with open ("newfile.txt","r+", encoding="utf-8") as file:
#     print(file.read())

# ***** Sayfa sonunda guncelleme *****

# with open ("newfile.txt","a", encoding="utf-8") as file:
#     file.write("\nEmel Turan")

# ***** Sayfa basinda guncelleme *****

# with open ("newfile.txt","r+", encoding="utf-8") as file:
#     content = file.read()
#     content = "Efe TURAN\n" + content
#     file.seek(0)
#     file.write(content)

# ***** Sayfa ortasinda guncelleme *****

with open ("newfile.txt","r+", encoding="utf-8") as file:
    list = file.readlines()
    list.insert(1,"Yilmaz Aygun\n")
    file.seek(0)
    file.writelines(list)
    
with open ("newfile.txt","r", encoding="utf-8") as file:
    print(file.read())
