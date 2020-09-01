
import sys
import socket

host='127.0.0.1'  
port=12000 

istemciSoketi=socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)
#istemci sunucuya baglanir.
istemciSoketi.connect((host,port))

while 1:
     ilkMesaj=istemciSoketi.recv(1024)
     print "\nSunucudan gelen hosgeldiniz mesaji: ",ilkMesaj
      
     #istemci uygulamayi yazan kisinin ismini gonderir.
     isim=raw_input()
     istemciSoketi.sendall(isim)

     GelenSoru=istemciSoketi.recv(1024)
     print "Sunucudan gelen soru: ",GelenSoru

     #kullanici gelen soruyu cevaplar.
     sorununCevabi=raw_input("")
     istemciSoketi.sendall(sorununCevabi)

     sonuc=istemciSoketi.recv(1024)
     print "Sunucudan gelen sonuc mesaji: ",sonuc

     istemciSoketi.close()


