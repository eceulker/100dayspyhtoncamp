#Question1
x=5
y=3
z=6
#tahmini cikti True(dogru)
print(x>y and z>x)
#Question2
#tahmin cikti True(dogru)
print(x<y or z>y)
#Question3
#tahmin cikti 18 ile 30 yaş arasında bir gençsiniz(dogru)
yas = 20

if yas < 18:
    print("18 yaşından küçüksünüz")
elif yas >= 18 and yas < 30:
    print("18 ile 30 yaş arasında bir gençsiniz")
elif yas >= 30 and yas < 40:
    print("30 ve 40 arasına gelmişsiniz")
else:
    print("40 yaşından daha büyüksünüz")
#Question4
#değerler içinde c harfinin geçip geçmediğini gösteren bir if koşulu yazınız
my_dictionary = { "k1":10, "k2k":"a", "k32":30, "k4":"c"}
for word in my_dictionary.values():
   if word=="c":
    print("c var")
#Question5
#anahtarlar içinde a harfinin geçip geçmediğini gösteren bir if koşulu yazınız
my_other_dictionary = {"b":203,"c":"a","a":400,"d":"f"}
for word2 in my_other_dictionary.keys():
    if word2=="a":
      print("keylerde a var")
      print("kod calisiyor")
#Question6
my_numbers = [1,2,3,4,5,6,19,20,32,21,20,1111,23,24]
for sayi in my_numbers:
  if  sayi%2==0:
    print(sayi)
#Question7
#Tüm dairelerin çevresini içeren başka yeni bir liste oluşturunuz. (İpucu: 2 * pi * r)  Pi 3.14 alınabilir.
r_list = [3,2,5,8,4,6,9,12]
pi=3.14
cevre_list= []
for a in r_list:
    cevre = 2 * pi * a
    print("kod calısıyo")
    cevre_list=cevre
print(cevre_list)
#Question8
age_name_list = [("Ahmet",30),("Ayse",24),("Mehmet",40),("Fatma",29)]
for yas_y in range(len(age_name_list)):
    print(age_name_list[yas_y][1])
    #print(new_list = age_name_list.append([yas_y][1]))
#Question9
metal_list = ["Metallica","Iron Maiden","Dream Theater","Megadeth","AC/DC"]
from random import metal_list
print(metal_list[randint(0,len(metal_list))])
#Question10
number_list = [5,7,18,21,20,10,405,24]
#[num % 2 == 0 for num in number_list]
#sadece ciftler yazilir 18 20 10 24