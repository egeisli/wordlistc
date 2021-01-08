import os
import sys
import time
from colorama import *
init()
#infos
bilgiler = []
print('------------------------------------------------------------------------')
print('önce isim, soyisim, takım gibi bilgiler')
print('------------------------------------------------------------------------')
name = input('ad : ')
if(name == '' or name == ' ' or name == '   '):
    print('isim yazmalısınız')
    exit()
else:
    bilgiler.append(name)
    bilgiler.append(name.lower())
    bilgiler.append(name.capitalize())
    bilgiler.append(name.upper())
print('------------------------------------------------------------------------')
surname = input('soyad : ')
if(surname == '' or surname == ' ' or surname == '   '):
    print('bir soyad da yazmalısınız')
    exit()
else:
    bilgiler.append(surname)
    bilgiler.append(surname.lower())
    bilgiler.append(surname.capitalize())
    bilgiler.append(surname.upper())
print('------------------------------------------------------------------------')
team = input('takım : ')
if(team == '' or team == ' ' or team == '   '):
    pass
else:
    bilgiler.append(team)
    bilgiler.append(team.lower())
    bilgiler.append(team.capitalize())
    bilgiler.append(team.upper())
print('------------------------------------------------------------------------')
babaadı = input('baba ad : ')
if(babaadı == '' or babaadı == ' ' or babaadı == '   '):
    pass
else:
    bilgiler.append(babaadı)
    bilgiler.append(babaadı.lower())
    bilgiler.append(babaadı.capitalize())
    bilgiler.append(babaadı.upper())
print('------------------------------------------------------------------------')
babadoğumtarihi = input('baba doğum yılı : ')
if(babadoğumtarihi == '' or babadoğumtarihi == ' ' or babadoğumtarihi == '   '):
    pass
else:
    bilgiler.append(babadoğumtarihi)
print('------------------------------------------------------------------------')
anneadı = input('anne ad : ')
if(anneadı == '' or anneadı == ' ' or anneadı == '   '):
    pass
else:
    bilgiler.append(anneadı)
    bilgiler.append(anneadı.capitalize())
    bilgiler.append(anneadı.lower())
    bilgiler.append(anneadı.upper())
print('------------------------------------------------------------------------')
annedoğumtarihi = input('anne doğum yılı : ')
if(annedoğumtarihi == '' or annedoğumtarihi == ' ' or annedoğumtarihi == '   '):
    pass
else:
    bilgiler.append(annedoğumtarihi)
print('------------------------------------------------------------------------')
annesoyadı = input('anne kızlık soyad : ')
if(annesoyadı == '' or annesoyadı == ' ' or annesoyadı == '   '):
    pass
else:
    bilgiler.append(annesoyadı)
    bilgiler.append(annesoyadı.capitalize())
    bilgiler.append(annesoyadı.lower())
    bilgiler.append(annesoyadı.upper())
print('------------------------------------------------------------------------')
kardeşadı = input('kardeş ad : ')
if(kardeşadı == '' or kardeşadı == ' ' or kardeşadı == '   '):
    pass
else:
    bilgiler.append(kardeşadı)
    bilgiler.append(kardeşadı.lower())
    bilgiler.append(kardeşadı.capitalize())
    bilgiler.append(kardeşadı.upper())
print('------------------------------------------------------------------------')
kardeşdoğumtarihi = input('kardeş doğum yılı : ')
if(kardeşdoğumtarihi == '' or kardeşdoğumtarihi == ' ' or kardeşdoğumtarihi == '   '):
    pass
else:
    bilgiler.append(kardeşdoğumtarihi)
print('------------------------------------------------------------------------')
eşininadı = input('eşinin adı : ')
if(eşininadı == '' or eşininadı == ' ' or eşininadı == '   '):
    pass
else:
    bilgiler.append(eşininadı)
    bilgiler.append(eşininadı.lower())
    bilgiler.append(eşininadı.capitalize())
    bilgiler.append(eşininadı.upper())
print('------------------------------------------------------------------------')
eşininsoyadı = input('eşinin soyadı : ')
if(eşininsoyadı == '' or eşininsoyadı == ' ' or eşininsoyadı == '   '):
    pass
