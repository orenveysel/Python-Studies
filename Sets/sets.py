fruits = { 'orange', 'apple', 'banana'}

# print(fruits[0])  indekslenemez

for x in fruits:
    print(x)

fruits.add('cherry')
fruits.update(['mango','grape','apple'])    # apple eklenmedi çünkü zaten vardı

fruits.remove('mango')      # parantezdeki silinir
fruits.discard('apple')     # parantezdeki silinir

fruits.pop()                # normalde sondaki elemanı ancak set'te sıralama rastgele olduğu için rastgele eleman siler

fruits.clear()              # tüm elemanlar silinir

print(fruits)

# myList = [1,2,5,4,4,2,1]

# print(myList)
# print(set(myList))

