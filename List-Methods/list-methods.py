numbers = [1, 10, 5, 16, 4, 9, 10]
letters = ['a', 'g', 's', 'b', 'y', 'a', 's']

val = min(numbers)
val = max(numbers)
val = max(letters)
val = min(letters)

val = numbers[3:6]
val = numbers[:3]
val = numbers[4:]

numbers [4] = 40

# numbers.append(49)        # 49 elemanını en sona ekler      
# numbers.append(59)        
# numbers.insert(3, 78)     # 78 elemanını 3. sıraya ekler
# numbers.insert(-1, 52)    # 52 elemanını sondan bi öncesine ekler

# numbers.pop()         # ilk indexi siler
# numbers.pop(0)        # silinecek numaranın indexini yazarsın
# numbers.pop(-1)       # son indexi siler
# numbers.remove(59)    # silinecek numaranın kendisini yazarsın


numbers.sort()          # numaralar küçükten büyüğe sıralandı
numbers.reverse()       # numaraların güncel sırası tersine döndü

letters.sort()          # harfler a-z sıralandı
letters.reverse()       # harflerin güncel sırası tersine döndü

print(len(numbers))     # eleman sayısı işte biliyosun artık 
print(len(letters))

print(numbers.count(10))    # kaç tane 10 var 
print(letters.count('a'))   # kaç tane a var falan 

numbers.clear()
print(numbers)