else:
    bilgiler.append(eşininsoyadı)
    bilgiler.append(eşininsoyadı.lower())
    bilgiler.append(eşininsoyadı.capitalize())
    bilgiler.append(eşininsoyadı.upper())
print('------------------------------------------------------------------------')
eşinindoğumtarihi = input('eşinin doğum yılı : ')
if(eşinindoğumtarihi == '' or eşinindoğumtarihi == ' ' or eşinindoğumtarihi == '   '):
    pass
else:
    bilgiler.append(eşinindoğumtarihi)
print('------------------------------------------------------------------------')
sevdiği_şarkıcı = input('en sevdiği şarkıcı : ')
if(sevdiği_şarkıcı == '' or sevdiği_şarkıcı == ' ' or sevdiği_şarkıcı == '   '):
    pass
else:
    bilgiler.append(sevdiği_şarkıcı)
    bilgiler.append(sevdiği_şarkıcı.lower())
    bilgiler.append(sevdiği_şarkıcı.capitalize())
    bilgiler.append(sevdiği_şarkıcı.upper())
print('------------------------------------------------------------------------')
eniyiarkadaşı = input('en iyi arkadaşı adı : ')
if(eniyiarkadaşı == '' or eniyiarkadaşı == ' ' or eniyiarkadaşı == '   '):
    pass
else:
    bilgiler.append(eniyiarkadaşı)
    bilgiler.append(eniyiarkadaşı.lower())
    bilgiler.append(eniyiarkadaşı.capitalize())
    bilgiler.append(eniyiarkadaşı.upper())
print('------------------------------------------------------------------------')
oluşturulacak_wordlist = str(input('=> oluşturulacak wordlist : '))
print('------------------------------------------------------------------------')
x = open(oluşturulacak_wordlist+'.txt', 'w')
for bilgi1 in bilgiler:
    x.write(bilgi1+'\n')

for bilgi1 in bilgiler:
    for bilgi2 in bilgiler:
        x.write(bilgi1+bilgi2+'\n')
for i in range(2000):
    i = str(i)
    for bilgi in bilgiler:
        x.write(bilgi+i+'\n')
        x.write(i+bilgi+'\n')
        x.write(bilgi+'_'+i+'\n')
    for bilgi1 in bilgiler:
        for bilgi2 in bilgiler:
            x.write(bilgi1+bilgi2+i+'\n')
            x.write(i+bilgi1+bilgi2+'\n')
            x.write(bilgi1+bilgi2+'_'+i+'\n')
#karakterler
cevap = str(input('> acaba wordlistteki kelimelerin sonuna birkaç özel karakter koyalım mı : ')).lower()
print('------------------------------------------------------------------------')
if(cevap == 'e'):
    for bilgi in bilgiler:
        x.write(bilgi+'#'+'\n')
        x.write(bilgi+'@'+'\n')
        x.write(bilgi+'%'+'\n')
        x.write(bilgi+'½'+'\n')
    for bilgi1 in bilgiler:
        for bilgi2 in bilgiler:
            x.write(bilgi1+bilgi2+'#'+'\n')
            x.write(bilgi1+bilgi2+'@'+'\n')
            x.write(bilgi1+bilgi2+'%'+'\n')
            x.write(bilgi1+bilgi2+'½'+'\n')
    for bilgi1 in bilgiler:
        for bilgi2 in bilgiler:
            for bilgi3 in bilgiler:
                x.write(bilgi1+bilgi2+bilgi3+'#'+'\n')
                x.write(bilgi1+bilgi2+bilgi3+'@'+'\n')
                x.write(bilgi1+bilgi2+bilgi3+'%'+'\n')
                x.write(bilgi1+bilgi2+bilgi3+'½'+'\n')
else:
    pass
for i in range(2000):
    i = str(i)
    x.write(name[:1]+i+'\n')
    x.write(name[:2]+i+'\n')
    x.write(name[:1]+surname[:1]+i+'\n')
dosya = open(oluşturulacak_wordlist+".txt","r")
x.close()
print('[+] wordlist oluşturuldu '+str(dosya.read().count("\n"))+' kelime')
print('[+] wordlist başarılı bir şekilde oluşturuldu')
quit()