#Question1
def toplama(a,b):
    print(a,b)
'''
    x = toplama(3,4)
    print(x)
'''
#answer= 3 4 (F) no return  none(T)

#Question2
def usselIslem(x=5,y=3):
    print(x ** y)
usselIslem(2,4)
#answer=16(T)
print(usselIslem(2,4))

#Question3
usselIslem()
#answer=125(T)
print(usselIslem())

#Question4
def myLoop(*args):
    for element in args:
        print(element / 2)
myLoop(3,2,1,5,3,4)
#answer=(1.5,1,0.5,2.5,1.5,2)(F) like
print(myLoop(3,2,1,5,3,4))

#Question5
def myFunc(num):
    return num**3
myList = [2,3,4,5,6]
#answer=[8,27,64,125,216]


#Question6
barkodDizisi = ["ABC231","SA3123XYZ","XYZA123Q","QRE1231KJ","X112QGL"]
#new_barkod=list(barkodDizisi.__contains__('XYZ'))
#print(new_barkod)

#Question7
myVar = "Atil Samancioglu"


def ornekFonksiyon():
    myVar = "Atil"

    def digerFonksiyon():
        print(myVar)

    digerFonksiyon()
#ornekFonksiyon()
#answer=Atil(T)
print(ornekFonksiyon())

#Question8
class Kedi():

    def __init__(self, isim, yas=5):
        self.isim = isim
        self.yas = yas

    def yasiCarp(self):
        return self.yas * 3


kedim = Kedi("Tonton")
#kedim.yasiCarp()
#answer=(Tonton,5,15)(F) 15(T)
print(kedim.yasiCarp())

#Question9
class Ogrenci():

    def __init__(self, isim, sinavNotu):
        self.isim = isim
        self.__sinavNotu = sinavNotu

    def notuGoster(self):
        print(f"{self.isim} sınav notu: {self.__sinavNotu}")


ogrenci = Ogrenci("Mehmet", 85)
ogrenci.__sinavNotu = 75
# ogrenci.notuGoster()
#answer=75(F) 85(T) ?
print(ogrenci.notuGoster())

#Question10
#10) Soyut sınıflar ve methodlar oluşturmamıza olanak tanıyan, kodlarımızı daha planlı şekilde yazmamızı mümkün kılan
# aynı zamanda büyük projelerde bize yapısal olarak fayda sağlayabilecek OOP prensibinin adı nedir?
#answer=Nesne Yönelimli Programlama