import random
import time #programın  1 sanıye beklemesi için 

print(""" 
*************
    sayı tahmin oyunu 
    1 ile 40 arasında sayıyı tahmin edin 


""" )

rastgele_sayı=random.randint(1,40)
tahmin_hakki=7


while True:
    tahmin=int(input("tahmininiz: "))
    if (tahmin<rastgele_sayı):
        print("bilgiler sorgulanıyor ")
        time.sleep(1)#programı 1 saniyeliğine durdurur 

        print("daha yüksek bir sayı söyleyin ")
        tahmin_hakki-=1
    elif(tahmin>rastgele_sayı):
        print("bilgiler sorgulanıyor")
        time.sleep(1)
        print("daha düşük bir sayı giriniz")
        tahmin_hakki-=1

    else:
        print("bilgiler sorgulanıyor")  
        time.sleep(1)
        print ("tebrikler ",rastgele_sayı)
        break
    if (tahmin_hakki==0):
        print("tahmin hakkınız bitmiştir")
        print("sayımız:",rastgele_sayı)
        break
    



