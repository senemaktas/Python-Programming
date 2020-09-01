
import socket
import sys
import random
import time

#HOST = '127.0.0.1'  
port=12000 

sunucuSoketi=socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)
sunucuSoketi.bind(('',port))
sunucuSoketi.listen(1)
print('Sunucu baglanti icin hazir')
while 1:
     baglanti,istemciIPadresi=sunucuSoketi.accept()
     #ilk mesaji sunucu gonderir.
     baglanti.sendall("\nHosgeldiniz! isminiz nedir?")

     kullaniciAdi=baglanti.recv(1024)
     print "kullanici adi: ",kullaniciAdi

     operatorler=['+','-','*']
     sayi1=random.randint(1,10)
     sayi2=random.randint(1,10)
     operation=random.choice(operatorler)
     randomSoru=str(sayi1)+" "+str(operation)+" "+str(sayi2)+"?"
     sonuc=eval(str(sayi1)+operation+str(sayi2))
     
     #sunucu kullanici mesajini alip, kullaniciya soru sorar.
     baglanti.send("Hosgeldin " +kullaniciAdi+"\n"+"Sorunuz: " +randomSoru+ "\n" + "Cevabinizi bekliyorum.")

     kullaniciCevabi=baglanti.recv(1024)
     print "Kullanicinin soruya cevabi: ",kullaniciCevabi

     #sunucu kullanici cevabini degerlendirir ve sonucu gonderir.
     if  sonuc==int(kullaniciCevabi) :
         baglanti.send("Cevap dogru! "+kullaniciAdi+ " ,odevi basariyla tamamladin.")
     else:
         baglanti.send("Cevap yanlis! "+kullaniciAdi+ " ,tekrar deneyebilirsin.")

     sunucuSoketi.close()
