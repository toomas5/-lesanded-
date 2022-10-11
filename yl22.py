#toomas
#11.10.22
#yl2
import math

#kütus
kytus = int(input("tangitud: "))
l2bi = int(input("läbitud: "))
kulu=(100*(kytus/l2bi))
print("kulu: ",kulu)



#arv
arv = int(input("sisesta arv: "))
print((bin(arv)),(hex(arv)))



#aeg
aeg = int(input("min: "))
tunnid = aeg//60
minutid = aeg % 60
print("vastus:",tunnid,":",minutid)



#hüpo
a,b = 16,9
c = round(math.sqrt(pow(a,2) +b**2), 2)
print(c)




#rull
kiirus=29.9
kiirusm=(kiirus/60)
aeg=24
jouab=(kiirusm*aeg)
print(round(jouab))



#pitsa
hind=12.90
sopru=3
tip=hind*1.1
maks=(tip/3)
print(maks)



#toote hind
hind=36.75
ale=0.4
kogus=3
summa=round((hind-hind*ale)*3,2)
print(kogus,"toote summa on",summa,"eurot")

#kolmnurga ümbermööt
a,b,c = 5,5,5
p = a+b+c
print('Kolmnurga ümbermõõt on:',p)