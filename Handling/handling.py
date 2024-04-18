# error handling => hata yonetimi

# try:
#     x = int(input('x: '))
#     y = int(input('y: '))
#     print(x/y)
# except (ZeroDivisionError,ValueError) as e:
#     print('Yanlis bilgi girdiniz.')
#     print(e)

# try:
#     x = int(input('x: '))
#     y = int(input('y: '))
#     print(x/y)
# except:
#     print('Yanlis bilgi girdiniz.')

while True:
    try:
        x = int(input('x: '))
        y = int(input('y: '))
        print(x/y)
    except Exception as ex:
        print('Yanlis bilgi girdiniz.', ex)
    else:
        break
    finally:
        print('try except sonlandi.')

