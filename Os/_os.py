import os
import datetime

result = dir(os)
result = os.name

# dizin degistirme
# os.chdir('C:\\')
# os.chdir('../..')

# klasor olusturma
# os.mkdir("newdirectory")
# os.makedirs("newdirectory/yeniklasor")
# os.rename("newdirectory","yeniklasor")
# os.rmdir("newdirectory")
# os.removedirs("yeniklasor/yeniklasor")

#listeleme
# result = os.listdir()
# result = os.listdir('C:\\')
# for dosya in os.listdir():
#     if dosya.endswith('.py'):
#         print(dosya)

# etkin dizin ogrenme
# result = os.getcwd()

# result = os.stat("date.py")
# result = result.st_size/1024
# result = datetime.datetime.fromtimestamp(result.st_ctime) # olusturma tarihi
# result = datetime.datetime.fromtimestamp(result.st_atime) # son erisilme tarihi
# result = datetime.datetime.fromtimestamp(result.st_mtime) # degistirilme tarihi

# os.system("notepad.exe")

# path 

result = os.path.abspath("_os.py")
result = os.path.dirname("C:/Users/veysi/Desktop/Python/_os.py")
result = os.path.dirname(os.path.abspath("_os.py"))
result = os.path.exists("C:/Users/veysi/Desktop/Python/_os1.py")
result = os.path.exists("C:/Users/veysi/Desktop/Python")
result = os.path.isdir("C:/Users/veysi/Desktop/Python")
result = os.path.isfile("C:/Users/veysi/Desktop/Python/_os.py")
result = os.path.join("C:\\","deneme","deneme1")
result = os.path.split("C:\\deneme")
result = os.path.splitext("_os.py")
# result = result[0]
result = result[1]

print(result)
