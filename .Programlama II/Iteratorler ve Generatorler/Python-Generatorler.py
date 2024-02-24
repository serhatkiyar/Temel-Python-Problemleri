def rakamsay():
    for i in range(10):
        yield i


# Burada tanımlanan fonksiyon özel bir fonksiyondur. Bu Fonksiyonun özelleşmiş ismi G E N E R A T O R dür.
# Generatorler fonksiyon oldukları gibi aynı zamanda iterable objelerdir.

print(type(rakamsay()))
# Bu fonksiyonun type' nı yazdırırsak
# rakamsay() fonksiyonun type' ı <class 'generator'> olarak görünür.

generator = rakamsay()
# rakamsay() generator' ü yani [iterable obje]' si burada başka bir değişkene atanıyor.
# Çünküüü... , (burayı iyi dinle!)

# Bizim burada generator fonksiyonumuzu bir değişkene atamamızın sebebi şudur:

# Önceden size Generatorler' in [iterable obje] olduklarını söylemiştim.
# Fakat Generatorler [iterable objeler]' in özelliklerinin dışında bir özelliği daha vardır.
# [ Biz Generatorler üzerinde next() fonksiyonunu kullanarak Generator' ün değer üretmesini sağlıyabiliriz. ]

# KISA NOT: Generatorler Değer Üretir!

# Ama biz generatorler 'in birer iterator olmadığı gerçeğini bilmemiz gerek.

# BUNLARI KAFANA SOK!:
# Madde 1: Generatörler İterable Objelerdir.) (İterable Obje gibi kavramların tanımlarını başta vermiştik!)
# Madde 2: Generatörler İterator Objeler Değillerdir.
# Madde 3: Generatörler iter() fonksiyonu ile İterator forma geçiş yapabilirler.
# Madde 4: next() fonksiyonu iteratorler ve generatorler üzerine uygulanabilir.

# Buunuuun devamında:
# Biz eğer bir Generator Fonksiyonunu bir değişkene atama işlemini gerçekleştirmezsek:

# Her next() fonksiyonunu Bu Generator Fonksiyon' u için kullandığımız zaman
# Her seferinde bu fonksiyon tekrar çağrılır. Ve buda şu olayı gerçekleştirir:
# Her next() fonksiyonu bize Generator' ün ilk elemanını döndürür.
# Çünkü çağrılan her fonksiyon önceki çağrılan fonksiyondan farklıdır.
# Bu yüzden Generatör Fonksiyonlarımızı bir [değişken]' e atama işlemini gerçekleştirip
# next() fonksiyonlarımızı o [değişken]' e ( [değişken] burada bir fonksiyondur. ) uygularsak
# Her seferinde aynı fonksiyon üzerinde işlem yapmış olucağımız için iterasyonlar sonucu
# Generator' ün ürettiği elemanları alabiliriz.

iterator_objesi = iter(generator)
# 'iter(generator)' bu yapı 'iter()' fonksiyonu aracılığı ile bir iterator oluşturur ve
# bu iterator 'iterator_objesi' adlı değişkene atanır.

# KISA NOT: Iteratorler iterable objeler üzerinde gezinmeye yarayan objelerdir.

print(next(iterator_objesi))
# 'next()' fonksiyonu ile iterator objesi üzerinde ilk iterasyonu gerçekleştirmiş olduk.
# Ve üzerinde işlem yaptığımız iterable objenin ilk elemanını bu yapıyla döndürdük.
 
# G E N E R A T O R l E R' i yani [İterable Objeler]' i oluşturmanın başka yolları da vardır:

# Şimdi  'list comprehension' ile Generator(Iterable Obje) oluşturmayı görüceğiz.
# KISA NOT: list comprehension [i for i in range(sayi)] şeklinde ki yapılara denir.

generator_objesi = (i for i in range(10))  # 0 dan 9' a kadar değer üreten bir generator objesi oluşturuldu.
# Burada  'list comprehension' ile bir Generator(Iterable Obje) oluşturmuş olduk.

print(type(generator_objesi))  # <class 'generator'>
print(next(generator_objesi))  # 0
print(next(generator_objesi))  # 1
# Yine iterasyonlarımızı 'next()' fonksiyonu ile gerçekleştirebiliriz.

# ~ G E N E R A T O R L E R e örnek olarak 'range()' fonksiyonu gösterilebilir ~.

# serhatkiyar
